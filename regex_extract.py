import re
sum = 0
count = 0
with open('regex2.txt','r') as rf:
    for line in rf:
        y = re.findall('[0-9]+', line)

        #print (y)
        for i in y:
            sum = sum + int(i)
            count = count + 1
            #sum_revised = re.findall('[7-8]+',sum)
            #print(sum_revised)
    print(sum)
    print(count)
