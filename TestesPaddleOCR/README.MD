# Manual de instalação e execução da biblioteca 

## Para Windows 10

1. **Verifique se o Python está instalado:**
   ```bash
   python --version
   ```

2. **Verifique se o pip está instalado:**
   ```bash
   pip --version
   ```

3. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   ```

4. **Ative o ambiente virtual:**
   ```bash
   venv\Scripts\activate
   ```

5. **Instale as bibliotecas necessárias:**
   ```bash
     pip install paddleocr
     pip install paddlepaddle -f https://paddlepaddle.org.cn/whl/simple
   ```

6. **Navegue até a pasta do projeto:**
   ```bash
   cd Caminho\para\a\pasta\do\projeto
   ```

7. **Execute o script Python:**
   ```bash
   python nomeDoProjeto.py
   ```
---

## Para Ubuntu 20.04+

1. **Verifique se o Python está instalado:**
   ```bash
   python3 --version
   ```

2. **Verifique se o pip está instalado:**
   ```bash
   pip3 --version
   ```

3. **Atualize os pacotes:**
   ```bash
   sudo apt update
   ```

4. **Instale o módulo de ambiente virtual:**
   ```bash
   sudo apt install python3-venv
   ```

5. **Crie o ambiente virtual:**
   ```bash
   python3 -m venv venv
   ```

6. **Ative o ambiente virtual:**
   ```bash
   source venv/bin/activate
   ```

7. **Instale as bibliotecas necessárias:**
   ```bash
     pip install paddleocr
     pip install paddlepaddle -f https://paddlepaddle.org.cn/whl/simple
   ```

8. **Acesse a pasta do projeto:**
   ```bash
   cd /caminho/para/o/projeto
   ```

9. **Execute o script Python:**
   ```bash
   python nomeDoProjeto.py
   ```

10. **Para sair do ambiente virtual:**
   ```bash
   deactivate
   ```
