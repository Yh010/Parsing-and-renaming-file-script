import os
os.chdir("path/to/file")

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    #print(file_name)
    f_title, f_course, f_num = file_name.split('-')
    print(f_title,"\n" ,f_course,"\n" ,f_num)

