# Reporting tool

The reporting tool is a collection of different components to discover bad practices in a Kubernetes cluster(s).

There are three main components:

- Agent: It lives in the target cluster to forward the pod definition to a external database.

- Processor: It is in charge of sanitize and enhance the ingested documents from targeted clusters. It add some metada to make the alerting process easier.

- Querying: It checks the processed documents looking for bad practices in the pod definitions (no limits, secrets as envs, ...). All found documents that fulfill the conditions are saved in a new DB in order to have an up to date index with all alerts.


The processor and querying components can run in the same cluster on the agent or in a differnet one, but the Elastic Search used to save the data should be accessible from the agent component. 

Diagram

![](/img/architecture.jpg)
