def find_all(filename, x):
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    # Write your code here.
    last_pos = -1
    position = text.find(x)
    while position != -1:
        outfile.write(str(position) + " ")
        position = text.find(x, position + 1)
        
    if last_pos ==-1:
        outfile.write(x + " is not found.\n")        
    else:
        outfile.write(x + " is at " + str(last_pos) + " the last time.\n")

    
    

    

    
    outfile.close()
    infile.close()
    print("Done")

# Test code
find_all('article.txt','computer')
# at 3269, 3357, 3601, 3725, 6209, 10975.
find_all('article.txt','Whole Earth')
# at 10735, 11280.
find_all('article.txt','Apple')
# at 4380, 4455, 4742, 5586, 5765, 6346, 6379, 6445, 6604.
#find_all('article.txt','apple')
# not found
