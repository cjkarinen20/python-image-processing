import os
from PIL import Image, ImageEnhance, ImageFilter


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

# Image Exercise 
# cat_rotated = image.rotate(30)
# cat_rotated.save('cat_rotated.png', 'png')

# -- Color Basics --
# images_path = os.path.join(images_dir, 'images', 'red.png')

# image = Image.open(images_path)

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

# Color Exercise 
# print(image.getpizel((0,0)))
# for x in range(image.size[0]):
#     for y in range(image.size[1]):
#         if image.getpixel((x, y))[0] == 0:
#             image.putpixel((x, y), (200, 20, 20))

# -- Image Enhancers --
# images_path = os.path.join(images_dir, 'images', 'cat.jpg')

# image = Image.open(images_path)

# Create an image enhancer
# vibrance_enhancer = ImageEnhance.Color(image)
# contrast_enhancer = ImageEnhance.Contrast(image)
# brightness_enhancer = ImageEnhance.Brightness(image)
# sharpness_enhancer = ImageEnhance.Sharpness(image)

# # Apply the enhancer
# enhanced_image = sharpness_enhancer.enhance(1.5)

# # Display the image
# image.show()
# enhanced_image.show()

# -- Image Filters --
images_path = os.path.join(images_dir, 'images', 'cat.jpg')

image = Image.open(images_path)

# Apply basic image filters
image_blur = image.filter(ImageFilter.BLUR)
image_contour = image.filter(ImageFilter.CONTOUR)
image_emboss = image.filter(ImageFilter.EMBOSS)
image_edge = image.filter(ImageFilter.FIND_EDGES)

# Apply advanced image filters
image_boxblur = image.filter(ImageFilter.BoxBlur(radius = 20))
image_gaussianblur = image.filter(ImageFilter.GuassianBlur(radius = 20))
image_unsharp = image.filter(ImageFilter.UnsharpMask(radius = 20))

image_unsharp.show()
