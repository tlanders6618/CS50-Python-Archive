import re, string;

def main():
    print(count(input("Text: ")));

def count(text):
    allowed=string.punctuation;
    list=re.findall(r"(?:\W|^)um(?:\W|$)", text.strip(), re.IGNORECASE);
    #for word in list:
        #print(word);
    return len(list);

if __name__ == "__main__":
    main();
