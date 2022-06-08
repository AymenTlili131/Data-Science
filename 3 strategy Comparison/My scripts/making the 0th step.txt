def main():
    import os
    os.system('cmd /c "pip install -r requirements.txt"') 
    import yfinance as yf
    Symbol="JPYCHF"
    JPYCHF = yf.Ticker("JPYCHF=X")

    # get stock info
    #print(JPYCHF.info)

    # get historical market data
    start_date="2021-10-30"
    end_date="2022-04-30"
    hist = JPYCHF.history(start="2021-10-30",end="2022-04-30",interval = "1h",auto_adjust = True)

    hist=hist[["Open","High","Low","Close"]]
    hist.to_csv(r'..\data\{Sym}_data_{s}_{e}.csv'.format(Sym=Symbol,s=start_date,e=end_date), index=True)

    Symbol="USDEUR"
    JPYCHF = yf.Ticker("EUR=X")
    hist = JPYCHF.history(start="2021-10-30",end="2022-04-30",interval = "1h",auto_adjust = True)
    hist=hist[["Open","High","Low","Close"]]
    hist.to_csv(r'..\data\{Sym}_data_{s}_{e}.csv'.format(Sym=Symbol,s=start_date,e=end_date), index=True)


    Symbol="GBPAUD"
    JPYCHF = yf.Ticker("GBPAUD=X")
    hist = JPYCHF.history(start="2021-10-30",end="2022-04-30",interval = "1h",auto_adjust = True)
    hist=hist[["Open","High","Low","Close"]]
    hist.to_csv(r'..\data\{Sym}_data_{s}_{e}.csv'.format(Sym=Symbol,s=start_date,e=end_date), index=True)

if __name__ == "__main__":
    main()