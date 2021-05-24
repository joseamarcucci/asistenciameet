import streamlit as st
import sys
import os

from multiapp import MultiApp

#import multiapp2 

import todas0,todasu,gral # import your app modules here


st.set_page_config(
page_title="Asistencia",
page_icon="http://idis.edu.ar/wp-content/uploads/2020/12/IDISfavicon2.png",
layout="wide",
initial_sidebar_state="expanded",)
app = MultiApp()

# Add all your application here

#st.sidebar.markdown("<h3 style='text-align: left; color: black;font-weight:500;'>Blackboard Collaborate y ULTRA</h3>", unsafe_allow_html=True)
app.add_app("Mostrar por:", gral.app)
app.add_app("Por docente", todasu.app)
#app.add_app("Febrero", tfebrero.app)
#app.add_app("Campus BBLearn ", home2.app)
#app.add_app("Campus Moodle ", moodle2.app)
#app.add_app("Marzo", tmarzo.app)
#app.add_app("Campus BBLearn", home.app)
#app.add_app("Campus Moodle ", moodle.app)
#app.add_app("Abril", tabril.app)
#app.add_app("16 al 21 de abril", data_stats.app)
#app.add_app("22 al 25 de abril", abril25.app)
#app.add_app("Campus BBLearn", home4.app)
#app.add_app("Campus Moodle", moodle4.app)
#app.add_app("Mayo", tmayo.app)
#app.add_app("16 al 21 de abril", data_stats.app)
#app.add_app("22 al 25 de abril", abril25.app)
#app.add_app("Campus BBLearn", home5.app)
#app.add_app("Campus Moodle", moodle5.app)
#app.add_app("Grabaciones", graba.app)
#app.add_app("Usuarios BBC x mes", mesesxuym.app)
#app.add_app("Usuarios Collaborate", usuariosbbc.app)
app.add_app("Por Fecha", todas0.app)
#app.add_app("Usuarios del campus por UA", usuarios.app)
#app.add_app("Usuarios totales del campus", usuarios0.app)

#app.add_app("16 al 21 de abril", data_stats.app)
#app.add_app("22 al 25 de abril", abril25.app)
#app.add_app("Datos x UA", todas.app)




app.run()

#PAGES = {
#    "Blackboard ULTRA:": todas0,
 #   "Usuarios del campus por UA": usuarios,
 #   "Usuarios totales del campus": usuarios0
#}
#st.sidebar.title('Navigation')
#election = st.sidebar.radio("", list(PAGES.keys()))
#page = PAGES[selection]
#page.app()

   
#app = MultiApp2()

#app.run()

