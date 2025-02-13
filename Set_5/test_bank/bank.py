def main(gig):
    gig=gig.strip(); gig=gig.lower();
    cash=value(gig);
    if (cash==0):
        print("$0.");
        print("What‽ Gosh darn you to heck, I guess you got me this time. Next time Jim, next time!");
    elif (cash==20):
        print("$20.");
        print("Hey, it's not a hundred, but I'll still take it. Pay up.");
    elif (cash==100):
        print("$100.");
        print("That's how much you owe me now, so pay up, fair and square!");

def value(greeting):
    if (greeting.startswith("hello")):#if ("hello" in greeting):
        return 0;
    elif (greeting.startswith("h")):
        return 20;
    else:
        return 100;

if __name__=="__main__":
    main(input("Alright everyone, this here is a stick-up! Give me all of your money or I'll shoot! "));
