class Livro:
    def __init__(self, title, author, publisher, publication_date, genre, description, pages, cover_image):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
        self.genre = genre
        self.description = description
        self.pages = pages
        self.cover_image = cover_image

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'publisher': self.publisher,
            'publication_date': self.publication_date,
            'genre': self.genre,
            'description': self.description,
            'pages': self.pages,
            'cover_image': self.cover_image
        }

    @classmethod
    def from_dict(cls, book_dict):
        return cls(
            title=book_dict['title'],
            author=book_dict['author'],
            publisher=book_dict['publisher'],
            publication_date=book_dict['publication_date'],
            genre=book_dict['genre'],
            description=book_dict['description'],
            pages=book_dict['pages'],
            cover_image=book_dict['cover_image']
        )

class Node:
    def __init__(self, livro):
        self.livro = livro
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def _get_altura(self, no):
        if not no:
            return 0
        return no.altura

    def _get_balanceamento(self, no):
        if not no:
            return 0
        return self._get_altura(no.esquerda) - self._get_altura(no.direita)

    def _rotacionar_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda

        y.esquerda = z
        z.direita = T2

        z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))

        return y

    def _rotacionar_direita(self, z):
        y = z.esquerda
        T3 = y.direita

        y.direita = z
        z.esquerda = T3

        z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))

        return y

    def inserir(self, livro):
        self.raiz = self._inserir(self.raiz, livro)

    def _inserir(self, raiz, livro):
        if not raiz:
            return Node(livro)
        elif livro.title < raiz.livro.title:
            raiz.esquerda = self._inserir(raiz.esquerda, livro)
        else:
            raiz.direita = self._inserir(raiz.direita, livro)

        raiz.altura = 1 + max(self._get_altura(raiz.esquerda), self._get_altura(raiz.direita))
        balanceamento = self._get_balanceamento(raiz)

        if balanceamento > 1:
            if livro.title < raiz.esquerda.livro.title:
                return self._rotacionar_direita(raiz)
            else:
                raiz.esquerda = self._rotacionar_esquerda(raiz.esquerda)
                return self._rotacionar_direita(raiz)
        if balanceamento < -1:
            if livro.title > raiz.direita.livro.title:
                return self._rotacionar_esquerda(raiz)
            else:
                raiz.direita = self._rotacionar_direita(raiz.direita)
                return self._rotacionar_esquerda(raiz)

        return raiz

    def busca_pelo_titulo(self, title):
        return self._busca_pelo_titulo(self.raiz, title)

    def _busca_pelo_titulo(self, raiz, title):
        resultado = []
        if raiz:
            if raiz.livro.title.lower().find(title.lower()) != -1:
                resultado.append(raiz.livro)
            resultado.extend(self._busca_pelo_titulo(raiz.esquerda, title))
            resultado.extend(self._busca_pelo_titulo(raiz.direita, title))
        return resultado

    def busca_pelo_autor(self, author):
        return self._busca_pelo_autor(self.raiz, author)

    def _busca_pelo_autor(self, raiz, author):
        resultado = []
        if raiz:
            if raiz.livro.author.lower().find(author.lower()) != -1:
                resultado.append(raiz.livro)
            resultado.extend(self._busca_pelo_autor(raiz.esquerda, author))
            resultado.extend(self._busca_pelo_autor(raiz.direita, author))
        return resultado

    def busca_pelo_genero(self, genre):
        return self._busca_pelo_genero(self.raiz, genre)

    def _busca_pelo_genero(self, raiz, genre):
        resultado = []
        if raiz:
            if raiz.livro.genre.lower().find(genre.lower()) != -1:
                resultado.append(raiz.livro)
            resultado.extend(self._busca_pelo_genero(raiz.esquerda, genre))
            resultado.extend(self._busca_pelo_genero(raiz.direita, genre))
        return resultado
    
    def busca(self, title):
        return self._busca(self.raiz, title)

    def _busca(self, raiz, title):
        if not raiz or raiz.livro.title == title:
            return raiz.livro if raiz else None
        if title < raiz.livro.title:
            return self._busca(raiz.esquerda, title)
        return self._busca(raiz.direita, title)

    def get_livros(self):
        todos_livros = []
        self._travessia_inorder(self.raiz, todos_livros.append)
        return todos_livros

    def _travessia_inorder(self, raiz, visitar):
        if raiz:
            self._travessia_inorder(raiz.esquerda, visitar)
            visitar(raiz.livro)
            self._travessia_inorder(raiz.direita, visitar)

    def atualizar(self, title, novo_livro):
        self.raiz = self._remover(self.raiz, title)
        self.raiz = self._inserir(self.raiz, novo_livro)

    def remover(self, title):
        self.raiz = self._remover(self.raiz, title)
        print(f"Livro com título '{title}' removido com sucesso") # Para fins de depuração

    def _remover(self, raiz, title):
        if not raiz:
            return raiz

        if title < raiz.livro.title:
            raiz.esquerda = self._remover(raiz.esquerda, title)
        elif title > raiz.livro.title:
            raiz.direita = self._remover(raiz.direita, title)
        else:
            if not raiz.esquerda:
                temp = raiz.direita
                raiz = None
                return temp
            elif not raiz.direita:
                temp = raiz.esquerda
                raiz = None
                return temp

            temp = self._no_menor_valor(raiz.direita)
            raiz.livro = temp.livro
            raiz.direita = self._remover(raiz.direita, temp.livro.title)

        if not raiz:
            return raiz

        raiz.altura = 1 + max(self._get_altura(raiz.esquerda), self._get_altura(raiz.direita))
        balanceamento = self._get_balanceamento(raiz)

        if balanceamento > 1:
            if self._get_balanceamento(raiz.esquerda) >= 0:
                return self._rotacionar_direita(raiz)
            else:
                raiz.esquerda = self._rotacionar_esquerda(raiz.esquerda)
                return self._rotacionar_direita(raiz)
        if balanceamento < -1:
            if self._get_balanceamento(raiz.direita) <= 0:
                return self._rotacionar_esquerda(raiz)
            else:
                raiz.direita = self._rotacionar_direita(raiz.direita)
                return self._rotacionar_esquerda(raiz)

        return raiz

    def _no_menor_valor(self, raiz):
        atual = raiz
        while atual.esquerda:
            atual = atual.esquerda
        return atual

