# data
colors = '0123456789'

# functions 

def check(s):
    for i in colors:
        if i*3 in s:
            return True
    return False

def bang(s, col):
    for i in colors:
        if i*3 in s:
            j = s.find(i*3)    #start index of substring
            while j<len(s)-1 and s[j]==s[j+1]:
                s = s[:j] +s[j+1:]
                col+=1
            s = s[:j] + s[j+1:]
            col+=1
    return [s, col]

# main 
input()
l = input().replace(' ','')
count = 0
while check(l):
    l, count = bang(l, count)[0], bang(l, count)[1] 
print(count)