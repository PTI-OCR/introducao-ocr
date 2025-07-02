# Teste 1 – Reconhecimento Óptico de Caracteres com EasyOCR

## Objetivo

Avaliar inicialmente a capacidade da biblioteca **EasyOCR** de realizar a extração de texto a partir de uma imagem contendo conteúdo em **português**.

---

## Descrição do Processo

Neste teste, foi utilizado um script em Python com a biblioteca EasyOCR para realizar o reconhecimento óptico de caracteres (OCR) em uma imagem de rótulo de produto (garrafa de Sprite). O processo foi dividido em etapas:

### 1. Inicialização do leitor OCR
- Uma instância da classe `Reader` foi criada com o parâmetro `lang_list=['pt']`.
- Isso permite que o modelo reconheça palavras específicas da **língua portuguesa**.

### 2. Leitura da imagem
- A imagem **`imagemsprite.jpeg`** foi carregada diretamente via caminho definido no script.
- Obs: o caminho pode precisar ser ajustado de acordo com a estrutura da pasta usada localmente.

### 3. Execução do OCR
- Foi utilizado o método `readtext()` da biblioteca.
- O retorno dessa função é uma **lista de tuplas** contendo:
  - `bbox`: coordenadas da **bounding box** do texto detectado;
  - `texto`: string com o texto reconhecido;
  - `confiança`: valor entre 0 e 1 representando o grau de confiança da previsão.

### 4. Exibição dos resultados
- Para cada texto detectado, o script imprime:
  - O texto reconhecido;
  - A confiança associada, formatada com duas casas decimais.

---

## Código utilizado

O código fonte deste teste está localizado em: https://github.com/PTI-OCR/introducao-ocr/new/main/TestesEASYOCR/TesteUm/projetoTesteUm.py

---

## Imagem utilizada

- `imagemsprite.jpeg` (deve estar na mesma pasta ou referenciada no caminho correto dentro do script)

---

## Observações

- Este é um teste inicial e simples, com o objetivo de verificar a funcionalidade básica da EasyOCR.
- Não houve aplicação de pré-processamento na imagem.
- A análise de desempenho (como precisão, taxa de erro etc.) será realizada em testes futuros.
