import pandas as pd


class Data():

    def fetch_data(self):
        url_pox_cases = "https://docs.google.com/spreadsheets/d/12OND1wYiqBGbp2XFmxGgMOItoTG55ojK-FMLmTSh-jU/export?format=csv"
        self.df_pox_cases = pd.read_csv(url_pox_cases)

    @staticmethod
    def preprocess_cases_data(df):
        df = df.groupby(['Province_State']).sum()
        df.loc['Total'] = df.sum()
        df = df.T #transpone the data matrix, states to columns and the dates to rows
        # # If there are less than 10 new cases in last 7 days, we omit that state
        # grouped_df = grouped_df.loc[:, (grouped_df.iloc[-7:, :] > 10).all(axis=0)]
        # grouped_df.index = pd.to_datetime(grouped_df.index, infer_datetime_format=True)
    #    df = df.rename(index=str, columns={"Province_State":"Date})
        df = df.set_index('Province_State').T
        df = df.set_index('Province_State').T.rename_axis('Date')
        return df

    @staticmethod
    def daily_data(df):
        new_df = df.diff()
        new_df = new_df.iloc[1:, :]
        return new_df

if __name__ == "__main__":
    d = Data()
    d.fetch_data()
    x = d.preprocess_cases_data(d.df_pox_cases)
    df = x
#    x = df.rename(columns={"Province_State":"Date"})
#    print(type(x))
    print(x)
#    y = d.daily_data(d.df_pox_cases)
#    print(y)
