import easyocr
# import cv2
# from matplotlib import pyplot as plt

# Cria o leitor especificando os idiomas
reader = easyocr.Reader(['pt'])  # 'pt' para português, pode colocar 'en' para inglês, etc.

# Caminho da imagem
caminho_imagem = 'imagemsprite.jpeg'

# Faz o OCR na imagem
resultado = reader.readtext(caminho_imagem)

# Mostra os resultados
for (bbox, texto, confianca) in resultado:
    print(f'Texto: {texto}, Confiança: {confianca:.2f}')
