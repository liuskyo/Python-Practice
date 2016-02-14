class student:
    
    def __init__(self,name,gender):
        self.grades=[]
        self.name=name
        self.gender=gender
    def avg(self):
        sum=0
        for i in self.grades:
            sum=sum+i
        return sum/len(self.grades)

    def add(self,grade):
        self.grades.append(grade)

    def fcount(self):
        fsum=0
        for n in self.grades:
            if n<60:
                fsum=fsum+1
        return fsum






def top(studentlist):
    maxe=0
    for s in studentlist:
        a=s.avg()
        if a>maxe:
            maxe=a
            maxeStudent=s
    return maxeStudent






s1 = student("Tom","M")
s2 = student("Jane","F")
s3 = student("John","M")
s4 = student("Ann","F")
s5 = student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)
