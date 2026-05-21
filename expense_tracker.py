# second project

import os
print("""
---Expense Tracker---

add expenses
total money spent
display all expense      
save to file

""")
add_expense=[]
def load_expense(): 
    try:    
        with open("expenses.txt","r")as f:
            if os.path.getsize("expenses.txt")<1:
                print("nothing to load")
            else:
                for num in f:
                    line=num.strip()
                    if line:
                        conv_int=int(line)
                        add_expense.append(conv_int)
    except FileNotFoundError:
        print("there is no such file")

def add_expenses():
    while True:
        try:
            add_amount=int(input("enter the amount :"))
            add_expense.append(add_amount)
            discription=input("would you like to descibe you expense(enter 'q' if you dont)").lower()
            if discription=="q":
                print("expense is not discribed")
                break
            else:
                print(f"you spent :{add_amount}\t(on {discription})")
                break
            
        except ValueError:
            print('please enter amount ')

def total_money_spent():
    total_expense=sum(add_expense)
    print(f"total expense is = {total_expense}")

def display_expenses():
    for expense in add_expense:
        print(expense)

def save_in_file():
    with open("expenses.txt","w")as f:
        for expense in add_expense:
            f.write(str(expense)+"\n")

def main():
    load_expense()
    while True:
        try:
            choice=int(input('enter the choice :'))
            if choice==1:
                add_expenses()
            elif choice ==2:
                total_money_spent()
            elif choice ==3:
                display_expenses()
            elif choice ==4:
                break
            else:
                print('invalid choice\njust these 1. 2. 3. 4. choices are available')
        except ValueError:
            print("invalid input! please enter a number")
    save_in_file()
main()
    
    