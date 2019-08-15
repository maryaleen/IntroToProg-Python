# Assignment 05
# Title: To Do List
# Description: Read data from text file, and allow user to add or
# remove items, view or save To Do List data, and exit.
# -------------------------- ChangeLog ---------------------------
#   Developer:      Date:       Reason:
#   MWilliams       08/14/2019  Assignment05 Initial Release


wLoop = True

# Initial file scrub to create list/dictionary table
objFile = open('ToDo.txt', 'r')
lines = objFile.readlines()
todoList = []
for item in lines:
    row = (item.split(','))
    dictrow = {'Tasks': row[0].strip(), 'Priority': row[1].strip()}
    todoList.append(dictrow)
objFile.close()

# Display To Do List to user
print('\n---- Current To Do List: ----')
for place in todoList:
    print(place.get('Tasks') + ', ' + place.get('Priority'))
print('-------- End of List --------\n')

# Allow user to interact with To Do List or exit program
while wLoop:
    print('---- To Do List Actions: ----')
    choice = int(input('1 - View current list\n'
                       '2 - Add new item\n'
                       '3 - Remove item\n'
                       '4 - Save list to file\n'
                       '5 - Save list and exit program\n\n'
                       'Enter 1, 2, 3, 4 or 5.\n'))

    # 1 - Show current list
    if choice == 1:
        print('\n---- Current To Do List: ----')
        for place in todoList:
            print(place.get('Tasks') + ', ' + place.get('Priority'))
        print('-------- End of List --------\n')

    # 2 - Add new item to To Do List
    elif choice == 2:
        task = input('Type task name: ')
        priority = input('Type task priority: ')
        dictrow = {'Tasks': task, 'Priority': priority}
        todoList.append(dictrow)

    # 3 - Remove item from To Do List
    elif choice == 3:
        rmtask = input('Type the name of the task you want to remove: ')
        for row in todoList:
            if row['Tasks'] == rmtask:
                todoList.remove(row)

    # 4 - Save To Do List to file
    elif choice == 4:
        objFile = open('ToDo.txt', 'w')
        for place in todoList:
            objFile.write(place.get('Tasks') + ', ' + place.get('Priority') + '\n')
        objFile.close()

    # 5 - Save To Do List and Exit Program
    elif choice == 5:
        objFile = open('ToDo.txt', 'w')
        for place in todoList:
            objFile.write(place.get('Tasks') + ', ' + place.get('Priority') + '\n')
        objFile.close()
        exit()

    # Handle bad user input
    else:
        print('Incorrect input. Try again.\n')
