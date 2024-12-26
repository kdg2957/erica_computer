def find_quotes_all(filename):
    infile = open(filename,"r")
    outfile = open(filename+"-out.txt","w")
    text = infile.read()
    count = 0
    quote_begin = text.find('"')
    while quote_begin != -1:
        quote_end = text.find('"', quote_begin+1)
        count += 1
        outfile.write(text[quote_begin:quote_end+1] + "\n\n")
        quote_begin = text.find('"',quote_end+1)
    outfile.write("There are " + str(count) + " quotes in total.\n")
    outfile.close()
    infile.close()
    print("Done")
    
# # Test code
find_quotes_all("article.txt")