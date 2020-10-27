import random
class Palavra:
    def __init__(self, palavra):
        self.palavra = sorteio()
        self.errou = []
        self.acertou = []

    def teste(self, l):
        if l in self.palavra:
            self.acertou.append(l)
        elif l not in self.palavra:
            self.errou.append(l)
        return

    def caixaP(self):
        caixa = ''
        for l in self.palavra:
            if l not in self.acertou:
                 caixa += '_'
            else:
                caixa += l
        return caixa

    def perde(self):
        self.erros = len(self.errou)
        print(forca[self.erros])

    def ganha(self):
        if '_' not in self.caixaP():
            return True
        return False

    def game(self):
        print('\nPalavra: ' + self.caixaP())
        print('\nLetras erradas: ', )
        for l in self.errou:
            print(f'{l}', end=', ')
        print()

def sorteio():
    with open("dados.txt", "r") as p:
        palavra = p.read().split()
        p.close()
        so = random.choice(palavra)
    return so.upper().strip()

def addBD():
    p = input('Digite a palavra que deseja ser adicionada: ')
    arquivo = open('dados.txt', 'r')
    palavra = arquivo.read()
    if p in palavra:
        print('\033[1;31m ERRO: Palavra já existe no banco de dados! Tente novamente!\033[m')
    else:
        with open('dados.txt', 'a') as escrever:
            escrever.write(' '+p)
            escrever.close()
            print(f'Palavra {p} gravada com sucesso!')
    return

def delBD():
    p = input('Digite a palavra que deseja ser removida: ')
    arquivo = open('dados.txt', 'r')
    palavra = arquivo.read().split()
    print(palavra)
    if p in palavra:
        palavra.remove(p)
        with open('dados.txt','w') as escrever:
            for i in palavra:
                escrever.write(i+' ')
        escrever.close()
    else:
        print('\033[1;31m ERRO: Palavra não existe no banco de dados!\033[m')
    return

def verBD():
    with open("dados.txt", "r") as ler:
        ler.seek(0,0)
        palavra = ler.read().split()
        ler.close()
        print(palavra)
    return palavra

def menu():
    print('+-' * 20)
    print('JOGO DA FORCA'.center(40))
    print('+-' * 20)
    print()
    print('MENU'.center(40))
    print('-'*40)
    escolha = int(input('[1] Jogar \n[2] Alterar banco de palavras \n[0] Sair\n'))
    print('-'*40)
    return escolha

def menu2():
    print()
    print('-'*40)
    print('Escolha uma opção:')
    escolha = int(input('[1] Adicionar palavra \n[2] Excluir palavra \n[3] Ver banco de palavras \n[0] Voltar\n'))
    print('-'*40)
    return escolha



#programa principal
forca = ['''

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']
escolha = 0
while True:
    while True:
        try:
            escolha = menu()
            break
        except:
            print('\033[1;31m ERRO: Digite um numero valido!\033[m \n')
    if 0 > escolha or escolha > 2:
        print('\033[1;31m ERRO: Digite um numero valido!\033[m \n')
    if escolha == 0:
        print('saindo...')
        break
    elif escolha == 2:
        while True:
            try:
                escolha = menu2()
                if escolha == 0:
                    break
                elif escolha == 1:
                    addBD()
                elif escolha == 2:
                    delBD()
                elif escolha == 3:
                    verBD()
            except:
                print('\033[1;31m ERRO: Digite um numero valido!\033[m \n')
            if 0 > escolha or escolha > 3:
                print('\033[1;31m ERRO: Digite um numero valido!\033[m \n')
    elif escolha == 1:
        jogo = Palavra(sorteio())
        jogo.erros = 0
        while True:
            if len(jogo.errou) == 6:
                print()
                print(f'TOTAL DE CHANCES EXCEDIDA! VOCÊ PERDEU!!! \nA PALAVRA ERA:{jogo.palavra}')
                print()
                break

            elif jogo.ganha():
                print()
                print(f'PARABÉNS! VOCÊ GANHOU!')
                print()
                break

            else:
                jogo.perde()
                jogo.game()
                letra = input('Digite uma letra: ').strip().upper()
                if letra.isnumeric():
                    print('\n\033[1;31m ERRO: Digite uma letra valida!\033[m \n')
                else:
                    if letra in jogo.acertou or letra in jogo.errou:
                        print('A Letra já foi utilizada, tente novamente!')
                    else:
                        jogo.teste(letra)
