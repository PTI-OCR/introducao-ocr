import easyocr
import Levenshtein
import os
import re


def limpar_texto(texto):
    texto = re.sub(r'[^A-Za-z0-9]', '', texto)
    return texto.upper().strip()

textosCorretos = {
    "img1.png": "AYO9034",
    "img2.png": "AZJ6991",
    "img3.png": "FBZ9581",
    "img4.png": "HPM9362",
    "img5.png": "JGZ3298",
    "img6.png": "JOG9221",
    "img7.png": "JPQ9870",
    "img8.png": "JQV5526",
    "img9.png": "JRD2238",
    "img10.png": "JSK5419",
}

reader = easyocr.Reader(['pt'])

totalCaracteres = 0
totalErros = 0

for nomeImagem, textoCorreto in textosCorretos.items():
    caminhoImagem = os.path.join("imagensTeste", nomeImagem)
    resultado = reader.readtext(caminhoImagem, detail=0)
    textoReconhecido = " ".join(resultado)

    textoReconhecidoLimpo = limpar_texto(textoReconhecido)
    textoCorretoLimpo = limpar_texto(textoCorreto)

    distancia = Levenshtein.distance(textoCorretoLimpo, textoReconhecidoLimpo)
    totalErros += distancia
    totalCaracteres += len(textoCorretoLimpo)

    print(f"{nomeImagem} → CER: {distancia/len(textoCorretoLimpo):.2%}")
    print(f"Reconhecido: {textoReconhecido}")
    print(f"Esperado:    {textoCorreto}")
    print("---")

cerMedio = totalErros / totalCaracteres
print(f"\nCharacter Error Rate (CER) média: {cerMedio:.2%}")
