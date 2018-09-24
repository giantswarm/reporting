

```bash
minikube start --bootstrapper kubeadm --kubernetes-version "v1.11.3" --memory 4096 --vm-driver kvm2
```

https://blog.giantswarm.io/what-you-yaml-is-what-you-get/

<!-- cd ./charts
helm create reporting

eval $(minikube docker-env) -->


<!-- docker -t local/reporting-agent:test1 build ./docker/reporting-agent -->


## render templates

```bash
rm -rf ./manifests/reporting
mkdir -p ./manifests/reporting

helm template \
  --values ./charts/reporting/values.yaml \
  --output-dir ./manifests \
    ./charts/reporting

mv ./manifests/reporting/templates/* ./manifests/reporting
rmdir ./manifests/reporting/templates
```

## start elasticstack

kubectl apply -f ./manifests/reporting/elasticstack



## prepare index

```bash
set elasticsearch_url (minikube service --url -n reporting-elasticstack elasticsearch)

curl --request DELETE "$elasticsearch_url/agent-test1"
echo
curl --request PUT "$elasticsearch_url/agent-test1" --header 'Content-Type: application/json' -d '
{
  "settings": {
    "index.mapping.coerce": true,
    "index.mapping.ignore_malformed": true
  },
  "mappings": {
    "_doc": {
      "properties": {
        "items": {
          "type": "nested",
          "properties": {
            "spec": {
              "enabled": false
            }
          }
        }
      }
    }
  }
}'

# curl --request GET "$elasticsearch_url/_cat/indices"
```


## start agent

```bash
kubectl apply -f ./manifests/reporting/agent

curl --request GET "$elasticsearch_url/_cat/indices"
```

minikube service -n reporting-elasticstack kibana


## run processing

```bash
docker build -t local/reporting-processing:test1 ./docker/processing

kubectl apply -f ./manifests/reporting/processing
```
