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
""" b=float(input("What is your bill?"))
t=input("Was the service ['bad', 'okay', 'good', 'great']?")
if t == "bad":
    y=0
elif t == "okay":
    y=0.15
elif t == "good":
    y=0.20
elif t == "great":
    y=0.25
z=b*y

total=b+z
q=input(f"Tip {z}?")
if q == "yes":
    print(f"Your total is {total}")
else:
    print(f"Your total is {b}") """

#challenge3
""" x=int(input("Enter a positive number "))
factors=[]
for i in range(1, x + 1):
    if x % i == 0:
        factors.append(i)
print(f"The factors of {x} are: {factors}") """

#challenge4
x=int(input("Enter a positive number "))
y=int(input("Enter another positive number "))
larger = max(x,y)
smaller = min(x,y)

z=larger/smaller
print(z)

