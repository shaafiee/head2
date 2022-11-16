from PIL import Image, ImageDraw, ImageFilter
import random
import json
import sys
import os

path = "nft"
if not os.path.exists(path):
	os.makedirs(path)
path = "meta"
if not os.path.exists(path):
	os.makedirs(path)

mypath = './'

background = {0:"None", 1:"Gold", 2:"Mars", 3:"Green", 4:"Azure", 5:"Magenta", 6:"Sky", 7:"Sandy", 8:"Lavender", 9:"Olive", 10:"Grey", 11:"Blue warp", 12:"Copper warp", 13:"Turquoise warp", 14:"Ion storm", 15:"Candy cloud"}

backgroundPct = {0:0, 1:10, 2:10, 3:10, 4:10, 5:10, 6:10, 7:10, 8:10, 9:10, 10:10, 11:10, 12:10, 13:10, 14:3, 15:3}



body = {0:"None", 1:"Nosferatu", 2:"That skin", 3:"Some skin", 4:"A skin", 5:"This skin", 6:"Traveller"}

bodyPct = {0:0, 1:10, 2:30, 3:30, 4:30, 5:30, 6:5}




eyes = {0:"None", 1:"Cyclops", 2:"Morning", 3:"Attentive", 4:"Droopy", 5:"Bloodshot", 6:"Furrowed", 7:"Googly", 8:"Starry", 9:"Pirate"}

eyesPct = {0:0, 1:5, 2:10, 3:30, 4:30, 5:20, 6:20, 7:30, 8:5, 9:10}




mouth = {0:"None", 1:"Pouty", 2:"Surprised", 3:"Unamused", 4:"Amused", 5:"Laughing", 6:"Beaming", 7:"Disgusted", 8:"Sharky", 9:"Stogy", 10:"Cheeky", 11:"Kiss", 12:"Pipe", 13:"Bubble gum", 14:"Singing", 15:"Smiling", 16:"Happy", 17:"Chagrined", 18:"Blabbering", 19:"Upset", 20:"Proud", 21:"Haughty"}

mouthPct = {0:0, 1:5, 2:10, 3:10, 4:10, 5:30, 6:30, 7:10, 8:10, 9:5, 10:5, 11:3, 12:3, 13:5, 14:20, 15:20, 16:30, 17:10, 18:20, 19:20, 20:20, 21:20}




piercings = {0:"None", 1:"Double helix", 2:"Helix", 3:"Pendants", 4:"Multiple", 5:"Rings"}

piercingsPct = {0:0, 1:3, 2:3, 3:1, 4:3, 5:3}




hairstyles = {0:"None", 1:"ET", 2:"Transylvanian", 3:"Supe", 4:"Normal", 5:"Rockstar", 6:"Beach", 7:"Fun", 8:"Green mop", 9:"Sandy mop", 10:"Fro", 11:"Purple spikes", 12:"Turquoise spikes", 13:"Slick blue", 14:"Slick red", 15:"Maybe punk", 16:"Perhaps punk"}

hairstylesPct = {0:0, 1:2, 2:5, 3:5, 4:30, 5:20, 6:20, 7:40, 8:20, 9:20, 10:20, 11:20, 12:20, 13:20, 14:20, 15:20, 16:20}




bling = {0:"None", 1:"Dog tag", 2:"Ring", 3:"Diamond", 4:"Crystal", 5:"Phial", 6:"Choker", 7:"Charm", 8:"Gold", 9:"Goth"}

blingPct = {0:0, 1:3, 2:5, 3:10, 4:10, 5:5, 6:10, 7:5, 8:3, 9:5}




glasses = {0:"None", 1:"Banray", 2:"Jetson", 3:"Hippie", 4:"Rocketman", 5:"Laser", 6:"Thug life", 7:"AR"}

glassesPct = {0:0, 1:7, 2:3, 3:5, 4:7, 5:3, 6:7, 7:7}




headwear = {0:"None", 1:"Halo", 2:"Beret", 3:"Cap", 4:"Viking", 5:"Crown", 6:"Mask", 7:"Fluffy"}

headwearPct = {0:0, 1:3, 2:4, 3:5, 4:3, 5:5, 6:3, 7:3}




for i in range(1, 11) :

	headwearSel = 0
	glassesSel = 0
	blingSel = 0
	hairstylesSel = 7
	piercingsSel = 0
	mouthSel = 6
	eyesSel = 3
	bodySel = 5
	backgroundSel = 4

	image = ''
	metadata = {"name":"Headz " + str(i), "description":"Putting our Headz together for a better metaverse", "image":"_url_", "attributes": list()}

	for key in background:
		r = random.randint(1,100)
		if r <= backgroundPct[key]:
			backgroundSel = key
			break;
	metadata["attributes"].append({"trait_type":"background", "value":background[backgroundSel]})

	for key in body:
		r = random.randint(1,100)
		if r <= bodyPct[key]:
			bodySel = key
			break;
	metadata["attributes"].append({"trait_type":"body", "value":body[bodySel]})

	for key in eyes:
		r = random.randint(1,100)
		if r <= eyesPct[key]:
			eyesSel = key
			break;
	metadata["attributes"].append({"trait_type":"eyes", "value":eyes[eyesSel]})

	for key in mouth:
		r = random.randint(1,100)
		if r <= mouthPct[key]:
			mouthSel = key
			break;
	metadata["attributes"].append({"trait_type":"mouth", "value":mouth[mouthSel]})

	for key in piercings:
		r = random.randint(1,100)
		if r <= piercingsPct[key]:
			piercingsSel = key
			break;
	metadata["attributes"].append({"trait_type":"piercings", "value":piercings[piercingsSel]})

	for key in hairstyles:
		r = random.randint(1,100)
		if r <= hairstylesPct[key]:
			hairstylesSel = key
			break;
	metadata["attributes"].append({"trait_type":"hairstyles", "value":hairstyles[hairstylesSel]})

	for key in bling:
		r = random.randint(1,100)
		if r <= blingPct[key]:
			blingSel = key
			break;
	metadata["attributes"].append({"trait_type":"bling", "value":bling[blingSel]})

	for key in glasses:
		r = random.randint(1,100)
		if r <= glassesPct[key]:
			glassesSel = key
			break;
	metadata["attributes"].append({"trait_type":"glasses", "value":glasses[glassesSel]})

	for key in headwear:
		r = random.randint(1,100)
		if r <= headwearPct[key]:
			headwearSel = key
			break;
	metadata["attributes"].append({"trait_type":"headwear", "value":headwear[headwearSel]})



	img1 = Image.open(mypath + '1. background/Solana_heads_-' + str(backgroundSel) + '.png')

	img2 = Image.open(mypath + '2. Body/Solana_heads_-' + str(bodySel) + '.png')
	img1.paste(img2, (0, 0), img2)

	img2 = Image.open(mypath + '3. Eyes/Solana_heads_-' + str(eyesSel) + '.png')
	img1.paste(img2, (0, 0), img2)

	img2 = Image.open(mypath + '4. Mouth/Solana_heads_-' + str(mouthSel) + '.png')
	img1.paste(img2, (0, 0), img2)

	if piercingsSel > 0:
		img2 = Image.open(mypath + '5. Piercings/Solana_heads_-' + str(piercingsSel) + '.png')
		img1.paste(img2, (0, 0), img2)

	img2 = Image.open(mypath + '6. Hairstyles/Solana_heads_-' + str(hairstylesSel) + '.png')
	img1.paste(img2, (0, 0), img2)

	if blingSel > 0:
		img2 = Image.open(mypath + '7. Bling/Solana_heads_-' + str(blingSel) + '.png')
		img1.paste(img2, (0, 0), img2)

	if glassesSel > 0:
		img2 = Image.open(mypath + '8. Glasses/Solana_heads_-' + str(glassesSel) + '.png')
		img1.paste(img2, (0, 0), img2)

	if headwearSel > 0:
		img2 = Image.open(mypath + '9. Headwear/Solana_heads_-' + str(headwearSel) + '.png')
		img1.paste(img2, (0, 0), img2)


	#f = open("/mnt/node/hdz/meta/" + str(i), "w")
	f = open("./meta/" + str(i), "w")
	f.write(json.dumps(metadata))
	f.close()

	#img1.save("/mnt/node/hdz/images/" + str(i) + ".png", format="png")
	img1.save("./nft/" + str(i) + ".png", format="png")



