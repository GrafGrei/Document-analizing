from docx import Document

def get_mas(doc_path):
    doc = Document(doc_path)
    Table = doc.tables[0]

    lessons = []

    for row in Table.rows:
        for cell in row.cells:
            lessons.append(cell.text)
    return lessons

