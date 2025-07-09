try:
    num= int(input("Enter Numerator:"))
    print(num**3)
except KeyboardInterrupt:
    print("You Should Have Enter Data Without Interrupting the Compiler........")
except ValueError:
    print("Enter number only..............................")
print("Program Terminated ")
print("Bye")