import streamlit as st
import pandas as pd
import numpy as np
import pybase64
import io

def app():
    #st.markdown('<img style="float: left;" src="https://virtual.usal.edu.ar/branding/themes/Usal_7Julio_2017/images/60usalpad.png" />', unsafe_allow_html=True)
    st.markdown('<style>div[data-baseweb="select"] > div {text-transform: capitalize;}body{background-color:#008357;}</style>', unsafe_allow_html=True)
    st.markdown(
    """<style>
      .css-19ih76x {
    text-align: right !important;
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
    </style>
    """, unsafe_allow_html=True) 
   
    st.markdown("<h2 style='text-align: left; color: #00b8e1;'>Asistencia por Fecha</h2>", unsafe_allow_html=True)
    buff, col = st.beta_columns([2,2])
    #SHEET_ID = '12D4hfpuIkT7vM69buu-v-r-UYb8xx4wM1zi-34Fs9ck'
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/1ceuBcvEPUa5iTr1uHsZr3UCNxT03mvzN_4u7A4rJtmY/export?format=csv')
   
    
    
    df['Fecha'] = pd.to_datetime(df['Fecha']).dt.strftime('%d-%m-%y')
    maxValue = df['Fecha'].max()
    minValue = df['Fecha'].min()
    with buff: st.write('Período:',minValue,' al ',maxValue)
    #df=df.sort_values(by=['Correo electrónico del organizador'])
    df=df.sort_values(by=['Fecha'],ascending=False)
    countries = df['Fecha'].unique()
    country = buff.selectbox('Elegir Fecha', countries)
    above_352 = df["Fecha"] == country
    
    
    #df = pd.read_csv('/mydrive/MyDrive/multiapps/bbc204.csv')
    #df=df.sort_values(by=['SessionOwner'])
    #options = ['USAL_lti_production', 'USAL_rest_production','josemarcucci']
    alumnos = df[above_352]['Identificador del participante'].unique()
    #usuarios=df[above_352].groupby("Fecha")['Minutos Usados'].sum()
    usuarios=df[above_352].groupby("Correo electrónico del organizador", as_index=False).agg({ 'Identificador del participante' : 'nunique'})
    usuarios.index = [""] * len(usuarios)
    df['Correo electrónico del organizador'] = df['Correo electrónico del organizador'].str.split('@').str[0]
    usuarios=usuarios.sort_values(by=['Correo electrónico del organizador'])
    usuarios.columns = ['Docente','Cantidad de Participantes']
    buff.table(usuarios)

    dias1 = df.sort_values(by=['Correo electrónico del organizador'])
    dias = dias1['Correo electrónico del organizador'].unique()
    

    
    #if col.checkbox('Ver detalle'):
    with col:st.write("Detalle de asistentes")
    buff1, col5, buff25,col25 = st.beta_columns([3,1,1,2])
    dia = col.selectbox('Elegir Docente', dias)
    above_3521 = df["Correo electrónico del organizador"] == dia
     #asistencia2=df[above_352][above_3521][['Identificador del participante','Duración']]
    asistencia2=df[above_352][above_3521].groupby(['Fecha','Nombre del participante'],as_index=False)['Duración'].sum()
     #asistencia2=df[above_352][above_3521].groupby(['Nombre del participante', 'Fecha']).agg({ 'Duración' : 'sum'})

     #asistencia2.columns = ['Fecha','Nombre','Duración']

    #st.table(df[['Fecha','Código de reunión','Identificador del participante','Tipo de cliente','Correo electrónico del organizador','Duración','Nombre del participante']])
    asistencia2.index = [""] * len(asistencia2)  
    col.table(asistencia2)
    import matplotlib.pyplot as plt

    from matplotlib.backends.backend_pdf import PdfPages 
   
    
    export_as_pdf = col.button("Exportar PDF")

    if export_as_pdf:
      with PdfPages(maxValue+'.pdf') as pdf:
        table = pd.DataFrame(asistencia2)
        header = table.columns
        table = np.asarray(table)
        fig = plt.figure(figsize=(15, 25))
        ax = plt.Axes(fig, [0., 0., 1., 1.])
        ax.set_axis_off()
        fig.add_axes(ax)


        plt.title('Asistencia')
        tab = plt.table(cellText=table, colWidths=[0.15, 0.35,0.35], colLabels=header, cellLoc='center', loc='center')
        tab.auto_set_font_size(False)
        tab.set_fontsize(10)
        tab.scale(0.7, 2.5)
        pdf.savefig(fig)

        st.write(fig)
        plt.close()













