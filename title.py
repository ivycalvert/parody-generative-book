from captcha.image import ImageCaptcha
from os import listdir
from os.path import isfile, join
import random
import os.path
import sys
import math
# create a list of the fonts installed on the computer to be used later
font_types = [f for f in listdir('/Library/Fonts/') if isfile(join('/Library/Fonts/', f))]
font_types = font_types[1:len(font_types)]

# print a list of all the fonts installed
# DEBUG
# print(listdir('/Library/Fonts/'))

# create a variable with the tongue twister in so it can be used later
# this allows for an easier change in the tongue twister later
# tongue_twister = 'Can crazy concerned carpenters carry caterpillars?'
title = ["careful poetry", "tiring sentences", "word challenges"]

c = 0
for eachone in title:
	try:
		if eachone[0] == eachone[len(eachone) - 1]:
			c += 1
		print(eachone)
		for index, item in enumerate(title):
			# DEBUG
			# print(index, item)
			i = index 
			for j in range(2):
				font = 'Library/Fonts/' + random.choice(font_types)
				image = ImageCaptcha(fonts=[font], width=(len(item)*20), height=60)
				data = image.generate(item)
				image.write(item, 'title/out-{}-{}.png'.format(i, j)) # naming scheme: "out-[tongue_twister version]-[CAPTCHA iteration version].png"
	# minor errors still occur when running the script, 
	# to bypass currently, the except instances are included below:
	except OSError:
		print("Oops! Cannot choose from an empty sequence. Skipping...")
	except UnicodeDecodeError:
		print("Oops! Cannot choose from an empty sequence. Skipping...")
	except ValueError:
		print("Oops! Cannot choose from an empty sequence. Skipping...")
