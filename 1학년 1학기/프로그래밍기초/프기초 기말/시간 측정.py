import time

def time_check(msg):
    start = time.perf_counter()
    value = input(msg + "\n >> ")
    end = time.perf_counter()
    
    
    print('걸린 시간 ',round(end-start,2))
    
time_check("dddd")