import csv

file = open('stores_old.csv', 'r')

list=[]

wlist=[]

for line in file.readlines():

    list.append(line.split(","))

for i in range(0,len(list)):
    list2=[list[i][0],list[i][3],list[i][5],list[i][6]]
    wlist.append(tuple(list2))



wfile = open('stores_new.csv', 'w')

writer=csv.writer(wfile)

writer.writerows(wlist)

   

    #print(line, end='')

file.close()

wfile.close()
