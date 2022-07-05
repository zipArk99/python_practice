#nested dictionary 
from xml.dom.minidom import Element


dict2={
    'one':{1:'one',2:'two',3:'three'},
    'two':{1:'one',5:'five',6:'six'},
    'three':{5:'five',6:'six',7:{
        'one':1,'two':[
            1,2,{
                'eight':8
            }
            ],},},
}
print(dict2['three'][7]['two'][2]['eight'])
 
