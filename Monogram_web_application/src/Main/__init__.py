
from PIL import Image
from PIL import ImageDraw 
from PIL import *
from PIL import ImageFont
import numpy as np

font_path = "C:\Windows\Fonts\monogram.ttf"
font_size = 1000 #font size defined 
#dimensions of the panel
width = 2000
height = 2000
y = 0 #zero variable used for lists
z = height/2 - (font_size)/2 #used for centering

#used to seperate the string into a 3 char list
def seperate (text):
    if check(text)==1:
        text = text.upper()
        l = list(text)
        list_image(l)
    else:
        print("please enter 3 letters")

#this checks if the string is 3 chars long
def check(text):
    if len(text)==3: 
        return 1
    else:
        return 0
        
#renders and generates the image
def list_image(l):    
    image = Image.new('RGBA',(width,height), (255, 255, 255,0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path,font_size)
    sum = np.divide(np.subtract(width,np.add( np.add(font.getsize(l[0]),font.getsize(l[1])),font.getsize(l[2]))),2)
                              
    #get size of letters in each position
    one = sum
    two = np.add(one,font.getsize(l[0]))
    three = np.add(sum,np.add(font.getsize(l[0]),font.getsize(l[1])))
    two_length = np.multiply(font.getsize(l[1]),.3)
    one_cord = np.add(one,two_length)
    three_cord = np.subtract(three,two_length)

    #draw each letter in picture
    draw.text((one_cord[0], z),l[y], fill=(0,0,0), font=font)
    draw.text((two[0], z), l[y+1], fill=(0,0,0), font=font)
    draw.text((three_cord[0], z),l[y+2], fill=(0,0,0), font=font)
    
    #text_height = font.getsize(l[0])
    draw.ellipse((900,100,1100,300), outline='red', width=10)
    draw.ellipse((0,0,2000,2000), outline='red', width=10)    
    image.show() #used for beguggin purposes
    
    image.save("test.png")

print("enter your initials in the order the you want the monogram to show: ")
monogram = "smp" #input() #set back to input when done with line spacing
seperate(monogram)
#output_image(monogram)