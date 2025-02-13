def main():
    hash=input("Nom nom. I am the Vowel Monster. I like to eat vowels. Give me a sentence to feed me. ");
    print(killallvowels(hash));
    print("*Burp* Thank you very much. That was delicious!");
    #print("Remember Java kids, always use your semicolons, and have a btfl dy!");

def killallvowels(word):
    replace="";
    for num in range(len(word)):
        if (isvowel(word[num])==False):
            replace+=word[num]; #strings are immutable; must make new one to change the message
    return replace;

def isvowel(char):
    char=char.lower();
    if (char=="a" or char=="e" or char=="i" or char=="o" or char=="u"): #or char=="y"): #nvm y isn't a vowel apparently
        return True;
    else:
        return False;

main();
