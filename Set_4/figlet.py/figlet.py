from pyfiglet import Figlet;
import sys;
import random;

def main():
    f = Figlet();
    list=f.getFonts();
    if (len(sys.argv)==1): #random font
        num=random.randint(0, len(list));
        f.setFont(font=list[num]);
        word=input("Choose a word(s): ");
        print(f.renderText(word))
    elif (len(sys.argv)==3): #chosen font
        if (sys.argv[1]=="-f" or sys.argv[1]=="-font"):
            if (sys.argv[2] in list):
                f.setFont(font=sys.argv[2]);
                word=input("Choose a word(s): ");
                print(f.renderText(word));
            else:
                print("Invalid font.");
        else:
            sys.exit("Invalid command.");
    elif (len(sys.argv)>3):
        sys.exit("Too many commands.");
    elif (len(sys.argv)==2):
            sys.exit("Invalid command.");

if __name__=="__main__": #main will only run if python game.py is called; ensures this will not trigger if imported
    main();
