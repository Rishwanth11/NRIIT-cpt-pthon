try:
    print("Divided two Strings...")
    try:
        quo= "abc"/"def"
        print(quo)
    finally:
        print("This is the finally block-------")
except TypeError:
    print("Here the type error is handled......")