import streamlit as st
import requests

st.title("💱 Currency Converter")

amount = st.number_input("Enter amount", min_value=1.0)

from_currency = st.text_input("From Currency (USD, INR)").upper()
to_currency = st.text_input("To Currency (USD, INR)").upper()

if st.button("Convert"):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    if to_currency in data["rates"]:
        rate = data["rates"][to_currency]
        result = amount * rate
        st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    else:
        st.error("Invalid currency code")