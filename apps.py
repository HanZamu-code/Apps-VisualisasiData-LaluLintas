import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

st.title("Analysis Data Lalu Lintas dan Angkutan Jalan Provinsi DKI Jakarta ")
st.markdown("Data Penindakan Pelanggaran Lalu Lintas dan Angkutan Jalan Tahun 2021 Bulan Mei")

st.sidebar.title("Analysis Data")
st.sidebar.markdown("Aplikasi adalah aplikasi untuk menvisualisasi dalam menganalisis Pelanggaran Lalu Lintas dan Angkutan Jalan Provinsi DKI Jakarta")

DATA_URL = ("Lalulintas.csv")

def load_data():
    data = pd.read_csv(DATA_URL)
    return data

data = load_data()
st.dataframe(data) 
st.info(data) 

# ---- SIDEBAR ----
st.sidebar.subheader("Select item data disini :")

choice = st.sidebar.multiselect("Pilih Wilayah", ('Bidang Dalops', 'Sudinhub Jakarta Pusat', 'Sudinhub Jakarta Utara', 'Sudinhub Jakarta Selatan', 'Sudinhub Jakarta Barat', 'Sudinhub Jakarta Timur'), key = '0')
if len(choice) >0:
    choice_data = data[data.wilayah.isin(choice)]
    fig_1 = px.histogram(choice_data, x='wilayah', y='bap_tilang', histfunc='sum', color='wilayah', labels={'wilayah':'Wilayah'},  title="<b>Wilayah yang Sering Terkena Tilang</b>", height=600, width=800)
    st.plotly_chart(fig_1)

if len(choice) >0:
    choice_data = data[data.wilayah.isin(choice)]
    fig_2 = px.pie(choice_data, values='bap_tilang', names='wilayah', title="<b>Wilayah yang Sering Terkena Tilang</b>")
    st.plotly_chart(fig_2)

st.sidebar.subheader("Filter item data disini :")
choice1 = st.sidebar.multiselect("Pilih Wilayah", ('Bidang Dalops', 'Sudinhub Jakarta Pusat', 'Sudinhub Jakarta Utara', 'Sudinhub Jakarta Selatan', 'Sudinhub Jakarta Barat', 'Sudinhub Jakarta Timur'), key = '1')
if len(choice1) >0:
    choice_data1 = data[data.wilayah.isin(choice1)]
    fig_3 = px.pie(choice_data1, values='angkut_motor', names='wilayah', title="<b>Wilayah dengan kendaran Terangkut</b>")
    st.plotly_chart(fig_3)

choice2 = st.sidebar.multiselect("Pilih Wilayah", ('Bidang Dalops', 'Sudinhub Jakarta Pusat', 'Sudinhub Jakarta Utara', 'Sudinhub Jakarta Selatan', 'Sudinhub Jakarta Barat', 'Sudinhub Jakarta Timur'), key = '2')
if len(choice2) >0:
    choice_data2 = data[data.wilayah.isin(choice2)]
    fig_4 = px.histogram(choice_data2, x='wilayah', y='penderekan', histfunc='sum', color='wilayah', labels={'wilayah':'Wilayah'},  title="<b>Wilayah dengan kendaran terkena Penderekan</b>", height=600, width=800)
    st.plotly_chart(fig_4)