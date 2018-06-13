# Trabalho Prático I: Implementar o jogo da forca
# Completar a seguinte informação:
# Nome: <Inserir nome>
# Matrícula: <Matrícula>
# jogoforca.py

# tomadas de https://duvidas.dicio.com.br/as-15-palavras-mais-engracadas-da-lingua-portuguesa/
# você pode incluir mais palavras na lista.
LISTA_PALAVRAS = ('Mequetrefe' , 'Salamaleque', 'Piripaque', 'Serelepe',
                  'Siricutico', 'Bugiganga', 'Borogodó', 'Quinquilharia',
                  'Beleléu', 'Balacobaco', 'Faniquito', 'Quiproquó', 'Pebolim',
                  'Ziquizira', 'Zunzunzum', 'Ziguezague')

# Número máximo de tentativas.
MAX_TENTATIVAS = 6

def obter_palavra():
    '''
    Retorna uma palavra aleatória da lista de palavras LISTA_PALAVRAS.
    '''
    # Eliminar esta linha uma vez que a função esteja implementada.
    raise NotImplementedError('Função obter_palavra() não implementada!')

    # seu código deve retornar um elemento de LISTA_PALAVRAS
    # palavra_secreta = ...
    # return palavra_secreta


def palavra_adivinhada(palavra_secreta, letras_usuario):
    '''
    Retorna True se os caracteres presentes na lista letras_usuario são
    suficentes para adivinhar a palavra palavra_secreta. Retorna False em outro caso.

    Parâmetros:
    * palavra_secreta: palavra a ser adivinhada.
    * letras_usuario: lista das letras que o usuário entrou até agora.
    '''

    raise NotImplementedError('Função palavra_adivinhada() não implementada!')

def tentativas_erradas(palavra_secreta, letras_usuario):
    '''
    Retorna a quantidade de letras em letras_usuario que não aparecem em
    palavra_secreta.

    Parâmetros:
    * palavra_secreta: palavra a ser adivinhada.
    * letras_usuario: lista das letras que o usuário entrou até agora.
    '''
    raise NotImplementedError('Função tentativas_erradas() não implementada!')

def mostra_adivinhadas(palavra_secreta, letras_usuario):
    '''
    Mostra que letras de palavra_secreta tem sido adivinhadas até agora e
    todas as letras entradas pelo usuário.

    Por exemplo, a saída para a palavra secreta "batatinha" e as entradas do
    usuário b, c e t deve ser do tipo:

    Palavra secreta: B _ T _ T _ _ _ _
    Letras tentadas até agora: B, C, T

    Parâmetros:
    * palavra_secreta: palavra a ser adivinhada.
    * letras_usuario: lista das letras que o usuário entrou até agora.
    '''

    raise NotImplementedError('Função mostra_adivinhadas() não implementada!')

def entra_tentativa():
    '''
    Permite ao usuário entrar uma letra. Deve garantir que a entrada não seja
    um caracter inválido (números, varias letras, signos de pontuação, etc.)
    '''

    raise NotImplementedError('Função entra_tentativa() não implementada!')

    # Perguntar ao usuário por uma letra e, se a entrada não é correta, insistir.
    # letra = ...
    # return letra


def jogo_da_forca():
    '''
    Função principal do jogo.
    '''

    print('Bem vindo ao jogo da forca.')

    while True:
        palavra_secreta = obter_palavra()

        letras_usuario = []

        while not palavra_adivinhada(palavra_secreta, letras_usuario) and \
              cuenta_tentativas_erradas(palavra_secreta, letras_usuario) < MAX_TENTATIVAS:

              mostra_adivinhadas(palavra_secreta, letras_usuario)

              restantes = MAX_TENTATIVAS - tentativas_erradas(palavra_secreta, letras_usuario)
              print('Tentativas restantes:', restantes)
              letra = entra_tentativa()
              letras_usuario.append(letra)

        mostra_adivinhadas(palavra_secreta, letras_usuario)

        if palavra_adivinhada(palavra_secreta, letras_usuario):
            print('Parabéns, você adivinhou a palavra!')
        else:
            print('¯\\_(ツ)_/¯ você perdeu.')

        print('')
        cont = input('Entre C se deseja continuar jogando.')

        if not (cont == 'C' or cont =='c'):
            break

    print('Game over.')

# chamada a função principal para executar o jogo.
jogo_da_forca()
