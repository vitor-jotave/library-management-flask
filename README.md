# Library Management System

## Descrição
Este é um aplicativo de gerenciamento de biblioteca desenvolvido em Python com Flask, para gerenciar os registros de livros. O aplicativo permite criar, atualizar, ver, e excluir livros, para cada entrada de livro, incluindo detalhes abrangentes como título, autor, editora, data de publicação, gênero, descrição, número de páginas e imagem de capa.

## Autores
- [João Vitor - 190089890](https://github.com/vitor-jotave)

## Contexto de Aplicação
O aplicativo foi desenvolvido para ser utilizado por leitores que tem vários livros e querem gerenciar o catálogo de seus livros de uma forma eficiente. O leitor adiciona os livros que ele tem na biblioteca virtual e a medida que ele vai terminando de ler, ele vai retirando os livros e deixando apenas os que ele ainda está lendo.

## Estruturas de Dados Utilizadas
O projeto utiliza uma estrutura de dados chamada Árvore AVL para gerenciar os registros de livros. A Árvore AVL foi escolhida devido à sua eficiência na realização de operações de busca, inserção e exclusão em conjuntos de dados organizados.

## Instruções de Execução

### Link Externo
1. A aplicação está disponível publicamente em `https://library-management-bice.vercel.app/`

### Ambiente Local
1. Certifique-se de ter o Python da versão 3 para cima e o Git instalado em sua máquina.
2. Clone o repositório para o seu ambiente local:

    ```bash
    git clone https://github.com/vitor-jotave/library-management-flask.git
    ```

3. Navegue até o diretório do projeto:

    ```bash
    cd library-management-flask
    ```

4. Instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ```

5. Inicie a aplicacão com o comando:

    ```bash
    flask run
    ```

5. Acesse o aplicativo em seu navegador através do link `http://localhost:5000` ou `http://localhost:8000`.

## Instruções de Uso
- Após executar o aplicativo, acesse a página principal para visualizar os registros de livros.
- Clique em Novo Livro para adicionar um novo registro.
- Você pode ver todas as informações do livro clicando em Ver Detalhes.
- Na página de Detalhes, você pode querer atualizar alguma informação, basta clicar em Atualizar.
- Você pode excluir o livro clicando em Excluir.
- A imagem de capa preferencialmente tem que ser enviada no tamanho `1043x1500`
- Utilize a funcionalidade de pesquisa para encontrar livros por título, autor ou gênero.

## Referências
- [Python Docs](https://www.python.org/doc/)
- [Árvore AVL - Canal Programação Dinâmica](https://www.youtube.com/watch?v=l8IBdCb2BWA&pp=ygUUYXJ2b3JlIGF2bCBlbSBweXRob24%3D)
- [Tutorial de Flask - Harvard CS50](https://www.youtube.com/watch?v=4o1SCMICZzo&pp=ugMICgJwdBABGAHKBQpmbGFzayBjczUw)
- [Tailwind CSS](https://tailwindui.com/)

