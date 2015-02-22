#Hangman

import sys
from sys import argv

name, answer = argv
words = answer.lower().replace(".", "").replace("'", "").split()
print ""


# Generates the list of all unique letters
list_letters = []
for x in range(0, len(words)):
	z = 0
	word_in_letters = list(words[x])
	while z < len(word_in_letters):
		if word_in_letters[z] in list_letters:
			z += 1
		else:
			list_letters.append(word_in_letters[z])
			z += 1

hang_count = 10
#Interact with user, while there are still unguessed letters
while len(list_letters) > 0:
	if hang_count < 1:
		print "You lose!"
		sys.exit(1)
	
	# Prints the line, where _ indicates an unguessed letter
	h = 0
	for i in range(0, len(words)):		
		this_word = words[h]
		g = 0
		while g < len(this_word):
			if this_word[g] in list_letters:
				print "_",
			else:
				print this_word[g],
			g += 1
		h += 1
		print " ",
	
	#User input - checks if the letter is still in the "available" list
	print ""
	
	usr = raw_input("> ")
	if usr in list_letters:
		print "OK, %s." % usr
		list_letters.remove(usr)
	elif len(usr) > 1:
		print "Only one letter at a time, please!"
	else:
		hang_count -= 1
		print "Wrong! Only %d more chances!" % hang_count

print "Congratulations, you win!"	
		
		



"""
Takes phrase, splits into words, then into letters. Adds all letters to a list.
Checks if a letter is in the list. If yes, remove. If no, error.

NEXT:
print phrase with missing letters as _
"""


#Attempted to split words into letters using classes - didnt work, used a list instead

#class Letters(object):
#	instances = []
#	all_letters = []
#	def __init__(self, word):
#		self.word = word
#		self.instances.append(self)
#	def printing(self):
#		print self.word
#	def split(self):
#		self.wordsplit = list(self.word)
#		return self.wordsplit
#		all_letters.append(self.wordsplit.items())
#		
#objs = list()
#for i in range(3):
#	objs.append(Letters(words[i]))
#word1 = Letters(words[0])
#word2 = Letters(words[1])
#word3 = Letters(words[2])
#word1.printing()



# for loop to create objs

#objs = list()
#for x in range(0, len(words)):
#	objs.append(Letters(words[x]))

#print objs


###
#def letters():
#	for x in range(0, len(words)):
#		letter.append = list(words[x])
#letters()
#print letter