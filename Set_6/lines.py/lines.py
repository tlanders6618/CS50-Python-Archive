import sys;

def main():
    if (len(sys.argv)>2):
        sys.exit("Only one file at a time please. ^_^");
    elif (len(sys.argv)<2):
        sys.exit("You need to input a file for the program to work. >_<");
    elif (sys.argv[1][(len(sys.argv[1])-3):]!=".py"):
        sys.exit("That doesn't look like a Python file. '_'");
    try:
        with open(sys.argv[1], "r") as file:
            lines=0;
            for line in file:
                if (not line.strip().startswith("#") and len(line.strip())>0):
                    lines+=1;
    except FileNotFoundError:
        sys.exit("Gosh, seems like you provided an invalid file. -_-");
    else:
        #print("Your file had "+str(lines)+" lines of code in it. O_O");
        print(lines);

if __name__=="__main__":
    main();
