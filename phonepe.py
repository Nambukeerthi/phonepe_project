import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
import numpy as np
import requests
import json

st.set_page_config(
        
        page_title="phoenpe analysis ",
        page_icon="",
        layout = "wide"
    )
# Data Exploration
def tacy_func(year):
        df1 = pd.read_csv("phonepe_data/aggrecated/1aggrecated_insurance.csv") 
        # df1["years"].unique()
        tacy = df1[df1["Years"] == year ]
        # Drop a column named 'ColumnName'
        #tacy.drop(" \ ", axis=1, inplace=True)
        tacy.drop(columns=['Unnamed: 0'], inplace=True)
        tacy.reset_index(drop= True, inplace=True) #inplace- store the data in same variable
        tacyg = tacy.groupby("States")[["Transaction_count","Transaction_amount"]].sum()
        # tacyg = tacy.groupby("States")[["Transaction_count","Transaction_amount"]].sum()
        tacyg.reset_index(inplace=True)
        return tacyg 


# Top Charts
def top_charts_amount_q1(df_csv):
       df_q1 = df_csv  # pd.read_csv("phonepe_data/aggrecated/1aggrecated_insurance.csv") 
       group1 = df_q1.groupby("States")["Transaction_amount"].sum().reset_index()
       st.dataframe(group1, use_container_width=True)
        
       q1_asce =group1.sort_values(by="Transaction_amount", ascending=True).head(10) 
       q1_asce.reset_index(drop= True, inplace=True)   
       fig_q1_asce = px.line(q1_asce , x = "States", y = "Transaction_amount", title = "HIGHEST", height= 600, width = 600)
       st.plotly_chart(fig_q1_asce, theme=None, use_container_width=True)
        
       q1_desc = group1.sort_values(by="Transaction_amount", ascending=False).head(10) 
       q1_desc.reset_index(drop= True, inplace=True)
       fig_q1_desc = px.line(q1_desc , x = "States", y = "Transaction_amount", title = "LOWEST", height= 600, width = 600)
       st.plotly_chart(fig_q1_desc, theme=None, use_container_width=True ) #
        
       q1_avg = df_q1.groupby("States")["Transaction_amount"].mean().reset_index()
       fig_q1_avg = px.bar(q1_avg , x = "States", y = "Transaction_amount", title = "AVERAGE")
       st.plotly_chart(fig_q1_avg, theme=None, use_container_width=True) 
        
def top_charts_count_q1(df_csv):        
      df_q1 = df_csv # pd.read_csv("phonepe_data/aggrecated/1aggrecated_insurance.csv")
      group1 = df_q1.groupby("States")["Transaction_count"].sum().reset_index()
      st.dataframe(group1, use_container_width=True)
        
      q1_asce =group1.sort_values(by="Transaction_count", ascending=True).head(10) 
      q1_asce.reset_index(drop= True, inplace=True)   
      fig_q1_asce = px.line(q1_asce , x = "States", y = "Transaction_count", title = "HIGHEST", height= 600, width = 600)
      st.plotly_chart(fig_q1_asce, theme=None, use_container_width=True)

      q1_desc = group1.sort_values(by="Transaction_count", ascending=False).head(10) 
      q1_desc.reset_index(drop= True, inplace=True)
      fig_q1_desc = px.line(q1_desc , x = "States", y = "Transaction_count", title = "LOWEST", height= 600, width = 600)
      st.plotly_chart(fig_q1_desc, theme=None, use_container_width=True )

      q1_avg = df_q1.groupby("States")["Transaction_count"].mean().reset_index()
      fig_q1_avg = px.bar(q1_avg , x = "States", y = "Transaction_count", title = "AVERAGE")
      st.plotly_chart(fig_q1_avg, theme=None, use_container_width=True) 






# streamlit part
# st.set_page_config(layout = "wide")
st.title("PHONPE DATA VISUALIZATION AND EXPLORATION")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")

with st.sidebar:
    
    select = option_menu("Main menu",["HOME","DATA EXPLORATION","TOP CHARTS"])
    
    
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
                st.link_button("DOWNLOAD APP NOW","https://www.phonepe.com/app-download/") 
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
       
        method_1 = st.radio("select",["Aggrecated insurance","Aggrecated transaction","Aggrecated user"])        
        
        if method_1 == "Aggrecated insurance": 
           
            # Data frame visualisation    
            df1 = pd.read_csv("phonepe_data/aggrecated/1aggrecated_insurance.csv")
            years = st.slider ("Select the year",df1["Years"].min(), df1["Years"].max(), df1["Years"].min())    
            tacyg_test = tacy_func(years)
            st.dataframe(tacyg_test, use_container_width=True) 
            fig_amount = px.bar(tacyg_test, x = "States", y = "Transaction_amount", title = f"{years} TRANSACTION AMOUNT")
            # fig_amount.show()
            st.plotly_chart(fig_amount, theme=None, use_container_width=True)   
            fig_count = px.bar(tacyg_test, x = "States", y = "Transaction_count", title = f"{years} TRANSACTION COUNT")
            st.plotly_chart(fig_count, theme=None, use_container_width=True)
            
            # Map visualisation 
            url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"    
            response= requests.get(url)   
            data1 = json.loads(response.content)    
            states_name =[]
            for i in data1["features"]:
              states_name.append(i["properties"]["ST_NM"])          
            states_name.sort()
             
            fig_india_1 = px.choropleth(
            tacyg_test,
            geojson=data1,
            locations="States",
            featureidkey="properties.ST_NM",
            color="Transaction_amount",
            color_continuous_scale="Rainbow",  # Corrected spelling from "color_continues_scale"
            range_color=(tacyg_test["Transaction_amount"].min(), tacyg_test["Transaction_amount"].max()),
            hover_name="States",
            title=f"{years} TRANSACTION AMOUNT",  # Fixed string interpolation
            fitbounds="locations",
            height=700,
            width=700
            )
            fig_india_1.update_geos(visible = False)
            st.plotly_chart(fig_india_1, use_container_width=True)

            fig_india_2 = px.choropleth(
            tacyg_test,
            geojson=data1,
            locations="States",
            featureidkey="properties.ST_NM",
            color="Transaction_amount",
            color_continuous_scale="Rainbow",  # Corrected spelling from "color_continues_scale"
            range_color=(tacyg_test["Transaction_count"].min(), tacyg_test["Transaction_count"].max()),
            hover_name="States",
            title=f"{years} TRANSACTION COUNT",  # Fixed string interpolation
            fitbounds="locations",
            height=700,
            width=700
            )
            fig_india_2.update_geos(visible = False)
            st.plotly_chart(fig_india_2, use_container_width=True)
            
        elif method_1 == "Aggrecated transaction":
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
    questions =  st.selectbox( "Select The Question", [ "1. Transaction Amount and Count of Aggrecated  Insurance",
                                                        "2. Transaction Amount and Count of Map  Insurance",
                                                        "3. Transaction Amount and Count of Top  Insurance",
                                                        "4. Transaction Amount and Count of Aggrecated  Transaction",
                                                        "5. Transaction Amount and Count of Map  Transaction",
                                                        "6. Transaction Amount and Count of Top  Transaction",
                                                        "7. Tansaction Count of Aggregated User",
                                                        "8. Registered users of Map User",
                                                        "9. App opens of Map User",
                                                        "10. Regeisterd users of Top User"
                                                       ]  )
    
   if questions ==      "1. Transaction Amount and Count of Aggrecated  Insurance":
                        df_csv = pd.read_csv("phonepe_data/aggrecated/1aggrecated_insurance.csv") 
                        top_charts_amount_q1(df_csv)
                        top_charts_count_q1(df_csv) 
                
   elif questions ==    "2. Transaction Amount and Count of Map  Insurance":
                        df1_csv = pd.read_csv("phonepe_data/map/1map_insurance.csv") 
                        top_charts_amount_q1(df1_csv)
                        top_charts_count_q1(df1_csv)
         
   elif questions ==    "2. Transaction Amount and Count of Map  Insurance":
                        df1_csv = pd.read_csv("phonepe_data/top/1top_insurance.csv") 
                        top_charts_amount_q1(df1_csv)
                        top_charts_count_q1(df1_csv)

