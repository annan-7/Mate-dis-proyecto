# Ciudades conectadas, peso de cada conexion, fuente de la informacion

grafooo_ciudadesss = {    #se ingresan toooodas las ciudades y su peso con el resto de ciudades
                    #solo hay de españa y pportugal
    
    "madrid": [
        (620, "barcelona"), (350, "valencia"), (530, "sevilla"), (320, "zaragoza"), (540, "malaga"), (400, "murcia"), (400, "bilbao"),
        (500, "alicante"), (400, "cordoba"), (210, "valladolid"), (590, "vigo"), (470, "gijon"), (420, "granada"), (350, "vitoria"),
    
        (590, "la coruna"), (450, "santander"), (430, "san sebastian"), (450, "oviedo"), (625, "lisboa"), (455, "porto")],
    "barcelona": [
        (620, "madrid"), (350, "valencia"), (1000, "sevilla"), (300, "zaragoza"), (1000, "malaga"), (600, "murcia"), (610, "bilbao"),
        (500, "alicante"), (850, "cordoba"), (700, "valladolid"), (1100, "vigo"), (860, "gijon"), (870, "granada"), (570, "vitoria"),
        (1100, "la coruña"), (700, "santander"), (570, "san sebastian"), (850, "oviedo"), (1250, "lisboa"), (1150, "porto")],
    
    
    "valencia": [
        (350, "madrid"), (350, "barcelona"), (650, "sevilla"), (310, "zaragoza"), (620, "malaga"), (240, "murcia"), (610, "bilbao"),
        (170, "alicante"), (510, "cordoba"), (560, "valladolid"), (950, "vigo"), (800, "gijon"), (500, "granada"), (560, "vitoria"),
        (970, "la coruña"), (700, "santander"), (630, "san sebastian"), (790, "oviedo"), (890, "lisboa"), (900, "porto")],
    
    
    "sevilla": [
        (530, "madrid"), (1000, "barcelona"), (650, "valencia"), (840, "zaragoza"), (200, "malaga"), (520, "murcia"), (860, "bilbao"),
        (600, "alicante"), (140, "cordoba"), (600, "valladolid"), (750, "vigo"), (860, "gijon"), (250, "granada"), (830, "vitoria"),
        (800, "la coruña"), (850, "santander"), (900, "san sebastian"), (850, "oviedo"), (450, "lisboa"), (575, "porto")],
    
    
    "zaragoza": [
        (320, "madrid"), (300, "barcelona"), (310, "valencia"), (840, "sevilla"), (840, "malaga"), (530, "murcia"), (300, "bilbao"),
        (480, "alicante"), (700, "cordoba"), (400, "valladolid"), (800, "vigo"), (560, "gijon"), (720, "granada"), (240, "vitoria"),
        (820, "la coruña"), (400, "santander"), (250, "san sebastian"), (540, "oviedo"), (945, "lisboa"), (850, "porto")],
    
    
    "malaga": [
        (540, "madrid"), (1000, "barcelona"), (620, "valencia"), (200, "sevilla"), (840, "zaragoza"), (400, "murcia"), (940, "bilbao"),
        (480, "alicante"), (160, "cordoba"), (730, "valladolid"), (900, "vigo"), (960, "gijon"), (130, "granada"), (900, "vitoria"),
        (1000, "la coruña"), (950, "santander"), (1000, "san sebastian"), (950, "oviedo"), (650, "lisboa"), (780, "porto")],
    
    
    "murcia": [
        (400, "madrid"), (600, "barcelona"), (240, "valencia"), (520, "sevilla"), (530, "zaragoza"), (400, "malaga"), (750, "bilbao"),
        (80, "alicante"), (400, "cordoba"), (600, "valladolid"), (1000, "vigo"), (880, "gijon"), (280, "granada"), (730, "vitoria"),
        (1000, "la coruña"), (850, "santander"), (800, "san sebastian"), (860, "oviedo"), (1030, "lisboa"), (1050, "porto")],
    
    
    "bilbao": [
        (400, "madrid"), (610, "barcelona"), (610, "valencia"), (860, "sevilla"), (300, "zaragoza"), (940, "malaga"), (750, "murcia"),
        (400, "alicante"), (750, "cordoba"), (280, "valladolid"), (650, "vigo"), (260, "gijon"), (830, "granada"), (60, "vitoria"),
        (640, "la coruña"), (100, "santander"), (110, "san sebastian"), (240, "oviedo"), (850, "lisboa"), (730, "porto")],
    
    
    "alicante": [
        (350, "madrid"), (500, "barcelona"), (170, "valencia"), (600, "sevilla"), (480, "zaragoza"), (480, "malaga"), (80, "murcia"),
        (400, "bilbao"), (500, "cordoba"), (550, "valladolid"), (980, "vigo"), (850, "gijon"), (350, "granada"), (680, "vitoria"),
        (1000, "la coruñ"), (800, "santander"), (750, "san sebastian"), (830, "oviedo"), (930, "lisboa"), (950, "porto")],
    
    
    "cordoba": [
        (400, "madrid"), (850, "barcelona"), (510, "valencia"), (140, "sevilla"), (700, "zaragoza"), (160, "malaga"), (400, "murcia"),
        (750, "bilbao"), (500, "alicante"), (500, "valladolid"), (750, "vigo"), (800, "gijon"), (160, "granada"), (740, "vitoria"),
        (830, "la coruña"), (800, "santander"), (800, "san sebastian"), (790, "oviedo"), (530, "lisboa"), (660, "porto")],
    
    
    "valladolid": [
        (210, "madrid"), (700, "barcelona"), (560, "valencia"), (600, "sevilla"), (400, "zaragoza"), (730, "malaga"), (600, "murcia"),
        (280, "bilbao"), (550, "alicante"), (500, "cordoba"), (440, "vigo"), (250, "gijon"), (620, "granada"), (240, "vitoria"),
        (450, "la coruña"), (250, "santander"), (340, "san sebastian"), (250, "oviedo"), (570, "lisboa"), (435, "porto")],
    
    
    "vigo": [
        (590, "madrid"), (1100, "barcelona"), (950, "valencia"), (750, "sevilla"), (800, "zaragoza"), (900, "malaga"), (1000, "murcia"),
        (650, "bilbao"), (980, "alicante"), (750, "cordoba"), (440, "valladolid"), (400, "gijon"), (900, "granada"), (630, "vitoria"),
        (160, "la coruña"), (500, "santander"), (700, "san sebastian"), (380, "oviedo"), (450, "lisboa"), (150, "porto")],
    
    
    "gijon": [
        (470, "madrid"), (860, "barcelona"), (800, "valencia"), (860, "sevilla"), (560, "zaragoza"), (960, "malaga"), (880, "murcia"),
        (260, "bilbao"), (850, "alicante"), (800, "cordoba"), (250, "valladolid"), (400, "vigo"), (880, "granada"), (220, "vitoria"),
        (300, "la coruña"), (180, "santander"), (270, "san sebastian"), (30, "oviedo"), (800, "lisboa"), (660, "porto")],
    
    
    "granada": [
        (420, "madrid"), (870, "barcelona"), (500, "valencia"), (250, "sevilla"), (720, "zaragoza"), (130, "malaga"), (280, "murcia"),
        (830, "bilbao"), (350, "alicante"), (160, "cordoba"), (620, "valladolid"), (900, "vigo"), (880, "gijon"), (800, "vitoria"),
        (1000, "la coruña"), (850, "santander"), (880, "san sebastian"), (870, "oviedo"), (760, "lisboa"), (890, "porto")],
    
    
    "vitoria": [
        (350, "madrid"), (570, "barcelona"), (560, "valencia"), (830, "sevilla"), (240, "zaragoza"), (900, "malaga"), (730, "murcia"),
        (60, "bilbao"), (680, "alicante"), (740, "cordoba"), (240, "valladolid"), (630, "vigo"), (220, "gijon"), (800, "granada"),
        (600, "la coruña"), (110, "santander"), (110, "san sebastian"), (200, "oviedo"), (890, "lisboa"), (760, "porto")],
    
    
    "la coruña": [
        (590, "madrid"), (1100, "barcelona"), (970, "valencia"), (800, "sevilla"), (820, "zaragoza"), (1000, "malaga"), (1000, "murcia"),
        (640, "bilbao"), (1000, "alicante"), (830, "cordoba"), (450, "valladolid"), (160, "vigo"), (300, "gijon"), (1000, "granada"),
        (600, "vitoria"), (440, "santander"), (680, "san sebastian"), (280, "oviedo"), (610, "lisboa"), (300, "porto")],
    
    
    "santander": [
        (450, "madrid"), (700, "barcelona"), (700, "valencia"), (850, "sevilla"), (400, "zaragoza"), (950, "malaga"), (850, "murcia"),
        (100, "bilbao"), (800, "alicante"), (800, "cordoba"), (250, "valladolid"), (500, "vigo"), (180, "gijon"), (850, "granada"),
        (110, "vitoria"), (440, "la coruña"), (200, "san sebastian"), (190, "oviedo"), (840, "lisboa"), (700, "porto")],
    
    
    "san sebastian": [
        (430, "madrid"), (570, "barcelona"), (630, "valencia"), (900, "sevilla"), (250, "zaragoza"), (1000, "malaga"), (800, "murcia"),
        (110, "bilbao"), (750, "alicante"), (800, "cordoba"), (340, "valladolid"), (700, "vigo"), (270, "gijon"), (880, "granada"),
        (110, "vitoria"), (680, "la coruña"), (200, "santander"), (260, "oviedo"), (920, "lisboa"), (790, "porto")],
    
    
    "oviedo": [
        (450, "madrid"), (850, "barcelona"), (790, "valencia"), (850, "sevilla"), (540, "zaragoza"), (950, "malaga"), (860, "murcia"),
        (240, "bilbao"), (830, "alicante"), (790, "cordoba"), (250, "valladolid"), (380, "vigo"), (30, "gijon"), (870, "granada"),
        (200, "vitoria"), (280, "la coruña"), (190, "santander"), (260, "san sebastian"), (770, "lisboa"), (630, "porto")],
    
    
    "lisboa": [
        (625, "madrid"), (1250, "barcelona"), (890, "valencia"), (450, "sevilla"), (945, "zaragoza"), (650, "malaga"), (1030, "murcia"),
        (850, "bilbao"), (930, "alicante"), (530, "cordoba"), (570, "valladolid"), (450, "vigo"), (800, "gijon"), (760, "granada"),
        (890, "vitoria"), (610, "la coruña"), (840, "santander"), (920, "san sebastian"), (770, "oviedo"), (310, "porto")],
    
    
    "porto": [
        (455, "madrid"), (1150, "barcelona"), (900, "valencia"), (575, "sevilla"), (850, "zaragoza"), (780, "malaga"), (1050, "murcia"),
        (730, "bilbao"), (950, "alicante"), (660, "cordoba"), (435, "valladolid"), (150, "vigo"), (660, "gijon"), (890, "granada"),
        (760, "vitoria"), (300, "la coruña"), (700, "santander"), (790, "san sebastian"), (630, "oviedo"), (310, "lisboa")]}


