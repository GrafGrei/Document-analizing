import get_lessons

groups = ['БС-11', 'БС-12', 'БС-21', 'БС-31', 'БС-32', 'ПС-46', 'БП-23', 'ЕС-24', 'БС-42', 'ЕС-34', 'БА-21', 'БП-13', 'БС-22', 'ЕС-14', 'ФС-15', 'ПС-26', 'ПС-36', 'ПС-16']

print(get_lessons.get_lessons(doc_path='documents/docx/2024-06-26_11_40_32.docx', groups=groups))