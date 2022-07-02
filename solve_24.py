# YOUR CODE HERE
numbers=input("Enter 4 integers: ")
numbers=numbers.split(" ")
judge=False
print()
if len(numbers) !=4:
	print("Input must consist of 4 integers")
	exit()
try:
	for a in numbers:
		test=int(a)
except ValueError:
	print("Input must consist of 4 integers")
	exit()
i=0
def cal(x,y):
	calcuate=[]
	try:
		x=float(x)
		y=float(y)
		calcuate.append(x+y)
		calcuate.append(x*y)
		try:
			calcuate.append(x/y)
			calcuate.append(y/x)
		except ZeroDivisionError:
			calcuate.append(None)
		calcuate.append(x-y)
		calcuate.append(y-x)
	except TypeError:
		return []
	return calcuate

for num1,i in enumerate(numbers):
	for num2,s in enumerate(numbers):
		if num2 !=num1:
			calcuate1=cal(i,s)
			for num3,a in enumerate(numbers):
				if num3 !=num1 and num3 !=num2:
					for b in calcuate1:
						calcuate2=cal(a,b)
						for num4,c in enumerate(numbers):
							if num4 !=num1 and num4 !=num2 and num4 !=num3:
								for d in calcuate2:
									calcuate3=cal(c,d)
									for e in calcuate3:
										if e !=None:
											if abs(e-24)<0.0000000000001:
												judge=True
												break
numbers=", ".join(numbers)
if judge==False:
	print("Noooo :( 24 is unreachable from {{ {} }}".format(numbers))
if judge==True:
	print("Yes! 24 is reachable from {{ {} }}".format(numbers))
