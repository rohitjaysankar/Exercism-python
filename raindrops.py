def convert(number):
    s=""
    if number%3==0:
        s=s+"Pling"
    if number%5==0:
        s=s+"Plang"
    if number%7==0:
        s=s+"Plong"

    if(len(s)==0):
        print(number)
    else:
        print(s)
    
