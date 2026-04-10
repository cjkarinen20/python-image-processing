import os
from PIL import Image


# Get the path of the images directory
images_dir = os.path.dirname(__file__)


# -- Image Basics -- 

# # Join other path with the relative path to the image
# images_path = os.path.join(images_dir, 'images', 'blue.png')

# # Create an image via import
# image = Image.open(images_path)

# # Analyze the image
# print(image.size)
# print(image.filename)
# print(image.format)


# # Flip the image
# image = image.transpose(Image.Transpose.ROTATE_90)

# # Show the image
# image.show()

# # Exercise 
# cat_rotated = image.rotate(30)
# cat_rotated.save('cat_rotated.png', 'png')

# -- Color Basics --
images_path = os.path.join(images_dir, 'images', 'red.png')

image = Image.open(images_path)

# # Get one pixel
# print(image.getpixel((0,0)))

# # Greyscale images
# red_greyscale_image = image.getchannel('R')
# blue_greyscale_image = image.getchannel('B')

# red_greyscale_image.show()
# blue_greyscale_image.show()

# # Change pixel color
# image.putpixel((0, 0), (255, 0, 0))
# image.show()

# Exercise 
print(image.getpizel((0,0)))
for x in range(image.size[0]):
    for y in range(image.size[1]):
        if image.getpixel((x, y))[0] == 0:
            image.putpixel((x, y), (200, 20, 20))
image.show()