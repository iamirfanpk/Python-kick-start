Todos = []

while True:
    Option = input('''
    =====================
    =     TODO LIST     =
    =====================

    1 - Todos
    2 - Add a new todo
    3 -  Mark as done
    4 - Delete a todo
    q - quit

    =====================

    Enter option : ''')

    if Option == 'q':
        print('''
        😊
        ''')
        break

    elif Option == '1':
        print('''
        Current Todo List:
        ''')
        i = 1
        for Todo in Todos:
            if Todo['status']:
                print(i, Todo['task'], '✔')
            else:
                print(i, Todo['task'], '❌')
            i += 1

    elif Option == '2':
        Task = input('Enter your new task : ')
        Item = {
            'task' : Task,
            'status' : False
        }
        Todos.append(Item)


    elif Option == '4':
        Index = int(input('Enter index which task do you want to delete : '))
        del(Todos[Index-1])

    elif Option == '3':
        Index = int(input('Enter index to mark completed : ')) - 1
        Item = Todos[Index]
        Item['status'] = True  


    else:
        print('Oops😪 \nPlease select the right choice.')