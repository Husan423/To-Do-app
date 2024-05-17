
from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)






while True:
    user_action=input("Type add,show,edit,complete or exit:\n>>>")
    user_action=user_action.strip()
    print(user_action)
    todo = user_action[4:]
    print(todo)

    if user_action.startswith("add"):
        todo=user_action[4:]

        # file=open("todos.txt",'r')
        # todos=file.readlines()
        # file.close()
        # with context manager
        todos = get_todos()

        todos.append(todo + '\n')

        # file=open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()
        write_todos(todos, "todos.txt")

    elif user_action.startswith("show"):

        todos = get_todos()




        for index,item in enumerate(todos):
            item=item.strip('\n')
            row=f"{index+1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number=int(user_action[5:])
            print(number)

            number=number-1

            todos = get_todos()

            new_todo=input("Enter a new todo: ")
            todos[number]=new_todo+"\n"

            write_todos(todos, "todos.txt", )
        except ValueError:
            print("Invalid input")
            continue


    elif user_action.startswith("complete"):
            number=int(user_action[9:])

            todos = get_todos('todos.txt')
            index=number-1
            todo_to_remove=todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos, "todos.txt", )
            message=f"Todo {todo_to_remove} was removed from the list."
            print(message)
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid!!!")

print('Bye!')
