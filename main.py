list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    list_3 = []
    # Merge student information from list_1 and list_2
    for student in list_1:
        merged_student = student.copy()
        for student_2 in list_2:
            if student_2.get('id') == student.get('id'):
                merged_student.update(student_2)
                break
        list_3.append(merged_student)
    # Add missing students from list_2 to list_3
    for student_2 in list_2:
        if not any(student_2.get('id') == student.get('id') for student in list_3):
            list_3.append(student_2)
    return list_3


list_3 = merge_lists(list_1, list_2)
