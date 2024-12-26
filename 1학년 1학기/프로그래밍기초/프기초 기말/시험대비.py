# def median(a,b):
#     c = (a+b)/2
#     
#     if int(c) == c:
#         return int(c)
#     
#     else:
#         return -1
# 
# def is_balanced(a,b):
#     
# 
#     if (a >= 10  and a<= 99) and (b >= 10 and b<= 99):
#         for i in range(10,91,10):
#             if median(a,b) == i:
#                 return True
#         return False
#     else:    
#         return False
#     
#     
# def solve(a,b):
#     if is_balanced(a,b):
#         print(f"{a} x {b}")
#         if a - median(a,b) > 0:
#             print(f"= ( {median(a,b)} + {a-median(a,b)} ) x ( {median(a,b)} {b-median(a,b)} )")
#         
#         else:
#             print(f"= ( {median(a,b)} {a-median(a,b)} ) x ( {median(a,b)} + {b-median(a,b)} )")
#         if a - median(a,b) > 0:
#             print(f"{median(a,b)} x {median(a,b)} - {median(a,b)-b} x {a-median(a,b)}")
#         else:
#             print(f"{median(a,b)} x {median(a,b)} - {median(a,b)-a} x {b-median(a,b)}")
#         print(f"{median(a,b)*median(a,b)} {(a-median(a,b))*(b-median(a,b))}")
#         print(f"{a*b}")
#     else:
#         print(f"{a} x {b} = ?")
#         
# print(median(22,23))
# print(is_balanced(21,19))
# solve(21,19)
32

def loewercase(a):
    s = ""
    for c in a:
        asc = ord(c)
        if asc >= 65 and asc <= 90:
            s = s + chr(ord(c)+32)
        elif asc >=97 and asc <= 122:
            s = s + c
        else:
            s = s + c
            
    return s

def split_words(a):
    c = []
    m = ''
    s = loewercase(a)
    
    for i in s:
        if ord(i) >=97 and ord(i) <= 122:
            m += i
        else:
            if len(m) == 1:
                m = ''
            else:
                if m =='':
                    pass
                else:
                    c.append(m)
                    m =''
    if m != '' and len(m) != 1:                
        c.append(m)
            
    return c


        
def word_counter(filename):
    infile = open(filename,"r")
    
    text = infile.read()
    
    
    a = loewercase(text)
    c = split_words(a)
    c.sort()
    d = {}
    
    for x in c:
        position = text.find(x)
        
        if x not in d:
            count = 0
            if position == -1:
                d[x] = 0
            
            while position != -1:
                count += 1
                position = text.find(x, position + 1)
            d[x] = count
        
    return d        
            
        
    outfile.close()
    infile.close()
    print("Done")
    
def most_used_words(filename,n):
    if n<1:
        n=5
    ff=word_counter(filename)
    x=sorted(ff.items(), key = lambda y:y[1],reverse=True)

    aa=[]
    for i in range(n):
        aa.append(x[i])
        
    return aa

    
#print(loewercase("It's High Noon ..."))
#print(split_words("It's High Noon. it is high and it is good"))
#print(word_counter('article.txt'))
#print(most_used_words('article.txt',3))
def mode(ds):
    
    r = set()
    ds.sort
    d = {}
    a = []
    
    
    for i in ds:
       if i not in a:
           a.append(i)
           
    for i in a:
        d[i] = ds.count(i)
        
    count = 0
    c = []
    l = []
    f = []
    print(d)
    for i in d.keys(): l.append(i)
    print(l)
    for i in d.values(): f.append(i)
    
    for i in range(len(l)):
        
        if count < l[i]:
            count = f[i]
            c.append(f[i])
        elif count == f[i]:
            c.append(f[i])
            
    t = set(c)
        
     
    if t != {}:
        return t
    
    else:
        return r

def median(ds):

    ds.sort()
    if ds != []:
        if len(ds) % 2 == 0:
            return float((ds[len(ds)//2] + ds[(len(ds)//2)-1]) / 2)
        else:
            return float(ds[len(ds)//2])
    else:
        return 0.0
    
    
print(median([0,1,2,3,4]))