import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import confusion_matrix
from PIL import Image
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

    col, coll = st.columns(2)
    x = df.iloc[:, :-1]

    model = ExtraTreesClassifier()
    model.fit(x, Y)
    feat_importances = pd.Series(model.feature_importances_, index=x.columns)
    with col:st.write(feat_importances)

    image = Image.open('fi.jpg')
    coll.image(image,
             caption='Feature Selection merupakan kegiatan pemodelan atau penganalisaan data yang dilakukan secara preprocessing dan bertujuan untuk memilih fitur optimal dan mengesampingkan fitur yang tidak berpengaruh terhadap target',
             use_column_width=True
             )

    image = Image.open('imp.png')
    st.image(image,
             caption='Histogram Feature Selection',
             use_column_width=True
             )

    col1, col2 = st.columns(2)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    dtc = DecisionTreeClassifier(max_leaf_nodes=3)
    dtc.fit(X_train, y_train)

    acc = dtc.score(X_test, y_test)*100
    acc = acc.astype(int)
    with col1: st.subheader("Model DecisionTree"), st.write('**Accuracy: **', acc,'%')

    fig5 = plt.figure(figsize=(8, 5))
    conf_matrix = confusion_matrix(dtc.predict(X_test), y_test)
    sns.heatmap(conf_matrix, cmap='coolwarm', annot=True)
    with col2: st.subheader("Confusion Matrix"), st.pyplot(fig5)

    col3, col4 = st.columns(2)
    with col3:  st.text(""), \
                st.text(""), \
                st.text(""), \
                st.text(""), \
                st.text(""), \
                st.text(""), \
                st.text(""), \
                st.text(""), \
                st.text(""), \
                st.text('M.Randy Anugerah'), \
                st.text(""), \
                st.text(""), \
                st.text('This Page Still in Beta Test')

    image = Image.open('fic.png')
    col4.image(image,
               caption='',
               use_column_width=True
               )
