try:
    file= open('file1.txt')
    str=file.readline()
    print(str)
except IOError:
    print("Error Occured due to input")
except ValueError:
    print("Could not convert into Integer")
except:
    print("Something is wrong")