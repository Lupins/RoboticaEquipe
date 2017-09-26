# Robô Segue Parede

### Algoritmo submetido ao processo seletivo para a equipe de robótica *NOME_NAO_DEFINIDO*, IC - UNICAMP.

* Ferramentas:
  * Python 3;
  * Vrep 3.4;

## Objetivo
Movimentar o robô do ponto inicial ao ponto final sem colisões.

## Método
O algoritmo usado é um segue parede baseado na diferença entre os sensores laterais, indíce [7] e [8].
O sensor de indíce [4] é usado para evitar colisões frontais.

## Observações
Pela função avaliativa deste código a documentação e boas práticas foram priorizadas.

## Resultados
Além do código presente foi gravado um vídeo mostrando o funcionamento do algoritmo, [Youtube](https://youtu.be/1zQgLIONleU).

## Executando o código
> * OSX:
>   * export VREP_LIB_PATH=/Applications/V-REP\ 3.4.0/programming/remoteApiBindings/lib/lib
>   * Python3 Main.py
