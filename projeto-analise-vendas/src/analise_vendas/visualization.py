import matplotlib.pyplot as plt


meses = {
    1: "Jan",
    2: "Fev",
    3: "Mar",
    4: "Abr",
    5: "Mai",
    6: "Jun",
    7: "Jul",
    8: "Ago",
    9: "Set",
    10: "Out",
    11: "Nov",
    12: "Dez"
}

def plot_kpis(kpis, df):
    nomes = ["Receita", "lucro", "Ticket médio"]
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
    plt.xticks(rotation=0)

    plt.show()

def plot_receita_mensal(df):
    receita_mensal = df.groupby(meses)['valor_total'].sum()

    plt.figure()
    receita_mensal.plot(kind='bar')
    plt.title("Receita Mensal")
    plt.xlabel("Mês")
    plt.ylabel("Receita (R$)")
    plt.xticks(rotation=0)


    plt.show()