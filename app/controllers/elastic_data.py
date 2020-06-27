from flask import jsonify
from app import es


"""
queries
"""

def produtos_query():
    body = {
        "size":100,
        "query": {
            "match_all":{}
        }
    }

    res = es.search(index="produto", body=body)

    resp = []
    for produtos in res['hits']['hits']:
        resp.append(produtos['_source'])
    return resp




