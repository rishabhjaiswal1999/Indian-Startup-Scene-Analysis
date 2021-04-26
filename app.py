import streamlit as st

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd
from database import Report
from visualization import plot, plotBar
from AnalyseData import Analyse

engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

analysis = Analyse()

st.title('Analysis on Indian Startup Scene')
# st.markdown("""
# # This is Heading 1
# ## This is Heading 2
# ### This is Heading 3
# #### This is Heading 4
# ##### This is Heading 5

# ![My Image](https://yostartups.com/wp-content/uploads/2016/01/startup-incubator.png)
# <img src="https://yostartups.com/wp-content/uploads/2016/01/startup-incubator.png" alt="drawing" width="500"/>
# """)
sidebar = st.sidebar

def viewForm():

    st.plotly_chart(plot())

    title = st.text_input("Report Title")
    desc = st.text_area('Report Description')
    btn = st.button("Submit")

    if btn:
        report1 = Report(title = title, desc = desc, data = "")
        sess.add(report1)
        sess.commit()
        st.success('Report Saved')

def viewReport():
    reports = sess.query(Report).all()
    titlesList = [ report.title for report in reports ]
    selReport = st.selectbox(options = titlesList, label="Select Report")
    
    reportToView = sess.query(Report).filter_by(title = selReport).first()

    markdown = f"""
        ## {reportToView.title}
        ### {reportToView.desc}
        
    """

    st.markdown(markdown)

def analyseIndustry():
    st.header('Analysis of Startup Industries')
    data = analysis.getTopIndustries(20)
    st.plotly_chart(plotBar(data, 'Trending Startup Industries', 'No. of STartups', 'Industry Name'))

sidebar.header('Choose Your Option')
options = [ 'View Database', 'Analyse Industry', 'View Report' ]
choice = sidebar.selectbox( options = options, label="Choose Action" )

if choice == options[1]:
    analyseIndustry()
elif choice == options[2]:
    viewReport()