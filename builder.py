import json
import os

# Variables
html = {
    "header" : "null",
    "article" : "null",
    "body" : "null",
    "footer" : "null"
}

article = {
    "date" : "null",
    "media" : "null",
    "title" : "null",
    "body" : "null",
    "link" : {
        "alt" : "null",
        "link" : "null"
    }
}

# Getting configuration params
with open('config.json') as json_data_file:
    conf = json.load(json_data_file)

path = conf["path"]
lowTechMode = conf["lowTech"]
exclusions = conf["exclusions"]

print('Loading conf file ...')
print('Path : ' + str(path))
print('LowtechMode : ' + str(lowTechMode))


# Layout loading
def layouts() :
    # main.html loading
    with open('layouts/main.html') as file:
        header = file.read()
        brackets = header.split('{{')
        html["header"] = brackets[0]
        brackets = brackets[1].split('articles}}')
        html["footer"] = brackets[1]
    # article.html loading
    with open('layouts/article.html') as file:
        html["article"] = file.read()
    

# Parses every folder and gets article content
def folderParse(path) : 
    # folder parsing
    folders = os.listdir(path)
    for folder in folders :
        print("Folder : " + folder)
        # Parse subfolder
        # TODO Does not parse avery folder 
        if os.path.isdir(folder) :
            articles = os.listdir(folder)
            for article in articles :
                print("Article : " + str(article))
        else :
            print('NOT A FOLDER')

def articleParse(path) :   
    files = os.listdir(path)
    for file in files :
        print("File : " + str(file))
        # Image checking
        if file.lower().endswith(('.png', '.jpg', '.jpeg')) :
            article["media"] = path + "/" + file
            
        # Markdown parse
        if file.lower().endswith(('.md')) :
            with open(path+"/"+file) as file :
                markdown = file.read()
                # Title parsing
                title = markdown.split('#')
                title = title[1].split('\n')
                article["title"] = title[0]
                # Date parsing
                date = markdown.split('##')
                date = date[1].split('\n')
                article["date"] = date[0]
                # Body parsing
                body = markdown.split("##" + str(date[0]))
                body = body[1].split('[')
                article["body"] = body[0]
                # Link parsing
                alt = markdown.split('[')
                alt = alt[1].split(']')
                article["link"]["alt"] = alt[0]
                link = alt[1].split('(')
                link = link[1].split(')')
                article["link"]["link"] = link[0]         
    return article


def main() :
    layouts()
    #folderParse(path)
    article = articleParse("../3d/03-11-19_landscape")
    print(article)

main()
