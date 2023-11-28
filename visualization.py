import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def visualization():
    data1 = pd.read_csv("rice_wheat_corn_prices.csv")
    print(data1.head(5))
    data1.drop_duplicates()
    data1 = data1.dropna()
    print(data1.head(30))

    def showlineplot(style, x, y, dataframe, alhp, rot, color, xlabel, ylabel, title):
        sns.set_style(style)
        sns.lineplot(x=x,
                     y=y,
                     data=dataframe,
                     alpha=alhp,
                     color=color
                     )
        plt.xticks(rotation=rot)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()

    print("Annual Wheat Price Graph")
    df_year_wheat = data1.groupby(["Year"])['Price_wheat_ton'].sum().reset_index()
    showlineplot("darkgrid", "Year", "Price_wheat_ton", df_year_wheat, 0.7, 80, "#129632", 'Years', "Price Wheat Tone",
                 "Prices 1992 with 2021")

    df_year_corn = data1.groupby(["Year"])["Price_corn_ton"].sum().reset_index()
    showlineplot("darkgrid", "Year", "Price_corn_ton", df_year_corn, 1, 80, "#129632", "Years", "Price Corn Tone",
                 "Prices 1992 with 2021")

    df_year_rice = data1.groupby(["Year"])["Price_rice_ton"].sum().reset_index()
    showlineplot("darkgrid", "Year", "Price_rice_ton", df_year_rice, 1, 80, "#88f113", "Years", "Price Rice Tone",
                 "Prices 1992 with 2021")

    print("Wheat Price Analyz for All Years Except 2022")

    # We erase the 2022 in data. Because 2022 values is a another column (Price_wheat_ton_infl)
    # If we dont filter [:30] 2022 count will a '0' value
    dataAllYears = data1.groupby(['Year'])['Price_wheat_ton'].sum().reset_index()

    # But this situation
    dataExcept2022Wheat = data1.groupby(['Year'])['Price_wheat_ton'].sum().reset_index()[:30]
    print(dataExcept2022Wheat)

    plt.figure(figsize=(18, 6))
    sns.set_style("darkgrid", {"axes.facecolor": ".8"})
    ax = sns.pointplot(x='Year',
                       y='Price_wheat_ton',
                       data=dataExcept2022Wheat,
                       alpha=0.2)

    plt.xticks(rotation=70)
    plt.xlabel('Years')
    plt.ylabel('Price Wheat Ton')
    plt.title('Prices 1992 to 2021')
    plt.show()

    print("Rice Price Analyz for All Years Except 2022")

    dataExcept2022Rice = data1.groupby(['Year'])['Price_rice_ton'].sum().reset_index()[:30]
    print(dataExcept2022Rice)

    plt.figure(figsize=(18, 6))
    sns.set_style("dark")
    sns.lineplot(x='Year',
                 y='Price_rice_ton',
                 data=dataExcept2022Rice,
                 color='#483d8b',
                 alpha=0.8,
                 )
    plt.xticks(rotation=70)
    plt.xlabel('Years')
    plt.ylabel('Price Rice Ton')
    plt.title('Prices 1992 to 2021')
    plt.savefig('my_plot.eps', format='eps')
    plt.show()

    print("Corn Price Analyz for All Years Except 2022")
    dataExcept2022Corn = data1.groupby(['Year'])['Price_corn_ton'].sum().reset_index()[:30]

    print(dataExcept2022Corn)

    plt.figure(figsize=(18, 6))
    sns.set_style("dark")
    sns.lineplot(x='Year',
                 y='Price_corn_ton',
                 data=dataExcept2022Corn,
                 color='r',
                 alpha=0.8,
                 )
    plt.xticks(rotation=70)
    plt.xlabel('Years')
    plt.ylabel('Price Corn Ton')
    plt.title('Prices 1992 to 2021')
    plt.show()

    print("Price Analyz For 2022")
    data2022prizes = data1.groupby(['Month'])[
                         ['Price_wheat_ton_infl', 'Price_rice_ton_infl', 'Price_corn_ton_infl']].sum().reset_index()[
                     :30]
    print(data2022prizes)

    f, ax = plt.subplots(figsize=(15, 15))

    sns.set_color_codes("muted")
    sns.barplot(x='Price_rice_ton_infl', y='Month', data=data2022prizes,
                label='Rice Prize', color='#53325c')

    sns.set_color_codes("dark")
    sns.barplot(x='Price_wheat_ton_infl', y='Month', data=data2022prizes,
                label='Wheat Prize', color='b')

    sns.set_color_codes("pastel")
    sns.barplot(x='Price_corn_ton_infl', y='Month', data=data2022prizes,
                label='Corn Prize', color='r')

    ax.legend(loc="lower right")
    ax.set(xlim=(0, 16000), ylabel="Months",
           xlabel="Price variaton in 2022")
    sns.despine(left=True, bottom=True)
    plt.show()


visualization()
