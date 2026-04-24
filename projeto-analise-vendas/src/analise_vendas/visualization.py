import matplotlib.pyplot as plt

def plot_kpis(kpis):
    nomes = ["Receita", "lucro", "Tciket medio"]
    valores = [
        
        float(kpis["receita_total"]),
        float(kpis["lucro_total"]),
        float(kpis["ticket_medio"])
        ]
    plt.figure()
    plt.bar(nomes, valores)

    plt.title("KPIs de Negócio")
    plt.xlabel("KPIs")
    plt.ylabel("Valores (R$)")

    plt.show()
    
