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


# DATA EXPLORATION
def transaction_func(df_csv):
        
        df1 = df_csv   
        years = st.slider("Select the Year of Below ", df1["Years"].min(), df1["Years"].max(), df1["Years"].min())
        tacy = df1[df1["Years"] == years ]
        tacy.drop(columns=['Unnamed: 0'], inplace=True)
        tacy.reset_index(drop= True, inplace=True) #inplace- store the data in same variable
        tacyg = tacy.groupby("States")[["Transaction_count","Transaction_amount"]].sum()
        tacyg.reset_index(inplace=True)
        
        tacyg_test = tacyg 
        st.dataframe(tacyg_test, use_container_width=True) 
        fig_amount = px.bar(tacyg_test, x = "States", y = "Transaction_amount", title = f"{years} TRANSACTION AMOUNT",color_discrete_sequence= px.colors.sequential.Aggrnyl)
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
        
        
def transaction_type(df_csv):
        
        df1 = df_csv   
        state = st.selectbox ("Select the State", df1["States"].unique())
        tacy = df1[df1["States"] == state ]
        tacy.reset_index(drop= True, inplace=True) #inplace- store the data in same variable
        tacyg = tacy.groupby("Transaction_type")[["Transaction_count","Transaction_amount"]].sum()
        tacyg.reset_index(inplace=True)
        fig_pie_1 = px.pie(data_frame = tacyg, names = "Transaction_type", values ="Transaction_amount", title = f"{state.upper()} TRANSACTION AMOUNT", hole =0.5 )
        st.plotly_chart(fig_pie_1, use_container_width=True)
        fig_pie_2 = px.pie(data_frame = tacyg, names = "Transaction_type", values ="Transaction_count", title = f"{state.upper()} TRANSACTION COUNT", hole =0.5 )
        st.plotly_chart(fig_pie_2, use_container_width=True)

def user_type(df_csv):
        
        df1 = df_csv   
        years = st.slider ("Select the Year of Given",df1["Years"].min(), df1["Years"].max(), df1["Years"].min())
        aguy = df1[df1["Years"] == years ]
        # aguy.drop(columns=['Unnamed: 0'], inplace=True)
        aguy.reset_index(drop= True, inplace=True) #inplace- store the data in same variable
        aguyg = pd.DataFrame(aguy.groupby("Brands")["Transaction_count"].sum())
        aguyg.reset_index(inplace=True)
        aguyg_test = aguyg
        st.dataframe(aguyg_test, use_container_width=True) 
        fig_bar_1 = px.bar(aguyg_test, x = "Brands", y = "Transaction_count", title = f"{years} BRANDS NAME AND TRANSACTION COUNT",color_discrete_sequence= px.colors.sequential.haline, hover_name="Brands")
        st.plotly_chart(fig_bar_1, theme=None, use_container_width=True)   
        
def user_states_type(df_csv):
        
        df1 = df_csv
        state = st.selectbox ("Select the State", df1["States"].unique())
        austg = df1.groupby(['States', 'Brands'])['Transaction_count'].sum()
        austgs =  pd.DataFrame(austg)
        austgs.reset_index(inplace=True)
        austgs_data = austgs[austgs["States"] == state]
        fig_line_1 = px.line(austgs_data, x = "Brands", y = "Transaction_count", title = f"{state.upper()} STATE - BRANDS TRANSCATION",color_discrete_sequence= px.colors.sequential.haline, markers= True)
        st.plotly_chart(fig_line_1, theme=None, use_container_width=True)
 

# map 
def map_insurance(df_csv):

        df2 = df_csv   
        years = st.slider("Select the Year of One ", df2["Years"].min(), df2["Years"].max(), df2["Years"].min(), key="year_slider_1")
        mity = df2[df2["Years"] == years ]
        mity.drop(columns=['Unnamed: 0'], inplace=True)
        mity.reset_index(drop= True, inplace=True) #inplace- store the data in same variable
        mityg = mity.groupby("States")[["Transaction_count","Transaction_amount"]].sum()
        mityg.reset_index(inplace=True)
        
        mityg_test = mityg 
        st.dataframe(mityg_test, use_container_width=True) 
        fig_amount_ins = px.bar(mityg_test, x = "States", y = "Transaction_amount", title = f"{years} TRANSACTION AMOUNT",color_discrete_sequence= px.colors.sequential.Aggrnyl)
        st.plotly_chart(fig_amount_ins, theme=None, use_container_width=True, key="unique_plotly_chart")   
        fig_count_ins = px.bar(mityg_test, x = "States", y = "Transaction_count", title = f"{years} TRANSACTION COUNT")
        st.plotly_chart(fig_count_ins, theme=None, use_container_width=True, key="plotly_chart_1")
            
        # Map visualisation 
        
        url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"    
        response= requests.get(url)   
        data1 = json.loads(response.content)    
        states_name =[]
        for i in data1["features"]:
           states_name.append(i["properties"]["ST_NM"])          
        states_name.sort()
             
        fig_india_ins_1= px.choropleth(
        mityg_test,
        geojson=data1,
        locations="States",
        featureidkey="properties.ST_NM",
        color="Transaction_amount",
        color_continuous_scale="Rainbow",  # Corrected spelling from "color_continues_scale"
        range_color=(mityg_test["Transaction_amount"].min(), mityg_test["Transaction_amount"].max()),
        hover_name="States",
        title=f"{years} TRANSACTION AMOUNT",  # Fixed string interpolation
        fitbounds="locations",
        height=700,
        width=700
            )
        fig_india_ins_1.update_geos(visible = False)
        st.plotly_chart(fig_india_ins_1, use_container_width=True, key="plotly_chart_india_1")

        fig_india_ins_2 = px.choropleth(
        mityg_test,
        geojson=data1,
        locations="States",
        featureidkey="properties.ST_NM",
        color="Transaction_amount",
        color_continuous_scale="Rainbow",  # Corrected spelling from "color_continues_scale"
        range_color=(mityg_test["Transaction_count"].min(), mityg_test["Transaction_count"].max()),
        hover_name="States",
        title=f"{years} TRANSACTION COUNT",  # Fixed string interpolation
        fitbounds="locations",
        height=700,
        width=700
            )
        fig_india_ins_2.update_geos(visible = False)
        st.plotly_chart(fig_india_ins_2, use_container_width=True, key="plotly_chart_india_2")        
        
def map_ins_dist(df_csv):

        df2 = df_csv  
        state = st.selectbox("Select the State",df2["States"].unique(), key="state_selectbox_1")
        midy = df2[df2["States"] == state ]
        midy.reset_index(drop= True, inplace=True) #inplace- store the data in same variable
        midyg = midy.groupby("Districts")[["Transaction_count","Transaction_amount"]].sum()
        midyg.reset_index(inplace=True)
        fig_bar_ins_1 = px.bar(data_frame = midyg, x = "Districts", y ="Transaction_amount", title = f"{state.upper()} TRANSACTION AMOUNT")
        st.plotly_chart(fig_bar_ins_1, use_container_width=True)
        fig_bar_ins_2 = px.bar(data_frame = midyg, x = "Districts", y ="Transaction_count", title = f"{state.upper()} TRANSACTION COUNT")
        st.plotly_chart(fig_bar_ins_2, use_container_width=True)

def map_user(df_csv):
        
        df2 = df_csv   
        years = st.slider("Select the Year of Given ", df2["Years"].min(), df2["Years"].max(), df2["Years"].min())
        muy = df2[df2["Years"] == years ]
        muy.drop(columns=['Unnamed: 0'], inplace=True)
        muy.reset_index(drop= True, inplace=True) #inplace- store the data in same variable
        muyg = muy.groupby("States")[["Registered_users","Appopens"]].sum()
        muyg.reset_index(inplace=True)
        fig_line_2 = px.line(muyg, x = "States", y = ["Registered_users","Appopens"], markers= True)
        st.plotly_chart(fig_line_2, theme=None, use_container_width=True)

def map_user_dist(df_csv):
        
        df2 = df_csv  
        state = st.selectbox ("Select the State of One",df2["States"].unique())
        musd = df2[df2["States"] == state ]
        musd.reset_index(drop= True, inplace=True) #inplace- store the data in same variable
        musdrg = musd.groupby("Districts")[["Registered_users"]].sum()
        musdrg.reset_index(inplace=True)
        musdag = musd.groupby("Districts")[["Appopens"]].sum()
        musdag.reset_index(inplace=True)
        fig_line_user_2 = px.line(data_frame = musdrg, x = "Districts", y ="Registered_users", title = "REGISTERD USERS", markers= True)
        st.plotly_chart(fig_line_user_2, theme=None, use_container_width=True)
        fig_line_user_3 = px.line(data_frame = musdag, x = "Districts", y ="Appopens", title = "APP OPENS", markers= True)
        st.plotly_chart(fig_line_user_3, theme=None, use_container_width=True)
# top
def Top_insurance(df_csv):
        
        df2 = df_csv   
        years = st.slider("Select the Year's One ", df2["Years"].min(), df2["Years"].max(), df2["Years"].min())
        tity = df2[df2["Years"] == years ]
        tity.drop(columns=['Unnamed: 0'], inplace=True)
        tity.reset_index(drop= True, inplace=True) #inplace- store the data in same variable
        tityg = tity.groupby("States")[["Transaction_count","Transaction_amount"]].sum()
        tityg.reset_index(inplace=True)
        
        tityg_test = tityg 
        st.dataframe(tityg_test, use_container_width=True) 
        fig_amount_ins_top = px.bar(tityg_test, x = "States", y = "Transaction_amount", title = f"{years} TRANSACTION AMOUNT",color_discrete_sequence= px.colors.sequential.Aggrnyl)
        st.plotly_chart(fig_amount_ins_top, theme=None, use_container_width=True)   # key="unique_plotly_chart"
        fig_count_ins_top = px.bar(tityg_test, x = "States", y = "Transaction_count", title = f"{years} TRANSACTION COUNT")
        st.plotly_chart(fig_count_ins_top, theme=None, use_container_width=True)  # key="plotly_chart_1"
            
        # Map visualisation 
        url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"    
        response= requests.get(url)   
        data1 = json.loads(response.content)    
        states_name =[]
        for i in data1["features"]:
           states_name.append(i["properties"]["ST_NM"])          
        states_name.sort()
             
        fig_india_ins_top_1= px.choropleth(
        tityg_test,
        geojson=data1,
        locations="States",
        featureidkey="properties.ST_NM", 
        color="Transaction_amount",
        color_continuous_scale="Rainbow",  # Corrected spelling from "color_continues_scale"
        range_color=(tityg_test["Transaction_amount"].min(), tityg_test["Transaction_amount"].max()),
        hover_name="States",
        title=f"{years} TRANSACTION AMOUNT",  # Fixed string interpolation
        fitbounds="locations",
        height=700,
        width=700
            )
        fig_india_ins_top_1.update_geos(visible = False)
        st.plotly_chart(fig_india_ins_top_1, use_container_width=True)

        fig_india_ins_top_2 = px.choropleth(
        tityg_test,
        geojson=data1,
        locations="States",
        featureidkey="properties.ST_NM",
        color="Transaction_amount",
        color_continuous_scale="Rainbow",  # Corrected spelling from "color_continues_scale"
        range_color=(tityg_test["Transaction_count"].min(), tityg_test["Transaction_count"].max()),
        hover_name="States",
        title=f"{years} TRANSACTION COUNT",  # Fixed string interpolation
        fitbounds="locations",
        height=700,
        width=700
            )
        fig_india_ins_top_2.update_geos(visible = False)
        st.plotly_chart(fig_india_ins_top_2, use_container_width=True)
    
def top_ins_pin(df_csv):
        
        df2 = df_csv
        state = st.selectbox ("Select One State",df2["States"].unique())
        tip = df2[df2["States"] == state ]
        tip.reset_index(drop= True, inplace=True) #inplace- store the data in same variable
        tipg = tip.groupby("Pincodes")[["Transaction_count","Transaction_amount"]].sum()
        tipg.reset_index(inplace=True)
        fig_pie_ins_pin_1 = px.pie(data_frame = tipg, names = "Pincodes", values ="Transaction_amount", title = f"{state.upper()} TRANSACTION AMOUNT", hole = 0.5)
        st.plotly_chart(fig_pie_ins_pin_1, use_container_width=True)
        fig_pie_ins_pin_1 = px.pie(data_frame = tipg, names = "Pincodes", values ="Transaction_count", title = f"{state.upper()} TRANSACTION COUNT", hole = 0.5)
        st.plotly_chart(fig_pie_ins_pin_1, use_container_width=True)

def top_user(df_csv):

        df2 = df_csv   
        years = st.slider("Select the Given Year ", df2["Years"].min(), df2["Years"].max(), df2["Years"].min())
        tuy = df2[df2["Years"] == years ]
        tuy.drop(columns=['Unnamed: 0'], inplace=True)
        tuy.reset_index(drop= True, inplace=True) #inplace- store the data in same variable
        tuyg = pd.DataFrame(tuy.groupby(["States","Quarter"])["Registered_users"].sum())
        tuyg.reset_index(inplace=True)
        fig_bar_top_user = px.bar(tuyg, x = "States", y = "Registered_users", color = "Quarter" ,color_discrete_sequence = px.colors.sequential.Burgyl, hover_name = "States")
        st.plotly_chart(fig_bar_top_user, theme=None, use_container_width=True)
        state = st.selectbox("Select the Given State", tuyg["States"].unique())
        tuygs = tuy[tuy["States"] == state]
        tuygs.reset_index(drop=True, inplace =True)
        fig_bar_top_user_1 = px.bar(tuygs, x= "Quarter", y="Registered_users", color= "Registered_users", title= "REGISTRED USERS", color_continuous_scale = px.colors.sequential.Magenta, hover_name= "Pincodes")
        st.plotly_chart(fig_bar_top_user_1, theme=None, use_container_width=True)


# TOP CHARTS
def top_charts_amount(df_csv):
        
       st.subheader("TRANSACTION AMOUNT")
       df_q1 = df_csv   
       group1 = df_q1.groupby("States")["Transaction_amount"].sum().reset_index()
       st.dataframe(group1, use_container_width=True)
        
       q1_asce =group1.sort_values(by="Transaction_amount", ascending=True).head(10) 
       q1_asce.reset_index(drop= True, inplace=True)   
       fig_q1_asce = px.line(q1_asce , x = "States", y = "Transaction_amount", title = "HIGHEST", height= 600, width = 600, color_discrete_sequence= px.colors.sequential.Bluered_r)
       st.plotly_chart(fig_q1_asce, theme=None, use_container_width=True)
        
       q1_desc = group1.sort_values(by="Transaction_amount", ascending=False).head(10) 
       q1_desc.reset_index(drop= True, inplace=True)
       fig_q1_desc = px.line(q1_desc , x = "States", y = "Transaction_amount", title = "LOWEST", height= 600, width = 600, color_discrete_sequence= px.colors.sequential.Bluered_r)
       st.plotly_chart(fig_q1_desc, theme=None, use_container_width=True ) #
        
       q1_avg = df_q1.groupby("States")["Transaction_amount"].mean().reset_index()
       fig_q1_avg = px.bar(q1_avg , x = "States", y = "Transaction_amount", title = "AVERAGE", color_discrete_sequence= px.colors.sequential.Aggrnyl)
       st.plotly_chart(fig_q1_avg, theme=None, use_container_width=True) 
        
def top_charts_count(df_csv): 
        
      st.subheader("TRANSACTION COUNT")
      df_q1 = df_csv 
      group1 = df_q1.groupby("States")["Transaction_count"].sum().reset_index()
      st.dataframe(group1, use_container_width=True)
        
      q1_asce =group1.sort_values(by="Transaction_count", ascending=True).head(10) 
      q1_asce.reset_index(drop= True, inplace=True)   
      fig_q1_asce = px.line(q1_asce , x = "States", y = "Transaction_count", title = "HIGHEST", height= 600, width = 600, color_discrete_sequence= px.colors.sequential.Bluered_r)
      st.plotly_chart(fig_q1_asce, theme=None, use_container_width=True)

      q1_desc = group1.sort_values(by="Transaction_count", ascending=False).head(10) 
      q1_desc.reset_index(drop= True, inplace=True)
      fig_q1_desc = px.line(q1_desc , x = "States", y = "Transaction_count", title = "LOWEST", height= 600, width = 600,color_discrete_sequence= px.colors.sequential.Bluered_r)
      st.plotly_chart(fig_q1_desc, theme=None, use_container_width=True )

      q1_avg = df_q1.groupby("States")["Transaction_count"].mean().reset_index()
      fig_q1_avg = px.bar(q1_avg , x = "States", y = "Transaction_count", title = "AVERAGE", color_discrete_sequence= px.colors.sequential.Blackbody_r)
      st.plotly_chart(fig_q1_avg, theme=None, use_container_width=True) 

def registerd_users(df_csv):
        
      st.subheader("REGISTERD USERS")  
      df_q1 = df_csv 
      group1 = df_q1.groupby("States")["Registered_users"].sum().reset_index()
      st.dataframe(group1, use_container_width=True)

      q1_asce =group1.sort_values(by="Registered_users", ascending=True).head(10) 
      q1_asce.reset_index(drop= True, inplace=True)   
      fig_q1_asce = px.line(q1_asce , x = "States", y = "Registered_users", title = "HIGHEST", height= 600, width = 600, color_discrete_sequence= px.colors.sequential.Blackbody_r)
      st.plotly_chart(fig_q1_asce, theme=None, use_container_width=True)

      q1_desc = group1.sort_values(by="Registered_users", ascending=False).head(10) 
      q1_desc.reset_index(drop= True, inplace=True)
      fig_q1_desc = px.line(q1_desc , x = "States", y = "Registered_users", title = "LOWEST", height= 600, width = 600, color_discrete_sequence= px.colors.sequential.Blackbody_r)
      st.plotly_chart(fig_q1_desc, theme=None, use_container_width=True )

      q1_avg = df_q1.groupby("States")["Registered_users"].mean().reset_index()
      fig_q1_avg = px.bar(q1_avg , x = "States", y = "Registered_users", title = "AVERAGE",color_discrete_sequence= px.colors.sequential.Agsunset_r)
      st.plotly_chart(fig_q1_avg, theme=None, use_container_width=True) 

def app_opens(df_csv):
        
      st.subheader("APP OPENS") 
      df_q1 = df_csv 
      group1 = df_q1.groupby("States")["Appopens"].sum().reset_index()
      st.dataframe(group1, use_container_width=True)

      q1_asce =group1.sort_values(by="Appopens", ascending=True).head(10) 
      q1_asce.reset_index(drop= True, inplace=True)   
      fig_q1_asce = px.line(q1_asce , x = "States", y = "Appopens", title = "HIGHEST", height= 600, width = 600, color_discrete_sequence= px.colors.sequential.Agsunset_r)
      st.plotly_chart(fig_q1_asce, theme=None, use_container_width=True)

      q1_desc = group1.sort_values(by="Appopens", ascending=False).head(10) 
      q1_desc.reset_index(drop= True, inplace=True)
      fig_q1_desc = px.line(q1_desc , x = "States", y = "Appopens", title = "LOWEST", height= 600, width = 600, color_discrete_sequence= px.colors.sequential.Agsunset_r)
      st.plotly_chart(fig_q1_desc, theme=None, use_container_width=True )

      q1_avg = df_q1.groupby("States")["Appopens"].mean().reset_index()
      fig_q1_avg = px.bar(q1_avg , x = "States", y = "Appopens", title = "AVERAGE")
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
        st.image( img1,use_container_width=True,channels="RGB" )
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
        st.image( img2,use_container_width=True,channels="RGB" )  
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

        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")

        st.markdown("[PROJECT GITHUB PAGE](https://github.com/Nambukeerthi/phonepe_project/)")



elif select == "DATA EXPLORATION":
    
    tab1, tab2, tab3 = st.tabs(["Aggrecated Analysis","Map Analysis","Top Analysis"])
    
    with tab1:
       
        method_1 = st.radio("select",["Aggrecated insurance","Aggrecated transaction","Aggrecated user"])        
        
        if method_1 == "Aggrecated insurance": 
            df_agg_ins_csv = pd.read_csv("phonepe_data/aggrecated/1aggrecated_insurance.csv")    
            transaction_func(df_agg_ins_csv)
                
        elif method_1 == "Aggrecated transaction":    
            df_agg_trans_csv = pd.read_csv("phonepe_data/aggrecated/2aggrecated_transaction.csv")    
            transaction_func(df_agg_trans_csv)
            transaction_type (df_agg_trans_csv)
            
        elif method_1 == "Aggrecated user":
            df_agg_user_csv = pd.read_csv("phonepe_data/aggrecated/3aggrecated_user.csv")    
            user_type(df_agg_user_csv)
            user_states_type(df_agg_user_csv)
                
    with  tab2:
       
        method_2 = st.radio("select",["Map insurance","Map trasaction","Map user"])
        
        if method_2 == "Map insurance":
             df_map_mins_csv = pd.read_csv("phonepe_data/map/1map_insurance.csv")    
             map_insurance(df_map_mins_csv)
             map_ins_dist(df_map_mins_csv)   
                
        elif method_2 == "Map trasaction":
            df_map_trans_csv = pd.read_csv("phonepe_data/map/2map_transaction.csv")
            map_insurance(df_map_trans_csv)
            map_ins_dist(df_map_trans_csv)
            
        elif method_2 == "Map user":
            df_map_user_csv = pd.read_csv("phonepe_data/map/3map_user.csv")    
            map_user(df_map_user_csv)
            map_user_dist(df_map_user_csv)
        
    with  tab3:
        
        method_3 = st.radio("select",["Top insurance","Top trasaction","Top user"])
        
        if method_3 == "Top insurance":
            df_top_ins_csv = pd.read_csv("phonepe_data/top/1top_insurance.csv")    
            Top_insurance(df_top_ins_csv) 
            top_ins_pin(df_top_ins_csv)    
                
        elif method_3 == "Top trasaction":
            df_top_trans_csv = pd.read_csv("phonepe_data/top/2top_transaction.csv")    
            Top_insurance(df_top_trans_csv) 
            top_ins_pin(df_top_trans_csv)   
                
        elif method_3 == "Top user":
            st.subheader("TOP USER")
            df_top_user_csv = pd.read_csv("phonepe_data/top/3top_user.csv")    
            top_user(df_top_user_csv)    
                
        
elif select == "TOP CHARTS":           
    questions =  st.selectbox( "Select The Question", [ "1. Transaction Amount and Count of Aggrecated  Insurance",
                                                        "2. Transaction Amount and Count of Map  Insurance",
                                                        "3. Transaction Amount and Count of Top  Insurance",
                                                        "4. Transaction Amount and Count of Aggrecated  Transaction",
                                                        "5. Transaction Amount and Count of Map  Transaction",
                                                        "6. Transaction Amount and Count of Top  Transaction",
                                                        "7. Transaction Count of Aggregated User",
                                                        "8. Registered users of Map User",
                                                        "9. App opens of Map User",
                                                        "10. Regeisterd users of Top User"
                                                       ]  )
    if st.button("Submit"):
            if questions ==      "1. Transaction Amount and Count of Aggrecated  Insurance":
                                df1_csv = pd.read_csv("phonepe_data/aggrecated/1aggrecated_insurance.csv") 
                                top_charts_amount(df1_csv)
                                top_charts_count(df1_csv) 
                        
            elif questions ==    "2. Transaction Amount and Count of Map  Insurance":
                                df2_csv = pd.read_csv("phonepe_data/map/1map_insurance.csv") 
                                top_charts_amount(df2_csv)
                                top_charts_count(df2_csv)
                 
            elif questions ==    "3. Transaction Amount and Count of Top  Insurance":
                                df3_csv = pd.read_csv("phonepe_data/top/1top_insurance.csv") 
                                top_charts_amount(df3_csv)
                                top_charts_count(df3_csv)
                    
            elif questions ==    "4. Transaction Amount and Count of Aggrecated  Transaction":
                                df4_csv = pd.read_csv("phonepe_data/aggrecated/2aggrecated_transaction.csv") 
                                top_charts_amount(df4_csv)
                                top_charts_count(df4_csv)

            elif questions ==    "5. Transaction Amount and Count of Map  Transaction":
                                df5_csv = pd.read_csv("phonepe_data/map/2map_transaction.csv") 
                                top_charts_amount(df5_csv)
                                top_charts_count(df5_csv)

            elif questions ==    "6. Transaction Amount and Count of Top  Transaction":
                                df6_csv = pd.read_csv("phonepe_data/top/2top_transaction.csv") 
                                top_charts_amount(df6_csv)
                                top_charts_count(df6_csv)

            elif questions ==    "7. Transaction Count of Aggregated User":
                                df7_csv = pd.read_csv("phonepe_data/aggrecated/3aggrecated_user.csv") 
                                top_charts_count(df7_csv)

            elif questions ==    "8. Registered users of Map User":
                                df8_csv = pd.read_csv("phonepe_data/map/3map_user.csv") 
                                registerd_users(df8_csv)
 
            elif questions ==    "9. App opens of Map User":
                                df9_csv = pd.read_csv("phonepe_data/map/3map_user.csv") 
                                app_opens(df9_csv)

            elif questions ==    "10. Regeisterd users of Top User":
                                df10_csv = pd.read_csv("phonepe_data/top/3top_user.csv") 
                                registerd_users(df10_csv)

