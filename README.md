# builder
Another static website builder

W.I.P
the **builder.py** generates a static html site based on the project in folders

### Folder structure : 
- category_1
    - DD-MM-YY
        - featured.jpg
        - readme.md
    - DD-MM-YY
- category_2
    - DD-MM-YY
- builder.py

### Readme structure
```md
# Title

Lorem ipsum sit dolor sit amet
consecudur 

[download](itch.io)

```

### What is outputed ?
#### Structure :
- public
    - index.html
    - classic
        - index.html
        - ca1.html
        - cat2.html
        - medias
            - DD-MM-YY
                - cat.title.jpg (ex : 3d.villages)
    - lowtech
        - index.html
        - ca1.html
        - cat2.html
        - medias
            - DD-MM-YY
                - cat.title.jpg (ex : 3d.villages)


#### classic mode
#### lowtech
all images are dithered and a default system fotn is used

### Templating structure
- main.html
- article.html
- style.css
