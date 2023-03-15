import os
os.chdir("path/to/file")

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    #print(file_name)
    f_title, f_course, f_num = f_name.split('-')
    #print(f_title,"\n" ,f_course,"\n" ,f_num)

    #remove white space
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2) 

    #print('{}-{}-{}{}'.format(f_num,f_course,f_title,f_ext))
    new_name = '{}-{}-{}{}'.format(f_num,f_course,f_title,f_ext)
    os.rename(f,new_name)
#this will rearrange the filenames in ascending order of f_num.
