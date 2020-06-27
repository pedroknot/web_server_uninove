#!/bin/bash
# for i in *.json; do
#   curl -XPOST http://localhost:9200/produto/doc/_bulk -H "Content-Type: application/x-ndjson" --data-binary @$i 
# done

#indexao via bulk
curl -XPOST http://localhost:9200/produto/doc/_bulk -H "Content-Type: application/x-ndjson" --data-binary @output_crawler_mercado.json
