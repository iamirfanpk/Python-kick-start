Friends = int(input("How many friends do you have? "))
list = []
for x in range(1,Friends+1):
   Name = input(f"Enter name of friend {x} : ")
   list.append(Name)
print()   
print("Your friends list")
print()
print('\n'.join(list))