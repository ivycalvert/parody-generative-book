from captcha.image import ImageCaptcha
from os import listdir
from os.path import isfile, join
import random
from genTwisters import gimme_a_tongue_twister
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
tongue_twister = gimme_a_tongue_twister()
# DEBUG
# print(tongue_twister) 


# # this function chops arrays up into character sets defined by "char_limit"
# def format_tongue_twister(twister): # take in string and spit out formatted  (the splitting thing)
# 	char_limit = 4
# 	amount_of_things = math.ceil(len(twister) / char_limit)
# 	results = []
# 	temp_string = twister
# 	for i in range(amount_of_things):
# 		result = temp_string[:char_limit]
# 		temp_string = temp_string[char_limit:]
# 		results.append(result)
# 	return results
# print(format_tongue_twister('rterterteryeryeryeryerye4'))

# for twister in tongue_twister: # go through array of tongue twisters and generate captchas
c = 0
for eachone in tongue_twister:
	try:
		if eachone[0] == eachone[len(eachone) - 1]:
			c += 1
		print(eachone)
		for index, item in enumerate(tongue_twister):
			# DEBUG
			# print(index, item)
			i = index 
			for j in range(2):
				font = 'Library/Fonts/' + random.choice(font_types)
				image = ImageCaptcha(fonts=[font], width=(len(item)*20), height=60)
				data = image.generate(item)
				image.write(item, 'CAPTCHAs/out-{}-{}.png'.format(i, j)) # naming scheme: "out-[tongue_twister version]-[CAPTCHA iteration version].png"
	# minor errors still occur when running the script, 
	# to bypass currently, the except instances are included below:
	except OSError:
		print("Oops! Cannot choose from an empty sequence. Skipping...")
	except UnicodeDecodeError:
		print("Oops! Cannot choose from an empty sequence. Skipping...")
	except ValueError:
		print("Oops! Cannot choose from an empty sequence. Skipping...")


# CODE TO ADJUST THE LENGTH OF THE CAPTCHA IMAGES IS BELOW, HOWEVER THERE ARE STILL SOME ERRORS
# THAT OCCUR WHEN USING THIS WITH THE SYSTEM ABOVE

# iterLength = 75
# prev_length = 0
# max_length = iterLength 
# if len(tongue_twister) > max_length:
# 	tongue_twister = tongue_twister[prev_length:max_length] + "\n" + tongue_twister[max_length:len(tongue_twister)]
# 	max_length += iterLength
# 	prev_length += iterLength
# # DEBUG
# # print(len(tongue_twister))

# lines = tongue_twister.split('\n') 
# iterate_length = len(lines);

# # find the extension of the font
# # extension = os.path.splitext(font)[1][1:]
# # print(extension)

# # select a random font from the font library on the computer
# # this ensures the font choice will be valid

# # generate the CAPTCHA image as a png
# # generate a couple versions due to the fonts not always working
# for j in range(2):
# 	# select a random font each time a CAPTCHA is created
# 	font = 'Library/Fonts/' + random.choice(font_types)
# 	for i in range( iterate_length ):
# 		image = ImageCaptcha(fonts=[font], width=(len(lines[i])*20), height=60)
# 		data = image.generate(lines[i])
# 		# create a naming scheme that will iterate through a list so that it can save multiple twisters
# 		image.write(lines[i], 'out-' + str(j) + str(i) + '.png')
# 		# DEBUG
# 		# print(j)



# NOTE:
# some fonts don't work, some are listed here:
# /Library/Fonts/KufiStandardGK.ttc
# /Library/Fonts/STIXSizThreeSymReg.otf
# /Library/Fonts/Mishafi Gold.ttf
# /Library/Fonts/AlBayan.ttc
# /Library/Fonts/STIXIntSmReg.otf
# /Library/Fonts/Wingdings.ttf
# /Library/Fonts/Mshtakan.ttc
# /Library/Fonts/STIXSizThreeSymBol.otf
# /Library/Fonts/Waseem.ttc
# /Library/Fonts/Farah.ttc
# However, these don't throw any error, they simply are presented in the CAPTCHA 
# as squares, so it's difficult to catch these without simply providing a list 
# of predefined fonts for the script to use (which I didn't want as I wanted
# it to have the opporunity to use a wider range of fonts)

# ALSO NOTE: some fonts do throw an "OSError: cannot open resource" error,
# however time constraints just require you to rerun the script when this occurs

