with open('file1.txt','w+') as file:
    file.write("HELLO TREVER BHAI ")
    file.seek(0)
    print(file.read())
   