from document import get_mas
from gruop import group_lessons, rebuilding_lessons


groups = ['БС-11', 'БС-12', 'ЕС-24', 'БП-13', 'БС-22', 'ЕС-14', 'ФС-15', 'ПС-26', 'ПС-36', 'ПС-16']

mas = get_mas("documents/docx/2024-06-26_11_40_32.docx")

for group in groups:
    print(f'--------------------------------------{group}---------------------------------------------')
    group_lessonss = group_lessons(group, mas)
    # print(group_lessonss)
    group_lessonsss = rebuilding_lessons(group_lessonss)
    for group_lesson in group_lessonsss:
        print(group_lesson)
    # print(group_lessonsss)