import streamlit as st

st.title("Power Calculator")
st.write("This is a simple power calculator that can calculate the power of a number.")

n=st.number_input("Enter a number" , value=1, step=1)

square=n**2
cube=n**3
fifth=n**5

st.write(f"The sqaure of {n} is :",{square})
st.write(f"The cube of {n} is :",{cube})
st.write(f"The fifth power of {n} is :",{fifth})