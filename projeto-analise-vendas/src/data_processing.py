import pandas as pd
import numpy as np


def integrar_dados(pedidos, produtos, clientes):
    # Merge pedidos com produtos para obter detalhes dos produtos
    pedidos_produtos = pedidos.merge(produtos, on='produto_id', how='left')
    
    # Merge o resultado com clientes para obter detalhes dos clientes
    dados_integrados = pedidos_produtos.merge(clientes, on='cliente_id', how='left')
    
    return dados_integrados

def criar_variaveis(dados):

    dados = dados.copy()
    dados['data_pedido'] = pd.to_datetime(dados['data_pedido'])
    dados['ano'] = dados['data_pedido'].dt.year
    dados['mes'] = dados['data_pedido'].dt.month
    dados['dia'] = dados['data_pedido'].dt.day
    dados['valor_total'] = dados['quantidade'] * dados['preco_unitario']
    return dados