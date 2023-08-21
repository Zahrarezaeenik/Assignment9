    
def add_times(t1, t2):
    result = {'h':0,'m':0,'s':0}
    result ["s"] = t1["s"] + t2["s"]
    if result['s']//60 :
        result['s'] %= 60
        result["m"] += 1

    result ["m"] += t1["m"] + t2["m"]

    if result['m'] // 60:
        result['m'] %= 60
        result["h"] += 1

    result ["h"] += t1["h"] + t2["h"]
    return result

def subtract_times(t1, t2):
    result = {'h':0,'m':0,'s':0}
    result['s']=t1['s']-t2['s']
    if result['s']<0:
        result['s']+=60
        result['m']-=1

    result['m']=t1['m']-t2['m']+result['m']

    if result['m']<0:
        result['m']+=60
        result['h']-=1

    result['h']=t1['h']-t2['h']+result['h']
    
    return result

def time_to_str(Time):
    return f"{Time['h']}:{Time['m']:02}:{Time['s']:02}"


def input_time(text):
    h,m,s=input(text).split(':')
    h,m,s=int(h),int(m),int(s)
    if m in range(0,60) and s in range(0,60):
        return {'h':h,'m':m,'s':s}
    print("Input error! try again.")
    return input_time(text)


def main():
    time1= input_time("Enter Time 1 in format (HH:MM:SS): ")
    time2= input_time("Enter Time 2 in format (HH:MM:SS): ")
    print(f"{time_to_str(time1)} + {time_to_str(time2)} = {time_to_str(add_times(time1,time2))}")
    print(f"{time_to_str(time1)} - {time_to_str(time2)} = {time_to_str(subtract_times(time1,time2))}")
    

if __name__ == "__main__":
    main()