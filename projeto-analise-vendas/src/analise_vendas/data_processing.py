import pandas as pd
import os


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

    dados['custo_total'] = dados['quantidade'] * dados['preco_custo']

    dados['lucro'] = dados['valor_total'] - dados['custo_total']
    return dados

def carregar_dados():
    base_path = os.path.dirname(os.path.dirname(__file__))

    path_pedidos = os.path.join(base_path, "data","raw","pedidos.csv")
    path_produtos = os.path.join(base_path, "data","raw","produtos.csv")
    path_clientes = os.path.join(base_path, "data","raw","clientes.csv")

    pedidos = pd.read_csv(path_pedidos)
    produtos = pd.read_csv(path_produtos)
    clientes = pd.read_csv(path_clientes)

    return pedidos, produtos, clientes