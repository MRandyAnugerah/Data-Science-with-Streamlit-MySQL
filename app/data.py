import streamlit as st
import pandas as pd
import mysql.connector

def app():
    conn = mysql.connector.connect( host="localhost",
                                    port="3306",
                                    user="root",
                                    passwd="",
                                    db="jantung"
                                  )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jantunggg LIMIT 1,300")
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['age',
                                     'anaemia',
                                     'creatinine_phosphokinase',
                                     'diabetes',
                                     'ejection_fraction',
                                     'high_blood_pressure',
                                     'platelets',
                                     'serum_creatinine',
                                     'serum_sodium',
                                     'sex',
                                     'smoking',
                                     'time',
                                     'DEATH_EVENT']
                      )
    df.to_csv("jantungg.csv")
    df = pd.read_csv('jantungg.csv')
    df.drop('Unnamed: 0', axis='columns', inplace=True)
    df['age']= df['age'].astype(int)

    st.subheader("Data diambil dari kaggle :")
    st.markdown("[DOWNLOAD](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data)")
    st.dataframe(df)

    shwdata = st.multiselect('Pilih Kolom yang mau ditampilkan:', df.columns, default=[])
    st.write(df[shwdata])

    st.text('M.Randy Anugerah')
