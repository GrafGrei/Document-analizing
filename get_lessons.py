from docx import Document


def get_mas(doc_path):
    try:
        doc = Document(doc_path)
        Table = doc.tables[0]
        lessons = []
        for row in Table.rows:
            for cell in row.cells:
                lessons.append(cell.text)
        return lessons
    except:
        return []

def cycle(ind, all_lessons, groups):
    group_lessons = []
    sel = True
    while sel:
        ind += 1
        if ind == len(all_lessons):
            break
        for gr in groups:
            if gr in all_lessons[ind]:
                sel = False
                break
        if sel:
            group_lessons.append(all_lessons[ind])
    return group_lessons

def group_lessons(group, all_lessons, groups):
    indexes = []
    group_lessons = []
    for i in range(len(all_lessons)):
        if group in all_lessons[i]:
            indexes.append(i)
    # print(indexes)
    for index in indexes:
        ind = index
        pr = cycle(ind, all_lessons, groups)
        group_lessons.append(pr)
    return group_lessons

def remove_duplicates(data):
    exit_array = []
    for element in data:
        if (element not in exit_array) and (len(element) != 0):
            exit_array.append(element)
    if len(exit_array) == 1 and len(exit_array[0]) == 1:
        return []
    return exit_array

def rebuilding_lessons(group_lessons):
    for lesson in group_lessons:
        less = remove_duplicates(lesson)
        group_lessons[group_lessons.index(lesson)] = less

    # print(group_lessons)
    new_group = []
    for lesson in group_lessons:
        if len(lesson) != 0:
            new_group.append(lesson)
    group_lessons = new_group

    i = 0

    while i < len(group_lessons):
        lesson = group_lessons[i]
        if lesson[0].isnumeric() == False:
            lesson.insert(0, f"{i+1}")
        i += 1
    return group_lessons

def get_lessons(doc_path, groups):
    mas = get_mas(doc_path)
    day_lessons = {}
    for group in groups:
        group_lessonss = group_lessons(group, mas, groups)
        group_lessonsss = rebuilding_lessons(group_lessonss)
        day_lessons[f"{group}"] = group_lessonsss
    return day_lessons



