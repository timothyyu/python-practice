#p.64 ex10 what was that

# Escape sequence 	
	# escape double-quotes and single-quotes so python knows to include them in the string
edqis = "I am 6'2\" tall." # escape double-quote inside string

esqis = 'I am 6\'2" tall.' # escape single-quote inside string

print(edqis)
print(esqis)

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)