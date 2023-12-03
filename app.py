from flask import Flask, render_template, request, redirect, url_for
from arvore import ArvoreAVL, Livro  # Importa as classes AVL tree e Book
import os
from werkzeug.utils import secure_filename
from helpers import allowed_file

app = Flask(__name__)
arvore = ArvoreAVL()  # Cria uma instância da arvore

UPLOAD_FOLDER = 'static/images'  # Define a pasta para armazenar imagens
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # Configura a aplicação para usar a pasta de armazenamento de imagens

# Rota para exibir a página principal com registros de livros
@app.route('/')
def display_books():
    all_books = arvore.get_livros()
    return render_template('index.html', books=all_books)

# Rota para adicionar um novo registro de livro
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        # Recupera os dados atualizados do formulário
        title = request.form['title']
        author = request.form['author']
        publisher = request.form['publisher']
        publication_date = request.form['publication_date']
        genre = request.form['genre']
        description = request.form['description']
        pages = request.form['pages']

        # Valida os dados do formulário atualizados
        if not title or not author or not publisher or not publication_date or not genre or not description or not pages:
            return "Campos Título, Autor, Editora, Data de Publicação, Gênero, Descrição e Páginas são obrigatórios."

        # Manipula o upload de imagem
        if 'cover_image' not in request.files:
            return "Nenhuma parte do arquivo"
        
        cover_image = request.files['cover_image']
        if cover_image.filename == '':
            return "Nenhum arquivo selecionado"
        
        if cover_image and allowed_file(cover_image.filename):  # Implementa a função allowed_file para tipos de arquivo de imagem
            filename = secure_filename(cover_image.filename)
            cover_image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Cria uma nova instância de Livro
            novo_livro = Livro(title, author, publisher, publication_date, genre, description, pages, f'images/{filename}')

            # Insere o novo livro na AVL tree
            arvore.inserir(novo_livro)
        
            return redirect(url_for('display_books'))  # Redireciona para a página principal após adicionar o livro
        else:
            return "Tipo de arquivo inválido. Tipos permitidos são .jpg, .jpeg, .png"

    return render_template('adicionar.html')  # Exibe o formulário para adicionar um novo livro

# Rota para exibir informações detalhadas sobre um livro
@app.route('/livro/<title>')
def detalhes(title):
    book = arvore.busca(title)
    if book:
        return render_template('detalhes.html', book=book)
    return "Livro não encontrado."

# Rota para atualizar um registro de livro
@app.route('/editar/<title>', methods=['GET', 'POST'])
def editar(title):
    if request.method == 'POST':
        # Recupera os dados atualizados do formulário
        updated_title = request.form['title']
        updated_author = request.form['author']
        updated_publisher = request.form['publisher']
        updated_publication_date = request.form['publication_date']
        updated_genre = request.form['genre']
        updated_description = request.form['description']
        updated_pages = request.form['pages']
        updated_cover_image_path = request.files['cover_image']

        # Manipula o upload de imagem
        if 'cover_image' not in request.files:
            return "Nenhuma parte do arquivo"
        
        updated_cover_image_path = request.files['cover_image']
        if updated_cover_image_path.filename == '':
            return "Nenhum arquivo selecionado"

        # Valida os dados atualizados do formulário
        if not updated_title or not updated_author or not updated_publisher or not updated_publication_date or not updated_genre or not updated_description or not updated_pages:
            return "Campos Título, Autor, Editora, Data de Publicação, Gênero, Descrição e Páginas são obrigatórios."
        
        if updated_cover_image_path and allowed_file(updated_cover_image_path.filename):  # Implementa a função allowed_file para tipos de arquivo de imagem
            filename = secure_filename(updated_cover_image_path.filename)
            updated_cover_image_path.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Cria uma instância atualizada de Livro
            updated_book = Livro(updated_title, updated_author, updated_publisher, updated_publication_date, updated_genre, updated_description, updated_pages, f'images/{filename}')

            # Atualiza o livro na AVL tree
            arvore.atualizar(title, updated_book)
        
            return redirect(url_for('display_books'))  # Redireciona para a página principal após atualizar o livro
    book = arvore.busca(title)
    if book:
        return render_template('editar.html', book=book)
    return "Livro não encontrado."

# Rota para excluir um registro de livro
@app.route('/excluir/<title>')
def excluir(title):
    book = arvore.busca(title)
    if book:
        # Obtém o caminho da imagem de capa do livro
        cover_image_path = book.cover_image

        # Exclui o livro da AVL tree
        arvore.remover(title)

        # Exclui o arquivo de imagem associado
        if cover_image_path:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], os.path.basename(cover_image_path))
            if os.path.exists(image_path):
                os.remove(image_path)
                print(f"Arquivo de imagem excluído: {image_path}") # Para fins de depuração
            else:
                print(f"Arquivo de imagem não encontrado: {image_path}") # Para fins de depuração

        return redirect(url_for('display_books'))  # Redireciona para a página principal após excluir o livro
    return "Livro não encontrado."  # Redireciona para a página principal após excluir o livro

# Rota para buscar um livro
@app.route('/busca', methods=['GET', 'POST'])
def busca():
    if request.method == 'POST':
        query = request.form['search_query']
        # Realiza operação de busca na AVL tree com base na consulta
        # Busca por Título, Autor ou Gênero e recupera livros correspondentes
        
        # Por exemplo (a lógica de busca dependerá de como você implementou a busca na AVLTree)
        resultados_busca = []  # Espaço reservado para os resultados da busca
        
        # Realiza a busca na AVL tree por livros correspondentes
        # Suponha arvore.search_by_title(query), arvore.search_by_author(query), arvore.search_by_genre(query)
        resultados_busca.extend(arvore.busca_pelo_titulo(query))
        resultados_busca.extend(arvore.busca_pelo_autor(query))
        resultados_busca.extend(arvore.busca_pelo_genero(query))
        
        return render_template('resultados.html', query=query, results=resultados_busca)
    return render_template('busca.html')

if __name__ == '__main__':
    app.run(port=8000, debug=True)