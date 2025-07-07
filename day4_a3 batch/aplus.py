with open('file1.txt','a+') as file:
    file.write("HELLO EVER BHAI ")
    file.seek(0)
    print(file.read())
   