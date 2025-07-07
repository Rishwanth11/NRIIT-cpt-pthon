with open('file1.txt','r') as file:
    data=file.read()
    print("ACCESING FOR THE FILE",data)
    print(file.closed)
    file.close()
    print(file.closed)
