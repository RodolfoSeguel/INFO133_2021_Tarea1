from pymongo import MongoClient
from scipy.io.wavfile import read
from datetime import date
from random import randint

client = MongoClient('localhost')

db = client['rs_FuSA']

col_archivos_audio = db['archivos_audio']
col_segmentos = db['segmentos']

# Input de usuario

user_RUT = input("RUT de usuario: ")
ID = input("ID: ")
file_name = input("Nombre del archivo de audio: ")
exterior = True if (input("¿Sonido exterior? (s/n): ") == "s") else False
recording_date = input("Fecha de grabación (aaaa-mm-dd): ")
latitude = float(input("Latitud: "))
longitude = float(input("Longitud: "))
city = input("Ciudad: ")

# Resto de datos requeridos

i = len(file_name)
while(i>0 and file_name[i-1]!='.'):
    i-=1
file_format = file_name[i:]
rate, data = read(file_name)
audio_list = data.tolist()
duration = (len(audio_list)//rate)+1
today = str(date.today())


col_archivos_audio.insert_one({
        "ID_archivo": ID,
        "rate": rate,
        "sonido": audio_list,
        "formato": file_format,
        "exterior": exterior,
        "fecha_grabacion": recording_date,
        "duracion": duration,
        "longitud": longitude,
        "latitud": latitude,
        "ciudad": city,
        "fecha_upload": today,
        "RUT": user_RUT
})


# Segmentación del archivo de audio

i = 10
while(duration>=i):
    col_segmentos.insert_one({
        "ID_segmento": ID + '_' + str(i//10),
        "duracion": 10,
        "formato": file_format,
        "inicio": i-10,
        "fin": i,
        "ID_archivo_origen": ID
    })
    i+=10

if(duration<i):
    col_segmentos.insert_one({
        "ID_segmento": ID + '_' + str(i//10),
        "duracion": duration-i+10,
        "formato": file_format,
        "inicio": i-10,
        "fin": duration,
        "ID_archivo_origen": ID
    })


# Análisis automático (ficticio)

col_tipos_de_fuentes = db['tipos_de_fuentes']

sources = ["Autos","Sirena","Martillo","Viento","Perro","Gritos"]

fuente = sources[randint(0,len(sources)-1)]

col_tipos_de_fuentes.update_one(
    { 'tipo': fuente },
    {
        '$push': {
            'archivos': ID
        }
    }
)
