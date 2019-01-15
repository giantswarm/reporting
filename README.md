# Reporting tool

The reporting tool is a collection of different components to discover bad practices in a Kubernetes cluster(s).

There are three main components:

- Agent: It lives in the target cluster to forward the pod definition to a external database.

- Processor: It is in charge of sanitize and enhance the ingested documents from targeted clusters. It add some metada to make the alerting process easier.

- Querying: It checks the processed documents looking for bad practices in the pod definitions (no limits, secrets as envs, ...). All found documents that fulfill the conditions are saved in a new DB in order to have an up to date index with all alerts.


The processor and querying components can run in the same cluster on the agent or in a differnet one, but the Elastic Search used to save the data should be accessible from the agent component. 

Diagram

![](/img/architecture.jpg)

## Installation

### Using git

```
# Clone Reposotory recusrively to get submodules

git clone --recursive https://github.com/giantswarm/reporting.git 

cd reporting

# Install Elastic stack
helm install ./helm/elastic-chart  -n reporting-elastic --namespace reporting

# Install Agent

helm install ./reporting-agent/helm/reporting-agent-chart  -n reporting-agent --namespace reporting

# Install Processor

helm install ./reporting-processor/helm/reporting-processor-chart  -n reporting-processor --namespace reporting

# Install Querying

helm install ./reporting-querying/helm/reporting-querying-chart  -n reporting-querying --namespace reporting
```

#### Check data in Kibana

```
kubectl -n reporting port-forward svc/reporting-elastic-reporting-chart-kibana 5601
```

- Open http://localhost:5601
- Add `alerts` index
- Check `Discover` for data


#### Tear Down everything

```
helm delete --purge reporting-elastic  reporting-agent reporting-processor reporting-querying 

kubectl -n reporting delete jobs --all
```

### Use Helm Registry

#### Install Elasticsearch & Kibana

```
git clone https://github.com/giantswarm/reporting.git
helm-28 install ./reporting/helm/elastic-chart  -n reporting-elastic --namespace reporting
rm -rf reporting
```

#### Install Agent

```
helm registry install quay.io/giantswarm/reporting-agent-chart -- --namespace reporting -n reporting-agent
```

#### Install Processor
```
helm registry install quay.io/giantswarm/reporting-processor-chart -- --namespace reporting -n reporting-processor
```

#### Install Querying
```
helm registry install quay.io/giantswarm/reporting-querying-chart -- --namespace reporting -n reporting-querying
```

#### Tear Down everything

```
helm delete --purge reporting-elastic  reporting-agent reporting-processor reporting-querying 

kubectl -n reporting delete jobs --all

```