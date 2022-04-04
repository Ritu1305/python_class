class student():
    def result(self):
        if self.marks>=40:
            return True
        else:
            return False
# created an object in python calling a class 
student1=student() 
# declaring marks
student1.marks=50

check=student1.result()
print(check)

 


