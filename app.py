import streamlit as st

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd
from database import Report
from visualization import *
from AnalyseData import Analyse

engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

analysis = Analyse()

st.title('Indian Startup Scene Analysis')
st.image('logo.jpg')
st.markdown("---")
sidebar = st.sidebar

def viewDataset():
    st.header('Data Used in Project')
    dataframe = analysis.getDataframe()

    with st.spinner("Loading Data..."):
        st.dataframe(dataframe)

        st.markdown('---')
        cols = st.beta_columns(4)
        cols[0].markdown("### No. of Rows :")
        cols[1].markdown(f"# {dataframe.shape[0]}")
        cols[2].markdown("### No. of Columns :")
        cols[3].markdown(f"# {dataframe.shape[1]}")
        st.markdown('---')

        st.header('Summary')
        st.dataframe(dataframe.describe())
        st.markdown('---')

        types = {'object' : 'Categorical', 'int64': 'Numerical', 'float64': 'Numerical'}
        types = list(map(lambda t: types[str(t)], dataframe.dtypes))
        st.header('Dataset Columns')
        for col, t in zip(dataframe.columns, types):
            st.markdown(f"### {col}")
            cols = st.beta_columns(4)
            cols[0].markdown('#### Unique Values :')
            cols[1].markdown(f"# {dataframe[col].unique().size}")
            cols[2].markdown('#### Type :')
            cols[3].markdown(f"## {t}")

def analyseTimeline():
    st.header('Year wise Startup Fundings')
    st.plotly_chart(plotBar(analysis.getYearwiseFundingsCount(), 'title', 'xlable', 'ylabel'))
    
    st.header('Year wise Startup Fundings Sum')
    st.plotly_chart(plotBar(analysis.getYearwiseFundingsSum(), 'title', 'xlable', 'ylabel'))

def analyseFundings():
    st.header('Year wise Startup Fundings')


def analyseIndustry():
    st.header('Analysis of Startup Industries')

    n = st.select_slider(options=[10, 40, 60] , label="Select Count")

    data = analysis.getTopIndustries(n)
    st.plotly_chart(plotBar(data, 'Trending Startup Industries', 'Name of Industry', 'Number of startup'))

    data = analysis.getTopStartups(n)
    st.plotly_chart(plotBar(data, 'Trending Startups', 'Name of startups', 'Number of Funding'))

    data = analysis.getTopStartupsSum(n)
    st.plotly_chart(plotBar(data, 'Trending Startups', 'Name of startups', 'Total Funding'))

    data = analysis.getFundingsTypeCount(n)
    st.plotly_chart(plotBar(data, 'Top funding type', 'Funding type', 'Number of Fundings'))

    data = analysis.getFundingsTypeSum(n)
    st.plotly_chart(plotBar(data, 'Trending Startups', 'No. of Fundings', 'Startup Name'))

    data = analysis.getCitySum(n)
    st.plotly_chart(plotBar(data, 'Trending Startups', 'No. of Fundings', 'Startup Name'))

    data = analysis.getCityCount(n)
    st.plotly_chart(plotBar(data, 'Trending Startups', 'No. of Fundings', 'Startup Name'))

def overview():
    st.header("project overview")
    st.markdown("""
    1. First ordered list item
    2. Another item
    """)

sidebar.header('Choose Your Option')
options = [ 'Project Overview','View Dataset', 'Analyse Industry', 'Analyse Timeline' ]
choice = sidebar.selectbox( options = options, label="Choose Action" )

if choice == options[0]:
    overview()
if choice == options[1]:
    viewDataset()
elif choice == options[2]:
    analyseIndustry()
elif choice == options[3]:
    analyseTimeline()




