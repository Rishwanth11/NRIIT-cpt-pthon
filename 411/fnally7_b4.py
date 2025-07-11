try:
    size= int(input("Enter size:"))
    user_list=[]
    for i in range(size):
        val=int(input(f"Enter Element {i+1}:"))
        user_list.append(val)
    print(user_list)
    index=int(input("Enter Index to access element"))
    print("Element at the index :",index,"is",user_list[index])
except ValueError:
    print("Error :Please Enter Only Integers")
except IndexError:
    print("Error : index .....Out of range")