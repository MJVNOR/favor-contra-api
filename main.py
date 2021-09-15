from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from pickle import dump

app = FastAPI()

# Aquí desempacamos nuestro modelo
nombreArchivo = "ClasificadorTweets.pkl"
modeloCargado = pickle.load(open(nombreArchivo, "rb"))
# Lo guardo en una dupla porque yo guarde mi modelo y para poder convertir el texto utilizo Tfidf
ClasificadorTweets, Tfidf_vect = modeloCargado


@app.get("/")
async def root():
    return {"message": "Hello World"}


class Tweet(BaseModel):
    texto: str


@app.post("/clasification/")
async def create_item(tweet: Tweet):
    """
    # Esta es una api que clasifica tweets a favor o en contra del gobierno de Amlo
    ### Hola 🖐 funciona enviandole un json de esta forma:
    {\n
        "texto": "Tweet a clasificar"
    }\n
    """
    # Convertimos el input a Tdfidf
    prediccionEjemplo = Tfidf_vect.transform([tweet.texto])

    # Hacemos la prediccion [[30.1454,67.436436]] ---> [[a favor, en contra]]
    resultadoPorcentaje = ClasificadorTweets.predict_proba(prediccionEjemplo)
    print(resultadoPorcentaje)
    favor = resultadoPorcentaje[0][0]
    contra = resultadoPorcentaje[0][1]
    return {"mensaje": tweet.texto, "A favor": favor, "En contra": contra}
