def main(gig):
    gig=gig.strip(); gig=gig.lower();
    if ("hello" in gig):
        print("$0.");
        print("What‽ Gosh darn you to heck, I guess you got me this time. Next time Jim, next time!");
    elif (gig.startswith("h")):
        print("$20.");
        print("Hey, it's not a hundred, but I'll still take it. Pay up.");
    else:
        print("$100.");
        print("That's how much you owe me now, so pay up, fair and square!");

#statutory semicolon supremacy statement still stands
#now try responding to this with a hello. Guaranteed $100
main(input("Alright everyone, this here is a stick-up! Give me all of your money or I'll shoot! "));
