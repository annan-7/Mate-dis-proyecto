# Ciudades conectadas, peso de cada conexion, fuente de la informacion

grafo_ciudades = {    #se ingresan todas las ciudades y su peso el cual representa los KM con el resto de ciudades
    "madrid": [
        (162, "valladolid"), (315, "zaragoza"), (302, "valencia"), 
        (360, "alicante"), (400, "murcia"), (400, "cordoba")
    ],

    "valladolid": [
        (210, "madrid"), (240, "vitoria"), (250, "santander"), 
        (250, "oviedo"), (450, "la_coruña"), (440, "vigo")
    ],

    "vigo": [
        (150, "porto"), (160, "la_coruña"), (440, "valladolid")
    ],
    "la_coruña": [
        (160, "vigo"), (450, "valladolid"), (280, "oviedo")
    ],
    "oviedo": [
        (250, "valladolid"), (280, "la_coruña"), (30, "gijon"), (190, "santander")
    ],
    "gijon": [
        (30, "oviedo"), (180, "santander")
    ],
    "santander": [
        (250, "valladolid"), (190, "oviedo"), (180, "gijon"), (100, "bilbao")
    ],
    "bilbao": [
        (100, "santander"), (60, "vitoria"), (110, "san_sebastian"), (300, "zaragoza")
    ],
    "vitoria": [
        (60, "bilbao"), (110, "san_sebastian"), (240, "zaragoza"), (240, "valladolid")
    ],
    "san_sebastian": [
        (110, "bilbao"), (110, "vitoria"), (250, "zaragoza")
    ],
    
    "zaragoza": [
        (320, "madrid"), (300, "barcelona"), (310, "valencia"), 
        (300, "bilbao"), (240, "vitoria"), (250, "san_sebastian")
    ],
    "barcelona": [
        (300, "zaragoza"), (350, "valencia")
    ],
    "valencia": [
        (350, "madrid"), (310, "zaragoza"), (350, "barcelona"), (170, "alicante")
    ],
    "alicante": [
        (350, "madrid"), (170, "valencia"), (80, "murcia")
    ],
    
    "murcia": [
        (400, "madrid"), (80, "alicante"), (280, "granada")
    ],
    "granada": [
        (280, "murcia"), (130, "malaga"), (160, "cordoba")
    ],
    "malaga": [
        (130, "granada"), (160, "cordoba"), (200, "sevilla")
    ],
    "cordoba": [
        (400, "madrid"), (160, "granada"), (160, "malaga"), (140, "sevilla")
    ],
    "sevilla": [
        (140, "cordoba"), (200, "malaga"), (450, "lisboa")
    ],
    "lisboa": [
        (450, "sevilla"), (310, "porto")
    ],
    "porto": [
        (310, "lisboa"), (150, "vigo")
    ]
}

