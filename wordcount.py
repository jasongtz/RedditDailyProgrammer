

data = {}
x = 0

def count(cur_word, num):
	data[cur_word] = num + 1

op = open(raw_input("Filename: "), "r")
raw_data = op.read().lower().replace(".", "").replace("'", "").split()
	
while x < len(raw_data):
	word = raw_data[x]
	if word in data:
		count(word, data[word])
	else:
		data[word] = 1
	x += 1
op.close()
quantity = int(raw_input("Show __ items: ")) 
final = sorted([(a, b) for (b, a) in data.items()], reverse = True)
for i in range(0, quantity):
	print final[i]