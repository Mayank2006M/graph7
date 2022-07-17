import pandas as pd
import pandas_datareader as Data
import datetime as dt
import streamlit as st
import time
from PIL import Image
import yfinance as yf
l=Image.open("n.png")
st.set_page_config(page_title='Neutron',page_icon=l)

c='FTT'
cur='USD'
end=dt.datetime.now()
start='2013-12-31'
btc=Data.DataReader(f'{c}-{cur}','yahoo',start,end)
btc=btc.reset_index()
    

st.subheader('Graphs representation')
end=dt.datetime.now()
start=st.date_input('Starting date',value=pd.to_datetime('2013-12-31'))
btc=yf.download('FTT-USD',start,end)
sub_head ='<p style="font-family:Calibri; font-size: 30px;">Opening prize graph</p>'
st.markdown(sub_head,unsafe_allow_html=True)
st.line_chart(btc['Open'])
sub_head ='<p style="font-family:Calibri; font-size: 30px;">Higest prize graph</p>'
st.markdown(sub_head,unsafe_allow_html=True)
st.line_chart(btc['High'])
sub_head ='<p style="font-family:Calibri; font-size: 30px;">Lowest prize graph</p>'
st.markdown(sub_head,unsafe_allow_html=True)
st.line_chart(btc['Low'])
sub_head ='<p style="font-family:Calibri; font-size: 30px;">Closing prize graph</p>'
st.markdown(sub_head,unsafe_allow_html=True)
st.line_chart(btc['Close'])
