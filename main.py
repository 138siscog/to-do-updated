import json
import sys
import os

todo_list = []

print("What Would You Like to Do? select: 1, 2, 3, or 4 \n")

print("1 - Create New Todo List\n")
print("2 - Edit Existing Todo List\n")
print("3 - Delete Existing todo list\n")
print("4 - Exit\n")

main_option = input(": ")
main_num = int(main_option)


match main_num:
    case 1:
        while True:
            todo = input("Enter a todo: \n")
            todo_list.append(todo)
            new = input("Would you like to add another todo? (Y/N)\n").upper()
            if new != "Y":
                break
            else:
                continue
        for index, todo in enumerate(todo_list, start=1):
            print(f"{index}: {todo}")
            with open("data.json", "w") as f:
                json.dump(todo_list, f, indent=4)
                input("press Enter to exit")
            break
    
    case 2: 
        print(os.path.dirname(os.path.abspath(sys.argv[0])))

    case 3:
        print(os.path.dirname(os.path.abspath(sys.argv[0])))
    
    case 4: 
        exit()
            