import os

exclusions = ['.git','.gitignore', '_builder']

path = '../'

# TODO :
# use exclusion from config file to exclude unecessary files

def menu (path) :
    menu = []
    print('Menu generator')
    folders = os.listdir(path)
    for folder in folders :
        if folder == '.git' or folder == '.gitignore' or folder == '_builder': 
           print('null')
        else : 
            menu.append(folder)
    return menu

    #print(menu)
    #for folder in listOfFiles:
    #listOfFiles = os.listdir(path+'/'+folder)

menu = menu(path)
print(menu)
#categories = menu(path)
#print(categories)