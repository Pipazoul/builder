import json
import os
import shutil
from PIL import Image 

# Variables definition
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
articles = []
outputDir = "public/"

# Getting configuration params
with open('config.json') as json_data_file:
    conf = json.load(json_data_file)

path = conf["path"]
categories = conf["categories"]
lowTechMode = conf["lowTech"]
exclusions = conf["exclusions"]

print('Loading conf file ...')
print('Path : ' + str(path))
print('LowtechMode : ' + str(lowTechMode))

# Creates the default output folder structure
def createFolderStruc(outputDir) :
    try :
        shutil.rmtree(outputDir)
    except Exception  :
        print("The folders already exist")

    os.mkdir(outputDir)
    os.mkdir(outputDir + "medias")
    if lowTechMode == True :
        os.mkdir(outputDir + "medias/dithered")


# Layout loading
def layouts() :
    print('layout import')
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
    
    # copy style css to outputDir
    print("Style copy to public folder")
    shutil.copy("layouts/style.css", outputDir)
    # copy post types images
    print("Type copy to public folder")
    shutil.copytree("layouts/types", outputDir + "medias/types")

# Parses every folder and gets article content
def folderParse(path, type) :
    #print('Folder parsing ...')
    # folder parsing
    folders = os.listdir(path)
    for folder in sorted(folders) :
        article = articleParse(path+'/'+folder, type)
        print(folder)
        #articles.append(article)
        genHtml(article)


# Parses the images an markdown file into the article variable
def articleParse(path, type) :   
    files = os.listdir(path)
    for file in sorted(files) : 
        # Checks the post type
        # Image checking
        if file.lower().endswith(('.png', '.jpg', '.jpeg'))  :
            #article["media"] = path + "/" + file
            # copy image to public
            #print("Image copy to public folder")
            try :
                os.mkdir(outputDir + "medias/")
            except OSError :
                print("The folders already exist")

            # Image compression
            image = Image.open(path + "/" + file)
            basewidth = 500
            wpercent = (basewidth/float(image.size[0]))
            hsize = int((float(image.size[1])*float(wpercent)))
            image = image.resize((basewidth,hsize), Image.ANTIALIAS)
            image.thumbnail("200, 200", Image.ANTIALIAS)
            image.save(outputDir+"medias/" + type + "_" + file)
            if lowTechMode == True :
                image = image.convert('1')
                image.save(outputDir+"medias/dithered/" + type + "_" + file)
            article["media"] =  "medias/" + type + "_" + file
            #print("ARTICLE MEDIA :" + str(article["media"]))
        

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
                #print(article)
                return article

# Generates the html structure for each article 
def genHtml(article) :

    print(article)
    
    f=open(outputDir + "/articles.html", "a")
    f.write('<div class="card">\
    <div class="date">'+article["date"]+'</div>\
    <div class="featured-image left">\
    <img src="'+article["media"]+'"></div>\
    <div class="text">\
    <h2>'+article["title"]+'</h2>\
    <p>'+article["body"]+'</p>\
    <a href="'+article["link"]["link"]+'">'+article["link"]["alt"]+'</a>\
    </div>\
    </div>')


def main() :
    
    print("Started Builder ...")
    createFolderStruc(outputDir)
    layouts()


    for category in categories  :
        print(category[1])
        folderParse(category[0],category[1])

    articlesFile = open(outputDir + "articles.html")
    f=open(outputDir +"/index.html", "a+")
    f.write(html["header"])
    f.write(articlesFile.read())
    f.write(html["footer"])
    #print(articles)
main()