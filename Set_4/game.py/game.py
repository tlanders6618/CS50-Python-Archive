import random;
#import javaskills;
def main():
    while (True):
        end=input("Level: "); end=end.strip();
        if (end.isdigit()==True and int(end)>0):
            end=int(end); break;
    #outside loop
    secret=random.randint(1, end); counter=0;
    while (True):
        guess=input("Guess: "); counter+=1;
        if (guess.isdigit()==True):
            guess=int(guess);
            if (guess>secret):
                print("Too large!");
            elif (guess<secret):
                print("Too small!");
            else:
                print("Just right! You took "+str(counter)+" tries."); break;

if __name__=="__main__": #main will only run if python game.py is called; ensures this will not trigger if imported
    main();
