num= int(input("Enter Numerator:"))
deno= int(input("Enter Denominator:"))
try:
    q=num/deno
    print("Quotient:",q)
except ZeroDivisionError:
    print("Denominator cannot be a zero........")
    