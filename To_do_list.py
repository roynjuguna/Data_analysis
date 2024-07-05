user_input = "random"
data = []



while user_input != "4":

    user_input = input('''Menu:
1. Add task
2. Mark task as done and remove from list
3. View all items in the list
4. Exit the to do list
Please Enter an option 1 through 4: ''')

    if user_input == "1":
        task = input("Please type the task to be added: ")
        data.append(task)

    elif user_input == "2":
        task = input("Please input the finished task: ")
        if task in data:
            data.remove(task)
            print(f"The {task} action is done")
        
    elif user_input == "3":
        print("The following are all the items: ")
        for current_items in data:
            print(current_items)

    elif user_input == "4":
        print("You have exited the programme")

    else:
        print("Enter a number from 1 through 4")

print(data)
    
    



