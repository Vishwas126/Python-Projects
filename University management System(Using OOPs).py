#University Management System
class person:
    def __init__(self,name,roll,mobile):
        self.name = name
        self.roll = roll
        self.mobile = mobile
class student(person):
    def __init__(self,name,roll,mobile,branch):
        self.branch = branch
        super().__init__(name,roll,mobile)
class teacher(person):
    def __init__(self,name,roll,mobile,subject):
        self.subject = subject
        super().__init__(name,roll,mobile)
class college:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.teachers = []
    def add_student(self,student):
        self.students.append(student)
    def add_teacher(self,teacher):
        self.teachers.append(teacher)
    def display_students(self):
        if len(self.students)==0:
            print("No students are there in this college")
        else:
            for i in range(len(self.students)):
                print(f"Student {i+1} details")
                print(f"Name: {self.students[i].name}")
                print(f"Roll Number: {self.students[i].roll}")
                print(f"Mobile Number: {self.students[i].mobile}")
                print(f"Branch: {self.students[i].branch}")
                print()
    def display_teachers(self):
        if len(self.teachers) == 0:
            print("No teachers are there in this college")
        else:
            for i in range(len(self.teachers)):
                print(f"Teacher {i+1} details")
                print(f"Name: {self.teachers[i].name}")
                print(f"Roll Number: {self.teachers[i].roll}")
                print(f"Mobile Number: {self.teachers[i].mobile}")
                print(f"Subject dealed: {self.teachers[i].subject}")
                print()
colleges = []
while True:
    print("Choose any option: ")
    print("1. Create College")
    print("2. Create Student")
    print("3. Create teacher")
    print("4. Display students")
    print("5. Display Teachers")
    print("6. To exit")
    x = int(input("Enter opted Value: "))
    if x == 1:
        cname = input("Enter College Name: ")
        x = True
        for i in colleges:
            if i.name == cname:
                x = False
                break
        if x==True:
            c1 = college(cname)
            colleges.append(c1)
        else:
            print("College already exists with the same name")
    elif x == 2:
        cname = input("Enter College name: ")
        x = False
        for i in colleges:
            if i.name == cname:
                x = True
                break
        if x == True:
            res = -1
            for i in range(len(colleges)):
                if colleges[i].name == cname:
                    res = i
            sname = input("Enter student name: ")
            sroll = input("Enter Student Roll: ")
            smobile = input("Enter mobile number: ")
            sbranch = input("Enter Student Branch: ")
            s1 = student(sname,sroll,smobile,sbranch)
            colleges[res].add_student(s1)
        else:
            print("college does not exists")
    elif x==3:
        cname = input("Enter College name: ")
        x = False
        for i in colleges:
            if i.name == cname:
                x = True
                break
        if x == True:
            res = -1
            for i in range(len(colleges)):
                if colleges[i].name == cname:
                    res = i
            tname = input("Enter teacher name: ")
            troll = input("Enter teacher Roll: ")
            tmobile = input("Enter mobile number: ")
            tsubject = input("Enter teacher subject: ")
            t1 = teacher(tname,troll,tmobile,tsubject)
            colleges[res].add_teacher(t1)
        else:
            print("college does not exists")
    elif x == 4:
        cname = input("Enter College name: ")
        x = False
        for i in colleges:
            if i.name == cname:
                x = True
                break
        if x == True:
            res = -1
            for i in range(len(colleges)):
                if colleges[i].name == cname:
                    res = i
            x = colleges[res]
            x.display_students()
        else:
            print("college does not exists")
    elif x == 5:
        cname = input("Enter College name: ")
        x = False
        for i in colleges:
            if i.name == cname:
                x = True
                break
        if x == True:
            res = -1
            for i in range(len(colleges)):
                if colleges[i].name == cname:
                    res = i
            x = colleges[res]
            x.display_teachers()
        else:
            print("college does not exists")
    else:
        break
'''
c1 = college("codegnan")
s1 = student("sai",101,9123456789,"CSE")
s2 = student("vardhan",102,9123456788,"ECE")
c1.add_student(s1)
c1.add_student(s2)
t1 = teacher("sai vardhan",201,9123456777,"Python")
t2 = teacher("sudheer",202,9123456666,"Java")
c1.add_teacher(t1)
c1.add_teacher(t2)
c1.display_students()
c1.display_teachers()
print(c1.students)
print(c1.teachers)
'''

                








        
        
