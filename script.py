import os

filepath = "your file path"

keyword = 'thumb'
for fname in os.listdir(filepath):
    if keyword in fname:
        path = os.path.join(filepath, fname)
        # print(path)
        # print(fname, "has the keyword")
        os.remove(path)