import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'logo.png'

logoIm = Image.open( LOGO_FILENAME )
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True) #Loop over all files in the working directory

for filename in os.listdir ('originals'):
    
    if not (filename.endswith ('.png') or filename.endswith ('.jpg'))or filename == LOGO_FILENAME:
        continue

    im = Image.open(os.path.join ('originals', filename))
    width, height = im.size

    
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE: #Check if file image needs to be

        
        if width > height: #Calculate the new width and height to resize to
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE


        print('Resizing %s...' % (filename)) #Add the logo
        im = im.resize((width, height))


    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)



    im.save(os.path.join('withLogo', filename))  #Save changes
