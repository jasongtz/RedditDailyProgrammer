


#if len(num) == 10:
#	print "Calculating..."
#else:
#	print "Error! Must be 10 digits."





nums = []
num = (raw_input("> ")).replace("-", "")
def calc():
	x = 10
	y = 0
	while x > 0:
		nums.append(int(num[y]) * x)
		x -= 1
		y += 1
calc()
if sum(nums) % 11 == 0:
	print "Valid ISBN!"
else:
	print "Not valid!"
