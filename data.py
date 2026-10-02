#x=input()
#y=x.split()
#print(total_words)

""" x=input()
y=x.split()
total_words=len(y)
print(total_words) """


#tipcalculator
""" b=input("What is your bill?")
x=float(b)
t=input("How much do you want to tip?")
y=int(t)
z=(x+y)
print(f"Your total bill is {z}") """


#challenge1
""" def odd_or_even(number):
	if number % 2 == 0:
		return "even"
	return "odd"


number = int(input("Enter a number: "))
print(odd_or_even(number)) """


#challenge2
""" b=input("What is your bill?")
x=float(b)
t=input("Was the service ['bad', 'okay', 'good', or 'great']?")
if t[1]:
    print(x*1.15)
elif t[2]:
    print(x*1.20)
elif t[3]:
    print(x*1.25) """

	
b = float(input("What is your bill? "))
service = input("Was the service ['bad', 'okay', 'good', or 'great']? ").lower().strip()

if service == "bad":
    total = b * 1
elif service == "okay":
    total = b * 1.15
elif service == "good":
    total = b * 1.20
elif service == "great":
    total = b * 1.25

print(f"Your total bill is {total}")