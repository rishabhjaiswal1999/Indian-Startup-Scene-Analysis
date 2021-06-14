import streamlit as st
from visualization import *
from AnalyseData import Analyse

analysis = Analyse('datasets/tourism_india.xlsx')

st.title('Indian Tourism Analysis')
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

        types = {'object': 'Categorical',
                 'int64': 'Numerical', 'float64': 'Numerical'}
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
    st.header('Analyse Timeline of Tourism in India')

    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getArrival(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))
    c2.plotly_chart(plotBar(analysis.getArrival(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))

    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getFTA(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))
    c2.plotly_chart(plotBar(analysis.getFTA(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))

    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getFEE(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))
    c2.plotly_chart(plotBar(analysis.getFEE(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))

    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getGDP(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))
    c2.plotly_chart(plotBar(analysis.getGDP(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))

    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getGDPPercent(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))
    c2.plotly_chart(plotBar(analysis.getGDPPercent(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))

    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getGDPDirect(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))
    c2.plotly_chart(plotBar(analysis.getGDPDirect(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))

    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getSpending(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))
    c2.plotly_chart(plotBar(analysis.getSpending(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))

    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getSpending(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))
    c2.plotly_chart(plotBar(analysis.getSpending(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))

    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getJobs(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))
    c2.plotly_chart(plotBar(analysis.getJobs(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))

    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getArrivalVisa(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))
    c2.plotly_chart(plotBar(analysis.getArrivalVisa(), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))



def overview():
    st.header("project overview")
    st.markdown("""
    1. First ordered list item
    2. Another item
    """)


sidebar.header('Choose Your Option')
options = ['Overview', 'View Dataset', 'Analyse Timeline']
choice = sidebar.selectbox(options=options, label="Choose Action")
if choice == options[0]:
    overview()
if choice == options[1]:
    viewDataset()
elif choice == options[2]:
    analyseTimeline()
