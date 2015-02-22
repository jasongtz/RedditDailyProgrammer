#Word Game

from sys import argv
name, left, right = argv

list_left = list(left)
list_right = list(right)
for x in list_left:
	if x in list_right:
		list_left.remove(x)
		list_right.remove(x)
	else:
		pass
		
if len(list_left) > len(list_right):
	print "Left wins!"
elif len(list_left) < len(list_right):
	print "Right wins!"
else:
	print "It's a tie!"