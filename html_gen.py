arrays = ['3d', 'code', 'cooking', 'games', 'music', 'pixel_art', 'template', 'writing']



def listGenerator (arrays, id) :
    list = '<ul>'
    for array in arrays :
        list+='<li>'+str(array)+'</li>'
    list+= '</ul>'
    return list



htmlMenu = listGenerator(arrays, 'menu')
print(htmlMenu)