import emoji;

def main():
    phrase=input("");
    phrase=(emoji.emojize(phrase, language="alias"));
    print(phrase);

if __name__=="__main__": #main will only run if python game.py is called; ensures this will not trigger if imported
    main();
