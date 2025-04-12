import streamlit as st
import functionTodo as ft
import os

if not os.path.exists('todo.txt'):
    with open('todo.txt','w'):
        pass
todos=ft.get_todos()
def add_todo():
    todo=st.session_state['new_todo']+ '\n'
    todos.append(todo)
    ft.write_todos(todos)
st.title("My Task App")
st.subheader("Increase your productivity with ease!")
st.write("Hey folks! This app helps to track your daily tasks and you won't forget your important tasks ;)")

for index,i in enumerate(todos):
    checkbox=st.checkbox(i,key=i)
    if checkbox:
        todos.pop(index)
        ft.write_todos(todos)
        del st.session_state[i]
        st.rerun()

st.text_input(label="",placeholder="Add your task here..",on_change=add_todo,key='new_todo')

print("hello")
st.session_state
