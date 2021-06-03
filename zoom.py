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
layout="wide",
)
    #st.markdown('<img style="float: left;" src="https://virtual.usal.edu.ar/branding/themes/Usal_7Julio_2017/images/60usalpad.png" />', unsafe_allow_html=True)
st.markdown('<style>div[data-baseweb="select"] > div {text-transform: capitalize;}body{background-color:#008357;}</style>', unsafe_allow_html=True)
st.markdown(
    """<style>
       
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

st.markdown("<h2 style='text-align: left; color: #00b8e1;'>Asistencia a proyectos Investigación</h2>", unsafe_allow_html=True)
buff, col = st.beta_columns([2,2])
    #SHEET_ID = '12D4hfpuIkT7vM69buu-v-r-UYb8xx4wM1zi-34Fs9ck'

data = [['Elaboración de un proyecto de investigación en Ciencias Sociales y Humanísticas', '1829217201'], ['Elaboración de un proyecto de investigación en Ciencias Naturales y Exactas', '965178173'],['SIGEVA USAL- Banco de Datos de CyT', '1107659696']]

# Create the pandas DataFrame
df0 = pd.DataFrame(data, columns=['Name', 'ID'])

values = df0['Name'].tolist()
options = df0['ID'].tolist()
dic = dict(zip(options, values))

a = buff.selectbox('Seleccionar sala:', options, format_func=lambda x: dic[x])


df = pd.read_csv('https://docs.google.com/spreadsheets/d/1mW4Cz6PZ6NYOJznn8xFYQHBDsXvv7m3uA6RFn_v9DaQ/export?format=csv&gid='+a)

#df['Hora para unirse'] = pd.to_datetime(df['Hora para unirse']).dt.strftime('%d/%m/%y')

sala=df['sala'].unique()

    #df=df.sort_values(by=['Correo electrónico del organizador'])
    
#df=df.sort_values(by=['Hora para unirse'],ascending=False)
countries = df['Hora para unirse'].unique()
country = buff.selectbox('Elegir Fecha', countries)
above_352 = df["Hora para unirse"] == country
buff1, buff2 = st.beta_columns([1,1])
maxValue = df[above_352]['Duración (minutos)'].max()
with buff:st.write('Fecha:',country,'   Duración:',maxValue) 

    
    
    #df = pd.read_csv('/mydrive/MyDrive/multiapps/bbc204.csv')
    #df=df.sort_values(by=['SessionOwner'])
    #options = ['USAL_lti_production', 'USAL_rest_production','josemarcucci']
alumnos = df[above_352]['Nombre (nombre original)'].unique()
    #usuarios=df[above_352].groupby("Fecha")['Minutos Usados'].sum()
usuarios=df[above_352].groupby("Nombre (nombre original)", as_index=False).agg({ 'Duración (minutos)' : 'sum'})
usuarios.index = [""] * len(usuarios)
#df['Correo electrónico del organizador'] = df['Correo electrónico del organizador'].str.split('@').str[0]
#usuarios=usuarios.sort_values(by=['Correo electrónico del organizador'])
usuarios.columns = ['Usuario','Duración (minutos)']
buff.table(usuarios)
    
dias1 = df.sort_values(by=['E-mail del usuario'])
dias = dias1['E-mail del usuario'].unique()
    

    
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

csv = usuarios.to_csv(index=False)
b64 = pybase64.b64encode(csv.encode()).decode()  # some strings
linko= f'<a class="css-qbe2hs" href="data:file/csv;base64,{b64}" download="asistencia2.csv">Bajar csv</a>'
buffi.markdown(linko, unsafe_allow_html=True)




#export_as_pdf = st.button("Export Report")

#if export_as_pdf:
pdf = FPDF()
pdf.add_page()
import matplotlib.image as mpimg

with NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
            table = pd.DataFrame(usuarios)
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
            colWidths=[0.45, 0.35,0.35], colLabels=header, cellLoc='center', loc ='upper left')         
   
            ax.set_title(sala, fontsize="8") 
          
            #fig.savefig(fig)
            #st.write(fig)
            fig.savefig(tmpfile.name,dpi=150) 
            pdf.image(tmpfile.name, 0, 0, 200, 200)
#html = create_download_link(pdf.output(dest="S").encode("latin-1"), "asistencia_"+str(maxValue))
b64 = pybase64.b64encode(pdf.output(dest="S").encode("latin-1"))  # val looks like b'...'
linki=f'<a class="css-qbe2hs" href="data:application/octet-stream;base64,{b64.decode()}" download="asistencia_'+str(maxValue)+'.pdf">Bajar PDF</a>'

coli.markdown(linki, unsafe_allow_html=True)

