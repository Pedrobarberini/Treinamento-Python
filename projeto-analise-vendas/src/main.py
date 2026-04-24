from analise_vendas.data_loading import carregar_dados
from analise_vendas.data_cleaning import limpar_pedidos, limpar_produtos, limpar_clientes
from analise_vendas.data_processing import integrar_dados, criar_variaveis
from analise_vendas.analysis import calcular_kpis
from analise_vendas.visualization import plot_kpis, plot_receita_mensal
import os 

def main():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    print("iniciando pipeline de dados...\n")

    pedidos, produtos, clientes = carregar_dados()
    print("dados carregados com sucesso!\n")

    pedidos = limpar_pedidos(pedidos)
    print("dados de pedidos limpos com sucesso!\n")
    produtos = limpar_produtos(produtos)
    print("dados de produtos limpos com sucesso!\n")
    clientes = limpar_clientes(clientes)
    print("dados de clientes limpos com sucesso!\n")

    print("dados limpos com sucesso!\n")
    pedidos.to_csv((os.path.join(base_path, "data", "processed", "dados_limpos.csv")), index=False)

    df = integrar_dados(pedidos, produtos, clientes)
    print("dados integrados com sucesso!\n")
    df = criar_variaveis(df)
    print("variáveis criadas com sucesso!\n")
    
    print("dados processados com sucesso!\n")
    df.to_csv((os.path.join(base_path, "data", "processed", "dados_processados.csv")), index=False)



    kpis = calcular_kpis(df)

    for chave, valor in kpis.items():
        print(f"{chave}: R$ {float(valor):,.2f}")
    

    df.to_csv((os.path.join(base_path, "data", "processed", "dados_integrados.csv")), index=False)
    print("dados integrados salvos com sucesso!\n")

    print("pipeline de dados finalizada com sucesso!")

    plot_kpis(kpis, df)
    plot_receita_mensal(df)

if __name__ == "__main__":
    main()


