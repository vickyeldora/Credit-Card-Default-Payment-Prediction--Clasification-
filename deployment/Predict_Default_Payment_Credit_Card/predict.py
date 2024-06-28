import streamlit as st
import pandas as pd
import numpy as np
import pickle

# load the files!
with open('best_model.pkl','rb') as file_1: # rb = read binary
    model_lin = pickle.load(file_1)

def run():
    st.title('Predict')

    with st.form('Inout Data for Predict'):
        st.title('Data')

        limit = st.number_input('Limit Balance', min_value=10000, max_value=800000, help='Masukan limit anda')
        
        descriptions_sex = {1: "Male", 2: "Female"}
        sex = st.radio("Sex", list(descriptions_sex.keys()), format_func=lambda x: descriptions_sex[x])

        descriptions_eduaction = {1: "Graduate School", 2: "University", 3:"High School", 4:"Others", 5:"Unknown", 6:"Unknown"}
        education = st.selectbox('Education Level', options=list(descriptions_eduaction.keys()), format_func=lambda x: descriptions_eduaction[x])

        descriptions_status = {1: "Married", 2: "Single", 3:"Others"}
        status = st.selectbox('Marital Status', options=list(descriptions_status.keys()), format_func=lambda x: descriptions_status[x])
        
        age = st.number_input('Age', min_value=21, max_value=69, help='Masukan usia dengan range 21-69')
        
        st.markdown('---')
        st.title('Repayment Status')
        descriptions_pay = {-2: "pay early",
                            -1:"pay duly",
                            0:"payment delay",
                            1:"payment delay for 1 month", 
                            2:"payment delay for 2 months",
                            3:"payment delay for 3 months",
                            4:"payment delay for 4 months",
                            5:"payment delay for 5 months",
                            6:"payment delay for 6 months",
                            7:"payment delay for 7 months",
                            8:"payment delay for 8 months", 
                            9:"payment delay for 9 months and above"}
        pay0 = st.select_slider('Repayment Status in September', options=list(descriptions_pay.keys()), format_func=lambda x: descriptions_pay[x],value=-1)
        pay2 = st.select_slider('Repayment Status in August', options=list(descriptions_pay.keys()), format_func=lambda x: descriptions_pay[x],value=-1)
        pay3 = st.select_slider('Repayment Status in July', options=list(descriptions_pay.keys()), format_func=lambda x: descriptions_pay[x],value=-1)
        pay4 = st.select_slider('Repayment Status in June', options=list(descriptions_pay.keys()), format_func=lambda x: descriptions_pay[x],value=-1)
        pay5 = st.select_slider('Repayment Status in May', options=list(descriptions_pay.keys()), format_func=lambda x: descriptions_pay[x],value=-1)
        pay6 = st.select_slider('Repayment Status in April', options=list(descriptions_pay.keys()), format_func=lambda x: descriptions_pay[x],value=-1)
        
        st.markdown('---')
        st.title('Bill Statement')
        bill1 = st.number_input('Ammout of bill statement in Septemeber', min_value=-80000, max_value=800000, value=0, help='Input your ammount of bill statement in dollar')
        bill2 = st.number_input('Ammout of bill statement in Auguts', min_value=-80000, max_value=800000, value=0,help='Input your ammount of bill statement in dollar')
        bill3 = st.number_input('Ammout of bill statement in July', min_value=-80000, max_value=800000, value=0,help='Input your ammount of bill statement in dollar')
        bill4 = st.number_input('Ammout of bill statement in June', min_value=-80000, max_value=800000, value=0,help='Input your ammount of bill statement in dollar')
        bill5 = st.number_input('Ammout of bill statement in May', min_value=-80000, max_value=800000, value=0,help='Input your ammount of bill statement in dollar')
        bill6 = st.number_input('Ammout of bill statement in April', min_value=-80000, max_value=800000, value=0,help='Input your ammount of bill statement in dollar')
        
        st.markdown('---')
        st.title('Previous Payment')
        payamt1 = st.number_input('Ammout of previous payment in Septemeber', min_value=0, max_value=1300000, value=0,help='Input your ammount of previous payment in dollar')
        payamt2 = st.number_input('Ammout of previous payment in August', min_value=0, max_value=1300000, value=0,help='Input your ammount of previous payment in dollar')
        payamt3 = st.number_input('Ammout of previous payment in July', min_value=0, max_value=1300000, value=0,help='Input your ammount of previous payment in dollar')
        payamt4 = st.number_input('Ammout of previous payment in June', min_value=0, max_value=1300000, value=0,help='Input your ammount of previous payment in dollar')
        payamt5 = st.number_input('Ammout of previous payment in May', min_value=0, max_value=1300000, value=0,help='Input your ammount of previous payment in dollar')
        payamt6 = st.number_input('Ammout of previous payment in April', min_value=0, max_value=1300000, value=0,help='Input your ammount of previous payment in dollar')
        
        st.markdown('---')
        submit = st.form_submit_button('Predict Default Payment Next Month')
        pass

        df_inf = {
            'limit_balance': limit, 
            'sex': sex, 
            'education_level': education, 
            'martial_status': status, 
            'age':age,
            'pay_0': pay0, 
            'pay_2': pay2, 
            'pay_3': pay3, 
            'pay_4': pay4, 
            'pay_5': pay5, 
            'pay_6': pay6,
            'bill_amt_1': bill1,
            'bill_amt_2': bill2, 
            'bill_amt_3': bill3, 
            'bill_amt_4': bill4, 
            'bill_amt_5': bill5, 
            'bill_amt_6': bill6,
            'pay_amt_1': payamt1, 
            'pay_amt_2': payamt2, 
            'pay_amt_3': payamt3, 
            'pay_amt_4': payamt4, 
            'pay_amt_5': payamt5,
            'pay_amt_6': payamt6,}
        
#
        #DATAFRAME
        df_new = pd.DataFrame([df_inf])

        # y_pred_inf = model_lin.predict(df_inf)

        # if submint:
        #     st.subheader("Prediction Result:")
        #     st.write(f'# Player Rating: {y_pred_inf}')
            # if y_pred_inf == 0:
            #     st.write(f'## Not Default Payment')
            # elif y_pred_inf == 1:
            #     st.write(f'## Default Payment')
            
        if submit:
            y_pred_inf = model_lin.predict(df_new)
            st.subheader("Prediction Result:")
            if y_pred_inf[0] == 1:
                st.write("Default Payment")
            else:
                st.write("Not Default Payment")


if __name__ == '__main__':
    run()