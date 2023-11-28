import pandas as pd
import inflection

# Ajustando o nome das colunas


def rename_columns(dataframe):
    df = dataframe.copy()
    def title(x): return inflection.titleize(x)
    def snakecase(x): return inflection.underscore(x)
    def spaces(x): return x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df


def process_data(file_path):
    df = pd.read_csv(file_path)
    df1 = df.copy()

    # Retirando dados faltantes
    df1 = df1.dropna()

    # Retirando linhas duplicadas
    df1 = df1.drop_duplicates()

    # Retirando coluna Switch to order menu
    df1 = df1.drop(['Switch to order menu'], axis=1)

    # categorizando a coluna de codigo do pais
    COUNTRIES = {1: "India",
                 14: "Australia",
                 30: "Brazil",
                 37: "Canada",
                 94: "Indonesia",
                 148: "New Zeland",
                 162: "Philippines",
                 166: "Qatar",
                 184: "Singapure",
                 189: "South Africa",
                 191: "Sri Lanka",
                 208: "Turkey",
                 214: "United Arab Emirates",
                 215: "England",
                 216: "United States of America"
                 }
    df1['Country Code'] = df1['Country Code'].map(COUNTRIES)

    # categorizando a coluna de price range
    df1['Price range'] = df1['Price range'].apply(
        lambda x: "cheap" if x == 1 else "normal" if x == 2 else "expensive" if x == 3 else "gourmet")

    # categorizando a coluna de cores
    COLORS = {
        "3F7E00": "darkgreen",
        "5BA829": "green",
        "9ACD32": "lightgreen",
        "CDD614": "orange",
        "FFBA00": "red",
        "CBCBC8": "darkred",
        "FF7800": "darkred",
    }
    df1['Rating color'] = df1['Rating color'].map(COLORS)

    # pegando o primeiro campo da coluna Cuisines
    # categorizar, inicialmente, todos os restaurantes somente por um tipo de culinária
    df1["Cuisines"] = df1.loc[:, "Cuisines"].apply(lambda x: x.split(",")[0])

    df1 = df1.drop(df1[(df1["Cuisines"] == "Drinks Only")].index)

    df1 = df1.drop(df1[(df1["Cuisines"] == "Mineira")].index)

    df1 = rename_columns(df1)

    df1 = df1.reset_index(drop=True)

    df1.to_csv('./dados/dados_tratados.csv',
               index=False, sep=';', encoding='utf-8-sig')

    return df1
