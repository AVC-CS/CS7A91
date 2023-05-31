def makeStudentDictionary():
    ##################################################
    # Code your program here
    ##################################################


def findStudent(students, tid):
    scores = []
    ##################################################
    # Code your program here
    ##################################################
    return scores


def printStudent(students):
    ##################################################
    # Code your program here
    #########################################
    print('***************')


def main():
    students = makeStudentDictionary()
    printStudent(students)
    targetID = '2023-0001'
    scores = findStudent(students, targetID)
    print(f'Student ID {targetID} scores: {scores}')


if __name__ == '__main__':
    main()
