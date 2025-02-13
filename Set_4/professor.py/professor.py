import random

def main():
    counter=1;
    correct=0;
    level=get_level();
    while (counter<11):
        d1=generate_integer(level); d2=generate_integer(level);
        real=int(d1)+int(d2);
        print(f"Question {counter}/10: ");
        for i in range(3):
            ans=input(str(d1)+" + "+str(d2)+" ="); ans=ans.strip();
            if (ans.isdigit()==True and int(ans)==real):
                correct+=1; break;
            else:
                print("EEE");
                if (i==2): #third and final failure
                    print(str(d1)+" + "+str(d2)+" ="+str(real));
        counter+=1;
    print(str(correct));
    #print("Score: "+str(correct)+"/10"); #good old check50

def get_level():
    while (True):
        level=input("Level: "); level=level.strip();
        if (level=="1" or level=="2" or level=="3"):
            return int(level);

def generate_integer(level):
    if (level==1):
        return random.randint(0, 9);
    elif (level==2):
        return random.randint(10, 99);
    elif (level==3):
        return random.randint(100, 999);
    else:
        raise ValueError("Level must be 1, 2, or 3");

if __name__=="__main__": #main will only run if python game.py is called; ensures this will not trigger if imported
    main();

