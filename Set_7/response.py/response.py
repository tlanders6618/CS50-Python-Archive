import validators;

def main():
    maybemail=input("Hi-dee-ho! What's your email, my dearest friend? ").strip();
    if (validators.email(maybemail)==True):
        print("Valid", end=""); #. Well, I'll be on my way for now, chum. But I'll be seeing you again very soon...");
    else:
        print("Invalid", end=""); #. EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE");

if __name__=="__main__":
    main();
