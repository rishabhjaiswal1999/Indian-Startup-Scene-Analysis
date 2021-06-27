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

    st.markdown('---')
    st.header("Arrival of Tourists Numbers in India")
    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getArrival(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))
    c2.plotly_chart(plotBar(analysis.getArrival(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))

    st.markdown('---')
    st.header("Percent of Share of India FTA")
    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getFTA(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="% of FTA"))
    c2.plotly_chart(plotBar(analysis.getFTA(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="% of FTA"))

    st.markdown('---')
    st.header(
        "FEE(Foreign Exchange Earning from Tourism) (in Indian Rupees Million")
    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getFEE(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="Indian Rupees Million"))
    c2.plotly_chart(plotBar(analysis.getFEE(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="Indian Rupees Million"))

    st.markdown('---')
    st.header("Tourism Total Contribution to GDP (US$ Billion)")
    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getGDP(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="US$ Billions"))
    c2.plotly_chart(plotBar(analysis.getGDP(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="US$ Billions"))

    st.markdown('---')
    st.header("Tourism contribution to GDP in Percent")
    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getGDPPercent(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="% of GDP"))
    c2.plotly_chart(plotBar(analysis.getGDPPercent(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="% of GDP"))

    st.markdown('---')
    st.header("Tourism contribution to GDP in Percent")
    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getGDPDirect(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="% of GDP"))
    c2.plotly_chart(plotBar(analysis.getGDPDirect(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="% of GDP"))

    st.markdown('---')
    st.header("Government spending on Tourism (In US$ Billion) Real Price")
    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getSpending(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="US$ Billion"))
    c2.plotly_chart(plotBar(analysis.getSpending(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="US$ Billion"))

    st.markdown('---')
    st.header("Tourism contribution to Employment ('000 jobs)")
    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getSpending(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Jobs"))
    c2.plotly_chart(plotBar(analysis.getSpending(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Jobs"))

    st.markdown('---')
    st.header("DOMESTIC TOURISM (in Million)")
    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getJobs(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists in Millions"))
    c2.plotly_chart(plotBar(analysis.getJobs(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists in Millions"))

    st.markdown('---')
    st.header("Visa on Arrival")
    c1, c2 = st.beta_columns(2)
    c1.plotly_chart(plotLine(analysis.getArrivalVisa(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))
    c2.plotly_chart(plotBar(analysis.getArrivalVisa(
    ), title="Arrival Count of Tourists in India", xlabel="Year", ylabel="No. of Tourists"))

    # st.header('Plan Period Analysis')
    # st.dataframe(analysis.getDataframe())
    # st.subheader('Fourth Five Year Plan (1969-74)')
    # st.plotly_chart(plotScatter(analysis.getDataframe(
    # ), 'Tourism Total Contribution to GDP (US$ Billion)', 'Period', 'Period.1'))

    st.header(
        "Foreign exchange earnings from tourism in India from 2000 to 2020(in billion U.S. dollars)")
    st.image('images/foreign_exchange.png', use_column_width=True)

    st.header(
        "Domestic expenditure on tourism across India from 2012 to 2018, with a forecast for 2028(in billion U.S. dollars)")
    st.image('images/domestic.png', use_column_width=True)

    st.header(
        "Number of employees in the travel and tourism sector across India from financial year 2014 to 2019(in millions)")
    st.image('images/employee.png', use_column_width=True)

    st.header(
        "Number of foreign tourist arrivals through e-tourist visa in India from 2014 to 2020(in 1,000s)")
    st.image('images/e-tourist.png', use_column_width=True)

    st.header(
        "Tourist arrivals at India from 2013 to 2019, by region(in millions)")
    st.image('images/region.png', use_column_width=True)

    st.header(
        "Number of foreign tourist arrivals in India from 2008 to 2019, by month")
    st.image('images/month.png', use_column_width=True)

    st.header(
        "Foreign tourist arrivals to India in 2019, by leading port of entry(in millions)")
    st.image('images/port.png', use_column_width=True)

    st.header(
        "Leading source countries of foreign tourist arrivals in India in 2019(in millions)")
    st.image('images/source.png', use_column_width=True)

    st.header(
        "Number of domestic tourist visits in India from 2000 to 2018, with an estimate for 2019(in millions)")
    st.image('images/visit.png', use_column_width=True)


def overview():
    st.header("Project overview")
    st.markdown("""
        ### Travel and tourism is one of the largest industries in India, with a total contribution of over 247 billion U.S. dollars to the country’s GDP and estimated to double in the coming years. Although other parts of the economy sailed on turbulent waters in recent years, the tourism industry had grown as an important source of foreign exchange for the country. And for the people on the ground, it has been creating jobs, both directly and indirectly.
        #
        ### Much like the rest of the world, the shock came in March 2020 with the onset of the coronavirus (COVID-19) pandemic. The government had to impose a strict lockdown, the first being travel restrictions. The travel and tourism industry was one of the worst impacted industries worldwide, and this was no different for India. In the hotel segment, the key indicators including occupancy rate, average daily rate, or revenue per available room shrunk in the second and third quarter of 2020. The employment situation of millions of Indians had been negatively impacted.
    """)


sidebar.header('Choose Your Option')
options = ['Overview', 'View Dataset', 'Analyse Indian Tourism']
choice = sidebar.selectbox(options=options, label="Choose Action")
if choice == options[0]:
    overview()
if choice == options[1]:
    viewDataset()
elif choice == options[2]:
    analyseTimeline()
