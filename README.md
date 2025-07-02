
# Introdução ao OCR

<br>

## Definição

OCR (Reconhecimento Óptico de Caracteres) é uma tecnologia que permite a conversão automática de textos presentes em imagens digitais, documentos escaneados ou fotografias em texto editável e pesquisável. Por meio do OCR, é possível transformar documentos físicos, como livros, contratos, cheques e formulários, em arquivos digitais que podem ser manipulados em softwares de edição ou armazenados para buscas futuras.

Essa tecnologia identifica caracteres — letras, números, símbolos — a partir dos pixels da imagem, interpretando-os para gerar uma versão textual. Softwares avançados de OCR também conseguem preservar a formatação, fonte e tamanho do texto original, facilitando a reutilização e acessibilidade dos documentos digitalizados.

Apesar da precisão crescente, o OCR não é perfeito e a revisão humana é fundamental para garantir a correção dos textos gerados, especialmente em documentos sensíveis. O funcionamento do OCR envolve técnicas como reconhecimento de padrões e detecção de características específicas dos caracteres, além de inteligência artificial e aprendizado de máquina nos sistemas mais modernos. Essa tecnologia é amplamente utilizada em diversas áreas, incluindo digitalização de arquivos históricos, automação de processos administrativos e suporte a pessoas com deficiência visual. 

**Fontes:**  
- https://www.explainthatstuff.com/how-ocr-works.html  
- https://techterms.com/definition/ocr  
- https://www.necc.mass.edu/wp-content/uploads/accessible-media-necc/uncategorized/resources/What-is-OCR.pdf  

<br>

---

## Pesquisa e Análise de Bibliotecas OCR

### Pesquisas realizadas

Bernardo, o antigo bolsista, realizou uma pesquisa preliminar sobre as principais bibliotecas e linguagens compatíveis com OCR. Pretendo ampliar essa pesquisa, comparando bibliotecas e linguagens entre si com base em critérios como: percentual de erro, facilidade de uso, comunidade ativa e capacidade de personalização.


### Linguagens de Programação e principais bibliotecas

### ● Python

#### 1.**EasyOCR**  
Biblioteca construída sobre PyTorch, uma das mais utilizadas em Python. É uma das soluções mais modernas, com suporte para GPUs CUDA, aproveitando o poder computacional das placas gráficas.
<br>

**Principais recursos:**  
- Programação baseada em Deep Learning, permitindo reconhecimento de padrões complexos.  
- Suporte multilíngue, capaz de identificar caracteres em vários idiomas.  
- Aproveitamento de GPU via CUDA.  
<br>

**Avaliação preliminar:**  
| Critério            | Detalhe                          |
|---------------------|---------------------------------|
| % de erro           | Pesquisas futuras                |
| Dificuldade         | Fácil para começar, mas requer PyTorch configurado |
| Comunidade          | Pouco ativa, suporte principalmente via GitHub Issues |
| Personalização      | Permite treinamento com datasets específicos |
<br>

**Fontes utilizadas:**  
- https://www.youtube.com/watch?v=QX0u69qqM3k  
- https://medium.com/@adityamahajan.work/easyocr-a-comprehensive-guide-5ff1cb850168  
- https://www.jaided.ai/easyocr/tutorial/  
- https://github.com/JaidedAI/EasyOCR  
- https://www.jaided.ai/easyocr/documentation/

---

#### 2. **PaddleOCR**  
Biblioteca baseada no framework PaddlePaddle, desenvolvido pela Baidu. Considerada mais avançada, é recomendada para cenários complexos, como textos manuscritos e documentos estruturados.
<br>

**Principais recursos:**  
- Alta performance com modelos otimizados para maior precisão e velocidade.  
- Suporte multilíngue para mais de 80 idiomas.  
- Compatível com GPU CUDA.  
- Permite treinamento personalizado com datasets específicos.  
<br>

**Avaliação preliminar:**  
| Critério            | Detalhe                          |
|---------------------|---------------------------------|
| % de erro           | Pesquisas futuras                |
| Dificuldade         | Difícil de configurar            |
| Comunidade          | Ativa, suporte via GitHub Issues |
| Personalização      | Permite treinamento com datasets específicos |
<br>

**Fontes utilizadas:**  
- https://www.youtube.com/watch?v=kkgN3hzkSs4  
- https://www.youtube.com/watch?v=0OA9RdW2saE  
- https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/quick_start.en.md  
- https://mlhive.com/2023/04/optical-character-recognition-using-paddleocr-in-python  
- https://github.com/PaddlePaddle/PaddleOCR  
- https://paddlepaddle.github.io/PaddleOCR/latest/en/index.html

---

#### 3. **MMOCR**  
Biblioteca de código aberto baseada em PyTorch e MMDetection, integrante do projeto OpenMMLab. Suporta detecção, reconhecimento e tarefas derivadas como extração de informações-chave.
<br>

**Principais recursos:**  
- Pipeline abrangente com múltiplos modelos para detecção e reconhecimento.  
- Design modular para customização profunda.  
- Utilitários para avaliação de desempenho.  
<br>

**Avaliação preliminar:**  
| Critério            | Detalhe                          |
|---------------------|---------------------------------|
| % de erro           | Pesquisas futuras                |
| Dificuldade         | Alta                            |
| Comunidade          | Suporte em inglês, comunidade limitada |
| Personalização      | Estrutura altamente modular      |
<br>

**Fontes utilizadas:**  
- https://colab.research.google.com/github/open-mmlab/mmocr/blob/dev-1.x/demo/tutorial.ipynb  
- https://www.ikomia.ai/blog/easy-text-extraction-using-mmocr  
- https://github.com/open-mmlab/mmocr  
- https://mmocr.readthedocs.io/en/latest/

---

### ● C++

#### 1. **Tesseract OCR**  
Biblioteca desenvolvida pelo Google, uma das mais famosas para OCR, com suporte para múltiplos idiomas e formatos.
<br>

**Principais recursos:**  
- Alta precisão, especialmente para texto impresso.  
- Modularidade para ajustes específicos.  
- Permite treinamento com datasets personalizados.  
<br>

**Avaliação preliminar:**  
| Critério            | Detalhe                          |
|---------------------|---------------------------------|
| % de erro           | Pesquisas futuras                |
| Dificuldade         | Moderada, requer pré-processamento de imagens |
| Comunidade          | Ativa, tecnologia madura        |
| Personalização      | Permite treinamento com datasets específicos |
<br>

**Fontes utilizadas:**  
- https://tesseract-ocr.github.io/tessdoc/Examples_C++.html  
- https://medium.com/building-a-simple-text-correction-tool/basic-ocr-with-tesseract-and-opencv-34fae6ab3400  
- https://github.com/tesseract-ocr/tesseract  
- https://tesseract-ocr.github.io/tessdoc/

---

## Próximos passos

Com base na análise preliminar das principais bibliotecas de OCR, os próximos passos visam aprofundar a avaliação das tecnologias selecionadas, tanto em termos de desempenho quanto de aplicabilidade prática. Até o momento, foram realizados testes iniciais utilizando a biblioteca **EasyOCR**, cujos resultados estão documentados na pasta https://github.com/PTI-OCR/introducao-ocr/tree/main/TestesEASYOCR deste repositório.

A partir dessa base, as próximas etapas do projeto incluem:

1. **Medição do percentual de erro nas demais bibliotecas**  
   - Repetir os testes aplicados à EasyOCR com outras bibliotecas, como **PaddleOCR**, **MMOCR** e **Tesseract**.  
   - Calcular métricas de desempenho, como o *CER* (*Character Error Rate*), utilizando um conjunto padronizado de imagens.

2. **Avaliação da facilidade de uso**  
   - Documentar o processo de instalação, configuração e testes iniciais de cada biblioteca.  
   - Classificar o nível de dificuldade com base em critérios objetivos: documentação, requisitos técnicos, etc.

3. **Análise da comunidade e suporte**  
   - Investigar a atividade das comunidades relacionadas (GitHub, fóruns, repositórios oficiais).  
   - Avaliar frequência de atualizações, número de contribuidores, etc.

4. **Testes de personalização e treinamento com datasets específicos**  
   - Verificar a viabilidade de treinar modelos personalizados com bases em dados obtidos online, com foco especial em placas de carro e textos em português.  
   - Avaliar as ferramentas e recursos oferecidos por cada biblioteca para customização.

5. **Criação de uma matriz comparativa**  
   - Guardar os dados obtidos em uma tabela comparativa entre as bibliotecas analisadas.  
   - Destacar pontos fortes e fracos de cada solução em termos de desempenho, usabilidade, personalização e suporte.

---

### Estudo de Repositórios Complementares

Além da análise das bibliotecas principais (EasyOCR, PaddleOCR, MMOCR e Tesseract), estou iniciando uma pesquisa exploratória sobre projetos complementares disponíveis no GitHub, especialmente mantidos pela organização **NanoNets**, que demonstram implementações práticas e estratégias de integração com OCR em Python. Estes estudos visam identificar boas práticas, arquiteturas e possibilidades de extensão do projeto.

Repositórios em análise inicial:

- https://github.com/NanoNets/ocr-python  
  Demonstração básica de OCR utilizando a API da NanoNets.

- https://github.com/NanoNets/docext
  Projeto voltado para extração de informações estruturadas em documentos digitalizados, com foco em tabelas e campos.

- https://github.com/NanoNets/ocr-with-tesseract
  Integração do Tesseract OCR com Python para digitalização de documentos. Inclui pré-processamento de imagens.

Objetivos desta análise:

- Observar estruturas de projeto e padrões de desenvolvimento adotados.  
- Investigar técnicas de pré e pós-processamento utilizadas nos exemplos.  
- Avaliar a possibilidade de incorporar ideias ou trechos desses projetos no escopo atual do projeto.

Esta é uma etapa preliminar de estudo. A partir do estudo, trechos relevantes podem ser adaptados, citados ou referenciados no desenvolvimento do projeto principal.

