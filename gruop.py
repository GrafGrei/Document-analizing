
groups = ['БС-11', 'БС-12', 'ЕС-24', 'БП-13', 'БС-22', 'ЕС-14', 'ФС-15', 'ПС-26', 'ПС-36', 'ПС-16']



def cycle(ind, all_lessons):
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

def group_lessons(group, all_lessons):
    indexes = []
    group_lessons = []
    for i in range(len(all_lessons)):
        if group in all_lessons[i]:
            indexes.append(i)
    print(indexes)
    for index in indexes:
        ind = index
        pr = cycle(ind, all_lessons)
        group_lessons.append(pr)
    return group_lessons

def remove_duplicates(data):
    exit_array = []
    for element in data:
        if (element not in exit_array) and (len(element) != 0):
            exit_array.append(element)
    if len(exit_array) == 1 and len(exit_array[0]) == 1:
        return  []
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

        for index, lesson in enumerate(group_lessons):
            if les

        return group_lessons



