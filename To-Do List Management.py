# Function to display the menu options
def display_menu():
    print('Menu:\n1. Add Task\n2. Mark Task as Completed\n3. View To-Do List\n4. Prioritize Task\n5. Remove Completed Tasks\n6. Exit')
    while True:
        try: 
            choice = int(input('Enter your choice (1-6): '))
            break
        except ValueError:
                print('Invalid choice. Please choose again')           
    return choice

# Function to add a new task to the to-do list
def add_task(todo_list):
    new_task = ['False', ' ']
    discription = input('Enter the task: ')
    todo_list[discription] = new_task 
    print('Task added successfully')
    return todo_list

# Function to display the current to-do list
def display_todo_list(todo_list):
    for index, (description, details) in enumerate(todo_list.items(), start=0):
        completion = "Pending" if details[0] == "False" else "Completed"
        priority = (f'Priority: {details[1]}') if details[1] != " " else " "

        print(f'{index}. {description} - {completion} - {priority}')

# Function to mark a task as completed
def mark_completed(todo_list):
    print('To-Do List:')
    (display_todo_list(todo_list))
    while True:
        try: 
            index = int(input('Enter the index of the task to mark as complete: '))
            if 0 <= index < len(todo_list):
                task_description = list(todo_list.keys())[index]
                todo_list[task_description][0] = 'True'
                break
            else:
                print('Invalid index. Try again.')
        except ValueError:
            print('Invalid index. Please enter a valid integer.')
    print(f"Task '{task_description}' marked as completed.")

# Function to prioritize a task
def prioritize_task(todo_list):
    print('To-Do List:')
    display_todo_list(todo_list)
    while True:
        try: 
            index = int(input('Enter the index of the task to prioritize: '))
            if 0 <= index < len(todo_list):
                task_description = list(todo_list.keys())[index]
                priority = input('Enter priority level (high, medium, low): ').capitalize()
                if priority in ['High', 'Medium', 'Low']:
                    todo_list[task_description][1] = priority
                    print('Task prioritized successfully')
                    break
                else:
                    raise ValueError
            else:
                print('Invalid index. Try again.')
        except ValueError:
            print("Invalid priority level. Please enter 'high', 'medium', or 'low'")

# Function to remove completed tasks
def remove_completed_tasks(todo_list):
    tasks_to_remove = [task for task, details in todo_list.items() if details[0] == 'True']
    for task in tasks_to_remove:
        del todo_list[task]
    print("Completed tasks removed successfully")    

# Main function to manage the to-do list
def main():
    todo_list = {}
    task = 0
    while task != 6:
        task = display_menu()
        if task == 1:
            add_task(todo_list)
            print()
        elif task == 2:
            mark_completed(todo_list)
            print()
        elif task == 3:
            display_todo_list(todo_list)
            print()
        elif task == 4:
            prioritize_task(todo_list)
            print()
        elif task == 5:
            remove_completed_tasks(todo_list)
            print()
        else:
            print('Exiting the program. Goodbye!')

    pass
# Call the main function
if __name__ == "__main__":
    main()
