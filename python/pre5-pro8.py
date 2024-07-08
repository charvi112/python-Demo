def Length(a):
	max = len(a[0])
	temp = a[0]

	for i in a:
		if(len(i) > max):

			max= len(i)
			temp = i

	print("longest length is:", temp," and length is ", max)
	
a = ["good","morning","hello","somewhere","whatever"]
Length(a)
