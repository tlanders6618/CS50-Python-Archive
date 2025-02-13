def main(name):
    name=name.strip();
    ignore, period, nn=name.partition("."); #nn is whatever is after the . in the file name; e.g. jpg or gif
    while ("." in nn): #loop is same as in java, just like semicolons are
        ignore, period, nn=nn.partition("."); #if filename has multiple .'s, keep going until the last one is found
    #e.g. name is k.l.j.pdf, nn is originally l.j,pdf, but then becomes j.pdf and finally pdf, as it should be
    nn=nn.lower(); #to ignore upper case
    match (nn):
        case "gif":
            print("image/gif");
        case "jpeg" | "jpg":
            print("image/jpeg");
        case "png":
            print ("image/png");
        case "pdf":
            print ("application/pdf");
        case "txt":
            print ("text/plain");
        case "zip":
            print ("application/zip");
        case _:
            print ("application/octet-stream");

main(input("Wahts ur file naame ? "));
