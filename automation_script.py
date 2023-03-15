import os
os.chdir("path/to/file")

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    print(file_name)