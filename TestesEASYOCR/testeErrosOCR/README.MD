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

### Dados de Entrada

- Um dicionário `textosCorretos` mapeia o nome de cada imagem para o texto correto da placa.  
- As imagens estão armazenadas na pasta `imagensTeste`.  

### Processamento

- O EasyOCR reconhece o texto presente nas imagens.  
- O texto reconhecido e o texto esperado são limpos pela função `limpar_texto`.  
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

Ainda há muitos erros no reconhecimento, principalmente quando o sistema tenta identificar o **nome das cidades nas placas**. Estes nomes costumam variar bastante em fonte, tamanho e posição, o que dificulta a leitura correta pelo OCR.  

Além disso, a qualidade das imagens (como baixa resolução ou presença de ruídos) compromete ainda mais o reconhecimento desses detalhes, aumentando a taxa de erro geral do sistema.

---

## Melhorias Planejadas

O objetivo principal do projeto é:  

- **Eliminar o reconhecimento dos nomes das cidades nas placas**, que geram muitos erros.  
- Focar apenas na leitura dos elementos essenciais.  
- Utilizar técnicas e bibliotecas adequadas para **segmentar ou filtrar a imagem**, permitindo reconhecer somente as informações necessárias. 
