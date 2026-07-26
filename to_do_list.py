# First ever project 
# project name= 'TO DO LIST'

import os

print("""
-----TO DO LIST-----

1. add task
2. view task
3. edit task
4. delete task
5. exit
""")

tasks = []
def loading_file():
    try:    
        with open("my_to_do_list.txt","r")as file:
            
            if os.path.getsize("my_to_do_list.txt")<1:
                print("nothing to load yet")
            else:
                for i in file: 
                    line=i.strip()
                    tasks.append(line)
    except FileNotFoundError:
        print("there is no file")
             
def add_task():
    
    new_task =input('enter the task to add :').lower().strip()  # use strip to avoid empty input or input with spaces
    while new_task.isdigit():
        print('enter valid task not number') 
        new_task=input('enter a valid task to add').lower()
    tasks.append(new_task)
    return tasks

def saved_file():
    with open('my_to_do_list.txt', 'w') as f:
        # i ran a loop here because python is saying write() parameter shoud be str not list !
        for tsk in tasks:   
           f.write(tsk+"\n")

def view_task():
    if not tasks:
        print('no task han been added yet')
    else:
        print('--here are your tasks to do :')
        for index, tsk  in  enumerate(tasks,start=1):
            print(f"{index}. {tsk}")
def edit_task():
  while True:
    if not tasks :
            print('nothing in list yet')
            break
    try:
        edit =int(input('enter the index of task you want to edit '))-1
    except ValueError:
        print('please enter the index of the task, nothing else')
        continue
    
    if edit <0 or edit >=len(tasks):
        print('please enter a valid number')
        continue
    
    edited=input('edit it as you want ')
    tasks[edit]=edited
    print("--- tasks are seccecfully edited")
    break

def delete_task():
    add_del_task=input('enter the task you want to remove :').lower()

    if add_del_task.isdigit():
        del_in_int=int(add_del_task) -1
        if not tasks:
            print('list is empty')
        elif del_in_int >= 0 and del_in_int < len(tasks):
            tasks.pop(del_in_int)
        else:
            print('this index in not found')
    else: 
        if not tasks:
            print('list is empty')
        elif add_del_task in tasks:
            tasks.remove(add_del_task)
        else:
            print('task is not found')


def main():
    loading_file()
    while True:
     try:
        choice=int(input('enter the choice :'))
        if choice==1:
            add_task()  
        elif choice ==2:
            view_task()
        elif choice ==3:
            edit_task()
        elif choice ==4:
            delete_task()
        elif choice ==5:
            break 
        else:
            print('invalid choice\njust these 1. 2. 3. 4. 5. choices are available')
     except ValueError:
         print("please enter a valid choice")
         continue
         
     saved_file()    
    
main()
