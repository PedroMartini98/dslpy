import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

av_fonts = figlet.getFonts()

if len(sys.argv) == 1:
   
    random_font = random.choice(av_fonts)
    figlet.setFont(font=random_font)
    
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '-font'):
    isRandomFont = False
    if sys.argv[2] not in av_fonts:
        print('Invalid usage')
        sys.exit()
    else:
        figlet.setFont(font=sys.argv[2])
else:
    print('Invalid usage')
    sys.exit()

msg = input("Input: ")
print(figlet.renderText(msg))



 