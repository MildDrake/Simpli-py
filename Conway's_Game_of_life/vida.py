""" Define funções para criar e iterar autómatos celulares.
Na versão actual, está implementado o Jogo da Vida, de Conway, incluindo
algumas variantes não-standard do mesmo. """


def celula_vive(submatriz, regra = (3, 2, 3)):
    """ Determina se uma célula vive na geração seguinte

    submatriz é uma matriz quadrada com 9 elementos, onde o elemento central é
    a célula cuja vida é determinada de acordo com a regra escolhida.
    1 denota uma célula viva, 0 denota uma célula morta.
    Seja regra = (max_vizinhos, min_vizinhos, vizinhos_para_nascer).
    Uma célula viva:
      -- morre se tiver mais de max_vizinhos vivos;
      -- morre se tiver menos de min_vizinhos vivos;
      -- permanece viva nos restantes casos.
    Uma célula morta:
      -- renasce se tiver exactamente vizinhos_para_nascer vizinhos vivos;
      -- permanece morta nos restantes casos.
    Requires:
      submatriz é uma matriz 3x3 de 0s e 1s, formatada como uma lista
        de 3 listas, cada uma com 3 elementos; 
      regra é um triplo de int em que cada int está entre 0 e 8 inclusive.
    Ensures:
      True se a célula central fica viva com a regra escolhida,
        False caso contrário.
    """

    elemento_central = submatriz[1][1]
    coordenadas = []
    max_vizinhos = regra[0]
    min_vizinhos = regra[1]
    vizinhos_para_nascer = regra[2]
    conta_vivos = 0
    conta_mortos = 0
    viva = True
    for k in range(len(submatriz)):
        for a in range(len(submatriz[k])):
            # São definidas coordenadas para assegurar que o elemento do meio
            # não é iterado
            coordenadas.append(k)
            coordenadas.append(a)
            if submatriz[k][a] == 1 and coordenadas != [1,1]:
                conta_vivos += 1
            elif submatriz[k][a] == 0 and coordenadas != [1,1]:
                conta_mortos += 1
            coordenadas.clear()
    # Dado que os critérios de sobrevivência de cada célula dependem do seu
    # estado inicial (viva ou morta), têm de ser definidos os critérios para
    # ambos casos
    if elemento_central == 1:
        if conta_vivos > max_vizinhos or conta_vivos < min_vizinhos:
            viva = False

    elif elemento_central == 0:
        if conta_vivos != vizinhos_para_nascer:
            viva = False

    return viva


def cria_mundo(linhas, colunas):
    """ Cria um novo mundo com todas as células mortas

    Requires: linhas e colunas são int, cada um maior ou igual a 2.
    Ensures: uma matriz de 0s com as dimensões indicadas; a matriz é uma lista
      de listas, em que cada lista interna tem número de elementos dado por
      colunas, e a lista externa tem número de elementos dado por linhas.
    """

    # Aqui jaz próprio
    lista_externa = []
    lista_interna = []
    # Vamos fazer as colunas
    for linha in range(0, colunas):
        lista_interna += [0]
    # Vamos fazer as linhas
    for coluna in range(0, linhas):
        lista_externa += [lista_interna.copy()]

    return lista_externa


def tamanho_mundo(mundo):
    """ Devolve o tamanho de um mundo

    Requires: mundo é uma matriz de 0s e 1s formatada como descrito no contrato
      de cria_mundo, com pelo menos 2 linhas e 2 colunas.
    Ensures: um par de int (linhas, colunas) correspondente às dimensões do
      mundo.
    """

    # Utiliza a função cria_mundo para calcular o seu tamanho
    lista_externa = mundo

    return (len(lista_externa), len(lista_externa[0]))


def atribui_valor_celula(mundo, linha, coluna, valor):
    """ Atribui um valor a uma célula

    Força a atribuição de um valor a uma célula.
    Requires:
      mundo é uma matriz de 0s e 1s formatada como descrito no contrato
        de cria_mundo, com pelo menos 2 linhas e 2 colunas;
      linha e coluna são os índices da linha e da coluna da célula que se quer
        afectar; o primeiro índice possível é 0 e o último é, respectivamente,
        (número de linhas) - 1 e (número de colunas) - 1
      valor é 0 ou 1.
    Side-effects: define o valor da célula na posição indicada.
    """

    mundo[linha][coluna] = valor


def le_valor_celula(mundo, linha, coluna):
    """ Lê o valor de uma célula

    Requires:
      mundo é uma matriz de 0s e 1s formatada como descrito no contrato
        de cria_mundo, com pelo menos 2 linhas e 2 colunas;
      linha e coluna são os índices da linha e da coluna da célula que se quer
        ler; o primeiro índice possível é 0 e o último é, respectivamente,
        (número de linhas) - 1 e (número de colunas) - 1
    Ensures: 0 ou 1, conforme o valor da célula.
    """

    valor_pedido = mundo[linha][coluna]

    return valor_pedido


def vive_prox_geracao(submatriz, regra, proxima_geracao):
    # % FUNÇÃO AUXILIAR %
    """ Verifica se uma dada célula vive na próxima geração do mundo
    e dá append desse valor (0 ou 1 consoante a condição final da célula) a uma
    lista separada que é devolvida.
    """
    if celula_vive(submatriz, regra):
        proxima_geracao.append(1)
    else:
        proxima_geracao.append(0)

    return proxima_geracao


def itera_mundo(mundo, regra = (3, 2, 3)):
    """ Actualiza o estado de todas as células do mundo, de acordo com a regra

    As condições de fronteira são periódicas, ou seja:
      mundo[i][colunas] é o mesmo que mundo[i][0]
      mundo[i][-1] é o mesmo que mundo[i][colunas - 1] (já é assim no Python)
      mundo[linhas][j] é o mesmo que mundo[0][j]
      mundo[-1][j] é o mesmo que mundo[linhas - 1][j] (já é assim no Python)     
    Requires:
      mundo é uma matriz de 0s e 1s formatada como descrito no contrato
        de cria_mundo, com pelo menos 2 linhas e 2 colunas;
      regra é um triplo de int em que cada int está entre 0 e 8 inclusive.
    Side-effects: define o valor de cada célula do mundo para a iteração
      seguinte com a regra dada, alterando esse valor onde necessário.
    """
    proxima_geracao = []

    for L in range(len(mundo)):
        for C in range(len(mundo[L])):
            # Dado que o mundo é um "loop" de ele próprio, é exigido um cuidado
            # acrescentado ao iterar sobre as suas margens, devido a tal facto,
            # no código que se segue foram elaborados todos os casos que seriam
            # problemáticos no âmbito de definir uma submatriz para a função
            # celula_vive()

            if L == 0:  # Primeira Linha
                if C == 0:  # Primeiro elemento da primeira L
                    submatriz = [
                        [mundo[-1][-1], mundo[-1][0], mundo[-1][1]],
                        [mundo[0][-1], mundo[0][0], mundo[0][1]],
                        [mundo[1][-1], mundo[1][0], mundo[1][1]]]
                    vive_prox_geracao(submatriz, regra, proxima_geracao)

                elif C not in [0, len(mundo[L]) - 1]:
                # Elementos entre os extremos da primeira L

                    submatriz = [
                        [mundo[-1][C - 1], mundo[-1][C], mundo[-1][C + 1]],
                        [mundo[0][C - 1], mundo[0][C], mundo[0][C + 1]],
                        [mundo[1][C - 1], mundo[1][C], mundo[1][C + 1]]]
                    vive_prox_geracao(submatriz, regra, proxima_geracao)

                elif C == len(mundo[L]) - 1:
                # Último elemento da primeira L

                    submatriz = [
                        [mundo[-1][-1 - 1], mundo[-1][-1],mundo[-1][0]],
                        [mundo[0][C - 1], mundo[0][C], mundo[0][0]],
                        [mundo[1][C - 1], mundo[1][C], mundo[1][0]]]
                    vive_prox_geracao(submatriz, regra, proxima_geracao)


            elif L == len(mundo) - 1:  # Última L

                if C == 0:  # Primeiro elemento da última L

                    submatriz = [
                        [mundo[L - 1][-1], mundo[L - 1][0], mundo[L - 1][1]],
                        [mundo[L][-1], mundo[L][0], mundo[L][1]],
                        [mundo[0][-1], mundo[0][0], mundo[0][1]]]
                    vive_prox_geracao(submatriz, regra, proxima_geracao)

                elif C not in [0, len(mundo[L]) - 1]:
                # Elementos entre os extremos da última L

                    submatriz = [
                        [mundo[L - 1][C - 1], mundo[L - 1][C], mundo[L - 1][C + 1]],
                        [mundo[L][C - 1], mundo[L][C], mundo[L][C + 1]],
                        [mundo[0][C - 1], mundo[0][C], mundo[0][C + 1]]]
                    vive_prox_geracao(submatriz, regra, proxima_geracao)

                elif C == len(mundo[L]) - 1:
                # Último elemento da última L

                    submatriz = [
                        [mundo[L - 1][C - 1], mundo[L - 1][C], mundo[L - 1][0]],
                        [mundo[L][C - 1], mundo[L][C], mundo[L][0]],
                        [mundo[0][-2], mundo[0][-1], mundo[0][0]]]
                    vive_prox_geracao(submatriz, regra, proxima_geracao)


            elif C in [0, len(mundo[L]) - 1] and L not in [0, len(mundo) - 1]:
            # Colunas laterais

                if C == 0:  # Primeira C

                    submatriz = [
                        [mundo[L - 1][-1], mundo[L - 1][0], mundo[L - 1][1]],
                        [mundo[L][-1], mundo[L][0], mundo[L][1]],
                        [mundo[L + 1][-1], mundo[L + 1][0], mundo[L + 1][1]]]
                    vive_prox_geracao(submatriz, regra, proxima_geracao)

                elif C == len(mundo[L]) - 1:  # Última C

                    submatriz = [
                        [mundo[L - 1][C - 1], mundo[L - 1][C], mundo[L - 1][0]],
                        [mundo[L][C - 1], mundo[L][C], mundo[L][0]],
                        [mundo[L + 1][C - 1], mundo[L + 1][C], mundo[L + 1][0]]]
                    vive_prox_geracao(submatriz, regra, proxima_geracao)


            else:
                submatriz = [
                    [mundo[L - 1][C - 1], mundo[L - 1][C], mundo[L - 1][C + 1]],
                    [mundo[L][C - 1], mundo[L][C], mundo[L][C + 1]],
                    [mundo[L + 1][C - 1], mundo[L + 1][C], mundo[L + 1][C + 1]]]
                vive_prox_geracao(submatriz, regra, proxima_geracao)

    linhas = len(mundo)
    colunas = len(mundo[0])
    final = []

    for k in range(0, linhas * colunas, colunas):
        # Vai ser feita a divisão entre linhas, dado que proxima_geracao é
        # apenas uma única lista que não se encontra dividida em sublistas
        # no seu interior
        final.append(proxima_geracao[k:k + colunas])

    # Por fim, altera-se o mundo de acordo com a lista "final" e deste modo
    # mundo será alterado de forma síncrona
    for L in range(0, linhas):
        for C in range(0, colunas):
            if final[L][C] == 0:
                atribui_valor_celula(mundo, L, C, 0)
            elif final[L][C] == 1:
                atribui_valor_celula(mundo, L, C, 1)
                

def itera_mundo_n_geracoes(n, mundo, regra = (3, 2, 3)):
    """ Itera o mundo n vezes, de acordo com a regra

    Requires:
      mundo é uma matriz de 0s e 1s formatada como descrito no contrato
        de cria_mundo, com pelo menos 2 linhas e 2 colunas;
      regra é um triplo de int em que cada int está entre 0 e 8 inclusive;
      n é um int positivo.
    Side-effects: define o valor com que cada célula do mundo fica após n
      iterações com a regra dada, alterando os valores onde necessário.
    """

    for vezes in range(n):
        itera_mundo(mundo)


def cria_mostra_mundo(mundo):
    # % FUNÇÃO AUXILIAR %
    # Esta função cria o desenho mas não o imprime, para que possa ser usada na
    # função escreve_mundo()
    desenho = ""
    desenho_linha = ""
    for lista_interna in mundo:
        # Verifica-se cada lista_interna || trata-se de separar as linhas
        for n in range(len(mundo[0])):
            # Neste 'for' vamos a cada entrada da lista determinar o seu valor
            if n == (len(mundo[0]) - 1):
                if lista_interna[n] == 0:
                    desenho_linha += " . \n"
                else:
                    desenho_linha += " X \n"
            else:
                if lista_interna[n] == 0:
                    desenho_linha += " ."
                else:
                    desenho_linha += " X"
        desenho += desenho_linha

        desenho_linha = ""
    return desenho


def mostra_mundo(mundo):
    """ Mostra o mundo no output standard (ecrã)

    Requires: mundo é uma matriz de 0s e 1s formatada como descrito no contrato
      de cria_mundo, com pelo menos 2 linhas e 2 colunas.
    Side-effects: imprime a matriz mundo no ecrã, linha a linha, representando
      cada 0 pela string ". " (ponto seguido de espaço) e
      cada 1 pela string "X " (x maiúsculo seguido de espaço);
      cada linha impressa termina com um espaço, que se segue a "." ou a "X".      
    """
    # Imprime o desenho formado na cria_mostra_mundo()
    desenho = cria_mostra_mundo(mundo)
    print(desenho)


def escreve_mundo(mundo, nome_ficheiro):
    """ Regista o mundo num ficheiro

    Comporta-se como mostra_mundo, mas escrevendo num ficheiro em vez de no
      ecrã.
    Requires:
      mundo é uma matriz de 0s e 1s formatada como descrito no contrato
        de cria_mundo, com pelo menos 2 linhas e 2 colunas;
      nome_ficheiro é uma string que representa um path válido para um ficheiro.
    Side-effects:
      se o ficheiro nome_ficheiro existir, ele é reescrito; caso contrário,
        é criado um novo ficheiro de texto com esse path;
      a função imprime a matriz mundo no ficheiro, linha a linha, representando
        cada 0 pela string ". " (ponto seguido de espaço) e
        cada 1 pela string "X " (x maiúsculo seguido de espaço);
        cada linha impressa termina com um espaço, que se segue a "." ou a "X";
      não é feita programação defensiva, pelo que o programa terminará com erro
        se não for possível escrever num ficheiro com o path indicado.
    """
    
    documento = open(nome_ficheiro, "w")
    # Aqui vamos buscar o desenho ao cria_mostra_mundo()
    por_escrever = cria_mostra_mundo(mundo)
    documento.write(por_escrever)
    
    documento.close()
    

def le_mundo(nome_ficheiro):
    """ Lê um mundo de um ficheiro

        Inicializa e devolve um novo mundo a partir de um ficheiro.
        Requires:
          nome_ficheiro é uma string que representa um path válido para um ficheiro
            de texto;
          o respectivo ficheiro está no mesmo formato indicado no contrato de
            escreve_ficheiro;
          os dados contidos no ficheiro permitem criar um matriz com pelo menos
            2 linhas e 2 colunas.
        Ensures: um mundo, ou seja, uma matriz de 0s e 1s formatada como descrito
          no contrato de cria_mundo, com pelo menos 2 linhas e 2 colunas.
        Side-effects: não é feita programação defensiva, pelo que o programa
          terminará com erro se não estiver acessível um ficheiro de texto com o
          path indicado e com formato de dados adequado.
        """

    ficheiro = open(nome_ficheiro, "r")
    mundo_lido = []
    leitura_inicial = ficheiro.readlines()
    add = []
    for k in leitura_inicial:
        for c in k:
            # add funcionará como uma lista auxiliar para fazer append
            # dos elementos de cada linha de leitura_inicial a mundo_lido em
            # cada iteração, formatando o mesmo com o número certo de linhas
            if c == ".":
                add.append(0)
            elif c == "X":
                add.append(1)
        mundo_lido.append(add.copy())
        add.clear()

    ficheiro.close()
    return mundo_lido


def anima_mundo(n, mundo, regra = (3, 2, 3), atraso = 0.9): 
    """ Mostra uma animação do mundo no output standard (ecrã)

    Requires:
      mundo é uma matriz de 0s e 1s formatada como descrito no contrato
        de cria_mundo, com pelo menos 2 linhas e 2 colunas;
      regra é um triplo de int em que cada int está entre 0 e 8 inclusive;
      n é um int positivo;
      atraso é um float positivo.
    Side-effects:
      imprime a condição inicial dada para o mundo, e imprime depois n
      sucessivos fotogramas (frames) de uma animação da evolução do mundo a
      partir dessa condição inicial, usando a regra dada; em cada frame,
      imprime a matriz mundo no ecrã, linha a linha, representando
        cada 0 pela string ". " (ponto seguido de espaço) e
        cada 1 pela string "X " (x maiúsculo seguido de espaço);
        cada linha impressa termina com um espaço, que se segue a "." ou a "X".
      Antes de ser impresso o fotograma inicial (condição inicial), o ecrã é
      apagado.
      Cada fotograma sobrepõe-se ao anterior, que foi entretanto apagado.
      O tempo entre fotogramas é dado pelo valor de atraso em segundos.
      O último fotograma não é apagado de imediato. No final, surge no ecrã a
      questão "Terminar? (carregue em return)"; após o utilizador carregar em
      return, a função termina.
      Esta função altera o estado do mundo.
    """
    import os, time
    
    os.system('CLS')
    mostra_mundo(mundo)
    time.sleep(atraso)
    for _ in range(n):
        os.system('CLS')
        itera_mundo(mundo, regra)
        mostra_mundo(mundo)
        time.sleep(atraso)
    input("Terminar? (carregue em return)")

