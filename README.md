# Projetos de Automação com Python

Este repositório reúne dois projetos desenvolvidos em Python com o objetivo de automatizar tarefas do dia a dia, aumentando a produtividade e reduzindo o trabalho manual.

##  Projetos

### 1. Mesclador de Arquivos PDF

Uma automação desenvolvida em Python para unir múltiplos arquivos PDF em um único documento de forma rápida e prática.

#### Funcionalidades

* Mescla vários arquivos PDF em um único arquivo.
* Mantém a ordem dos documentos selecionados.
* Processo automatizado e simples de executar.
* Ideal para juntar relatórios, apostilas, contratos e outros documentos.

#### Tecnologias utilizadas

* Python 3
* Biblioteca **PyPDF2** (ou outra utilizada no projeto)

---

### 2. Organizador de Arquivos

Uma automação que organiza automaticamente os arquivos de uma pasta, separando-os em diretórios de acordo com o tipo de arquivo.

#### Funcionalidades

* Identifica a extensão de cada arquivo.
* Cria pastas automaticamente quando necessário.
* Move arquivos para suas respectivas categorias.
* Facilita a organização de downloads, documentos e arquivos pessoais.

Exemplo de organização:

```text
Pasta Original/
│
├── Documentos/
│   ├── arquivo.pdf
│   ├── contrato.docx
│
├── Imagens/
│   ├── foto.jpg
│   ├── logo.png
│
├── Planilhas/
│   ├── vendas.xlsx
│
└── Vídeos/
    ├── aula.mp4
```

#### Tecnologias utilizadas

* Python 3
* Biblioteca **os**
* Biblioteca **shutil**

---

# Como executar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acesse a pasta do projeto:

```bash
cd seu-repositorio
```

3. Instale as dependências (caso existam):

```bash
pip install -r requirements.txt
```

4. Execute o projeto desejado:

```bash
python nome_do_arquivo.py
```

---

# Estrutura do projeto

```text
📦 automacoes-python
│
├── Mesclar_PDF/
│   ├── main.py
│   └── arquivos/
│
├── Organizador_Arquivos/
│   ├── main.py
│   └── arquivos/
│
└── README.md
```

---

# Objetivo

Esses projetos foram desenvolvidos com o objetivo de praticar automação utilizando Python, demonstrando como tarefas repetitivas podem ser simplificadas por meio da programação.

---

# Autor

Desenvolvido por **Thiago Leandro**.

Se este projeto foi útil para você, considere deixar uma ⭐ no repositório.
