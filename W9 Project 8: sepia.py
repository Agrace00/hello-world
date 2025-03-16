from PIL import Image

def sepia(image):
  
    grayscale_image = image.convert('L')

    for y in range(image.height):
        for x in range(image.width):
            (r, g, b) = image.getpixel((x, y))

            new_r = min(255, int(0.393 * r + 0.769 * g + 0.189 * b))
            new_g = min(255, int(0.349 * r + 0.686 * g + 0.168 * b))
            new_b = min(255, int(0.272 * r + 0.534 * g + 0.131 * b))

            image.putpixel((x, y), (new_r, new_g, new_b))

    return image  

input_image = Image.open(r'smokey.gif') 

input_image.show()                  
