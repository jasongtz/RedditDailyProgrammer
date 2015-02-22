#Bank Numbers

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

nums = {"0" : [" _ ", "| |", "|_|"]
        , "1" :["   ", "  |", "  |"]
        , "2" : [" _ ", " _|", "|_ "]
        , "3" : [" _ ", " _|", " _|"]
        , "4" : ["   ", "|_|", "  |"]
        , "5" : [" _ ", "|_ ", " _|"]
        , "6" : [" _ ", "|_ ", "|_|"]
        , "7" : [" _ ", "  |", "  |"]
        , "8" : [" _ ", "|_|", "|_|"]
        , "9" : [" _ ", "|_|", " _|"]
        }

text_list = []

#Someday, try and redo with list comprehension.
def calc(line):
	listx = list(line)
	for x in range(3):
		for y in listx:
			var = nums[y]
			text_list.append(var[x])
		text_list.append("\n")

calc(line1)
calc(line2)
calc(line3)

for item in text_list:
	print item,
	
