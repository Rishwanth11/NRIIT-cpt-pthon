try:
    n=10
    print(n**2)
    raise ValueError
except:
    print("Exception Occured...")
