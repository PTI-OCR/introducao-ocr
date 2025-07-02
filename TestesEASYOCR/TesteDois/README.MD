# Teste 2 – Detecção e Visualização Gráfica com EasyOCR

## Objetivo

Realizar o reconhecimento de texto em uma imagem e apresentar **visualmente** os resultados por meio de marcações na própria imagem processada.

---

## Descrição do Processo

Neste teste, a biblioteca **EasyOCR** foi novamente utilizada para extrair textos de uma imagem contendo informações escritas. O diferencial deste teste está na **visualização gráfica**, onde os textos reconhecidos são destacados diretamente na imagem, permitindo uma análise visual da eficácia do OCR.

### Bibliotecas utilizadas:
- **EasyOCR**: reconhecimento de texto.
- **OpenCV**: manipulação e anotação da imagem.
- **Matplotlib**: conversão de cores (BGR → RGB) e exibição/salvamento da imagem final.

---

## Etapas do Processo

1. **Inicialização do leitor OCR**  
   O leitor da EasyOCR foi configurado com suporte ao idioma **português**, aumentando a precisão para textos na língua.

2. **Carregamento da imagem**  
   A imagem **`imagem.png`** foi carregada em memória com o comando:
   ```python
   cv2.imread()

3. **Execução do OCR**  
    Foi utilizado o método `readtext()` para detectar textos. O retorno dessa função inclui:
    - O conteúdo textual reconhecido
    - O grau de confiança
    - As coordenadas da bounding box onde o texto foi localizado.

4. **Desenho das caixas e textos**  
    Para cada texto detectado:
    - Uma **caixa verde** foi desenhada ao redor da região do texto;
    - O próprio texto foi **escrito acima da caixa em vermelho**, para facilitar a leitura e validação visual.

5. **Exibição do resultado**  
    Como o OpenCV utiliza o espaço de cor **BGR**, foi realizada uma conversão para **RGB** antes de exibir a imagem com o Matplotlib.  
    A imagem final foi salva com o nome: `resultado.png`

---

## Código utilizado

O código fonte deste teste está localizado em: https://github.com/PTI-OCR/introducao-ocr/new/main/TestesEASYOCR/TesteDois/projetoTesteDois.py

---

## Imagem utilizada

- `imagem.png` (deve estar na mesma pasta ou referenciada no caminho correto dentro do script)
