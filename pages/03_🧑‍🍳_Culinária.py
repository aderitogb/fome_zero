import plotly.express as px
import streamlit as st
from PIL import Image

from utils.process_data import process_data

# =======================================================
#  DADOS
# =======================================================

# Carrega dados
RAW_DATA_PATH = f"./dados/zomato.csv"
# Tratamento de dados
df = process_data(RAW_DATA_PATH)

# =======================================================
#  STREAMLIT
# =======================================================

# =======================================================
#  CONFIGURA PÁGINA
# =======================================================
st.set_page_config(page_title='Fome Zero',
                   page_icon='🍽️',
                   layout="wide",
                   initial_sidebar_state="auto",
                   menu_items=None)

path = f"./img/"
image = Image.open(path + 'fome_zero.png')


# =======================================================
#  BARRA LATERAL
# =======================================================
st.sidebar.markdown('# **Fome Zero** 🍽️')
st.sidebar.image(image, width=300)
st.sidebar.markdown('---')


st.sidebar.markdown("### Filtros")

paises_options = st.sidebar.multiselect('Selecione os países que deseja visualizar',
                                        df['country_code'].sort_values(
                                            ascending=True).unique(),
                                        default=['Brazil', 'England', 'Qatar', 'South Africa', 'Canada', 'Australia'])
st.sidebar.markdown('---')

qtd_restaurante_options = st.sidebar.slider('Selecione a quantidade de restaurantes que deseja visualizar',
                                            value=10,
                                            min_value=1,
                                            max_value=50)
st.sidebar.markdown('---')

culinaria_options = st.sidebar.multiselect('Selecione os tipos de culinária que deseja visualizar',
                                           df['cuisines'].sort_values(
                                               ascending=True).unique(),
                                           default=['Arabian', 'American', 'BBQ', 'Brazilian', 'Italian', 'Japanese'])
st.sidebar.markdown('---')

st.sidebar.markdown('')
st.sidebar.markdown('##### Criado por **Adérito Bernardes**')


# =======================================================
#  APLICANDO FILTROS
# =======================================================
df_filter = df[(df['country_code'].isin(paises_options))
               & (df['cuisines'].isin(culinaria_options))]


# =======================================================
#  LAYOUT STREAMLIT
# =======================================================
st.write('# Culinária 🧑‍🍳')
st.markdown('---')
st.sidebar.markdown('')
st.sidebar.markdown('')


# =======================================================
#  MÉTRICAS GERAIS
# =======================================================
st.markdown('## Melhores restaurantes dos principais tipos culinários')
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5, gap='large')
    with col1:
        aux = df.loc[df['cuisines'] == 'Italian', :]
        aux = aux[['restaurant_name', 'aggregate_rating', 'restaurant_id']].groupby(
            'restaurant_name').agg({'aggregate_rating': 'mean', 'restaurant_id': 'min'})
        aux.columns = ['aggregate_rating', 'restaurant_id']
        aux = aux.reset_index().sort_values(
            by=['aggregate_rating', 'restaurant_id'], ascending=[False, True])
        top_cuisines = df[(df['cuisines'] == 'Italian') &
                          (df['restaurant_name'] == aux.iloc[0, 0])
                          ].iloc[0, :].to_dict()
        st.metric(label=f'Italiana: {aux.iloc[0,0]}',
                  value=f'{aux.iloc[0, 1]}⭐',
                  help=f"""
                      País: {top_cuisines['country_code']}\n
                      Cidade: {top_cuisines['city']}\n
                      Avaliações: {top_cuisines['votes']}\n                      
                      Média Prato para dois: {top_cuisines['average_cost_for_two']} ({top_cuisines['currency']})
                      """)

    with col2:
        aux = df.loc[df['cuisines'] == 'American', :]
        aux = aux[['restaurant_name', 'aggregate_rating', 'restaurant_id']].groupby(
            'restaurant_name').agg({'aggregate_rating': 'mean', 'restaurant_id': 'min'})
        aux.columns = ['aggregate_rating', 'restaurant_id']
        aux = aux.reset_index().sort_values(
            by=['aggregate_rating', 'restaurant_id'], ascending=[False, True])
        top_cuisines = df[(df['cuisines'] == 'American') &
                          (df['restaurant_name'] == aux.iloc[0, 0])
                          ].iloc[0, :].to_dict()
        st.metric(label=f'Americana: {aux.iloc[0,0]}',
                  value=f'{aux.iloc[0, 1]}⭐',
                  help=f"""
                      País: {top_cuisines['country_code']}\n
                      Cidade: {top_cuisines['city']}\n
                      Avaliações: {top_cuisines['votes']}\n
                      Média Prato para dois: {top_cuisines['average_cost_for_two']} ({top_cuisines['currency']})
                      """)

    with col3:
        aux = df.loc[df['cuisines'] == 'Arabian', :]
        aux = aux[['restaurant_name', 'aggregate_rating', 'restaurant_id']].groupby(
            'restaurant_name').agg({'aggregate_rating': 'mean', 'restaurant_id': 'min'})
        aux.columns = ['aggregate_rating', 'restaurant_id']
        aux = aux.reset_index().sort_values(
            by=['aggregate_rating', 'restaurant_id'], ascending=[False, True])
        top_cuisines = df[(df['cuisines'] == 'Arabian') &
                          (df['restaurant_name'] == aux.iloc[0, 0])
                          ].iloc[0, :].to_dict()
        st.metric(label=f'Árabe: {aux.iloc[0,0]}',
                  value=f'{aux.iloc[0, 1]}⭐',
                  help=f"""
                      País: {top_cuisines['country_code']}\n
                      Cidade: {top_cuisines['city']}\n
                      Avaliações: {top_cuisines['votes']}\n
                      Média Prato para dois: {top_cuisines['average_cost_for_two']} ({top_cuisines['currency']})
                      """)
    with col4:
        aux = df.loc[df['cuisines'] == 'Japanese', :]
        aux = aux[['restaurant_name', 'aggregate_rating', 'restaurant_id']].groupby(
            'restaurant_name').agg({'aggregate_rating': 'mean', 'restaurant_id': 'min'})
        aux.columns = ['aggregate_rating', 'restaurant_id']
        aux = aux.reset_index().sort_values(
            by=['aggregate_rating', 'restaurant_id'], ascending=[False, True])
        top_cuisines = df[(df['cuisines'] == 'Japanese') &
                          (df['restaurant_name'] == aux.iloc[0, 0])
                          ].iloc[0, :].to_dict()
        st.metric(label=f'Japonesa: {aux.iloc[0,0]}',
                  value=f'{aux.iloc[0, 1]}⭐',
                  help=f"""
                      País: {top_cuisines['country_code']}\n
                      Cidade: {top_cuisines['city']}\n
                      Avaliações: {top_cuisines['votes']}\n
                      Média Prato para dois: {top_cuisines['average_cost_for_two']} ({top_cuisines['currency']})
                      """)
    with col5:
        aux = df.loc[df['cuisines'] == 'Brazilian', :]
        aux = aux[['restaurant_name', 'aggregate_rating', 'restaurant_id']].groupby(
            'restaurant_name').agg({'aggregate_rating': 'mean', 'restaurant_id': 'min'})
        aux.columns = ['aggregate_rating', 'restaurant_id']
        aux = aux.reset_index().sort_values(
            by=['aggregate_rating', 'restaurant_id'], ascending=[False, True])
        top_cuisines = df[(df['cuisines'] == 'Brazilian') &
                          (df['restaurant_name'] == aux.iloc[0, 0])
                          ].iloc[0, :].to_dict()
        st.metric(label=f'Brasileira: {aux.iloc[0,0]}',
                  value=f'{aux.iloc[0, 1]}⭐',
                  help=f"""
                      País: {top_cuisines['country_code']}\n
                      Cidade: {top_cuisines['city']}\n
                      Avaliações: {top_cuisines['votes']}\n
                      Média Prato para dois: {top_cuisines['average_cost_for_two']} ({top_cuisines['currency']})
                      """)
st.markdown('---')

# =======================================================
#  VISÃO 2
# =======================================================
st.markdown(f"##### Top {qtd_restaurante_options} Restaurantes")
cols = ["restaurant_id",
        "restaurant_name",
        "country_code",
        "city",
        "cuisines",
        "average_cost_for_two",
        "currency",
        "aggregate_rating",
        "votes"]

st.dataframe(df_filter[cols].sort_values(["aggregate_rating", "restaurant_id"], ascending=[
             False, True]).head(qtd_restaurante_options), hide_index=True, use_container_width=True, column_config={'restaurant_id': st.column_config.NumberColumn('Restaurante ID', format="%.0f"),
                                                                                                                    'restaurant_name': 'Nome Restaurante',
                                                                                                                    'country_code': 'País',
                                                                                                                    'city': 'Cidade',
                                                                                                                    'cuisines': 'Culinária',
                                                                                                                    'average_cost_for_two': st.column_config.NumberColumn('Custo para 2 pessoas', format="%.2f 💵"),
                                                                                                                    'currency': 'Moeda',
                                                                                                                    'aggregate_rating': st.column_config.NumberColumn('Avaliação média', format="%.2f ⭐"),
                                                                                                                    'votes': st.column_config.NumberColumn('Avaliações', format="%.0f 🗳️")
                                                                                                                    })


# =======================================================
#  VISÃO 3
# =======================================================
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('##### Top 10 melhores tipos de culinárias')
        aux = df_filter[['cuisines', 'aggregate_rating']].groupby('cuisines').mean(
        ).reset_index().sort_values(by=['aggregate_rating'], ascending=False)
        fig = px.bar(aux.head(10), x='cuisines', y='aggregate_rating',  labels={
                     'cuisines': 'Tipo de culinária', 'aggregate_rating': 'Avaliação média'}, text_auto='.2f')
        fig.update_traces(textfont_size=16, textangle=0,
                          textposition="outside", cliponaxis=False)
        fig.update_traces(marker_color='rgb(0,0,153)',
                          marker_line_color='rgb(0,0,0)', marker_line_width=1, opacity=0.8)
        fig.update_layout(xaxis_tickangle=-90)
        fig.update_yaxes(showgrid=False, showticklabels=False)
        fig.update_xaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown('##### Top 10 piores tipos de culinárias')
        aux = df_filter[['cuisines', 'aggregate_rating']].groupby('cuisines').mean(
        ).reset_index().sort_values(by=['aggregate_rating'], ascending=True)
        fig = px.bar(aux.head(10), x='cuisines', y='aggregate_rating',  labels={
                     'cuisines': 'Tipo de culinária', 'aggregate_rating': 'Avaliação média'}, text_auto='.2f')
        fig.update_traces(textfont_size=16, textangle=0,
                          textposition="outside", cliponaxis=False)
        fig.update_traces(marker_color='rgb(0,0,153)',
                          marker_line_color='rgb(0,0,0)', marker_line_width=1, opacity=0.8)
        fig.update_layout(xaxis_tickangle=-90)
        fig.update_yaxes(showgrid=False, showticklabels=False)
        fig.update_xaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)
