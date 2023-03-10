from PIL import Image


def board(num, size):
    num = int(num)
    size = int(size)
    z = 1
    new_color = (0, 0, 0)  
    new_image = Image.new("RGB", (size * num, size * num), new_color)
    pixels = new_image.load()
    for i in range(num):        
        for j in range(num):
            if z == 1:
                z = 0
            else:
                z = 1
            for x in range(size):
                for y in range(size):
                    if z == 0:
                        pixels[x + j * size, y + i * size] = 0, 0, 0
                    if z == 1:
                        pixels[x + j * size, y + i * size] = 255, 255, 255
    new_image.save('res.png')
board(5, 30)