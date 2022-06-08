def main():
    import yfinance as yf
    import pandas as pd
    import datetime 
    hour = datetime.timedelta(hours=1)

    def Step_JPYCHF():
        Symbol="JPYCHF"
        JPYCHF = yf.Ticker("JPYCHF=X")
        # get historical market data
        start_date_str="2022-04-30"
        start_date=datetime.datetime.strptime(start_date_str,'%Y-%m-%d').date()
        hist = JPYCHF.history(start=start_date,interval = "1h")
        hist=hist[["Open","High","Low","Close"]]
        new_step=hist.head(1)
        #read old and make copy of it:
        old_csv=pd.read_csv(r'../data/JPYCHF_data_2021-10-30_2022-04-30.csv')
        old_csv.set_index("Unnamed: 0", drop=True, append=False, inplace=True)
        last_row = len(old_csv) - 1
        old_csv = old_csv.drop(old_csv.index[last_row])
        old_csv.to_csv('../data/JPYCHF_step0.csv', mode='a', index=True, header=True)
    def Step_USDEUR():
        Symbol="USDEUR"
        JPYCHF_1 = yf.Ticker("EUR=X")
        start_date_str="2022-04-30"
        start_date=datetime.datetime.strptime(start_date_str,'%Y-%m-%d').date()
        hist = JPYCHF_1.history(start=start_date,interval = "1h")
        hist=hist[["Open","High","Low","Close"]]
        new_step=hist.head(1)
        #read old and make copy of it:
        old_csv=pd.read_csv(r'../data/USDEUR_data_2021-10-30_2022-04-30.csv')
        old_csv.set_index("Unnamed: 0", drop=True, append=False, inplace=True)
        last_row = len(old_csv) - 1
        old_csv = old_csv.drop(old_csv.index[last_row])
        old_csv.to_csv('../data/USDEUR_step0.csv', mode='a', index=True, header=True)
    def Step_GBPAUD():
        Symbol="GBPAUD"
        JPYCHF_2 = yf.Ticker("GBPAUD=X")
        start_date_str="2022-04-30"
        start_date=datetime.datetime.strptime(start_date_str,'%Y-%m-%d').date()
        hist = JPYCHF_2.history(start=start_date,interval = "1h")
        hist=hist[["Open","High","Low","Close"]]
        new_step=hist.head(1)
        #read old and make copy of it:
        old_csv=pd.read_csv(r'../data/GBPAUD_data_2021-10-30_2022-04-30.csv')
        old_csv.set_index("Unnamed: 0", drop=True, append=False, inplace=True)
        last_row = len(old_csv) - 1
        old_csv = old_csv.drop(old_csv.index[last_row])
        old_csv.to_csv('../data/GBPAUD_step0.csv', mode='a', index=True, header=True)
    Step_JPYCHF()
    Step_USDEUR()
    Step_GBPAUD()

if __name__ == "__main__":
    main()