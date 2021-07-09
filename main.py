from PIL import Image

img = Image.open('Bubble_Grid.tif')
rgba = img.convert("RGBA")
datas = rgba.getdata()

newData = []

for item in datas:
	if item[0] > 200 and item[1] > 200 and item[2] > 200:  # finding color greater than threshold
		# storing a transparent value when we find a white colour
		newData.append((255, 255, 255, 0))
	else:
		newData.append(item)  # other colours remain unchanged
  
rgba.putdata(newData)
rgba.save("Bubble_Grid.png", "PNG")