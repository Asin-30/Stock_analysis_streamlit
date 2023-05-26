import streamlit as st
import numpy as np 
import pandas as pd 
import yfinance as yf
import datetime as dt

st.title("Stock Market Analysis page") # title on the page
st.write("This is my first app") # creating text

# create a dataframe
# st.write(
#     pd.DataFrame(
#         {
#             'first_col':[1,2,3],
#             'secon_col': [4,5,6]
#         }
#     )
# )

# st.write('This is my firrst app')


# Building stock app
stock_name = st.text_input("please enter stock name: ", 'MSFT', key = 'placeholder')

ticker_symbol = stock_name
ticker_data= yf.Ticker(ticker_symbol)


#input data from user

col1, col2 = st.columns(2)

with col1:
   st.write("Enter start date:")

   start_date = st.date_input(
    "Start date for analysis: ",
    dt.date(2019, 7, 6))

with col2:
   st.write("Enter end date")

   end_date = st.date_input(
    "End date for analysis: ",
    dt.date(2020, 7, 6))

# get historical market data
ticker_df = ticker_data.history(period="1d" ,start = f"{start_date}", end = f"{end_date}")


st.write(f"we are viewing info for {ticker_symbol}")
st.write(ticker_df ) # sometimes doesn't giver proper format so st.dataframe can be used.

# st.dataframe(ticker_df)



# plotting charts
col1, col2 = st.columns(2)

with col1:
   st.write("Volume price analysis")
   st.line_chart(ticker_df['Volume'])

with col2:
   st.write("Close price analysis")
   st.line_chart(ticker_df['Close'])
