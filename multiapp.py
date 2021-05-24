"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
#from load_css import local_css
#local_css("/mydrive/MyDrive/multiapps/style.css")

class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """
    
    
    def __init__(self):
        st.sidebar.markdown('<img style="float: left;width:80%;margin-top:-70px;" src="http://idis.edu.ar/wp-content/uploads/2020/11/LOGO36svg.svg" />', unsafe_allow_html=True)
        st.markdown(
    """<style>
        .css-19ih76x{text-align: left !important}
        .css-1l02zno {
    background-color: #00b8e1;
    background-attachment: fixed;
    flex-shrink: 0;
    height: 100vh;
    overflow: auto;
    padding: 5rem 1rem;
    position: relative;
    transition: margin-left 300ms ease 0s, box-shadow 300ms ease 0s;
    width: 21rem;
    color:#ffff;
    z-index: 100;
    margin-left: 0px;
}
    </style>
    """, unsafe_allow_html=True) 
        st.sidebar.title('Control Asistencia Meet:')
 
        self.apps = []

    def add_app(self, title, func):
        
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
   
             
        })
  
    def run(self):
        
        app = st.sidebar.radio(
            '',
            self.apps,
            
            format_func=lambda app: app['title'])
      
              

        app['function']()


