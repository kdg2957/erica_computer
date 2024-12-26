def find_all_count(filename, x):
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    # Write your code here.
    for i in text:
        print(i)
    
#     position = text.find(x)
#     
#     count = 0
#     if position == -1:
#         outfile.write(x + " is not found.\n")
#     
#     while position != -1:
#         count += 1
#         outfile.write(str(position) + " ")
#         position = text.find(x, position + 1)
#         
#     if count > 0:
#         outfile.write(str(count) + " time(s)")
        
    outfile.close()
    infile.close()
    print("Done")


# Test code
find_all_count('article.txt','computer')     # 6 time(s).
# find_all_count('article.txt','Whole Earth')  # 2 time(s).
# find_all_count('article.txt','Apple')        # 9 time(s).
# find_all_count('article.txt','commencement') # 1 time(s).
# find_all_count('article.txt','apple')        # 0 time(s).
