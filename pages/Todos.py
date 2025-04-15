import streamlit as st

with open("todo.txt","r") as file:
    content=file.readlines()

result=[i.split('\n')[0] for i in content]
for index,todos in enumerate(result):
    st.write(index,todos)
