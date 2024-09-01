import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd

st.set_page_config(
        layout = "wide"
        page_title="phoenpe analysis ",
        page_icon="",

    )

# streamlit part
# st.set_page_config(layout = "wide")
st.title("PHONPE DATA VISUALIZATION AND EXPLORATION")

with st.sidebar:
    
    select = option_menu("Main menu",["HOME","DATA EXPLORATION","TOP CHARTS","CODINGS"])
    
    
if select == "HOME":
    pass

elif select == "DATA EXPLORATION":
    
    tab1, tab2, tab3 = st.tabs(["Aggrecated Analysis","Map Analysis","Top Analysis"])
    
    with tab1:
       
        method_1 = st.radio("select",["Aggrecated insurance","Aggrecated trasaction","Aggrecated user"])    
        
        if method_1 == "Aggrecated insurance":
            pass
        elif method_1 == "Aggrecated trasaction":
            pass
        elif method_1 == "Aggrecated user":
            pass
    
    with  tab2:
       
        method_2 = st.radio("select",["Map insurance","Map trasaction","Map user"])
        
        if method_2 == "Map insurance":
            pass
        elif method_2 == "Map trasaction":
            pass
        elif method_2 == "Map user":
            pass
        
    with  tab3:
        
        method_3 = st.radio("select",["Top insurance","Top trasaction","Top user"])
        
        if method_3 == "Top insurance":
            pass
        elif method_3 == "Top trasaction":
            pass
        elif method_3 == "Top user":
            pass     
        
elif select == "TOP CHARTS":           
    pass

elif select == "CODINGS":
    pass
