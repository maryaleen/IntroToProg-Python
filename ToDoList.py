# Assignment 06
# Title: To Do List
# Description: Read data from text file, and allow user to add or
# remove items, view or save To Do List data, and exit.
# -------------------------- ChangeLog ---------------------------
#   Developer:      Date:       Reason:
#   MWilliams       08/14/2019  Assignment05 Initial Release
#   MWilliams       08/18/2019  Refactor code to use a Class and
#                               Functions for Assignment 06.


class Tasks(object):
    # Class for task list (to do list)
    # Defines methods for managing list

    # 0 - Read from file to create list/dictionary table
    @staticmethod
    def read_todo():
        obj_file = open('ToDo.txt', 'r')  # renamed objFile to follow PEP 8
        lines = obj_file.readlines()
        todo_list = []  # renamed todoList to follow PEP 8
        for item in lines:
            row = (item.split(','))
            dictrow = {'Tasks': row[0].strip(), 'Priority': row[1].strip()}
            todo_list.append(dictrow)
        obj_file.close()
        return todo_list

    # 1 - Show current list
    @staticmethod
    def view_todo(a):
        todo_list = a
        print('\n---- Current To Do List: ----')
        for place in todo_list:
            print(place.get('Tasks') + ', ' + place.get('Priority'))
        print('-------- End of List --------\n')

    # 2 - Add new item to To Do List
    @staticmethod
    def add_task(b):
        todo_list = b
        task = input('Type task name: ')
        priority = input('Type task priority: ')
        dictrow = {'Tasks': task, 'Priority': priority}
        todo_list.append(dictrow)
        return todo_list

    # 3 - Remove item from To Do List
    @staticmethod
    def rm_task(c):
        todo_list = c
        rmtask = input('Type the name of the task you want to remove: ')
        for row in todo_list:
            if row['Tasks'] == rmtask:
                todo_list.remove(row)
        return todo_list

    # 4 - Save To Do List to file
    @staticmethod
    def save_todo(d):
        todo_list = d
        obj_file = open('ToDo.txt', 'w')
        for place in todo_list:
            obj_file.write(place.get('Tasks') + ', ' + place.get('Priority') + '\n')
        obj_file.close()


# Instantiate Tasks class as userList
userList = Tasks()

# Create initial to do list with the read_todo() method
master_list = userList.read_todo()


# Allow user to interact with to do list or exit program
while True:
    print('---- To Do List Actions: ----')
    choice = int(input('1 - View current list\n'
                       '2 - Add new item\n'
                       '3 - Remove item\n'
                       '4 - Save list to file\n'
                       '5 - Save list and exit program\n\n'
                       'Enter 1, 2, 3, 4 or 5.\n'))

    # 1 - Show current list
    if choice == 1:
        userList.view_todo(master_list)

    # 2 - Add new item to To Do List
    elif choice == 2:
        master_list = userList.add_task(master_list)

    # 3 - Remove item from To Do List
    elif choice == 3:
        master_list = userList.rm_task(master_list)

    # 4 - Save To Do List to file
    elif choice == 4:
        userList.save_todo(master_list)

    # 5 - Save To Do List and Exit Program
    elif choice == 5:
        userList.save_todo(master_list)
        exit()

    # Handle bad user input
    else:
        print('Incorrect input. Try again.\n')