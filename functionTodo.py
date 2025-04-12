def get_todos(filepath='todo.txt'):
    with open(filepath,'r') as file:
        todo_local=file.readlines()
    return todo_local

def write_todos(todo_arg,filepath='todo.txt'):
    """ writes the to-do item in the file."""
    with open(filepath,'w') as file:
            todo_local=file.writelines(todo_arg)
    return todo_local


if __name__=="__main__":
      print("hello guys!")