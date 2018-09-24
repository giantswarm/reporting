
import os
import json
from elasticsearch import Elasticsearch

# print(os.environ['HOME'])
# print(os.environ['ELASTICSEARCH_INDEX_URL'])

# es = Elasticsearch('http://localhost:9200/')

host, index = os.environ['ELASTICSEARCH_INDEX_URL_AGENT'].rsplit('/', 1)
_, index_processing = os.environ['ELASTICSEARCH_INDEX_URL_PROCESSING'].rsplit('/', 1)
es = Elasticsearch([host])

# res = es.index(index=index, doc_type='_doc', id=1, body=doc)
# print(res['result'])
#
# res = es.get(index=index, doc_type='_doc', id=1)
# print(res['_source'])


res = es.search(index=index, body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])

for hit in res['hits']['hits'][0:1]:
    for item in hit["_source"]["items"]:
        # print(json.dumps(item, indent=2))
        print(item["kind"])

        res = es.index(index=index_processing, doc_type='_doc', id=1, body=item)
        print(res['result'])


# todo
# dest-index
# item["_reporting_meta"] = { customer, installation, node, }
