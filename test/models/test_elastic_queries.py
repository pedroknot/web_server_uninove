"""Documentação do módulo
   Tests elasticsearch queries
"""
from app.models.elastic_queries import ElasticQueries

elastic = ElasticQueries()

def test_produtos_search():
    """ Test querie math_all """

    output = [{
        "categoriaId" : 4233,
        "categoriaNome" : "Limpeza",
        "subcategoriaId" : 4448,
        "subcategoriaNome" : "Alcool e removedor",
        "produtoId" : 155006,
        "produtoSku" : "1039443",
        "produtoPreco" : 27.49,
        "produtoPrecoVenda" : 27.49,
        "produtoNome" : "Removedor sem Cheiro VIMAK 500ml",
        "timestamp" : "2018-11-19 23:00:18"
        }]

    assert elastic.produtos_search() == output
