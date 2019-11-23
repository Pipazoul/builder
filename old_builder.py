import os

menu = []

path = '../'

def menu (path) :
    print('Menu generator')
    listOfFiles = os.listdir(path)
    for folder in listOfFiles:
    #listOfFiles = os.listdir(path+'/'+folder)


# Gets the path to folder and the project type (image/audio/code/video)
def parseFiles(path, projectType) :
    # Will be used to generate the project list
    htmlList = ''
    listOfFiles = os.listdir(path)
    htmlList +='<h2>'+ projectType +'</h2><ul>'

    # Gets every folder from path var
    for folder in listOfFiles:
        listOfFiles = os.listdir(path+'/'+folder)
        # Gets every file from folder
        for file in listOfFiles:
            # Project type is image
            if projectType == "image" :
                if file.lower().endswith(('.png', '.jpg', '.jpeg')) :
                    htmlList+='<li><img src="'+path+'/'+folder+'/'+file+'" width="20%"></li>'
                    print(file)
            # Project type is audio
            elif projectType == 'audio' :
                if file.lower().endswith(('.mp3')) :
                    htmlList+='<li> <audio controls><source src="'+path+'/'+folder+'/'+file+'" type="audio/mpeg"></audio></li>'
                    print(file)
    htmlList +='</ul>'

    return htmlList   


# Main declarations

# Import the default html header
#header = open("header.html", "r")
#header = header.read() 


#html3dList = parseFiles('3d', 'image')
h#tmlAudioList = parseFiles('music', 'audio')

#html = '<html><head></head><body>'+header+html3dList+htmlAudioList+'</body></html>'     
#print(html)

# Writes the generated html to a file
#f = open("index.html", "w")
#f.write(html)
#f.close()
