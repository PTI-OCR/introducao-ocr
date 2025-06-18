import easyocr
import cv2
from matplotlib import pyplot as plt

# Leitor OCR
reader = easyocr.Reader(['pt'])

# Carrega imagem
img = cv2.imread('imagem.png')

# OCR
resultado = reader.readtext('imagem.png')

# Desenha caixas delimitadoras na imagem
for (bbox, texto, confianca) in resultado:
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple([int(val) for val in top_left])
    bottom_right = tuple([int(val) for val in bottom_right])

    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
    cv2.putText(img, texto, (top_left[0], top_left[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

# Converte BGR para RGB para exibir corretamente
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.savefig('resultado.png')
