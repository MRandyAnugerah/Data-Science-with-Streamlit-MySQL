import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from PIL import Image
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns

def app():

    df = pd.read_csv('jantungg.csv')
    df.drop('Unnamed: 0', axis='columns', inplace=True)
    X = df[['ejection_fraction',
            'serum_creatinine',
            'time'
            ]]
    Y = df['DEATH_EVENT']

    col1, col2 = st.columns(2)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    dtc = DecisionTreeClassifier(max_leaf_nodes=3)
    dtc.fit(X_train, y_train)

    acc = dtc.score(X_test, y_test)*100
    acc = acc.astype(int)
    with col1: st.subheader("**Explanation Model DecisionTree**"), \
               st.write('**Accuracy: **', acc,'%'),\
               st.write('Decision tree adalah model prediksi menggunakan struktur pohon atau struktur berhirarki. Penggunaan decision tree adalah kemampuannya untuk mem-break down proses pengambilan keputusan yang kompleks menjadi lebih simple, sehingga pengambil keputusan akan lebih menginterpretasikan solusi dari permasalahan.')

    image = Image.open('is.jpg')
    col2.image(image,
             caption='',
             use_column_width=True
             )

    st.subheader("**Explanation Confusion Matrix**")
    data = [["n=60", "Predicted:Negatif(0)", "Predicted:Positif(1)",""],
            ["Actual:Negatif(0)", "TN:43", "FP:6","TN+FN:49"],
            ["Actual :Positif(1)", "FN:0", "TP:11","FN+TP:11"],
            ["", "TN+FN:43", "FP+TP:17",""]]

    df2 = pd.DataFrame(data)
    st.dataframe(df2)

    col3, col4 = st.columns(2)

    with col3: st.write('Pada kasus ini :'), \
               st.write('*True Negative (TN)*: mesin berhasil memprediksi 43 pasien negatif gagal jantung dan memang benar 43 pasien negatif gagal jantung.'),\
               st.write('*False Positive (FP)*: mesin memprediksi 6 pasien positif gagal jantung tetapi prediksi salah, ternyata 6 pasien tersebut negatif gagal jantung'), \
               st.write('*True Positive (TP)*: mesin berhasil memprediksi 11 pasien positif gagal jantung dan memang benar 11 pasien positif gagal jantung.')

    with col4: st.write(''), \
               st.write(''), \
               st.write('*False Negative (FN)*: FN merupakan kesalahan fatal dalam prediksi sebuah pembelajaran mesin dimana kesalahan ini sangat berbahaya. Contoh: pasien diprediksi negatif gagal jantung padahal ternyata pasien positif gagal jantung, maka pasien tersebut terlambat mengetahui keadaan sebenarnya sehingga tidak segera dilakukan tindakan pengobatan, dimana dapat menyebabkan kematian.'), \
               st.write('**Pada Model Klasifikasi ini mesin berhasil mengatasi kesalahan fatal tersebut dengan hasil 0 pada False Negative**')

    fig5 = plt.figure(figsize=(8, 5))
    conf_matrix = confusion_matrix(dtc.predict(X_test), y_test)
    sns.heatmap(conf_matrix, cmap='PuOr', annot=True)
    st.subheader("Confusion Matrix"), st.pyplot(fig5)

    st.text('M.Randy Anugerah')
