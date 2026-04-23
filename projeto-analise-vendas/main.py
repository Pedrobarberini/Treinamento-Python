

from src.data_loading import carregar_dados
from src.data_cleaning import limpar_pedidos, limpar_produtos, limpar_clientes
from src.data_processing import integrar_dados, criar_variaveis
from src.analysis import calcular_kpis

def main():
    
    print("iniciando pipeline de dados...\n")

    pedidos, produtos, clientes = carregar_dados()
    print("dados carregados com sucesso!\n")

    pedidos = limpar_pedidos(pedidos)
    produtos = limpar_produtos(produtos)
    clientes = limpar_clientes(clientes)

    print("dados limpos com sucesso!\n")

    df = integrar_dados(pedidos, produtos, clientes)
    df = criar_variaveis(df)
    print("dados processados com sucesso!\n")


    kpis = calcular_kpis(df)

    print("KPIs calculados com sucesso!\n")
    print(kpis)

    df.to_csv("data/processed/dados_integrados.csv", index=False)
    print("dados integrados salvos com sucesso!\n")

    print("pipeline de dados finalizada com sucesso!")


if __name__ == "__main__":
    main()


