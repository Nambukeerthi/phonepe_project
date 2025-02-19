<h1> Phonepe_Pulse_Data_Visualization_and_Exploration  </h1>


<h1 align="center">
  <br>
  <a href=""><img src="images/phonepe2.png" alt="Phonepe Pulse Data Visualization" width="200"></a>
  <br>
  <br>
</h1>


<p align="center">
  <a href="#Introduction"></a> 
  <a href="#Technologies Applied"></a> 
</p>

Video Link: [Linked-IN Video](https://www.linkedin.com/posts/keerthi-r-9b8839283_project-name-phonepe-pulse-data-visualization-activity-7296601209677787136-LPuf?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEUARVwBltI0ri4ApeK7YzcbHxGViaHfWEM)

Portfolio: [Nambu Keerthi](https://portfolio-b5zieg8xn5nhwau5b4bhp8.streamlit.app/)

## Introduction 
The purpose of this project is to create an intuitive Streamlit app that pulls data about a YouTube channel from the Google API, stores it in a MongoDB database, moves it to a SQL data warehouse, and then lets users perform searches for channel details and join tables to view the data.



## Technologies Applied
* python
* streamlit 
* Plotly 
* Pandas
* Numpy
* json
* OS


## Project Setup
1. Firstly install all the required extensions/libraries/modules in the requirements.txt
```
pip install -r requirements.txt
```
    After installing the required libraries one need to import them in the program before one can use them.
```
import streamlit as st
from PIL import Image
import numpy as np
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import os
import json

```
   
2. Now one need to clone the GitHub Repository to fetch the data from the Phonepe pulse GitHub repository.
```
from git.repo.base import Repo
Repo.clone_from("Github Repository URL that need to be cloned", "Local URL where one need to clone there data")

```

3. Data Tranformation - JSON to Pandas DataFrame. After the Data Extraction part is completed one need to transform the data. The data that was extracted from the Phonepe Pulse Repository is in form of .json file, now we need to transform that data into Pandas DataFrame for visualisatiopn and etc.

4. After that one need to create a MySQL Database in there local system. Now below is the Python code to connect to that SQL Database.
```
hostname = "your host name goes here"
database = "your database name goes here"
username = "your username goes here"
pwd = "your password goes here"

mydb = sql.connect(host=hostname, user=username, password=pwd, database=database)
                   
cursor1 = mydb.cursor()
```

5. The last process is create the streamlit application and it by using the below comment. 
```
streamlit run phonpe.py
```
