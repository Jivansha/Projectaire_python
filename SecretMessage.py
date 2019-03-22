import os

def rename_files():
    # get files for renaming
    pic_list= os.listdir(r"C:\Users\Dell\Downloads\prank\prank")
    print(pic_list)
    saved_path=os.getcwd()
    print(saved_path)
    os.chdir(r"C:\Users\Dell\Downloads\prank\prank")
    # rename the files
    for file_name in pic_list:
        #os.rename(file_name, file_name.translate("","0123456789"))
        print("Old file name " + file_name)
        os.rename(file_name, file_name.translate(str.maketrans('','','1234567890')))
        print("New file name " + file_name.translate(str.maketrans('','','1234567890')))
    os.chdir(saved_path)
rename_files()    
