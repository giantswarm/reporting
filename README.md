# reporting [WIP]

## Installation

## via Helm chart

1. Clone this repository

```
git clone https://github.com/giantswarm/reporting.git
```

2. Install via helm, specifying the targeted namespace

```
helm install ./helm/reporting-chart  -n reporting-tool --namespace <target-namespace>
```

3. Test installation by port-forwarding kibana

```
kubectl -n <target-namespace> port-forward svc/kibana 5601
```

Open Kibana via `http://localhost:5601/app/kibana#/management/kibana/index?_g=()`, create the index, and than check the data in Discover

## Minikube
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



