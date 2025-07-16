# Teste 1 – Reconhecimento Óptico de Caracteres com PaddleOCR

## Objetivo

Avaliar inicialmente a capacidade da biblioteca **PaddleOCR** de realizar a extração de texto a partir de uma imagem contendo conteúdo em **português**.

---

## Descrição do Processo

Neste teste, foi utilizado um script em Python com a biblioteca **PaddleOCR** para realizar o reconhecimento óptico de caracteres (OCR) em uma imagem de rótulo de produto (garrafa de Sprite). O processo foi dividido em etapas:

### 1. Inicialização do leitor OCR
- Uma instância da classe `PaddleOCR` foi criada com o parâmetro `lang='pt'`.
- Isso garante que o modelo esteja ajustado para reconhecer palavras em **português**, o que é fundamental para lidar com rótulos de produtos locais, mesmo que haja algumas partes do rótulo em Inglês.

### 2. Leitura da imagem
- A imagem **`imagemsprite.jpeg`** foi carregada a partir de um caminho local definido no script.
- A imagem deve estar no mesmo diretório do código ou ter seu caminho corretamente especificado.

### 3. Execução do OCR
- Foi utilizado o método `predict()` da biblioteca.
- A saída desse método contém diversas informações, incluindo:
  - `rec_texts`: lista com os textos reconhecidos;
  - `rec_scores`: lista com os respectivos valores de confiança (entre 0 e 1);
  - (Além de coordenadas de localização, que não foram utilizadas neste teste.)

### 4. Exibição dos resultados
- O script percorre todos os textos detectados e imprime:
  - O conteúdo textual identificado;
  - A pontuação de confiança, formatada com duas casas decimais.

---

## Código utilizado

O código fonte deste teste está localizado em: https://github.com/PTI-OCR/introducao-ocr/edit/main/TestesPaddleOCR/TesteUm/teste.py
---

## Imagem utilizada

- `imagemsprite.jpeg` (deve estar na mesma pasta ou referenciada no caminho correto dentro do script)

---

## Observações

- Este é um teste inicial e simplificado, com o objetivo de validar a funcionalidade básica da biblioteca PaddleOCR.
- Não houve aplicação de pré-processamento na imagem ou ajustes de contraste.
- A análise de desempenho (como precisão, taxa de erro etc.) será realizada em testes futuros.
