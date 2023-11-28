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

st.sidebar.markdown('')
st.sidebar.markdown('##### Criado por **Adérito Bernardes**')

# =======================================================
#  APLICANDO FILTROS
# =======================================================
df_filter = df[df['country_code'].isin(paises_options)]


# =======================================================
#  LAYOUT STREAMLIT
# =======================================================
st.write('# Cidades 🏙️')
st.markdown('---')
st.sidebar.markdown('')
st.sidebar.markdown('')

# =======================================================
#  VISÃO 1
# =======================================================
with st.container():
    st.markdown('##### Top 10 cidades com mais restaurantes registrados')
    aux = df_filter.loc[:, ['country_code', 'city', 'restaurant_id']].groupby(
        ['country_code', 'city']).agg({'restaurant_id': ['count', 'min']})
    aux.columns = ['qtd', 'min']
    aux = aux.reset_index().sort_values(
        by=['qtd', 'min'], ascending=[False, True])
    fig = px.bar(aux.head(10), x='city', y='qtd',  labels={
                 'city': 'Cidade', 'qtd': 'Quantidade de restaurantes', 'country_code': 'País'}, text_auto='.0f', color='country_code')
    fig.update_traces(textfont_size=16, textangle=0,
                      textposition="outside", cliponaxis=False)
    fig.update_layout(xaxis_tickangle=-45)
    fig.update_yaxes(showgrid=False, showticklabels=False)
    fig.update_xaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True)


# =======================================================
#  VISÃO 2
# =======================================================
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            '##### Top 10 cidades com restaurantes com média de avaliação acima de 4⭐')
        aux = df_filter.loc[df_filter['aggregate_rating'] >= 4, ['country_code', 'city', 'restaurant_id']].groupby(
            ['country_code', 'city']).agg({'restaurant_id': ['count', 'min']})
        aux.columns = ['qtd', 'min']
        aux = aux.sort_values(by=['qtd', 'min'], ascending=[
                              False, True]).reset_index()
        fig = px.bar(aux.head(10), x='city', y='qtd',  labels={
                     'city': 'Cidade', 'qtd': 'Quantidade de restaurantes', 'country_code': 'País'}, text_auto='.0f', color='country_code')
        fig.update_traces(textfont_size=16, textangle=0,
                          textposition="outside", cliponaxis=False)
        fig.update_layout(xaxis_tickangle=-90)
        fig.update_yaxes(showgrid=False, showticklabels=False)
        fig.update_xaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown(
            '##### Top 10 cidades com restaurantes com média de avaliação abaixo de 2.5⭐')
        aux = df_filter.loc[df_filter['aggregate_rating'] <= 2.5, ['country_code', 'city', 'restaurant_id']].groupby(
            ['country_code', 'city']).agg({'restaurant_id': ['count', 'min']})
        aux.columns = ['qtd', 'min']
        aux = aux.reset_index().sort_values(
            by=['qtd', 'min'], ascending=[False, True])
        fig = px.bar(aux.head(10), x='city', y='qtd', labels={
                     'city': 'Cidade', 'qtd': 'Quantidade de restaurantes', 'country_code': 'País'}, text_auto='.0f', color='country_code')
        fig.update_traces(textfont_size=16, textangle=0,
                          textposition="outside", cliponaxis=False)
        fig.update_layout(xaxis_tickangle=-90)
        fig.update_yaxes(showgrid=False, showticklabels=False)
        fig.update_xaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)


# =======================================================
#  VISÃO 3
# =======================================================
with st.container():
    st.markdown(
        '##### Top 10 cidades com mais restaurantes com tipos de culinária distintos')
    aux = df_filter[['country_code', 'city', 'cuisines']].groupby(
        ['country_code', 'city']).nunique().sort_values(by=['cuisines'], ascending=False).reset_index()
    fig = px.bar(aux.head(10), x='city', y='cuisines',  labels={
                 'city': 'Cidade', 'cuisines': 'Tipos de culinárias', 'country_code': 'País'}, text_auto='.0f', color='country_code')
    fig.update_traces(textfont_size=16, textangle=0,
                      textposition="outside", cliponaxis=False)
    fig.update_layout(xaxis_tickangle=-90)
    fig.update_yaxes(showgrid=False, showticklabels=False)
    fig.update_xaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True)
