# LAB2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

import random
from re import L
#A simple class that stores the id, name, and number of credits for a class. 
class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    #Initializes attributes of Course
    #course id, course name, course credits
    def __init__(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        self.cid = cid
        self.cname = cname 
        self.credits = credits
        pass

    #formatting method
    def __str__(self):
        # YOUR CODE STARTS HERE
        return f'{self.cid}({self.credits}): {self.cname}'
        pass

    __repr__ = __str__
    #Checks if two courses have the same id
    def __eq__(self, other):
        isEq = False
        if(isinstance(self,Course) and isinstance(other,Course)):
            if(self.cid == other.cid):
                isEq = True
        return isEq

        pass


#Stores a collection of Course objects and their capacity as a dictionary, accessible by their ids. 
class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> C.courseOfferings
        {'CMPSC132': (CMPSC132(3): Programming in Python II, 400), 'CMPSC360': (CMPSC360(3): Discrete Mathematics, 200)}
        >>> C.removeCourse('CMPSC360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC132': (CMPSC132(3): Programming in Python II, 400)}
        >>> isinstance(C.courseOfferings['CMPSC132'][0], Course)
        True
    '''
    #Initializes dictionary of all course offerings
    def __init__(self):
        # YOUR CODE STARTS HERE
        self.courseOfferings = {}
        pass
    #Adds course to dictionary
    #Course obj composed of id, name, and credits
    #Adds capacity attribute as well to courseOfferings dictonary
    #If no statements are executed, course must already be in dictionary

    def addCourse(self, cid, cname, credits, capacity):
        # YOUR CODE STARTS HERE
        if(cid not in self.courseOfferings):
            self.courseOfferings[cid] = (Course(cid, cname, credits),capacity)
            return 'Course added successfully'
        return 'Course already added'
        pass
    #Checks if course is in dictionary and removes it if so
    def removeCourse(self, cid):
        # YOUR CODE STARTS HERE
        if(cid not in self.courseOfferings):
            return 'Course not found'
        del self.courseOfferings[cid]
        return 'Course removed successfully'
        pass

#Stores a collection of Course objects for a semester for a student. 
class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> semester = Semester(1)
        >>> semester
        No courses
        >>> semester.addCourse(cmpsc132)
        >>> isinstance(semester.courses['CMPSC132'], Course)
        True
        >>> semester.addCourse(math230)
        >>> semester
        CMPSC132, MATH 230
        >>> semester.isFullTime
        False
        >>> semester.totalCredits
        7
        >>> semester.addCourse(phys213)
        >>> semester.addCourse(econ102)
        >>> semester.addCourse(econ102)
        'Course already added'
        >>> semester.addCourse(phil119)
        >>> semester.isFullTime
        True
        >>> semester.dropCourse(phil119)
        >>> semester.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> semester.totalCredits
        16
        >>> semester.dropCourse(cmpsc131)
        'No such course'
        >>> semester.courses
        {'CMPSC132': CMPSC132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    '''
    #Initializes Semester object with semester # and courses dictionary
    def __init__(self, sem_num):
        # --- YOUR CODE STARTS HERE
        self.sem_num = sem_num
        self.courses = {}
        pass
    #formatting method
    def __str__(self):
        # YOUR CODE STARTS HERE
        if(len(self.courses) == 0):
            return 'No courses'
        allCourses = ""
        for key in self.courses:
            if key == list(self.courses.keys())[-1]: #if course is the last in the dictionary no comma is added
                allCourses+=key
            else:
                allCourses += key + ", "
        return allCourses

    __repr__ = __str__
    #Adds course to Semester obj
    def addCourse(self, course):
        # YOUR CODE STARTS HERE
        if course.cid not in self.courses:
            self.courses[course.cid] = course
        else:
            return 'Course already added'
        
        pass
    #Removes course from Semester obj
    def dropCourse(self, course):
        # YOUR CODE STARTS HERE
        if course.cid not in self.courses:
            return 'No such course'
        del self.courses[course.cid]
        pass

    @property
    #Iterates through dictionary of Course objs
    #Sums credit attribute of each Course obj
    def totalCredits(self):
        # YOUR CODE STARTS HERE
        creds = 0
        for key in self.courses:
            creds += self.courses[key].credits
        return creds
        pass

    @property
    #Returns True if the total credits is more than 11 and false if not
    def isFullTime(self):
        # YOUR CODE STARTS HERE
        return self.totalCredits > 11
        pass

class Loan:
    '''
        >>> import random
        >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    '''
    #Initializes Loan Obj with loan id and amount 
    def __init__(self, amount):
        # YOUR CODE STARTS HERE
        self.loan_id = self.__getloanID
        self.amount = amount
        pass
    #formatting method
    def __str__(self):
        # YOUR CODE STARTS HERE
        return f'Balance: ${self.amount}'
        pass

    __repr__ = __str__

    @property
    #Assings random number as loan id
    def __getloanID(self):
        # YOUR CODE STARTS HERE
        return random.randint(10000,99999)
    
        pass

class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''
    #Initializes Person obj with name and social security
    def __init__(self, name, ssn):
        # YOUR CODE STARTS HERE
        self.name = name
        self.__ssn = ssn
        pass
    #Formatting method
    def __str__(self):
        # YOUR CODE STARTS HERE
        last4 = ""
        for i in range (len(self.get_ssn())): 
            if i >= 7: #Gets last 4 numbers of ssn
                last4 += self.get_ssn()[i]
        return f'Person({self.name}, ***-**-{last4})'
        pass

    __repr__ = __str__
    #Gets ssn
    def get_ssn(self):
        # YOUR CODE STARTS HERE
        return self.__ssn
        
        pass
    #Checks if two people are the same by comparing their ssn
    #self and other must also be Person objects
    def __eq__(self, other):
        isEq = False
        if(isinstance(self,Person) and isinstance(other,Person)):
            if(self.get_ssn() == other.get_ssn()):
                isEq = True
        return isEq
        pass
#Inherits Person Class
class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> st1 = s1.createStudent(p)
        >>> isinstance(st1, Student)
        True
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC360', C, 1)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC132}
    '''
    #Initializes Staff obj
    #Gets name and ssn from super class (Person)
    def __init__(self, name, ssn, supervisor=None):
        # YOUR CODE STARTS HERE
        super().__init__(name,ssn)
        self.__supervisor = supervisor
        pass
    #Formatting method
    def __str__(self):
        # YOUR CODE STARTS HERE
        return f'Staff({self.name}, {self.id})'
        pass

    __repr__ = __str__

    @property
    #Gets id of staff
    def id(self):
        # YOUR CODE STARTS HERE

        firstInitial = self.name[0].lower() #First inital is first letter of self.name
        lastInitial = ""
        for i in range (len(self.name)):
            if(self.name[i] == ' '): #When space is found, next letter must be first letter of last name
                lastInitial = self.name[i+1].lower()
        last4 = ""

        for i in range (len(self.get_ssn())):
            if i >= 7:
                last4 += self.get_ssn()[i]
        return '905' + firstInitial + lastInitial + last4
        pass

    @property   
    #Returns supervisor
    def getSupervisor(self):
        # YOUR CODE STARTS HERE
        return self.__supervisor
        pass
    #Default supervisor value is none
    #Sets supervisor
    def setSupervisor(self, new_supervisor):
        # YOUR CODE STARTS HERE
        if isinstance(new_supervisor, Staff):
            self.__supervisor = new_supervisor
            return self.__supervisor
        pass
    #applies hold if student is Student obj (sets value to True)
    def applyHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student,Student):
            student.hold = True
            return 'Completed!'
        pass
    #removes hold if student is Student obj (sets value to False)
    def removeHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student,Student):
            student.hold = False
            return 'Completed!'
        pass
    #Unenrolls student if student is Student Obj (sets value to False)
    def unenrollStudent(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student,Student):
            student.active = False
        return 'Completed!'
        pass
    #Creates person if person 
    def createStudent(self, person):
        # YOUR CODE STARTS HERE
        if isinstance(person,Person):
            return Student(person.name, person.get_ssn(), "Freshman")
        pass


class Student(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC311', C, 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132, CMPSC360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC132', C, 1)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC360')
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC360')
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: No courses}
        >>> s1.enrollCourse('CMPSC360', C, 2)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
    '''
    #Initializes student Obj
    #Gets name and ssn from super class (Person)
    def __init__(self, name, ssn, year):
        random.seed(1)
        # YOUR CODE STARTS HERE
        super().__init__(name,ssn)
        self.year = year
        self.semesters = {}
        self.hold = False
        self.active = True
        self.account = self.__createStudentAccount()
        self.temp = 0



    #Formatting method
    def __str__(self):
        # YOUR CODE STARTS HERE
        return f'Student({self.name}, {self.id}, {self.year})'
        pass

    __repr__ = __str__
    #Creates student account obj
    def __createStudentAccount(self):
        # YOUR CODE STARTS HERE
        return StudentAccount(self)
        pass


    @property
    def id(self):
        # YOUR CODE STARTS HERE
        if (self.active):
            firstInitial = self.name[0].lower() #first initial is first letter of self.name
            lastInitial = ""
            for i in range (len(self.name)):
                if(self.name[i] == ' '):
                    lastInitial = self.name[i+1].lower() #when space occurs first initial of last name is letter after
            last4 = ""
            for i in range (len(self.get_ssn())): #use getter method because ssn is a private attribute
                if i >= 7:
                    last4 += self.get_ssn()[i]
            return firstInitial + lastInitial + last4
        pass
    #Registers semester
    def registerSemester(self):
        # YOUR CODE STARTS HERE
        if(self.active and not self.hold):
            self.semesters[len(self.semesters)+1] = Semester(len(self.semesters)+1) #Current semester is length of semester + 1
            #year is dependant on length of semesters 
            if len(self.semesters) < 3: #less than 3 means 2 or less semesters (equivalent to 1 year)
                self.year = 'Freshman'
            elif len(self.semesters)<5:
                self.year = 'Sophomore'
            elif len(self.semesters)<7:
                self.year = 'Junior'
            else:
                self.year = 'Senior'
        else:
            return 'Unsuccessful operation'
        pass

    #Adds course to semester dict
    def enrollCourse(self, cid, catalog, semester):
        # YOUR CODE STARTS HERE
        self.temp = catalog #Stores catalog so we can access it in dropCourse
        if(not self.active or self.hold):
            return 'Unsuccessful operation'

        if cid in catalog.courseOfferings and cid not in self.semesters[semester].courses: #Checks if course id is found in catalog and not in semesters
            self.semesters[semester].courses[cid] = catalog.courseOfferings[cid] #adds cid to semester dictionary
            self.account.chargeAccount(self.account.CREDIT_PRICE*catalog.courseOfferings[cid][0].credits) #Charges account based on # of credits
            return 'Course added successfully'

        elif cid in catalog.courseOfferings and cid in self.semesters[semester].courses:
            return 'Course already enrolled'   

        return 'Course not found'
        pass
    #Removes course from semester dict
    def dropCourse(self, cid):
        # YOUR CODE STARTS HERE
        if(self.hold or not self.active):
            return 'Unsuccessful operation'
        elif cid in str(self.semesters[len(self.semesters)]): #checks if cid is found at key (key is current semester)
            self.account.makePayment(0.5*self.account.CREDIT_PRICE*self.temp.courseOfferings[cid][0].credits) #Refunds half of course cost (based on credits)
            self.semesters[len(self.semesters)].dropCourse(self.semesters[len(self.semesters)].courses[cid][0]) #Calls drop course to remove course
            return 'Course dropped successfully'
        else:
            return 'Course not found'

        pass

    def getLoan(self, amount):
        # YOUR CODE STARTS HERE
        if not self.active:
            return 'Unsuccessful operation'
        elif len(self.semesters) == 0:
            return 'Student not enrolled in any courses yet'
        #Commented out b/c of Tuple Obj Error 
        #Should not give loan if student is not full time
        elif self.temp.courseofferings[str(self.semesters[len(self.semesters)])].isFullTime == False:
            return 'Not full-time'
        else: #If all conditions are met gives loan
            l = Loan(amount) #creats Lone object
            self.account.loans[l.loan_id] = l #updates loan dictionary in StudentAccount
            self.account.makePayment(amount) #Subtracts loan amount from student's balance
        
        pass




class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4, 600)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2, 500)
        'Course added successfully'
        >>> C.addCourse('CMPEN270', 'Digital Design', 4, 300)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.dropCourse('CMPEN270')
        'Course dropped successfully'
        >>> s1.account.balance
        1900.0
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
        >>> StudentAccount.CREDIT_PRICE = 1500
        >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
        >>> s2.registerSemester()
        >>> s2.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s2.account.balance
        4500
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        7900.0
    '''
    CREDIT_PRICE = 1000
    #Initializes StudentAccount obj
    def __init__(self, student):
        # YOUR CODE STARTS HERE
        self.student = student
        self.balance = 0
        
        self.loans = {}
        pass
    #Formatting method
    def __str__(self):
        # YOUR CODE STARTS HERE
        return f'Name: {self.student.name}\nID: {self.student.id}\nBalance: ${self.balance}'
        pass

    __repr__ = __str__
    #Subtracts from balance
    def makePayment(self, amount):
        # YOUR CODE STARTS HERE
        self.balance -= amount
        return self.balance
        pass
    #Adds to balance
    def chargeAccount(self, amount):
        # YOUR CODE STARTS HERE
        self.balance += amount
        return self.balance
        pass


if __name__=='__main__':
    import doctest
    doctest.testmod()  # OR
    #doctest.run_docstring_examples(Student, globals(), name='HW22',verbose=True) # replace Course for the class name you want to test