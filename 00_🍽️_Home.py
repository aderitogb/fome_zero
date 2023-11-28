import folium
import pandas as pd
import streamlit as st
from folium.plugins import MarkerCluster
from PIL import Image
from streamlit_folium import folium_static

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


st.sidebar.markdown("### Dados Tratados")
processed_data = pd.read_csv(
    "./dados/dados_tratados.csv", sep=';', encoding='utf-8-sig')
st.sidebar.download_button(
    label="Download",
    data=processed_data.to_csv(index=False, sep=';', encoding='utf-8-sig'),
    file_name="data.csv",
    mime="text/csv"
)

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
st.write('# Fome Zero! 🍽️')
st.markdown('---')
st.markdown("""
            ## O melhor lugar para encontrar o seu mais novo restaurante favorito!
            ### Temos as seguintes marcas dentro da nossa plataforma:
            """)

# =======================================================
#  MÉTRICAS GERAIS
# =======================================================
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric(label='Restaurantes cadastrados',
                  value=len(df['restaurant_id'].unique()))
    with col2:
        st.metric(label='Países cadastrados',
                  value=len(df['country_code'].unique()))
    with col3:
        st.metric(label='Cidades cadastrados',
                  value=len(df['city'].unique()))
    with col4:
        st.metric(label='Avaliações feitas',
                  value=f"{df['votes'].sum():,}".replace(",", "."))
    with col5:
        st.metric(label='Tipos de culinárias',
                  value=len(df['cuisines'].unique()))
st.markdown('---')

# =======================================================
#  MAPA
# =======================================================
f = folium.Figure(width=1920, height=1080)
m = folium.Map(max_bounds=True, zoom_start=13).add_to(f)
marker_cluster = MarkerCluster().add_to(m)

for _, line in df_filter.iterrows():
    name = line["restaurant_name"]
    price_for_two = line["average_cost_for_two"]
    cuisine = line["cuisines"]
    currency = line["currency"]
    rating = line["aggregate_rating"]
    color = f'{line["rating_color"]}'

    html = "<p><strong>{} 🍽️ </strong></p>"
    html += "<p>Preço para dois: {},00 ({})"
    html += "<br />Tipo culinária: {}"
    html += "<br />Avaliação: {} ⭐"
    html = html.format(name, price_for_two, currency, cuisine, rating)

    popup = folium.Popup(
        folium.Html(html, script=True),
        max_width=500,
    )

    folium.Marker(
        [line["latitude"], line["longitude"]],
        popup=popup,
        icon=folium.Icon(color=color, icon="utensils", prefix="fa"),
    ).add_to(marker_cluster)

folium_static(m, width=1024, height=768)
