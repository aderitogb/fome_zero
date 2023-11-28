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
st.write('# Países 🌎')
st.markdown('---')
st.sidebar.markdown('')
st.sidebar.markdown('')


# =======================================================
#  VISÃO 1
# =======================================================
with st.container():
    st.markdown('##### Quantidade de restaurantes por país')
    aux = df_filter.loc[:, ['country_code', 'restaurant_id']].groupby(
        'country_code').nunique().sort_values('restaurant_id', ascending=False).reset_index()
    fig = px.bar(aux, x='country_code', y='restaurant_id',  labels={
                 'country_code': 'País', 'restaurant_id': 'Qunatidade de restaurantes'}, text_auto='.0f')
    fig.update_traces(textfont_size=16, textangle=0,
                      textposition="outside", cliponaxis=False)
    fig.update_traces(marker_color='rgb(0,0,153)',
                      marker_line_color='rgb(0,0,0)', marker_line_width=1, opacity=0.8)
    fig.update_layout(xaxis_tickangle=0)
    fig.update_yaxes(showgrid=False, showticklabels=False)
    fig.update_xaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True)


# =======================================================
#  VISÃO 2
# =======================================================
with st.container():
    st.markdown('##### Quantidade de cidades por país')
    aux = df_filter.loc[:, ['city', 'country_code']].groupby(
        'country_code').nunique().sort_values('city', ascending=False).reset_index()
    fig = px.bar(aux, x='country_code', y='city',  labels={
                 'country_code': 'País', 'city': 'Quantidade de cidades'}, text_auto='.0f')
    fig.update_traces(textfont_size=16, textangle=0,
                      textposition="outside", cliponaxis=False)
    fig.update_traces(marker_color='rgb(0,0,153)',
                      marker_line_color='rgb(0,0,0)', marker_line_width=1, opacity=0.8)
    fig.update_layout(xaxis_tickangle=0)
    fig.update_yaxes(showgrid=False, showticklabels=False)
    fig.update_xaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True)


# =======================================================
#  VISÃO 3
# =======================================================
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('##### Média de avaliações por país')
        aux = df_filter.loc[:, ['country_code', 'votes']].groupby(
            'country_code').mean().sort_values('votes', ascending=False).reset_index()
        fig = px.bar(aux, x='country_code', y='votes',  labels={
                     'country_code': 'País', 'votes': 'Quantidade de avaliações'}, text_auto='.2f')
        fig.update_traces(textfont_size=16, textangle=0,
                          textposition="outside", cliponaxis=False)
        fig.update_traces(marker_color='rgb(0,0,153)',
                          marker_line_color='rgb(0,0,0)', marker_line_width=1, opacity=0.8)
        fig.update_layout(xaxis_tickangle=-90)
        fig.update_yaxes(showgrid=False, showticklabels=False)
        fig.update_xaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown('##### Preço médio de um prato para 2 pessoas por país')
        aux = df_filter[['country_code', 'average_cost_for_two']].groupby(
            'country_code').mean().sort_values('average_cost_for_two', ascending=False).reset_index()
        fig = px.bar(aux, x='country_code', y='average_cost_for_two',  labels={
                     'country_code': 'País', 'average_cost_for_two': 'Preço médio para 2 pessoas'}, text_auto='.2f')
        fig.update_traces(textfont_size=16, textangle=0,
                          textposition="outside", cliponaxis=False)
        fig.update_traces(marker_color='rgb(0,0,153)',
                          marker_line_color='rgb(0,0,0)', marker_line_width=1, opacity=0.8)
        fig.update_layout(xaxis_tickangle=-90)
        fig.update_yaxes(showgrid=False, showticklabels=False)
        fig.update_xaxes(showgrid=False)
        st.plotly_chart(fig, use_container_width=True)
