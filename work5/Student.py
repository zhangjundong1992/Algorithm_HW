class student:
    id = ""
    name = ""
    school = ""
    tel = 0
    email = ""

    def __init__(self, id, name, school, tel, email):
        self.id = id
        self.name = name
        self.school = school
        self.tel = tel
        self.email = email


class ele_radix:
    stu = student
    val = 0
    rem = 0

    def __init__(self, stu, val, rem):
        self.stu = stu
        self.val = val
        self.rem = rem
