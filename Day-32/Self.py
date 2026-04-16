""" Stage 1
class Test:
    def __init__(self,name):
        self._name = name
    
A = Test("Ayush")
print(A._name) """


"""Stage 2
 class Retest:
    def __init__(self,name):
        self.__name = name
    def get(self):
        return self.__name
    def set(self,val):
        self.__name = val
        return self.__name

A = Retest("Ayush")
x = A.get()
print(x) """

"""Stage 3
 class SR:
    def __init__(self,name):
        self.__name = name
        self.__cgpa = 0
    def get_cgpa(self):
        return self.__cgpa
    def set_cgpa(self,value):
        if not (0 <= value <= 10):
            raise ValueError("The cgpa must be between 0 - 10")
        self.__cgpa = value
        return self.__cgpa

S1 = SR("Ayush")
print(S1.set_cgpa(10))
 """

""" class SR:
    def __init__(self,name):
        self.__name = name
        self.__cgpa = 0
    @property
    def cgpa(self):
        return self.__cgpa
    @cgpa.setter
    def cgpa(self,value):
        if not (0 <= value <= 10):
            raise ValueError("The cgpa must be between 0 - 10")
        self.__cgpa = value
        return self.__cgpa

S1 = SR("Ayush")
print(S1.cgpa)
S1.cgpa = 10
print(S1.cgpa)
 """

""" class GroupAssignment:
    def __init__(self,groupname,rollno = [None],submissions = []): #None
        self.rollno = []
        self.submissions = submissions
        self.groupname = groupname
    def add_rollnum(self,num):
        self.rollno.append(num)
        return self.rollno
    def add_submission(self,sub):
        self.submissions.append(sub)
        return self.submissions
    
    
G1 = GroupAssignment('Chipkali')
G2 = GroupAssignment('Mc')
G3 = GroupAssignment('Jhingur')

G1.add_rollnum('AU030')
G1.add_rollnum('AU031')
G1.add_rollnum('AU032')
print(G1.rollno)

print(G2.rollno)
print(G3.rollno)
    
if(id(G1.rollno) == id(G2.rollno)):
    print("True")
else:
    print("False")

print(id(GroupAssignment.__init__.__defaults__[0]))
print(id(G1.rollno))
print(id(G2.rollno))
print(id(G3.rollno))
 """


class GroupAssignment:
    def __init__(self,groupname,rollno = [],submissions = []): #None
        self.rollno = rollno
        self.submissions = submissions
        self.groupname = groupname
    def add_rollnum(self,num):
        self.rollno.append(num)
        return self.rollno
    def add_submission(self,sub):
        self.submissions.append(sub)
        return self.submissions
    
    
G1 = GroupAssignment('Chipkali')
G2 = GroupAssignment('Mc')
G3 = GroupAssignment('Jhingur')

G1.add_rollnum('AU030')
G1.add_rollnum('AU031')
G1.add_rollnum('AU032')
print(G1.rollno)

print(G2.rollno)
print(G3.rollno)
    
if(id(G1.rollno) == id(G2.rollno)):
    print("True")
else:
    print("False")

print(id(GroupAssignment.__init__.__defaults__[0]))
print(id(G1.rollno))
print(id(G2.rollno))
print(id(G3.rollno))