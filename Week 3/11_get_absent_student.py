# 나의 풀이

all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    all_array.sort()
    present_array.sort()
    for student, present in zip(all_array, present_array):
        if student != present:
            return student
    return all_array[-1]


print(get_absent_student(all_students, present_students))


# 강의 풀이

all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    student_dict = {}
    for key in all_array:
        student_dict[key] = True
    for key in present_array:
        del student_dict[key]
    for key in student_dict.keys():
        return key

print(get_absent_student(all_students, present_students))