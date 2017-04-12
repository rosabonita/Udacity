import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Users\esaae\OneDrive\Academic\Udacity\Front End Web Developer\Lesson 1 Mini Project\alphabet\message")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is " +saved_path)
    os.chdir(r"C:\Users\esaae\OneDrive\Academic\Udacity\Front End Web Developer\Lesson 1 Mini Project\alphabet\message")
    #(2) for eac file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))
rename_files()
