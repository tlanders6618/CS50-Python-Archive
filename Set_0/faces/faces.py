def convert(face): #java programming taking over...must...use...semicolons...
    if ("(:" in face or ":)" in face): #accepts forwards or backwards smiley faces, just in case
        print("I'm glad to hear it kiddo. That makes me happy too.");
    elif (":(" in face or "):" in face):
        print("I'm sorry to hear that kiddo. I can sympathise.");
    face=face.replace("(:", "🙂"); face=face.replace(":)", "🙂"); #replace all happy faces
    face=face.replace(":(", "🙁"); face=face.replace("):", "🙁"); #then replace all sad faces
    return face;

def main ():
    print("Hey kiddo. How ya feeling? You feeling like you could jump for joy, or are you a little blue? Tell me with a :) or :(");
    print(convert(input()));

main();
