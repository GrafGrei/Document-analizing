from os import walk

filenames = next(walk('documents/doc'), (None, None, []))[2]

for name in filenames:
    with open(f"documents/doc/{name}", "rb") as doc:
        data = doc.read()
        name = name[:-4]
        with open(f"documents/docx/{name}.docx", "wb") as docx:
            docx.write(data)