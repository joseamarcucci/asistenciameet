import streamlit as st
import pandas as pd
import numpy as np
import pybase64
import io


import matplotlib.pyplot as plt
from fpdf import FPDF

from tempfile import NamedTemporaryFile
st.set_page_config(
page_title="Asistencia",
page_icon="https://webinars.usal.edu.ar/sites/default/files/favicon.ico",
layout="wide",
)
    #st.markdown('<img style="float: left;" src="https://virtual.usal.edu.ar/branding/themes/Usal_7Julio_2017/images/60usalpad.png" />', unsafe_allow_html=True)
st.markdown('<style>div[data-baseweb="select"] > div {text-transform: capitalize;}body{background-color:#008357;}</style>', unsafe_allow_html=True)
st.markdown(
    """<style>
        .css-19ih76x{text-align: left !important}
        .css-17eq0hr {
    background-color: #00b8e1;
    background-attachment: fixed;
    flex-shrink: 0;
    height: 100vh;
    overflow: auto;
    padding: 5rem 1rem;
    position: relative;
    transition: margin-left 300ms ease 0s, box-shadow 300ms ease 0s;
    width: 21rem;
    z-index: 100;
    margin-left: 0px;
}    .css-1v3fvcr {
    display: flex;
    flex-direction: column;
    width: 100%;
    margin-top: -100px;
    overflow: auto;
    -webkit-box-align: center;
    align-items: center;
    }
    .css-qbe2hs {
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.25rem;
    margin: 0px;
    line-height: 1.6;
    color: inherit;
    width: auto;
    text-decoration: none;
    background-color: rgb(255, 255, 255);
    border: 1px solid rgba(38, 39, 48, 0.2);
}
     .css-qbe2hs a{ text-decoration: none;}
    </style>
""", unsafe_allow_html=True) 

st.markdown("<h2 style='text-align: left; color: #00b8e1;'>Registración a Webinars 2021</h2>", unsafe_allow_html=True)
buff, col = st.beta_columns([2,2])

    #SHEET_ID = '12D4hfpuIkT7vM69buu-v-r-UYb8xx4wM1zi-34Fs9ck'

#data = [['Elaboración de un proyecto de investigación en Ciencias Sociales y Humanísticas', '965178173'], ['Elaboración de un proyecto de investigación en Ciencias Naturales y Exactas', '1829217201']]
data=pd.read_csv('https://docs.google.com/spreadsheets/d/1gltz1w3wS4krdU7md1vocTENb_ufRCGiKn2AUAuRFRc/export?format=csv')

# Create the pandas DataFrame
#df0 = pd.DataFrame(data, columns=['Webinar', 'Planilla'])

values = data['Webinar'].tolist()
options = data['Planilla'].tolist()
dic = dict(zip(options, values))

a = buff.selectbox('Seleccionar Webinar:', options, format_func=lambda x: dic[x])


df = pd.read_csv('https://docs.google.com/spreadsheets/d/'+a+'/export?format=csv')
inscriptostodos=df[['Marca temporal','Apellido','Nombre', 'Documento ','Institución a la que pertenece','Ocupación','Correo electrónico','Como conoció el Webinar','Desea recibir información de la actividades de la Universidad:']] 
inscriptostodos.index = [""] * len(inscriptostodos) 

df5=pd.value_counts(df['Correo electrónico'])
times3t=df5.index
aulast=len(times3t) 
with buff:st.write('Cantidad de inscriptos:',aulast) 
csv = inscriptostodos.to_csv(index=False)
b64 = pybase64.b64encode(csv.encode()).decode()  # some strings
linko= f'<a class="css-qbe2hs" href="data:file/csv;base64,{b64}" download="inscriptos.csv">Bajar csv</a>'
buff.markdown(linko, unsafe_allow_html=True)

if buff.checkbox('Ver todos'):
   buff.table(inscriptostodos) 
df['Marca temporal'] = pd.to_datetime(df['Marca temporal']).dt.strftime('%d/%m/%y')
countries = df['Marca temporal'].unique()
#st.bar_chart(inscriptostodos)
country = buff.selectbox('Elegir Fecha', countries)
above_352 = df["Marca temporal"] == country
df5=pd.value_counts(df[above_352]['Correo electrónico'])
times3t=df5.index
aulast=len(times3t) 

with buff:st.write('Cantidad de inscriptos esa fecha:',aulast)

inscriptos=df[above_352][['Marca temporal','Apellido','Nombre', 'Documento ','Institución a la que pertenece','Ocupación','Correo electrónico','Como conoció el Webinar','Desea recibir información de la actividades de la Universidad:']] 
inscriptos.index = [""] * len(inscriptos)  
#df.columns = ['Marca temporal','Apellido']

buff.table(inscriptos)

#sala=df['sala'].unique()

    #df=df.sort_values(by=['Correo electrónico del organizador'])
    
#df=df.sort_values(by=['Hora para unirse'],ascending=False)
#countries = df['Hora para unirse'].unique()
#country = buff.selectbox('Elegir Fecha', countries)
#above_352 = df["Hora para unirse"] == country
#buff1, buff2 = st.beta_columns([1,1])
#maxValue = df[above_352]['Duración (minutos)'].max()
#with buff:st.write('Fecha:',country,'   Duración:',maxValue) 

    
    

    

    
    #if col.checkbox('Ver detalle'):
#with col:st.write("Detalle de asistentes")
#buff1, col5, buff25,col25 = st.beta_columns([3,1,1,2])
#dia = col.selectbox('Elegir Docente', dias)
#above_3521 = df["E-mail del usuario"] == dia
     #asistencia2=df[above_352][above_3521][['Identificador del participante','Duración']]
#asistencia2=df[above_352][above_3521].groupby(['Fecha','Nombre del participante'],as_index=False)['Duración'].sum()
     #asistencia2=df[above_352][above_3521].groupby(['Nombre del participante', 'Fecha']).agg({ 'Duración' : 'sum'})

     #asistencia2.columns = ['Fecha','Nombre','Duración']

    #st.table(df[['Fecha','Código de reunión','Identificador del participante','Tipo de cliente','Correo electrónico del organizador','Duración','Nombre del participante']])
#asistencia2.index = [""] * len(asistencia2)  
#st.table(asistencia2)
#download=buff.button('Bajar csv') 
#if download:
buffi, coli = st.beta_columns([1,2])






#export_as_pdf = st.button("Export Report")

#if export_as_pdf:
