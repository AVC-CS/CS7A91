import main


def test_main_1():

    students = main.makeStudentDictionary()
    main.printStudent(students)

    assert len(students) == 4
    assert isinstance(students[0], dict) == True
    keys = students[0].keys()
    print(keys)
    students.sort(key=lambda d: d['Name'])
    assert list(keys) == ['Name', 'ID', 'Math', 'English', 'Computer']
    assert students[0]['Name'] == 'Bill Watson'
    assert students[3]['Name'] == 'Mary Smith'


def test_main_2():

    students = main.makeStudentDictionary()
    main.printStudent(students)
    scores = main.findStudent(students, '2023-0001')

    assert len(scores) == 3
    assert scores == [70, 100, 90]
