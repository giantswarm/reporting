# reporting [WIP]

Snapshot cluster manifests in a history to allow inspection for reporting.

```bash
minikube start --bootstrapper kubeadm --kubernetes-version "v1.11.2" --memory 4096
```

```bash
kubectl apply -f ./manifests-minikube/elasticstack

minikube service -n reporter-elasticstack kibana

# elasticsearch_url=$(minikube service --url -n reporter-elasticsearch elasticsearch)
set elasticsearch_url (minikube service --url -n reporter-elasticsearch elasticsearch)

curl --request DELETE "$elasticsearch_url/test3"
curl --request PUT "$elasticsearch_url/test3" --header 'Content-Type: application/json' -d '
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
```

REPL:

```bash
kubectl apply --recursive -f ./manifests-minikube/reporter
kubectl delete --recursive -f ./manifests-minikube/reporter
```



