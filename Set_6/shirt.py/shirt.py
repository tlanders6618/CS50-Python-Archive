import sys;
import os;
from PIL import Image, ImageOps;

def main():
    file1, file2=checkvalid();
    makeimg(file1, file2);

def checkvalid():
    size=len(sys.argv);
    if (size>3):
        sys.exit("Quack! Too much for me to handle. Please try again with a shorter message.");
    elif (size<3):
        sys.exit("It seems like your message is incomplete. Please provide more details.");
    #else
    file1=sys.argv[1]; file2=sys.argv[2];
    name1, ext1=os.path.splitext(file1);
    name2, ext2=os.path.splitext(file2);
    if ( (ext1.lower()==".jpeg" or ext1.lower()==".jpg" or ext1.lower()==".png") and
        (ext2.lower()==".jpeg" or ext2.lower()==".jpg" or ext2.lower()==".png") ):
        if (ext2==ext1):
            return file1, file2;
        else:
            sys.exit("Input and output have different extensions. Try harder!");
    else:
        sys.exit("Invalid input. Those 'files' aren't good enough. Try harder!");

def makeimg(file1, file2):
    try: #do not need to open file2/output because it isn't supposed to exist; doing .save below creates it
        input=Image.open(file1);
        shirt=Image.open("shirt.png");
    except FileNotFoundError:
        sys.exit("File not found. This wouldn't happen with Java.");
    else:
        shirtsize=shirt.size;
        input=ImageOps.fit(input, shirtsize); #input img made same size as shirt img
        input.paste(shirt, shirt); #paste shirt over input
        input.save(file2); #save img to output file; must be file2 (the file name), not input (an image object)

if __name__=="__main__":
    main();
