import cv2
import easyocr

# Inicializa o OCR
reader = easyocr.Reader(['pt'])

# Abre a câmera (0 é a webcam padrão)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Falha ao capturar vídeo")
        break

    # Faz o OCR no frame atual
    resultados = reader.readtext(frame)

    # Desenha as caixas, confiança e textos detectados
    for (bbox, texto, confianca) in resultados:
        if confianca > 0.75:  # Filtra resultados com baixa confiança
            (top_left, top_right, bottom_right, bottom_left) = bbox
            top_left = tuple([int(val) for val in top_left])
            bottom_right = tuple([int(val) for val in bottom_right])

            cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
            
            # Exibe a confiança acima do texto
            confianca_str = f"{confianca:.2f}"
            cv2.putText(frame, confianca_str, (top_left[0], top_left[1] - 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            
            # Exibe o texto
            cv2.putText(frame, texto, (top_left[0], top_left[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        
    # Exibe o vídeo com as caixas e textos
    cv2.imshow('OCR em Tempo Real', frame)

    # Sai se apertar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha janelas
cap.release()
cv2.destroyAllWindows()
