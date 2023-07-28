import os
import sys
import shutil
from collections import defaultdict

print('Tamatem task project is working')



def get_file_names(folder_path):
    file_names = []
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            # condition here for ignore any untext files
            if file.lower().endswith('.txt'):
                file_names.append(file)
    return file_names

def set_path():
    print(len(sys.argv))
    if len(sys.argv) < 2:
        print("Because you didn't add specific folder I will read it from my defalt one ;)")
        return r"C:\Users\hamza\OneDrive\Desktop\tamatem-python-test\test_samples"
    else:
        print('else')
        return sys.argv[1]

def get_language_dictonary(arr):
    language = defaultdict(list)
    for txt in arr:
        langName = txt.split('-')[0]
        language[langName].append(txt)
    return language


def move_files(source_folder, destination_folder):
    shutil.move(source_folder, destination_folder)


def create_folder_if_not_exists(languageDictonary, path):
    for key in languageDictonary.keys():
        folder_path = os.path.join(path, key)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            for file in languageDictonary.get(key):
                source_path = os.path.join(path, file)
                target_path = os.path.join(folder_path, file)
                shutil.move(source_path, target_path)




#       Main        
path = set_path()
filesArr = get_file_names(path)
languageDictonary = get_language_dictonary(filesArr)

create_folder_if_not_exists(languageDictonary, path)

