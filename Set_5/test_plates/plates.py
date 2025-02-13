def main(): #java is easier to use than this lol
    plate = input("Welcome to the Massachusetts State DMV, valued customer. My name is Archibald Knox III. How may I help you? ");
    if (is_valid(plate)):
        print("Valid");
    else:
        print("Invalid");

def is_valid(plate):
    plate=plate.upper(); plate=plate.strip();
    ranger=len(plate);
    if (ranger<2 or ranger >6): # between 2 and 6 chars, inclusive
        return False;
    first=False;
    for integer in range(ranger): # no spaces or punctuation allowed
        if (plate[integer].isalpha()==False and plate[integer].isdigit()==False): #so if not an int or char, auto fail
            return False;
        if (plate[integer].isdigit()==True and first==False): # first num in plate cannot be 0
            first=True;
            if (integer!=ranger-1 and int(plate[integer])==0): #first number can be 0 if it's also the last number
                return False;
        if ((integer==0 or integer==1) and plate[integer].isalpha()==False): #first two chars must be letters, or fail
            return False;
        elif (1<integer<ranger-1 and plate[integer].isdigit()==True): # no numbers unless they are last or chained to the end
#if there is a number before the last char (i.e. charAt(2)) and the char after it (charAt(3)) also isn't a number, fail
#if charAt(2) is an int, all charAt after it must also be, bc otherwise it's a char, and no int can be between chars
#don't check 0 and 1 since they must be chars, and skip last index bc it's the end and doesn't matter if it's an int or not
            index=integer;
            while (index<ranger):
                if (plate[integer+1].isdigit()==False):
                    return False;
                else:
                    index+=1;
    #else, after passing all the above checks
    return True;

if __name__=="__main__":
    main();
