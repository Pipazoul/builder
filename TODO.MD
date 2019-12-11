
# TODO

## Integrate template 
- [x] html / css

- Create a main entry point
    - [ ] builder.py
        - [x] load config file
            - [x] path variable
            - [x] lowtech = false
        - [x] load layouts :
            - [x] html object (html.header html.footer html.body)
        - [ ] folder parsing :
            - [x] articles array
            - [ ] Articles type :
                - Image
                - Text (with choosen default image)
        - [ ] html gen
            - [ ] get layout
                - [ ] Filter articles per date to mix every category
                - [ ] foreach article append to html.body
                - [ ] write 
    - [x] config.yml :
        - [x] lowtechmode : true/false
        - [x] path to articles
## ClassicMode
- [ ] Generate layout with content inside
- [ ] Generate homepage
    - [ ] Display all images
    - [ ] Display Date
    - [ ] Display title
    - [ ] Display content
    - [ ] output in /public folder

## Debug 
- [ ] The last image project is not displayed (replaced by the fractal image)
- [ ] The script cant write without sudo


## Features for 0.1
A public folder generated
A Homepage :
- [ ] Layout
- [ ] Article : 
    - [ ] Date
    - [ ] Image
    - [ ] Title
    - [ ] Content
- [ ] End Layout

In two version classic and lowtech


## Features for 0.2
DATE ORDERING
IMAGE COMPRESSION
MUSIC PLAYER
MENU
RESPONSIVE WEBSITE


## In the future
EXCLUDE FOLDERS 
FTP sync 
Music compression :
    - 320kb/s classic mode
    - 96 kb/s lowtech mode ?
VIDEO PLAYER
TEMPLATING SYSTEM ?
PAGES ?