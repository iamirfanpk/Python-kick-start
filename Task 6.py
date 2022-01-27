data = {}
Number_of_friends = int(input("How many friend do you have? : "))
list_of_friends = ["👇"]
for x in range(1,Number_of_friends+1):
    Name = input(f"Enter the name of friend {x} : ")
    Age = input(f"Enter the age of friend {x} : ")
    Department = input(f"Enter the department of friend {x} : ")
    print()
    data[Name]=[Age,Department]
print()    
print("===============================\n|      Your Friends List      |\n===============================")
print()
for x,y in data.items():
    print(x)
    for m in y:
        print(m)