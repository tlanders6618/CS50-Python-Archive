def main():
    list=[];
    while (True):
        try:
            name=input("Name: ");
        except EOFError:
            printnames(list); break;
        else:
            list.append(name);

def printnames(list):
    long=len(list);
    if (long>2): #3+
        print("\nAdieu, adieu, to ", end="");
        for index in range(long):
            if (index==0):
                print(list[index], end="");
            elif (index==(long-1) ): #the last name
                print(", and "+list[index]);
            elif (index>0):
                print(", "+list[index], end="");
    elif (long>1): #2
        print("Adieu, adieu, to "+list[0]+" and "+list[1]);
    elif (long>0): #1, else nothing to print
        print("Adieu, adieu, to "+list[0]);

if __name__=="__main__":
    main();
