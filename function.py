def read_todo_file(filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            todos_local = file.readlines()
        return todos_local

def append_todo_file(filepath, todo):
        with open(filepath, "a", encoding="utf-8") as file:
            file.write(todo + "\n")
        return todo

def write_todo_file(filepath, todos):
        with open(filepath, "w", encoding="utf-8") as file:
            file.writelines(todos)
            return todos
        
def remove_todo_file(filepath, todo):
        with open(filepath, "r", encoding="utf-8") as file:
            todos = file.readlines()
        todos.remove(todo + "\n")
        with open(filepath, "w", encoding="utf-8") as file:
            file.writelines(todos)
        return todo