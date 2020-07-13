from app import es


"""
Queries
"""
class ElasticQueries():
    def produtos_search(self, query="match_all"):
        body = {
            "size":1,
            "query": {
                f"{query}":{}
            }
        }

        res = es.search(index="produto", body=body)

        resp = []
        for produtos in res['hits']['hits']:
            resp.append(produtos['_source'])
        return resp




