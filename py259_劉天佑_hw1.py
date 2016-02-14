#Q1
mathSet={'Tom','John','Mary','Jimmy','Sunny','Amy'}
englishSet={'John','Mary','Tony','Bob','Pony','Tom','Alice'}
print("Math pass but Englis not pass:")
print((mathSet-englishSet))
print("Math not pass but Englis pass:")
print((englishSet-mathSet))
print("All pass:")
print((englishSet&mathSet))

#Q2
Dict={'Tom':[80,100,90,95],'John':[100,93,75,80]}
print("Tom average:")
print((Dict['Tom'][0]+Dict['Tom'][1]+Dict['Tom'][2]+Dict['Tom'][3])/4)
print("John average:")
print((Dict['John'][0]+Dict['John'][1]+Dict['John'][2]+Dict['John'][3])/4)
