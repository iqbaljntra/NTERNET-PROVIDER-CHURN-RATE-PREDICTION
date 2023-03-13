import streamlit as st
import pandas as pd
import numpy as np
import joblib

with open('all_process', 'rb') as file_1:
  all_process= joblib.load(file_1)



battery_power = st.slider('Masukan Jenis Batre (Dalam Mha)',501, 1998, step=1)
px_height =  st.slider('Masukan Panjang',500, 1960)
px_width =  st.slider('Masukan Lebar',500, 1998)
ram = st.slider('Masukan Jumlah Ram:',256, 3998)
four_g = st.radio('Masukan 4G 1=ya, 0=tidak',(1,0))
touch_screen = st.radio('Masukan Touch Screen? 1=ya, 0=tidak',(1,0))
dual_sim = st.radio('Masukan Dual Sim? 1=ya, 0=tidak',(1,0))
n_cores = st.radio('Masukan Jumlah Core?',(2, 3, 5, 6, 1, 8, 4, 7))
primary_camera = st.radio('Masukan Pixel Camera Belakang',(4, 11, 16, 21,  2))
front_camera = st.radio('Masukan Pexel Camera Depan',(4, 11, 16, 20,  2))



if st.button('Predict'):

    data_inf = pd.DataFrame({'battery_power' : battery_power, 
                             'px_height' : px_height, 
                             'px_width' : px_width, 'ram':ram,
                             'four_g' : four_g, 
                             'touch_screen' : touch_screen, 
                             'dual_sim' : dual_sim, 
                             'n_cores' : n_cores, 
                             'primary_camera' : primary_camera,
                             'front_camera' : front_camera},index=[0])
    hasil = all_process.predict(data_inf)
    if hasil == 0 :
        pred = 'Low Cost'
        st.write(pred)
    elif hasil == 1 :
        pred = 'Medium Cost'
        st.write(pred)
    elif hasil == 2 :
        pred = 'High cost'
        st.write(pred)
    else :
            pred = 'Very High Cost'
            st.write(pred)
    