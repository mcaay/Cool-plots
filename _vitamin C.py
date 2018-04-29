import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image
from matplotlib.offsetbox import(OffsetImage, AnnotationBbox)


# values from Cronometer.com
red_pepper = 152
orange = 69.7
broccoli = 58.4
strawberries = 44.7
potatoes = 18.5
tomato = 16.9
banana = 10.3
apple = 8.4
blueberries = 7.2


# make an array with the values and sort it in descending order
values = np.array([red_pepper, tomato, orange, banana, blueberries, strawberries, broccoli, apple, potatoes])
values.sort()
values = values[::-1]

# RDA for adult males is 90 mg
percentages_RDA = values / 90 * 100
# Likely the most optimal daily intake is 200 mg
percentages_200mg = values / 200 * 100

# x-axis labels
x = ['1 medium\nred bell pepper', '1 medium\norange', '1/2 medium\nbroccoli', '1/2 cup\nstrawberries', '0.25 kg / 0.55 lbs\npotatoes', '1 medium\ntomato', '1 medium\nbanana', '1 medium\napple', '1/2 cup\nblueberries']


# need to set figsize (in inches), or otherwise labels are overcrowded
plt.figure(0, figsize=(13, 8))
plt.title('Vitamin C in some common foods', fontsize=20)
plt.ylabel('% RDA (Recommended Daily Allowance)', fontsize=16)
plt.ylim(0, 212)   ################################### ADJUSTABLE
# the red line marking 100% 
plt.axhline(y=100, linewidth=1, color='r', linestyle='--')
scores = plt.bar(x, percentages_RDA, color='#0080dd') ################# ADJUSTABLE

# show percentages above bars
for score in scores:
	height = score.get_height()
	plt.text(score.get_x() + score.get_width()/2, height + 1, '%d%%' % int(round(height)), ha='center', va='bottom')

# add images to the plot
image_names = ['_pepper.png', '_orange.png', '_broccoli.png', \
	'_strawberries.png', '_potatoes.png', '_tomato.png', \
	'_banana.png', '_apple.png', '_blueberries.png']
for i in range(len(scores)):
	# load .png file as an array
	image_as_array = image.imread(image_names[i])

	# set zoom (all pictures are 500x500 px)
	imagebox = OffsetImage(image_as_array, zoom=0.14)
	imagebox.image.axes = plt.axes()

	# place the pictures a bit above the bars
	height = scores[i].get_height()
	height += 25

	# i is the number of the bar starting from the left 
	ab = AnnotationBbox(imagebox, (i, height), xycoords='data', frameon=False)	
	plt.axes().add_artist(ab)

plt.savefig('vitamin C.png', dpi=300)



