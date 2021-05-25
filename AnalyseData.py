import pandas as pd
import re
import string

class Analyse():

    def __init__(self, path="datasets/startup.csv"):
        self.df = pd.read_csv(path)
        self.cleanData()

    def cleanData(self):
        # cols = self.df.columns
        # self.df.rename(columns = { cols[1] : 'Date', 'StartupName' : 'Name', cols[-2] : 'Amount' }, inplace=True)
        # self.df.drop(columns=[cols[0], cols[-1]], inplace=True)

        # self.df['Amount'].fillna('0', inplace=True)
        # self.df['Amount'] = self.df['Amount'].str.replace(',', '')
        # self.df['Amount'] = self.df['Amount'].str.strip('+')

        # toremove = self.df.loc[self.df['Amount'].str.contains('a', na=True)]
        # self.df.drop(toremove.index, inplace=True)

        # self.df['Amount'].replace(['undisclosed'],'0', inplace=True)
        # self.df['Amount'].replace(['unknown'],'0', inplace=True)
        # self.df['Amount'].replace(['Undisclosed'],'0', inplace=True)

        # self.df['Amount'] = self.df['Amount'].astype('float64')

        self.df.columns=['SNo', 'Date', 'StartupName', 'IndustryVertical', 'SubVertical',
       'City', 'InvestorsName', 'InvestmentType', 'AmountInUSD',
       'Remarks']

        for i in range(0,len(self.df["IndustryVertical"])):
            if self.df["IndustryVertical"][i] in ["ECommerce",
                                            "ecommerce",
                                            "Ecommerce", 
                                            "E-Commerce",
                                            "E-commerce"]:
                self.df["IndustryVertical"][i]="eCommerce"
                
        for i in range(0,len(self.df["StartupName"])):
            if self.df["StartupName"][i] in ["Ola",
                                        "Ola Cabs", 
                                        "Olacabs"]:
                self.df["StartupName"][i]="Ola"  
            elif self.df["StartupName"][i] =="Flipkart.com":
                self.df["StartupName"][i]="Flipkart"    
            elif self.df["StartupName"][i] =="Paytm Marketplace":
                self.df["StartupName"][i]="Paytm"   
        for i in range(0,len(self.df["StartupName"])):
            if self.df["InvestorsName"][i] in ['Undisclosed investors',
                                            'Undisclosed Investors',
                                            'Undisclosed',
                                            'Undisclosed investor',
                                            'Undisclosed Investor',
                                            'undisclosed investors']:
                self.df["InvestorsName"][i]="Undisclosed"
            
        for i in range(0,len(self.df["StartupName"])):
            if self.df["StartupName"][i] in ["OYO",
                                        "OYO Rooms", 
                                        "OyoRooms", 
                                        "Oyorooms", 
                                        "Oyo",
                                        "Oyo Rooms"]:
                self.df["StartupName"][i]= "OYO Rooms"
            elif self.df["StartupName"][i] in ["Byjuxe2x80x99s",
                                            "BYJU'S"]:
                self.df["StartupName"][i]= "Byju's"    
            
        for i in range  (0,len(self.df["City"])):
            if self.df["City"][i] in ["New Delhi",
                                        "Delhi",
                                        "Noida", 
                                        "Gurugram",
                                        "Gurgaon"]:
                self.df["City"][i]="NCR"
            elif self.df["City"][i]=="Bangalore":
                self.df["City"][i]="Bengaluru"

        self.df.loc[self.df['City'].isin(['\\\\xc2\\\\xa0Noida', '\\xc2\\xa0Noida']), 'City'] = 'Noida'
        self.df.loc[self.df['City'].isin(['\\\\xc2\\\\xa0Bangalore', '\\xc2\\xa0Bangalore', 'Bangalore']), 'City'] = 'Bengaluru'
        self.df.loc[self.df['City'].isin(['\\\\xc2\\\\xa0New Delhi', '\\xc2\\xa0New Delhi']), 'City'] = 'New Delhi'
        self.df.loc[self.df['City'].isin(['\\\\xc2\\\\xa0Gurgaon', 'Gurugram']), 'City'] = 'Gurgaon'
        self.df.loc[self.df['City'].isin(['\\\\xc2\\\\xa0Mumbai', '\\xc2\\xa0Mumbai']), 'City'] = 'Mumbai'
                

        self.df.loc[self.df['IndustryVertical'] == "\\\\xc2\\\\xa0News Aggregator mobile app", 'IndustryVertical'] = 'News Aggregator mobile app'
        self.df.loc[self.df['IndustryVertical'] == "\\\\xc2\\\\xa0Online Jewellery Store", 'IndustryVertical'] = 'Online Jewellery Store'
        self.df.loc[self.df['IndustryVertical'] == "\\\\xc2\\\\xa0Fashion Info Aggregator App", 'IndustryVertical'] = 'Fashion Info Aggregator App'
        self.df.loc[self.df['IndustryVertical'] == "\\\\xc2\\\\xa0Online Study Notes Marketplace", 'IndustryVertical'] = 'Online Study Notes Marketplace'
        self.df.loc[self.df['IndustryVertical'] == "\\\\xc2\\\\xa0Warranty Programs Service Administration", 'IndustryVertical'] = 'Warranty Programs Service Administration'
        self.df.loc[self.df['IndustryVertical'] == "\\\\xc2\\\\xa0Pre-School Chain", 'IndustryVertical'] = 'Pre-School Chain'
        self.df.loc[self.df['IndustryVertical'] == "\\\\xc2\\\\xa0Premium Loyalty Rewards Point Management", 'IndustryVertical'] = 'Premium Loyalty Rewards Point Management'
        self.df.loc[self.df['IndustryVertical'] == "\\\\xc2\\\\xa0Contact Center Software Platform", 'IndustryVertical'] = 'Contact Center Software Platform'
        self.df.loc[self.df['IndustryVertical'] == "\\\\xc2\\\\xa0Casual Dining restaurant Chain", 'IndustryVertical'] = 'Casual Dining restaurant Chain'
        self.df.loc[self.df['IndustryVertical'] == "\\\\xc2\\\\xa0Online Grocery Delivery", 'IndustryVertical'] = 'Online Grocery Delivery'
        self.df.loc[self.df['IndustryVertical'] == "Online home d\\\\xc3\\\\xa9cor marketplace", 'IndustryVertical'] = 'Online home decor marketplace'
        self.df.loc[self.df['IndustryVertical'].isin(["Fin-Tech"]), 'IndustryVertical'] = 'FinTech'   

        self.df.loc[self.df['InvestorsName'].isin(['Undisclosed investors', 'Undisclosed', 'undisclosed investors', 'Undisclosed Investor', 'Undisclosed investors']), 'InvestorsName'] = 'Undisclosed Investors'
        self.df.loc[self.df['InvestorsName'] == "\\\\xc2\\\\xa0Tiger Global", 'InvestorsName'] = 'Tiger Global'
        self.df.loc[self.df['InvestorsName'] == "\\\\xc2\\\\xa0IndianIdeas.com", 'InvestorsName'] = 'IndianIdeas'
        self.df.loc[self.df['InvestorsName'] == "\\\\xc2\\\\xa0IvyCap Ventures, Accel Partners, Dragoneer Investment Group", 'InvestorsName'] = 'IvyCap Ventures, Accel Partners, Dragoneer Investment Group'
        self.df.loc[self.df['InvestorsName'] == "\\\\xc2\\\\xa0Goldman Sachs", 'InvestorsName'] = 'Goldman Sachs'


        self.df.drop([2602,2603,2604,2605,2606,2607,2608,2609,2610,2611], inplace = True)
        self.df.reset_index(drop=True, inplace=True)

        for i in range (0, len(self.df["AmountInUSD"])):
            self.df["AmountInUSD"][i]=re.sub('\D',"",str(self.df["AmountInUSD"][i]))
        self.df["AmountInUSD"]=pd.to_numeric(self.df["AmountInUSD"])

        for i in range (0, len(self.df["StartupName"])):
            self.df["StartupName"][i]=re.sub('xc2xa0',"",str(self.df["StartupName"][i]))

        self.df['InvestmentType'] = self.df['InvestmentType'].apply(lambda x: (str(x).replace("\\\\n"," ")))
        #Recent cleaning code is taken from  from jagannathrk notebook.

        location_map = {
            "Bengaluru": "Bangalore",
            "Delhi": "NCR",
            "New Delhi": "NCR",
            "Gurugram": "NCR",
            "Gurgaon": "NCR",
            "Noida": "NCR"
        }
        for i, v in location_map.items():
            self.df['City'][self.df['City']==i] = v

        self.df['InvestmentType'] = self.df['InvestmentType'].apply(lambda x: self.remove_punctuation(str(x)))

        funding_map = {
            "SeedAngel Funding": "Seed Angel Funding",
            "SeedFunding": "Seed Funding",
            "PrivateEquity": "Private Equity",
            "Crowd funding": "Crowd Funding",
            "Angel  Seed Funding": "Seed Angel Funding",
            "Seed  Angel Funding": "Seed Angel Funding",
            "Seed Angle Funding": "Seed Angel Funding",
            "Seed  Angle Funding": "Seed Angel Funding",
            "SeednFunding": "Seed Funding",
            "Seed funding": "Seed Funding",
            "Seed Round": "Seed Funding",
            "preSeries A": "PreSeries A",
            "preseries A": "PreSeries A",
            "Pre Series A": "PreSeries A"
        }

        for i, v in funding_map.items():
            self.df['InvestmentType'][self.df['InvestmentType']==i] = v

        self.df['Date'][self.df['Date']=='12/05.2015'] = '12/05/2015'
        self.df['Date'][self.df['Date']=='13/04.2015'] = '13/04/2015'
        self.df['Date'][self.df['Date']=='15/01.2015'] = '15/01/2015'
        self.df['Date'][self.df['Date']=='22/01//2015'] = '22/01/2015'
        self.df['Date'][self.df['Date']=='05/072018'] = '05/07/2018'
        self.df['Date'][self.df['Date']=='01/07/015'] = '01/07/2015'
        self.df['Date'][self.df['Date']=='\\\\xc2\\\\xa010/7/2015'] = '10/07/2015'
        self.df['Year'] = pd.DatetimeIndex(self.df['Date']).year

    def remove_punctuation(self, text):
        """custom function to remove the punctuation"""
        return text.translate(str.maketrans('', '', string.punctuation))

    def getDataframe(self):
        return self.df

    def getTopIndustries(self, n):
        return self.df.groupby('IndustryVertical').count().sort_values('StartupName', ascending = False).head(n)['StartupName']

    def getTopStartups(self, n):
        return self.df.groupby('StartupName').count().sort_values('IndustryVertical', ascending = False).head(n)['IndustryVertical']

    def getTopStartupsSum(self, n):
        return self.df.groupby('StartupName').sum().sort_values('AmountInUSD', ascending = False).head(n)['AmountInUSD']

    def getTypesSum(self):
        return self.df.groupby('InvestmentnName').sum().sort_values('IndustryVertical', ascending = False).head(n)['IndustryVertical']

    def getTypesCount(self):
        return self.df.groupby('InvestmentnName').count().sort_values('IndustryVertical', ascending = False).head(n)['IndustryVertical']

    def getYearwiseFundingsCount(self):
        return self.df.groupby("Year").count()['AmountInUSD']

    def getYearwiseFundingsSum(self):
        return self.df.groupby("Year").sum()['AmountInUSD']

    def getFundingsTypeCount(self, n):
        return self.df.groupby("InvestmentType").count().sort_values('AmountInUSD', ascending = False).head(n)['AmountInUSD']

    def getFundingsTypeSum(self, n):
        return self.df.groupby("InvestmentType").sum().sort_values('AmountInUSD', ascending = False).head(n)['AmountInUSD']

    def getCityCount(self, n):
        return self.df.groupby("City").sum().sort_values('AmountInUSD', ascending = False).head(n)['AmountInUSD']

    def getCitySum(self, n):
        return self.df.groupby("City").count().sort_values('AmountInUSD', ascending = False).head(n)['AmountInUSD']