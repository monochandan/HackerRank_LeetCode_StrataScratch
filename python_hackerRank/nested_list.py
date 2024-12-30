
if __name__ == "__main__":
    # min = 999999
    # sec_min = []
    # name_list = []
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # print(students)
    grades = sorted(set(student[1] for student in students))

    second_lowest_grade = grades[1]

    second_lowest_student = [student[0] for student in students if student[1] == second_lowest_grade]

    second_lowest_student.sort()

    for i in second_lowest_student:
        print(i)



    #     if score <= min:
    #         #sec_min.clear()
    #         sec_min.append(min)
    #         name_list.clear()
    #         name_list.append(name)
    #         min = score
    #     if score == sec_min[0]:
    #         sec_min.append(score)
    #         name_list.append(name)
    #     print(sec_min)

    # print(sec_min)
    # print(name_list)

    
# second lowest score 
