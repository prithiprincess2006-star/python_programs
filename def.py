class student:
    name="ragul"
    age=20
    def marks(self):
        print("tamil: 89, english: 90")
s1=student()
print(s1.name)
print(s1.age)
s1.marks()

class student:
    name="Unknown"
    mark=0

    def display(self):
        print("Name: ",self.name)
        print("Mark: ",self.mark)
s1=student()
s1.name="naveen"
s1.mark=90
s2=student()      
s2.name="praveen"
s2.mark=98
s3=student()
s3.name="praveena"
s3.mark=89
s1.display()
s2.display()
s3.display()