from pymongo import MongoClient

client = MongoClient('localhost')

db = client['rs_FuSA']

col_usuarios = db['usuarios']

col_usuarios.insert_many([
    {
        "RUT": "20724412-9",
        "nombre": "Luis",
        "apellido": "Jiménez"
    },
    {
        "RUT": "19934428-6",
        "nombre": "Andrés",
        "apellido": "Rivera"
    },
    {
        "RUT": "20849233-2",
        "nombre": "Javiera",
        "apellido": "Rojas"
    }
])

col_tipos_de_fuentes = db['tipos_de_fuentes']

col_tipos_de_fuentes.insert_many([
    {
        "tipo": "Perro",
        "archivos": []
    },
    {
        "tipo": "Gritos",
        "archivos": []
    },
    {
        "tipo": "Viento",
        "archivos": []
    },
    {
        "tipo": "Autos",
        "archivos": []
    },
    {
        "tipo": "Sirena",
        "archivos": []
    },
    {
        "tipo": "Martillo",
        "archivos": []
    }
])

col_fuentes = db['fuentes']

col_fuentes.insert_many([
    {
        "nombre_fuente": "Humanos",
        "descripcion": "Descripción de Humanos",
        "nombre_super_categoria": ""
    },
    {
        "nombre_fuente": "Música",
        "descripcion": "Descripción de Música",
        "nombre_super_categoria": ""
    },
    {
        "nombre_fuente": "Animales",
        "descripcion": "Descripción de Animales",
        "nombre_super_categoria": ""
    },
    {
        "nombre_fuente": "Climáticos y Medio ambientales",
        "descripcion": "Descripción de Climáticos y Medio ambientales",
        "nombre_super_categoria": ""
    },
    {
        "nombre_fuente": "Mecánicos",
        "descripcion": "Descripción de Mecánicos",
        "nombre_super_categoria": ""
    },
    {
        "nombre_fuente": "Vehículos",
        "descripcion": "Descripción de Vehículos",
        "nombre_super_categoria": ""
    },
    {
        "nombre_fuente": "Alertas",
        "descripcion": "Descripción de Alertas",
        "nombre_super_categoria": ""
    },
    {
        "nombre_fuente": "Perro",
        "descripcion": "Descripción de Perro",
        "nombre_super_categoria": "Animales"
    },
    {
        "nombre_fuente": "Gritos",
        "descripcion": "Descripción de Gritos",
        "nombre_super_categoria": "Humanos"
    },
    {
        "nombre_fuente": "Viento",
        "descripcion": "Descripción de Viento",
        "nombre_super_categoria": "Climáticos y Medio ambientales"
    },
    {
        "nombre_fuente": "Martillo",
        "descripcion": "Descripción de Martillo",
        "nombre_super_categoria": "Climáticos y Medio ambientales"
    },
    {
        "nombre_fuente": "Sirena",
        "descripcion": "Descripción de Sirena",
        "nombre_super_categoria": "Climáticos y Medio ambientales"
    },
    {
        "nombre_fuente": "Autos",
        "descripcion": "Descripción de Autos",
        "nombre_super_categoria": "Climáticos y Medio ambientales"
    }
])
