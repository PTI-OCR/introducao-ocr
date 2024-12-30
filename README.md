
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
📺 [Tutorial: EasyOCR - Extraindo texto de imagens (Português)](https://www.youtube.com/watch?v=QX0u69qqM3k) <br>
🗒️ [Artigo: EasyOCR - A Comprehensive Guide (Inglês)](https://medium.com/@adityamahajan.work/easyocr-a-comprehensive-guide-5ff1cb850168) <br>
🗒️ [Artigo: EasyOCR - Quickstart (Inglês)](https://www.jaided.ai/easyocr/tutorial/) <br>
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
📺 [Tutorial: Domine o Reconhecimento Óptico de Caracteres com PaddleOCR: Tutorial Completo em Python (Português)](https://www.youtube.com/watch?v=kkgN3hzkSs4) <br>
📺 [Tutorial: PaddleOCR Python Demo (Inglês)](https://www.youtube.com/watch?v=0OA9RdW2saE) <br>
🗒️ [Documento: PaddleOCR Quickstart (Inglês)](https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/quick_start.en.md)<br>
🗒️ [Artigo: Optical Character Recognition using PaddleOCR in Python (Inglês)](https://mlhive.com/2023/04/optical-character-recognition-using-paddleocr-in-python)<br>
📁 [Repositório no GitHub](https://github.com/PaddlePaddle/PaddleOCR) <br>
📄 [Documentação Oficial](https://paddlepaddle.github.io/PaddleOCR/latest/en/index.html)

<br>

#### MMOCR

O **MMOCR** é uma biblioteca de código aberto baseada em **[PyTorch](https://pytorch.org)** e **[mmdetection](https://github.com/open-mmlab/mmdetection)** para detecção de texto, reconhecimento de texto e as correspondentes tarefas derivadas, incluindo extração de informações-chave. Faz parte do projeto [OpenMMLab](https://openmmlab.com).
##### Recursos

-   **Pipeline Abrangente** A caixa de ferramentas suporta não apenas detecção e reconhecimento de texto, mas também suas tarefas derivadas, como extração de informações-chave.
-   **Múltiplos Modelos** A biblioteca suporta uma ampla variedade de modelos avançados para detecção de texto, reconhecimento de texto e extração de informações chave
-  **Design Modular** O design modular do MMOCR permite que os usuários definam seus próprios otimizadores, pré-processadores de dados e componentes do modelo, como backbones, necks e heads, bem como funções de perda. 
-   **Numerosas Utilidades** A biblioteca fornece um conjunto abrangente de utilidades que podem ajudar os usuários a avaliar o desempenho dos modelos. Inclui visualizadores que permitem a visualização de imagens, ground truths e caixas delimitadoras previstas, além de uma ferramenta de validação para avaliar checkpoints durante o treinamento.

##### Avaliação
| Critério  | Detalhe  |
|---|---|
| Dificuldade  | Curva de aprendizado é consideravelmente íngreme  |
|  Comunidade |  Suporte em Inglês limitado |
|  Personalização | Estrutura altamente modular  |


##### Links
⚙️ [Tutorial prático: MMOCR Official Colab Tutorial (Inglês)](https://colab.research.google.com/github/open-mmlab/mmocr/blob/dev-1.x/demo/tutorial.ipynb)<br>
🗒️ [Artigo: Easy text extraction using MMOCR: A Comprehensive Guide (Inglês)](https://www.ikomia.ai/blog/easy-text-extraction-using-mmocr)<br>
📁 [Repositório no GitHub](https://github.com/open-mmlab/mmocr) <br>
📄 [Documentação Oficial](https://mmocr.readthedocs.io/en/latest/)

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
⚙️ [Exemplo: Tesseract API C++ Examples](https://tesseract-ocr.github.io/tessdoc/Examples_C++.html) <br>
🗒️ [Artigo: Basic OCR with Tesseract and OpenCV (Inglês)](https://medium.com/building-a-simple-text-correction-tool/basic-ocr-with-tesseract-and-opencv-34fae6ab3400) <br>
📁 [Repositório no GitHub](https://github.com/tesseract-ocr/tesseract)<br>
📄 [Documentação Oficial](https://tesseract-ocr.github.io/tessdoc/)

<br>

