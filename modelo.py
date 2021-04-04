class Programa:
    def __init__(self,nome,ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes =0

    @property
    def nome(self):
        return self._nome;
    @property
    def likes(self):
        return self._likes;

    def dar_like(self):
        self._likes += 1

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title();

class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome, ano);
        self.duracao=duracao

    def retorna_cadastro_diferenciado(self):
        pass


class Serie(Programa):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome, ano);
        self.temporadas=temporadas



vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
print(f'{vingadores.nome} - {vingadores.duracao}: {vingadores.likes}')
atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
print(f'{atlanta.nome} - {atlanta.temporadas}: {atlanta.likes}')

filmes_e_series = [vingadores, atlanta];

for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas;
    print(f'{programa.nome} - {detalhes} D - : {programa.likes}')