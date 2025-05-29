
# making a class. Name students
class Students:
    #here I init the name, student id and the grades
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    # here is just a adding a grade in the grade list
    def add_grade(self, score):
        self.grades.append(score)

    ## here is just a returning the average of all grade. round for the round off the all grades. the sum is add all the grades in the list and the len is going to grab how many in the list

    def average(self):
        if not self.grades:
            return 0
        return round(sum(self.grades) / len(self.grades), 0)

    # here is going to get remarks
    def get_remarks(self):
        avg = self.average()
        if avg >= 90:
            return "Excellent"
        elif avg >= 75:
            return "Good"
        elif avg >= 60:
            return "Need Improvement"
        else:
            return "Failing"
    # geting all the information about the student
    def info(self):
        print(self.name)
        print( self.student_id )
        print( self.grades )
        print( self.average() )
        print( self.get_remarks() )


s1 = Students("jamie", "24-0083")

s1.add_grade(88)
s1.add_grade(82)
s1.add_grade(75)


s1.info()