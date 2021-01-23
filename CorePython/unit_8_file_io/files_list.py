import os

def get_picture_list(rel_path):
    abs_path = os.path.join(os.getcwd(),rel_path)
    print('abs_path =', abs_path)
    dir_files = os.listdir(abs_path)
    #print dir_files
    return dir_files

files = get_picture_list('C:/Users/admin/karyal@imagineit.com.np/Learning/Python/Projects/CorePython/unit_8_file_io')
print(files)