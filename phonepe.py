import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(
        
        page_title="phoenpe analysis ",
        page_icon="",
        layout = "wide"
    )

# streamlit part
# st.set_page_config(layout = "wide")
st.title("PHONPE DATA VISUALIZATION AND EXPLORATION")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")

with st.sidebar:
    
    select = option_menu("Main menu",["HOME","DATA EXPLORATION","TOP CHARTS","CODINGS"])
    
    
if select == "HOME":
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        img1 = Image.open("images/phonepe3.jpg")
        st.image( img1,use_column_width=True,channels="RGB" )
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        col1,col2 = st.columns(2)
        with col1:
                st.subheader(" INDIA'S BEST TRANSACTION APP ")
                st.markdown(" PhonePe is an Indian digital payments and financial technology company ")
                st.write("****FEATURES**** ")
                st.write("****credit and debit card linking**** ")
                st.write("****Bank Balance check**** ")
                st.write("****Money Storage**** ")
                st.write("****PIN Authorization**** ")
                st.download_button("DOWNLOAD APP NOW","https://www.phonepe.com/app-download/")
        with col2:
                img = Image.open("images/phonepe2.png")
                st.image( img,width=400,channels="RGB" )
                #st.image("https://github.com/Nambukeerthi/phonepe_project/blob/main/images/phonepe2.png")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        img2 = Image.open("images/phonepe4.jpg")
        st.image( img2,use_column_width=True,channels="RGB" )  
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        col3,col4 = st.columns(2)
        with col3:
                img3 = Image.open("images/phonepe1.png")
                st.image(img3,width=400,channels="RGB" )  
        with col4:
                #st.subheader(" INDIA'S BEST TRANSACTION APP ")
                #st.markdown(" PhonePe is an Indian digital payments and financial technology company ")
                st.write("****Easy Transaction**** ")
                st.write("****One App for All your Payments**** ")
                st.write("****Multiple Payments Method**** ")
                st.write("****PhonePe Merchants**** ")
                st.write("****Multiple Ways to Pay**** ")
                st.write("****1. Direct Transfer & More**** ")
                st.write("****2. QR Code**** ")
                st.write("****Earn Great Rewards**** ")
               
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
