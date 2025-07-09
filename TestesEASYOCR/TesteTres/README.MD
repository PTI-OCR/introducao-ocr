# Teste 3 – OCR em Tempo Real com Câmera e EasyOCR

## Objetivo

Testar a capacidade da biblioteca EasyOCR de reconhecer textos em tempo real capturados pela webcam do computador.

## Descrição do Processo

Neste experimento, foi desenvolvida uma aplicação que utiliza a câmera do dispositivo para capturar imagens em tempo real. O objetivo é avaliar o desempenho da biblioteca EasyOCR em situações dinâmicas, onde o texto pode variar em posição, iluminação e outros fatores.

### Bibliotecas utilizadas:

- **EasyOCR**: reconhecimento de texto.
- **OpenCV**: captura de vídeo e anotação dos frames.

## Etapas do Processo

1. **Inicialização do leitor OCR**  
   O leitor da EasyOCR foi configurado com suporte ao idioma português, aumentando a precisão para textos na língua.

2. **Abertura da câmera**  
   A câmera padrão do sistema foi selecionada com o comando:  
   ```python
   cv2.VideoCapture(0)

3. **Processamento em tempo real**  
   Um laço de repetição infinito (`while True`) foi utilizado para capturar cada novo frame da câmera. A cada iteração:  
   - O frame atual era processado pelo método `readtext()` da EasyOCR.  
   - Os resultados com nível de confiança superior a **0.75** foram considerados válidos e, para cada um deles:  
     - O texto reconhecido e sua respectiva confiança foram desenhados;  
     - Uma caixa verde foi adicionada ao redor da área detectada.  

4. **Exibição do vídeo anotado**  
   O vídeo com os textos detectados e destacados foi exibido em tempo real em uma janela chamada **"OCR em Tempo Real"**.

5. **Finalização**  
   O programa foi configurado para encerrar o processamento quando a tecla **"q"** fosse pressionada.  
   Ao sair, a câmera foi liberada e todas as janelas abertas pelo OpenCV foram fechadas corretamente.  

## Código utilizado

O código utilizado pode ser encontrado dentro do diretório:  
`TestesEASYOCR/TesteTres/projetoTesteTres.py`
