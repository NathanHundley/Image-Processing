from PIL import Image, ImageFilter

img = Image.open('Pokedex/pikachu.jpg')

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert('L')
crooked_img = filtered_img.rotate(180)
resized_img = crooked_img.resize((300,300))
box = (100, 100, 400, 400)
region = resized_img.crop(box)

filtered_img.save("blur.png", "png")
resized_img.show()
region.show()

img = Image.open('Other_Images/astro.jpg')
img.thumbnail((400,400))
img.show()

