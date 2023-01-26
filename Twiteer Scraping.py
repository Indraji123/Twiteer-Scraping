# twiteer Scraping
# pip install snscrape (for scraping any social media web data)
# pip install pandas (for read and write data)
# pip install streamlit (for preare a web app & user interface)
import snscrape
import pandas 
import streamlit as st
import pandas as pd
import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import timedelta, date
# difining a dataframe for after use
df = pd.DataFrame()

# takig data from user user to scrape the data using streamlit
d3 = st.text_input("enter user name").strip()

col1, col2 , col3 = st.columns(3) 
d1 =  col1.date_input("enter starting date (since)")
d2 =  col2.date_input("enter ending date (untill)")
d4 =  int(col3.number_input("enter the limit how many data you want"))
st.write([str(d3),str(d1),str(d2),d4])
extractInfosBtn = st.button('Get data')
# condition & content of scraping data
if extractInfosBtn: 
    tweets_list = []
    for tweet in sntwitter.TwitterSearchScraper("from:{} since:{} until:{}".format(str(d3),str(d1),str(d2))).get_items():
        if len(tweets_list) == d4:
            break
        else:
            tweets_list.append([tweet.date, tweet.content,tweet.url])

    df = pd.DataFrame(tweets_list, columns=["date","content","url"])
    st.write(df.head(20))


# After scraping download button is ceate to download the data
downloadcol , noneed= st.columns([1,1])

downloadcol.download_button( 
label="Download to csv",
data= df.to_csv().encode('utf-8'),
file_name= 'file.csv',
mime= 'text/csv',
)



