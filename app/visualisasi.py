import seaborn as sns
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from matplotlib import pyplot as plt
from plotly.subplots import make_subplots
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

def app():
    df = pd.read_csv('jantungg.csv')
    df.drop('Unnamed: 0', axis='columns', inplace=True)

    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=df['age'],
        xbins=dict(
            start=40,
            end=95,
            size=2
        ),
        marker_color='#e8ab60',
        opacity=1
    ))

    fig.update_layout(
        title_text='AGE DISTRIBUTION',
        xaxis_title_text='AGE',
        yaxis_title_text='COUNT',
        bargap=0.05,
        template='plotly_dark'
    )

    st.plotly_chart(fig)

    fig = px.histogram(df, x='age', color='DEATH_EVENT', hover_data=df.columns,
                       title="AGE & DEATH_EVENT",
                       labels={"age": "AGE"},
                       template="plotly_dark",
                       color_discrete_map={"0": "RebeccaPurple", "1": "MediumPurple"}
                       )

    st.plotly_chart(fig)

    d1 = df[(df["DEATH_EVENT"] == 0) & (df["sex"] == 1)]
    d2 = df[(df["DEATH_EVENT"] == 1) & (df["sex"] == 1)]
    d3 = df[(df["DEATH_EVENT"] == 0) & (df["sex"] == 0)]
    d4 = df[(df["DEATH_EVENT"] == 1) & (df["sex"] == 0)]

    label1 = ["Male", "Female"]
    label2 = ['Male - Survived', 'Male - Died', "Female -  Survived", "Female - Died"]
    values1 = [(len(d1) + len(d2)), (len(d3) + len(d4))]
    values2 = [len(d1), len(d2), len(d3), len(d4)]

    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
    fig.add_trace(go.Pie(labels=label1, values=values1, name="GENDER"), 1, 1)
    fig.add_trace(go.Pie(labels=label2, values=values2, name="GENDER VS DEATH_EVENT"), 1, 2)

    fig.update_traces(hole=.6, hoverinfo="label+percent")
    fig.update_layout(
        title_text="GENDER DISTRIBUTION                                       GENDER & DEATH_EVENT",
        annotations=[dict(text='GENDER', x=0.18, y=0.5, font_size=10, showarrow=False),
                     dict(text='GENDER & DEATH_EVENT', x=0.875, y=0.5, font_size=9, showarrow=False)],
        autosize=False, width=800, height=400, paper_bgcolor="white")

    st.plotly_chart(fig)

    pr = ProfileReport(df, explorative=True)
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)

    st.subheader("Correlation")
    st.subheader("")
    fig, ax = plt.subplots(figsize=(15, 10))
    sns.heatmap(df.corr(), linewidths=.5, ax=ax, cmap='coolwarm', annot=True)
    st.write(fig)

    st.text('M.Randy Anugerah')
