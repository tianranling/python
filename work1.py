Max = 0
Min = 0
while True:
	a = input("please input a number:")
	if  a == 'done':
		break
	try:
		a = float(a)
	except:
		print(" %s is not a number"% a)
		continue
	if Max is 0 or Max < a:
		max = a
	if Min is 0 or Min > a:
		min = a
print(Max,Min)
input( )