import streamlit as st
import pandas as pd
import numpy as np
import pybase64

import pybase64
import io

from fpdf import FPDF

import matplotlib.image as mpimg
from math import ceil
st.set_page_config(
page_title="Asistencia",
layout="wide",
)
#st.markdown('<img style="float: left;" src="https://virtual.usal.edu.ar/branding/themes/Usal_7Julio_2017/images/60usalpad.png" />', unsafe_allow_html=True)
st.markdown('<style>div[data-baseweb="select"] > div {text-transform: capitalize;}body{background-color:#008357;}</style>', unsafe_allow_html=True)
st.markdown(
    """<style>
        .css-19ih76x {
    border-top: 1px solid rgba(38, 39, 48, 0.1);
    border-bottom: 1px solid rgba(38, 39, 48, 0.1);
    vertical-align: middle;
    padding: 0.25rem;
    text-align: center;
    /* font-size: 1px; */
}
.css-d56p6e {
    border-top: 1px solid rgba(38, 39, 48, 0.1);
    border-bottom: 1px solid rgba(38, 39, 48, 0.1);
    vertical-align: middle;
    padding: 0.25rem;
}
p, ol, ul, dl {
    margin: 0px 0px 1rem;
    padding: 0px;
    font-size: 12px;
    font-weight: 400;
}
.st-af {
    font-size: 12px;
}
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
    font-size: 12px;
    text-decoration: none;
    background-color: rgb(255, 255, 255);
    border: 1px solid rgba(38, 39, 48, 0.2);
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
   
#st.markdown("<h2 style='text-align: left; color: #00b8e1;'>Asistencia</h2>", unsafe_allow_html=True)
buff, col = st.beta_columns([2,2])

country = buff.text_input('Ingrese mail USAL',value='@usal.edu.ar')
if country != "":
    
    #SHEET_ID = '12D4hfpuIkT7vM69buu-v-r-UYb8xx4wM1zi-34Fs9ck'
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/1sHkx_qlz7hNogun235B5_nEcLguVYRr6cRtk6rRF0wo/export?format=csv')
   
    
    df['Fecha'] = pd.to_datetime(df['Fecha']).dt.strftime('%d-%m-%y')
    maxValue = df['Fecha'].max()
    minValue = df['Fecha'].min()
    with buff: st.write('Período:',minValue,' al ',maxValue)
    df=df.sort_values(by=['Correo electrónico del organizador'])
   #df = pd.DataFrame(['Correo electrónico del organizador'], columns= ['Correo electrónico del organizador'])
    #BeforeSymbol = df['Correo electrónico del organizador'].str.split('@').str[0]
#df['Correo electrónico del organizador'] = df['Correo electrónico del organizador'].str.split('@').str[0]
    countries = df['Correo electrónico del organizador'].unique()
    #text_input_container.empty()
    above_352 = df["Correo electrónico del organizador"] == country
    df=df.sort_values(by=['Fecha'],ascending=False)


    #df = pd.read_csv('/mydrive/MyDrive/multiapps/bbc204.csv')
    #df=df.sort_values(by=['SessionOwner'])
    #options = ['USAL_lti_production', 'USAL_rest_production','josemarcucci']
    alumnos = df[above_352]['Identificador del participante'].unique()
    #usuarios=df[above_352].groupby("Fecha")['Minutos Usados'].sum()
    usuarios=df[above_352].groupby("Fecha", as_index=False).agg({ 'Identificador del participante' : 'nunique'})
    usuarios.index = [""] * len(usuarios)
    usuarios=usuarios.sort_values(by=['Fecha'],ascending=False)
    usuarios.columns = ['Fecha','Cantidad de Participantes']
    buff.table(usuarios)

    
    dias = df[above_352]['Fecha'].unique()
    
    
    
    buff1, col5, buff25,col25 = st.beta_columns([3,1,1,2])
    dia = col.selectbox('Elegir Fecha', dias)
    with col:st.write("Detalle de asistentes")
    above_3521 = df["Fecha"] == dia
     #asistencia2=df[above_352][above_3521][['Identificador del participante','Duración']]
    asistencia2=df[above_352][above_3521].groupby(['Fecha','Nombre del participante'],as_index=False)['Duración'].sum()
     #asistencia2=df[above_352][above_3521].groupby(['Nombre del participante', 'Fecha']).agg({ 'Duración' : 'sum'})

    asistencia2.columns = ['Fecha','Nombre','Duración']

    #st.table(df[['Fecha','Código de reunión','Identificador del participante','Tipo de cliente','Correo electrónico del organizador','Duración','Nombre del participante']])
    asistencia2.index = [""] * len(asistencia2) 
    c1, c2, c3, c4 = st.beta_columns((2, 1, 1, 1)) 
    col.table(asistencia2)

    import matplotlib.pyplot as plt

    from matplotlib.backends.backend_pdf import PdfPages 
   
    buffi, coli =st.beta_columns([3,4])
    

    csv = asistencia2.to_csv(index=False)
    b64 = pybase64.b64encode(csv.encode("latin-1")).decode()  # some strings
    linko= f'<a class="css-qbe2hs" href="data:file/csv;base64,{b64}" download="asistencia'+dia+'.csv">Bajar csv/Excel</a>'

#export_as_pdf = st.button("Export Report")

#if export_as_pdf:
    pdf = FPDF()
    pdf.add_page()
    import matplotlib.image as mpimg
    from tempfile import NamedTemporaryFile
    with NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
            table = pd.DataFrame(asistencia2)
            header = table.columns
            table = np.asarray(table)
            plt.title('Asistencia')
            fig = plt.figure()
            ax = plt.Axes(fig, [0., 0., 1., 1.])
            ax.set_axis_off()
            
            
            fig.add_axes(ax)
            tab = plt.table(cellText=table, colWidths=[0.45, 0.35,0.35], colLabels=header, cellLoc='center', loc='center')
            tab.auto_set_font_size(False)
            tab.set_fontsize(10)
            tab.scale(1, 1)
            val1 = ["{:X}".format(i) for i in range(10)] 

           
            fig, ax = plt.subplots() 
            ax.set_axis_off() 
            table = ax.table( 
            cellText = table,  
            colWidths=[0.45, 0.25,0.25], colLabels=header, cellLoc='center', loc ='upper left')         
   
            ax.set_title('Período:'+minValue+' al '+maxValue, fontsize="8") 
          
            #fig.savefig(fig)
            #st.write(fig)
            fig.savefig(tmpfile.name,dpi=150) 
            pdf.image(tmpfile.name, 0, 5, 200, 200)
#html = create_download_link(pdf.output(dest="S").encode("latin-1"), "asistencia_"+str(maxValue))
    b64 = pybase64.b64encode(pdf.output(dest="S").encode("latin-1"))  # val looks like b'...'
    linki=f'<a class="css-qbe2hs" href="data:application/octet-stream;base64,{b64.decode()}" download="asistencia_'+str(maxValue)+'.pdf">Bajar PDF</a>'
    c3.markdown(linko, unsafe_allow_html=True)
    c4.markdown(linki, unsafe_allow_html=True)
