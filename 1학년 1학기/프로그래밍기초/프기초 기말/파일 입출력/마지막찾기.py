def find_last(filename,x):
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    last_pos = -1
    position = text.find(x)
    while position != -1:
        last_pos = position
        position = text.find(x,  last_pos+ 1)
        
    if last_pos ==-1:
        outfile.write(x + " is not found.\n")        
    else:
        outfile.write(x + " is at " + str(last_pos) + " the last time.\n")

    
    

    

    
    outfile.close()
    infile.close()
    print("Done")

# Test code
find_last('article.txt','computer')    # at 10975 the last time.
find_last('article.txt','Whole Earth') # at 11280 the last time.
find_last('article.txt','Apple')       # at 6604 the last time.
find_last('article.txt','apple')       # not found.
