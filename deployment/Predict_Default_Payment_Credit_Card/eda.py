# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
from plotly.express import pie
from PIL import Image

st.set_page_config(
    page_title= 'CREDIT CARD PREDICT',
    layout= 'wide',
    initial_sidebar_state='expanded'
)

def run():
    #membuat title
    st.title('CREDIT CARD DEFAULT PAYMENT PREDICT')

    # buat sub header
    st.subheader('EDA untuk analisis Dataset Credit Card Default ayment')

    st.image('https://cdn.britannica.com/02/160902-050-B58BAD84/Credit-cards.jpg'
             ,caption='Credit Card')
    
    # menambah deskripsi
    st.write('Page ini dibuat oleh Vicky Eldora Wuisan')

    # membuat garis lurus
    st.markdown('---')

    # magic syntax 
    '''
    Pada page kali ini, penulis akan melakukan 
    eksplorasi sederhana mengenai sex, umur, education level, martial status, pembayaran, dan masih banyak lagi
    Dataest yang digunakan adalah dataset Credit Card Default Payment.
    '''

    # Load dataset
    df=pd.read_csv('P1G5_Set_1_vicky_eldora.csv')
    st.dataframe(df)

    # membuat pie chart
    st.write("#### Pie Chart")
    sex_counts = df['sex'].value_counts()  # Get sex distribution
    fig = pie(sex_counts, labels=sex_counts.index, values=sex_counts.values, title='Male vs. Female')
    fig.update_layout(
    xaxis_title="Jenis Kelamin (1: Laki-laki, 2: Perempuan)",
    autosize=True  # Adjust figure size automatically
    )
    st.plotly_chart(fig)

    # Membuat Barplot
    st.write('##### Age')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='age', data=df)
    st.pyplot(fig)

    # Membuat Barplot
    st.write('##### Martial status')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='martial_status', data=df)
    st.pyplot(fig)

    # Membuat Barplot
    st.write('##### Education Level')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='education_level', data=df)
    st.pyplot(fig)

    # Membuat Histogram berdasarkan input user
    st.write('#### Repayment Status in September, August, July, June, May, April')
    pilihan = st.selectbox('Pilih kolom:',
                           ('pay_0','pay_2','pay_3','pay_4','pay_5','pay_6'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(df[pilihan], bins = 30)
    st.pyplot(fig)

    # Membuat Barplot
    st.write('##### Default Payment')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='default_payment_next_month', data=df)
    st.pyplot(fig)

if __name__ == '__main__':
    run()