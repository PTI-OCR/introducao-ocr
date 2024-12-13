# Introdução ao OCR

<br>

## Definição

OCR é um acrónimo para o inglês Optical Character Recognition, é uma tecnologia para reconhecer caracteres a partir de um arquivo de imagem ou mapa de bits sejam eles escaneados, escritos a mão, datilografados ou impressos. Dessa forma, através do OCR é possível obter um arquivo de texto editável por um computador.

Combinado com outras tecnologias, como a inteligência artificial, empresas de diversos segmentos têm aplicado o OCR para automatizar processos de cadastro, onboarding e formalização, extraindo informações de documentos de identificação pessoal, contratos e comprovantes de residência. 

Fonte: [Wikipedia](https://pt.wikipedia.org/wiki/Reconhecimento_%C3%B3tico_de_caracteres)

<br>

## Linguagens de Programação

### Python

#### EasyOCR

**EasyOCR** é uma biblioteca moderna para reconhecimento óptico de caracteres, construída com a biblioteca **[PyTorch](https://pytorch.org)**. Ela oferece suporte a **GPUs CUDA**, possibilitando aceleração em tarefas de OCR para grandes volumes de dados ou imagens complexas.

##### Recursos

-   **Baseada em Deep Learning**: Modelos avançados para detecção e reconhecimento de texto.
-   **Suporte Multilíngue**: Compatível com mais de 80 idiomas.
-   **Aproveitamento de GPU**: Acelera a execução com CUDA (se disponível).

##### Avaliação
| Critério  | Detalhe  |
|---|---|
| Dificuldade  | Fácil de começar, requer o PyTorch configurado  |
|  Comunidade |  Pouco ativa, suporte através do Issues do GitHub |
|  Personalização | Permite treinamento com datasets específicos  |

##### Links
📁 [Repositório no GitHub](https://github.com/JaidedAI/EasyOCR) <br>
📄 [Documentação Oficial](https://www.jaided.ai/easyocr/documentation/)

<br>

#### PaddleOCR

**PaddleOCR** é uma biblioteca de OCR avançada, baseada no framework de aprendizado profundo [**PaddlePaddle**](https://github.com/PaddlePaddle/Paddle), desenvolvida pela **Baidu**. Ela é altamente eficiente e projetada para cenários complexos, com suporte para reconhecimento de texto em múltiplos idiomas, incluindo manuscritos e documentos estruturados.

##### Recursos

-   **Alta Performance**: Modelos otimizados para precisão e velocidade em detecção e reconhecimento de texto.
-   **Suporte Multilíngue**: Reconhece mais de 80 idiomas, incluindo suporte avançado para texto manuscrito.
-   **Aproveitamento de GPU**: Totalmente compatível com CUDA para aceleração de inferência.
-   **Treinamento Personalizado**: Permite treinar modelos em datasets específicos.

##### Avaliação
| Critério  | Detalhe  |
|---|---|
| Dificuldade  | Difícil de configurar  |
|  Comunidade |  Ativa, suporte através do Issues do GitHub |
|  Personalização | Permite treinamento com datasets específicos  |


##### Links

📁 [Repositório no GitHub](https://github.com/PaddlePaddle/PaddleOCR) <br>
📄 [Documentação Oficial](https://paddlepaddle.github.io/PaddleOCR/latest/en/index.html)

<br>

### C++

#### Tesseract OCR

**Tesseract OCR** é uma das bibliotecas de OCR mais conhecidas, desenvolvida pelo Google. Ela oferece suporte para reconhecimento de texto em diversos idiomas e formatos.

##### Recursos

-   **Precisão Confiável**: Focado em texto impresso com excelente suporte para idiomas diversos.
-   **Modularidade**: Permite ajustes finos em parâmetros de reconhecimento para cenários especializados.
-   **Treinamento Personalizado**: Permite treinar modelos em datasets específicos.

##### Avaliação
| Critério  | Detalhe  |
|---|---|
| Dificuldade  | Moderada, requer pré-processamento de imagens  |
|  Comunidade |  Ativa, tecnologia madura e documentada |
|  Personalização | Permite treinamento com datasets específicos  |

##### Links

📁 [Repositório no GitHub](https://github.com/tesseract-ocr/tesseract)<br>
📄 [Documentação Oficial](https://tesseract-ocr.github.io/tessdoc/)

<br>

### Java

Não existem bibliotecas escritas puramente em Java, com amplo suporte e documentação. Apenas Wrappers de bibliotecas de outras linguagens.

