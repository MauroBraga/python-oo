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

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes';

class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome, ano);
        self.duracao=duracao

    def retorna_cadastro_diferenciado(self):
        pass

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes';

class Serie(Programa):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome, ano);
        self.temporadas=temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} Temporadas - {self._likes} Likes';

class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome;
        super().__init__(programas);




vingadores = Filme('vingadores - guerra infinita', 2018, 160)

tmep = Filme('Todo Mundo em pânico', 1999, 100);
atlanta = Serie('atlanta', 2018, 2)
demolidor =Serie('demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
demolidor.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep];

fim_de_semana = Playlist('Fim de semana', filmes_e_series);

print(f'Tamanho do playlist: {len(fim_de_semana)}')

for programa in fim_de_semana:
   print(programa)

print(f'Tá ou não tá? {demolidor in fim_de_semana}');