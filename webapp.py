import streamlit as st
# This is a simple Streamlit app for managing a to-do list
import function

path = "todos.txt"  # Path to the todo file

def add_task():
    todo = st.session_state.get("new_task", "").strip()  # Get the new task from session state
    function.append_todo_file(path, todo)  # Append the new task to the file

st.title("To-Do List App")
st.subheader("Manage your tasks efficiently")
read_tasks = function.read_todo_file(path)

for index, task in enumerate(read_tasks):
   checkbox = st.checkbox(task, key=task)
   if checkbox:
         read_tasks.pop(index)
         function.write_todo_file(path, read_tasks)  # Update the file after removing
         del st.session_state[task]  # Remove the task from session state
         st.rerun()
    
    #modules.function.remove_todo_file(path, task.strip())  # Remove the task from the
st.text_input(label="Add a new task", placeholder="Enter task here", on_change=add_task, key="new_task")

