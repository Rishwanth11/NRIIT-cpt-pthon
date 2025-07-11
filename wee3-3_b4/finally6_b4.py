n=0
while True:
    try:
        n=n+1
        if n==31:
            raise StopIteration
    except StopIteration:
        break
    else:
        print(n, end="-")