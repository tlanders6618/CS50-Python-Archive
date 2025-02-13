def main():
    #print("Hey, this is your Dasher. I'm here at the store already, so just let me know what you want and I'll go get it. ");
    list=[];
    while (True):
        try:
            string=input();
            string=string.upper(); string=string.strip();
            list.append(string);
            list.sort();
        except EOFError:
            printlist(list);
            break;

def printlist(list):
    #print("Alright, let me read that back to you to make sure I have everything right.");
    done=[];
    for item in list:
        num=0; #start at 0 bc nested loop below counts the first item when checking for duplicates
        if (item not in done): #Java is easier to write in; this is the second time I've wasted half an hour on nothing
            for item2 in list: #my code was literally correct the whole time, but the syntax in Python is whack
                if (item2==item): #I only fixed it because the ai duck saved me; (item in done==False)!=(item not in done)
                    num+=1; #I don't know why I'm writing this; call it venting I guess, plus praise the robot duck
            print(str(num)+" "+item);
            done.append(item);
    #print("Okay, I'm on my way with your order, ETA 25 mins. I hope there's a nice tip waiting for me there :)");

main();
