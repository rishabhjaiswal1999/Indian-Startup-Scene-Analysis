import pandas as pd

class Analyse():

    def __init__(self, path="datasets/startup.csv"):
        self.df = pd.read_csv(path)
        self.cleanData()

    def cleanData(self):
        cols = self.df.columns
        self.df.rename(columns = { cols[1] : 'Date', 'Startup Name' : 'Name', cols[-2] : 'Amount' }, inplace=True)
        self.df.drop(columns=[cols[0], cols[-1]], inplace=True)

        self.df['Amount'].fillna('0', inplace=True)
        self.df['Amount'] = self.df['Amount'].str.replace(',', '')
        self.df['Amount'] = self.df['Amount'].str.strip('+')

        toremove = self.df.loc[self.df['Amount'].str.contains('a', na=True)]
        self.df.drop(toremove.index, inplace=True)

        self.df['Amount'].replace(['undisclosed'],'0', inplace=True)
        self.df['Amount'].replace(['unknown'],'0', inplace=True)
        self.df['Amount'].replace(['Undisclosed'],'0', inplace=True)

        self.df['Amount'] = self.df['Amount'].astype('float64')

    def getTopIndustries(self, n):
        return self.df.groupby('Industry Vertical').count().sort_values('Name', ascending = False).head(n)['Name']