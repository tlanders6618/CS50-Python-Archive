def main():
    total=0;
    print("Your cocaine will be $0.50. Please insert a coin. ");
    while (total<50):
        donkey=str(50-total);
        print("Amount Due: "+donkey+"\n", end=""); #has to be done like this or check50 fails me :)
        store=input(); slot=0;
        if (store.isdigit()==True): #to avoid casting a non int to an int and causing exception
            slot=int(store);
        if (slot==25 or slot==10 or slot==5):
            total+=slot;
        elif (slot==1):
            print("Sorry, we don't accept pennies. They weigh down our pockets too much.");
    #out of loop
    print ("Change Owed: "+str(total-50));
    if (total-50>1):
        print("Oh sorry man, looks like we owe you, but we don't have any change on us.");
        print("Look, come back next week and you can have a discount on your next purchase, promise.");
    else:
        print("Thanks man. We'll see you again next week. We have a new shipment coming in that we think you'll really like.");
        print("It's called Java experience, and it'll make you leave semicolons everywhere, but it's real strong stuff.");
main();
