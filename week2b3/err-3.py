try:
    raise Exception('Rishi','ECE')
except Exception as errorObj:
    print(type(errorObj))
    print(errorObj.args)
    arg1,arg2=errorObj.args
    print("2nd Argument",arg2)
    print("1nd Argument",arg1)
