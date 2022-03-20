from PIL import Image

im = Image.open('logo_do_Pillow.JPG')
thumbnail = im.resize((320, 300))
thumbnail.save('logo_do_Pillow_resized.jpg')
