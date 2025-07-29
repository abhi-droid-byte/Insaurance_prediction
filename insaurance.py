import pickle
import streamlit as st
model1=pickle.load(open("insaurance.pkl","rb"))

def mydeploy():
    st.title("insaurance prediction")
    age=st.number_input("Enter your age:")
    pred=st.button("predict")

    if pred:
        x=model1.predict([[age]])
        st.write("insaurance is :", x[0])
mydeploy()


