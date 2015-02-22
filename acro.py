

acro = {"lol" : "laugh out loud",
		"dw" : "dont worry",
		"hf" : "have fun",
		"gg" : "good game",
		"brb" : "be right back",
		"g2g" : "got to go",
		"wtf" : "what the F%*$&",
		"wp" : "well played",
		"gl" : "good luck",
		"imo" : "in my opinion"}

x = (raw_input("> ")).lower()
for i, j in acro.iteritems():
	x = x.replace(i, j)
print x