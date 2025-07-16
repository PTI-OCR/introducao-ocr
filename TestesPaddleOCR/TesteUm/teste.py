from paddleocr import PaddleOCR

# Inicializa o OCR
ocr = PaddleOCR(lang='pt')  # Português

# Caminho da imagem
caminho_imagem = 'imagemsprite.jpeg'

# Faz o OCR usando predict()
resultado = ocr.predict(caminho_imagem)
output = resultado[0]  # ou o índice correto
rec_texts = output['rec_texts']
rec_scores = output['rec_scores']


# Mostra os textos detectados
for result in resultado:
    rec_texts = result['rec_texts']
    rec_scores = result['rec_scores']
    for texto, confianca in zip(rec_texts, rec_scores):
        print(f"Texto: {texto}, Confiança: {confianca:.2f}")