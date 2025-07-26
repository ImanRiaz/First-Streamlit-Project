import streamlit as st
st.title("Welcome to my first streamlit app!")
st.write("Please fill the form to print customized message.")
name=st.text_input("Enter your name: ",key="name")
age=st.number_input("Enter your age: ",min_value=0,max_value=100,key="age")
email=st.text_input("Enter your email: ",key="email")


col1,col2=st.columns(2)

with col1:
    if st.button("Save information."):
        st.success("Information saved.")

with col2:
    if st.button("Print Information"):
        st.write("Your name is ",name)
        st.write("Your age is ",age)
        st.write("Thank you for using our app. See you soon.")
