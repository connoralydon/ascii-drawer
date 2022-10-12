# ascii-script.py

import sys
import PIL.Image
import PIL.ImageOps

# for black density conversion
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

# resizing image to a new width
def resize_image(image: PIL.Image, new_width):
    width, height = image.size
    ratio = height / width / 1.65# height to width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image
    

# convert each pixel to grayscale
def grayify(image: PIL.Image, invert = 0):
    grayscale_image = image.convert("L")
    if invert: grayscale_image = PIL.ImageOps.invert(grayscale_image)
    return grayscale_image

# convert pixels to a string of ASCII characters
def pixels_to_ascii(image: PIL.Image):
    pixels = image.getdata() # list of each pixel grayscale value
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters

def main(argv):
    
    path = argv[1]
    
    
    
    try:
        invert = int(argv[2])
    except:
        invert = 0
    
    try:
        new_width = int(argv[3])
    except:
        new_width = 100 
    
    
    # open image from user input
    # path = input("Enter pathname to an image: \n")
    
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not a valid pathname to an image.")
        
    new_image_data = pixels_to_ascii(grayify(resize_image(image, new_width = new_width), invert=invert))
    
    # format
    pixel_count = len(new_image_data)
    ascii_image = '\n'.join(new_image_data[i:(i+new_width)] for i in range(0,pixel_count,new_width)) 
    # from 0 -> pixel_len with jumps of new_width
    
    # print result
    print(ascii_image)
    
    # save result to "ascii_image.txt"
    save_name = path.split(".")[0] + ".txt"
    with open(save_name,'w') as f:
        f.write(ascii_image)

if __name__ == "__main__":
    main(sys.argv)