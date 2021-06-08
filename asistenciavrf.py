import streamlit as st
import pandas as pd
import numpy as np
import pybase64
import io
from bokeh.plotting import figure
import bokeh, bokeh.plotting

import matplotlib.pyplot as plt
from fpdf import FPDF

from tempfile import NamedTemporaryFile
st.set_page_config(
page_title="Actividades VRF",
page_icon="https://webinars.usal.edu.ar/sites/default/files/favicon.ico",
layout="wide",
)
    #st.markdown('<img style="float: left;" src="https://virtual.usal.edu.ar/branding/themes/Usal_7Julio_2017/images/60usalpad.png" />', unsafe_allow_html=True)
st.markdown('<style>div[data-baseweb="select"] > div {text-transform: capitalize;}body{background-color:#008357;}</style>', unsafe_allow_html=True)
st.markdown(
    """<style>
        .css-5h0m38 {
    display: inline-flex;
    flex-direction: column;
    border: 2px solid rgb(246, 51, 102);
    border-radius: 3px;
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
    text-decoration: none;
    background-color: rgb(255, 255, 255);
    border: 1px solid rgba(38, 39, 48, 0.2);
}
     .css-qbe2hs a{ text-decoration: none;}
     img {
    border: 2px solid rgb(246, 51, 102);}
    </style>
""", unsafe_allow_html=True) 

st.markdown("<h2 style='text-align: left; color: #00b8e1;'>VRF Registración actividades 2021</h2>", unsafe_allow_html=True)
buff1,buff, col = st.beta_columns([1,2,2])

    #SHEET_ID = '12D4hfpuIkT7vM69buu-v-r-UYb8xx4wM1zi-34Fs9ck'

#data = [['Elaboración de un proyecto de investigación en Ciencias Sociales y Humanísticas', '965178173'], ['Elaboración de un proyecto de investigación en Ciencias Naturales y Exactas', '1829217201']]
data=pd.read_csv('https://docs.google.com/spreadsheets/d/1wQaw4oh2StAh1wvi6VbwMF9JY9ji5qicTXOu86Pk3Sg/export?format=csv')
data=data.sort_values(by=['orden'],ascending=False)
# Create the pandas DataFrame
#df0 = pd.DataFrame(data, columns=['Webinar', 'Planilla'])

values = data['Webinar'].tolist()
options = data['Planilla'].tolist()

dic = dict(zip(options, values))


a = buff.selectbox('Seleccionar actividad:', options, format_func=lambda x: dic[x])


df = pd.read_csv('https://docs.google.com/spreadsheets/d/'+a+'/export?format=csv')
reunion = data['Planilla'] ==a
df['Marca temporal'] = pd.to_datetime(df['Marca temporal']).dt.strftime('%d/%m/%y')
inscriptostodos=df[['Marca temporal','Apellido','Nombre','Correo electrónico', 'Número de DNI ','Cómo conoció la actividad?','Conferencia a la que desea asistir','País','Institución']] 
inscriptostodos.index = [""] * len(inscriptostodos) 
      
df99 = pd.DataFrame({
"Fecha": inscriptostodos['Marca temporal'],"Nombre":inscriptostodos['Nombre'],"Apellido": inscriptostodos['Apellido'],"'Correo electrónico": inscriptostodos['Correo electrónico'],"País": inscriptostodos['País'],"Institución": inscriptostodos['Institución']
})
cds = ColumnDataSource(df99)
columns = [
TableColumn(field="Fecha", title="Fecha",formatter=HTMLTemplateFormatter(template='<%= value %>'),width = 200),
TableColumn(field="Nombre", title="Nombre",formatter=HTMLTemplateFormatter(template='<%= value %>'),width = 200),
TableColumn(field="Apellido", title="Apellido",formatter=HTMLTemplateFormatter(template='<%= value %>'),width = 200),
TableColumn(field="Conferencia", title="Conferencia",formatter=HTMLTemplateFormatter(template='<%= value %>'),width = 200),  
TableColumn(field="País", title="País",formatter=HTMLTemplateFormatter(template='<%= value %>'),width = 200),
TableColumn(field="Institución", title="Institución",formatter=HTMLTemplateFormatter(template='<%= value %>'),width = 200),
#TableColumn(field="links", title="Grabacion", formatter=HTMLTemplateFormatter(template='<a href="<%= value %>"target="_blank"><%= value %></a>'),width = 400),
]
p = DataTable(source=cds, columns=columns, css_classes=["my_table"],index_position=None,width=1000, height=250)
st.bokeh_chart(p) 
df5=pd.value_counts(df['Correo electrónico']) 
times3t=df5.index
aulast=len(times3t) 
with buff:st.write('Cantidad de inscriptos:',aulast) 
csv = inscriptostodos.to_csv(index=False)
b64 = pybase64.b64encode(csv.encode()).decode()  # some strings
linko= f'<a class="css-qbe2hs" href="data:file/csv;base64,{b64}" download="inscriptos.csv">Bajar csv</a>'
buff.markdown(linko, unsafe_allow_html=True)
imagen=str(data[reunion]['imagen'].max())
link=str(data[reunion]['link'].max())
b=str(data[reunion]['zoom'].max())
with buff1:st.markdown("<a href='"+link+"' target='_blank'><img src='"+imagen+"' style='width:90%;border-radius:3px;'></a>", unsafe_allow_html=True)
#with buff1:st.image(imagen, width=None)

#with col:st.bar_chart(inscriptostodos['Desea recibir información de la actividades de la Universidad:'])
df2 = pd.read_csv('https://docs.google.com/spreadsheets/d/'+a+'/export?format=csv&gid='+b)

#df['Hora para unirse'] = pd.to_datetime(df['Hora para unirse']).dt.strftime('%d/%m/%y')

#sala=df['sala'].unique()

    #df=df.sort_values(by=['Correo electrónico del organizador'])
    
#df=df.sort_values(by=['Hora para unirse'],ascending=False)
#usuarios=df2.groupby("Nombre (nombre original)", as_index=False).agg({ 'Duración (minutos)' : 'sum'})
#df5=pd.value_counts(usuarios['Nombre (nombre original)'])
#times3tz=df5.index
#aulastz=len(times3tz) 
#usuarios.index = [""] * len(usuarios)
#df['Correo electrónico del organizador'] = df['Correo electrónico del organizador'].str.split('@').str[0]
#usuarios=usuarios.sort_values(by=['Correo electrónico del organizador'])
#tiempo=usuarios['Duración (minutos)'].max()
#usuarios.columns = ['Usuario','Duración (minutos)']

 




   
  
df['Marca temporal'] = pd.to_datetime(df['Marca temporal']).dt.strftime('%d/%m/%y')
display_code =   buff1.radio("Mostrar", ( "Inscriptos por fecha","Total de Inscriptos", "Participantes en Zoom"))
countries = df['Marca temporal'].unique()
#st.bar_chart(inscriptostodos)
if display_code == "Inscriptos por fecha":
  country = buff1.selectbox('Elegir Fecha', countries) 
  above_352 = df["Marca temporal"] == country
  df5=pd.value_counts(df[above_352]['Correo electrónico'])
  times3t=df5.index
  aulast=len(times3t) 
  with buff1:st.write('Cantidad de inscriptos esa fecha:',aulast)
  aulast=len(times3t) 


  inscriptos=df[above_352][['Marca temporal','Apellido','Nombre','Correo electrónico', 'Número de DNI ','Cómo conoció la actividad?','Conferencia a la que desea asistir','País','Institución']] 
  inscriptos.index = [""] * len(inscriptos)  
#if buff1.checkbox('Ver todos los inscriptos'):
   #buff.table(inscriptostodos)
#if buff1.checkbox('Ver participantes en Zoom'):
   #with buff:st.write('Cantidad de participantes Zoom:',aulastz)
   #buff.table(usuarios)


 
#df.columns = ['Marca temporal','Apellido']

#buff.table(inscriptos)
#display_code =   buff1.radio("Mostrar", ( "Inscriptos por fecha","Total de Inscriptos", "Participantes en Zoom"))

if display_code == "Inscriptos por fecha":
    buff.table(inscriptos)



elif (display_code == "Total de Inscriptos"):
    buff.table(inscriptostodos)


else:
  with buff1:st.write('Cantidad de inscriptos:',aulast) 
  with buff1:st.write('Cantidad de participantes Zoom:',aulastz)
  with buff1:st.write('Duración de la reunión Zoom:',tiempo,' min')
  buff.table(usuarios)


   

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
