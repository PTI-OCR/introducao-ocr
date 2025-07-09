# Relatório do Código de OCR com EasyOCR e Cálculo de CER

## Objetivo

O código tem como objetivo realizar o reconhecimento óptico de caracteres (OCR) em um conjunto de imagens que contém placas de veículos, comparar o texto reconhecido com o texto esperado e calcular o **Character Error Rate (CER)**, que é uma métrica de qualidade do reconhecimento. O CER indica a taxa de erro caractere a caractere entre o texto esperado e o texto reconhecido.

---

## Funcionamento do Código

### Importação de Bibliotecas

- **EasyOCR**: biblioteca para reconhecimento óptico de caracteres.  
- **Levenshtein**: biblioteca que utiliza o algoritmo de Vladimir Levenshtein, conhecido por comparar a semelhança entre duas strings a partir das modificações necessárias para transformar uma na outra (incluindo inserções, substituições e exclusões). Com isso, mede a distância entre essas duas strings com um número inteiro.  
- **os** e **re**: para manipulação de arquivos e limpeza de texto.  

### Função `limpar_texto`

- Remove tudo que não for letras ou números usando expressão regular.  
- Converte para letras maiúsculas e remove espaços em branco.  
- Essa padronização permite uma comparação mais justa entre os textos.  

### Função `filtrar_placa`

- Remove tudo o que não faz parte do padrão de uma placa com expressão regular.
- Usa a função `limpar_texto`para limpar o texto.
- Compara com o texto que deveria ser reconhecido.
- Caso não encontre algo que possa ser enquadrado no padrão de placa, retorna a última coisa que leu, no caso, quando lê juntamente com o nome da cidade, é a placa! Caso não consiga nem isso, retorna vazio.

### Dados de Entrada

- Um dicionário `textosCorretos` mapeia o nome de cada imagem para o texto correto da placa.  
- As imagens estão armazenadas na pasta `imagensTeste`.  

### Processamento

- O EasyOCR reconhece o texto presente nas imagens.  
- O texto reconhecido e o texto esperado são limpos pela função `limpar_texto`.
- Com a função `filtrar_placa` ele pega o texto reconhecido e coloca no formato de placa Brasileira (AAA0000).
- Calcula-se a **distância de Levenshtein** entre os dois textos limpos.  
- Essa distância representa o número de caracteres errados.  
- O **CER** daquela imagem é calculado como:  

  \[
  CER = \frac{\text{distância}}{\text{comprimento do texto correto}}
  \]

- Para cada imagem, imprime-se:  
  - O CER individual  
  - O texto reconhecido  
  - O texto esperado  

---

## Resultado

- Ao final, calcula-se o **CER médio total**, considerando todas as imagens.  
- Esse valor indica a taxa geral de erro do sistema OCR para o conjunto analisado.  

---

## Erros Identificados

Ainda há muitos erros no reconhecimento, principalmente quando o sistema tenta identificar o **nome das cidades nas placas**, que foi parcialmente resolvido com a função `filtrar_placa`. Estes nomes costumam variar bastante em fonte, tamanho e posição, o que dificulta a leitura correta pelo OCR. Além disso, a imagem das placas, devido a variação de luz e posição, podem atrapalhar, e muito, a leitura do OCR.
