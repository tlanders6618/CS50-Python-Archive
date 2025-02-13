import re;


def main():
    print(parse(input("HTML: ")));


def parse(html):
    #if (html==""): #default for testing
        #html='<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"> </iframe>';
    link=re.search(r'^<iframe.+src="(https?://(?:www\.)?youtube.com/embed/.+)".+', html);
    if (link==None):
        return None;
    else:
        link=link.groups(1); #returns a tuple containing everything in the () above
        link=str(link[0]); #turn tuple into string
        #print("Captured: "+link); #should be https://www.youtube.com/embed/xvFZjo5PgG0
        if ("http" in link and "https" not in link): #replace with https
            index=link.find("http");
            link=link[0:index+4]+"s"+link[index+4:];
            #print("Https: "+link);
        if ("www." in link): #slice it out
            index=link.find("www.");
            link=link[0:index]+link[index+4:];
            #print("After removing www: "+link);
        #remove embed
        index=link.find(".com/embed") #substring is 10 characters
        link=link[0:index]+link[index+10:];
        #print("After removing .com/embed: "+link);
        #insert . in between youtu and be
        index=link.find("youtu");
        link=link[0:index+5]+"."+link[index+5:];
        #print("Final verion: "+link)
        return link;

if __name__ == "__main__":
    main();
