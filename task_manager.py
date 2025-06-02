#=====importing libraries===========
from datetime import date

#====Login Section====

# Function to get the total number of tasks
def get_total_tasks():
    with open('tasks.txt', 'r') as file:
        return len(file.readlines())

# Function to get the total number of users
def get_total_users():
    with open('user.txt', 'r') as file:
        return len(file.readlines())

# Function to display statistics
def show_statistics():
    total_tasks = get_total_tasks()
    total_users = get_total_users()
    print(f"\nTotal number of tasks: {total_tasks}")
    print(f"Total number of users: {total_users}\n")

# Dictionary to store usernames and passwords
usernames = {} 

# Username as the key and password as the values
with open('user.txt', 'r+') as file:
    for line in file:
        username, password = line.strip().split(", ")
        usernames[username] = password

# User input to login using username and password
while True:
    login_username = input("Enter your username: ")
    login_password = input("Enter your password: ")
    
    if login_username in usernames:
        if usernames[login_username] != login_password:
            print("You have entered an invalid password, please try again: ")

# If username and password match, then menu is presented
        elif usernames[login_username] == login_password:
            while True:
                menu = input('''Select one of the following options:
                         r - register a user
                         a - add task
                         va - view all tasks
                         vm - view my tasks
                         s - show statistics (admin only)
                         e - exit
                          : ''').lower()
            
            
# Only 'admin' can register new users            
                if menu == 'r':
                    if login_username == 'admin':
                        new_username = input("Enter username for new user : ")
                        new_password = input("Enter password for new user: ")
                        confirm_new_password = input("Please confirm the password: ")

                        if new_password == confirm_new_password:
                            with open('user.txt', 'a+') as file:
                                file.write("\n" + new_username + ", " + new_password)
                
                        else:
                            print("The passwords do not match. Please ensure the passwords match correctly: ")

                    else:
                        print("You must be logged in as admin to register new users.")

                
                    '''If user selects 'a' to assign task, they are presented
                    with the following user inputs. Datetime library was
                    imported so the assigment date of the task could be put 
                    as whatever the current date is
                    '''
                elif menu == 'a':
                    new_task_user = input("Please enter the username that the task will be assigned to: ")
                    new_task_title = input("Please enter the title of the task: ")
                    new_task_desc = input("Please enter the description of the task: ")
                    new_task_due = input("Please enter the due date for the task: ")
                    new_task_comp = "No"
                    fdate = date.today().strftime('%d %b %Y')

                    with open('tasks.txt', 'a+') as file:
                        file.write("\n" + new_task_user + ", " + new_task_title + ", " + new_task_desc + ", " + fdate + ", " + new_task_due + ", " + new_task_comp)    


                    '''List was used to store tasks in a presentable manner.
                    Each section of the 'tasks.txt' file was split using the
                    (", ) as the delimiter. Using the corresponding index 
                    values, they were then presented in a readable manner.
                    '''
                elif menu == 'va':
                    with open('tasks.txt', 'r+') as file:
                        lines = file.readlines()
                        tasks = []
                        for line in lines:
                            parts = line.strip().split(", ")
                            if len(parts) == 6:
                                tasks.append(parts)
                                for task in tasks:
                                    print(f"Task:               {task[1]}")
                                    print(f"Assigned to:        {task[0]}")
                                    print(f"Date assigned:      {task[3]}")
                                    print(f"Due date:           {task[4]}")
                                    print(f"Task Complete?      {task[5]}")
                                    print(f"Task description:   {task[2]}")
                                    print("\n")

                
                    '''Similar to 'va' however if the [0] index of the
                    'tasks.txt' which should be the user. If this was the
                    same as the initial login username, then it would 
                    present any tasks assigned to the particular user.
                    '''
                elif menu == 'vm':
                    with open('tasks.txt', 'r+') as file:
                        user_tasks = file.readlines()
                        for line in user_tasks:
                            parts_vm = line.strip().split(", ")
                            if parts_vm[0] == login_username:
                                print(f"Task:               {parts_vm[1]}")
                                print(f"Assigned to:        {parts_vm[0]}")
                                print(f"Date assigned:      {parts_vm[3]}")
                                print(f"Due date:           {parts_vm[4]}")
                                print(f"Task Complete?      {parts_vm[5]}")
                                print(f"Task description:   {parts_vm[2]}")
                                print("\n")

                
                # Admin only statistics menu option
                elif menu == 's':  
                    if login_username == 'admin':
                        show_statistics()
                
                    else:
                        print("You must be logged in as admin to view statistics.")

                
                # Exits the menu and ends the programme
                elif menu == 'e':
                    print('Goodbye!!!')
                    exit()

    else:
        print("You have entered an invalid username. Please try again")


'''This was quite a difficult task which I had a lot of trouble with
however with the help of youtube videos and stackoverflow i was 
able to put together a programme to the best of my ability'''