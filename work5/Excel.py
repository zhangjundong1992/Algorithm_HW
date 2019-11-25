import xlrd
from work5.Student import *


def get_xls():
    workbook = xlrd.open_workbook(r"D:\Python\Algorithm\work5\选课名单.xls", formatting_info=False)
    sheet = workbook.sheet_by_index(0)

    lst = []

    for i in range(1, sheet.nrows):
        id = str(sheet.row_values(i)[1])
        name = str(sheet.row_values(i)[2])
        school = str(sheet.row_values(i)[3])
        tel = int(sheet.row_values(i)[4])
        email = str(sheet.row_values(i)[5])

        stu = student(id, name, school, tel, email)

        lst.append(stu)

    return lst
