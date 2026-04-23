import pandas as pd

def carregar_dados ():

    path_pedidos  = "data/raw/pedidos.csv"
    path_produtos = "data/raw/produtos.csv"
    path_clientes = "data/raw/clientes.csv"

    pedidos = pd.read_csv(path_pedidos)
    produtos = pd.read_csv(path_produtos)
    clientes = pd.read_csv(path_clientes)

    return pedidos, produtos, clientes;