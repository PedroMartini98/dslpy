import sys
from os.path import splitext
from PIL import Image, ImageOps

#TERMINAR DE FAZER PROBLEMA 6
def main():
    check_clia()
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    
    shirtfile = Image.open("shirt.png")

    size = shirtfile.size 

    output = ImageOps.fit(imagefile,size)

    output.paste(shirtfile,shirtfile)

    output.save(sys.argv[2])

def check_clia():
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit()
    elif len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit()

    root1,ext1=splitext(sys.argv[1])
    root2,ext2=splitext(sys.argv[2])
    
    if check_extension(ext1) == False:
        sys.exit('Invalid input')
    if check_extension(ext2) == False:
        sys.exit('Invalid output')
    if ext1.lower() != ext2.lower():
        sys.exit("input and output have diferent extensions")
def check_extension(file):
    if file in [".jpg",".jpeg",".png"]:
        return True
    else:
        return False

if __name__ == "__main__":
    main()