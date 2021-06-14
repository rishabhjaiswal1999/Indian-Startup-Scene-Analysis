import pandas as pd


class Analyse():

    def __init__(self, path):
        self.df = pd.read_excel(path, skipfooter=13, skiprows=range(1))
        self.cleanData()

    def cleanData(self):
        self.df.drop(columns=['Plan Period', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15',
                              'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19',
                              'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23',
                              'Unnamed: 24', 'Unnamed: 25'], inplace=True, axis=1)

    def getDataframe(self):
        return self.df

    def getArrival(self):
        return self.df.set_index('Period')['Foreing Tourist Arrival']

    def getFTA(self):
        return self.df.set_index('Period')['Percent of Share of India FTA ']

    def getFEE(self):
        return self.df.set_index('Period')['FEE(Foreign Exchange Earning from Tourism) (in Indian Rupees Million']

    def getGDP(self):
        return self.df.set_index('Period')['Tourism Total Contribution to GDP (US$ Billion)']

    def getGDPPercent(self):
        return self.df.set_index('Period')['Tourism contribution to GDP in Percent']

    def getGDPDirect(self):
        return self.df.set_index('Period')['Direct Contribution to GDP (in US$Billion)']

    def getSpending(self):
        return self.df.set_index('Period')['Government spending on Tourism (In US$ Billion) Real Price']

    def getJobs(self):
        return self.df.set_index('Period')["Tourism contribution to Employment ('000 jobs)"]

    def getDomestic(self):
        return self.df.set_index('Period')['DOMESTIC TOURISM (in Million)']

    def getArrivalVisa(self):
        return self.df.set_index('Period')['Visa on Arrival']

    def getFEEDoller(self):
        return self.df.set_index('Period')['FEE (US$ Million)']

    def getArrivaal(self):
        return self.df.set_index('Period')['']

    def getArriaval(self):
        return self.df.set_index('Period')['']

    def getArrivaal(self):
        return self.df.set_index('Period')['']

    def getArrivaal(self):
        return self.df.set_index('Period')['']

    def getArrivaal(self):
        return self.df.set_index('Period')['']
