import os

def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r'/home/vbuni/Documents/rename_files/prank')
    saved_path = os.getcwd()
    print 'Current Working Directory is %s' % (saved_path)
    os.chdir(r'/home/vbuni/Documents/rename_files/prank')
    # (2) for each file, rename filename
    for file_name in file_list:
        new_file_name = file_name.translate(None, '0123456789')
        print 'Old name - %s' % (file_name)
        print 'New name - %s' % (new_file_name)
        os.rename(file_name, new_file_name)

    os.chdir(saved_path)


rename_files()
