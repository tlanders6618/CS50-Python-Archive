def main(word):
    word=cameltosnake(word);
    print(word);

def cameltosnake(word):
    new="";
    for char in word:
        if (char.isupper()==True):
            new+="_"+char.lower();
        else:
            new+=char;
    return new;

frag=input("Something something Java. I'm too messed up from the coke to write anything else. ");
main(frag);
