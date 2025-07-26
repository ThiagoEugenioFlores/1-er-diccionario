print("Bienvenido al diccionario moderno")
print("Escribe palabras que no entiendas y con mayuscula")
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "AFK": "Estar ausente ",
            "CREEPY":"Aterrador,siniestro",
            "SHEESH" : "ligera desaprobación"
            }
for i in range(5):            
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(word + " : " + meme_dict[word] )
    else:
        print("esa palabra no esta en el diccionario intenta con otra y hazlo con mayuscula")
            
