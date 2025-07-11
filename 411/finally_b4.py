try:
    print("Raising Exception.....")
    raise ValueError
except:
    print("Exception caught..")
finally:
    print("Performing cleanup.......")