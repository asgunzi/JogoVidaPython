# JogoVidaPython
Implementação em Python do Jogo da Vida de John Conway


O matemático John Conway faleceu na semana passada, vítima do Coronavírus.
![](https://ideiasesquecidas.files.wordpress.com/2020/04/john_h_conway_2005_cropped.jpg)


Ele foi o criador do “Jogo da Vida”, o primeiro exemplo de autômato celular. É bastante interessante e lúdico.

![](https://ideiasesquecidas.files.wordpress.com/2020/04/conway01.gif?w=640)
O jogo faz a seguinte análise:

    Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.
    Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.
    Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.
    Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado para a próxima geração.

Um pouco da história

O conceito de autômato celular foi criado pela genial dupla John Von Neumann e Stanislaw Ulam, durante o Projeto Manhattan, que criou a primeira bomba atômica. Von Neumann tinha interesse em entender organismos autorreplicáveis.

John Conway inventou o Jogo da Vida enquanto um estudante de graduação. Ele gostava de jogos, e já tinha dominado vários quando quis criar um novo. Ele se inspirou nos trabalhos de Neumann e Ulam.
![](https://ideiasesquecidas.files.wordpress.com/2020/04/floorgoban.jpg?w=1024)

Ele fazia simulações num tabuleiro de Go, aquele jogo oriental que tem um tabuleiro de 19 x 19 quadrados e peças pretas e brancas, numa época que não tinha computador.

Dependendo das regras, a população pode explodir para a superpopulação, ou para a extinção total.

As regras do jogo acima foram cuidadosamente escolhidas, para entrar em equilíbrio. Rodando várias iterações, começam a surgir alguns padrões.

O Jogo da Vida ficou famoso em 1970, após artigo de Martin Gardner na Scientific American. Gardner é um dos maiores divulgadores de puzzles de todos os tempos (tenho uns 5 livros dele), e Conway enviava cartas frequentemente para contribuir.

![](https://ideiasesquecidas.files.wordpress.com/2020/04/conway02.gif?w=640)

Anos depois, em 2002, o matemático Stephen Wolfram (do Wolfram Alpha) publicou um estudo detalhado de autômatos celulares em geral, com classificação de tipos, regras, etc.

Esta técnica pode ter utilidade em diversas áreas do conhecimento: modelos biológicos, economia, etc. Inclusive, há alguns modelos de transmissão de Coronavírus baseados em autômato celular.

Em homenagem a Conway, fiz duas implementações do Jogo da Vida. Uma em Python e outra em Excel. É um bom exercício, para um nível intermediário de programação. Seguem alguns estudos.
![](https://ideiasesquecidas.files.wordpress.com/2020/04/gravar-_2.gif?w=1024)

![](https://ideiasesquecidas.files.wordpress.com/2020/04/conway03.gif?w=640)

Vide links a seguir.

https://github.com/asgunzi/JogodaVidaExcel

https://github.com/asgunzi/JogoVidaPython

https://mathworld.wolfram.com/CellularAutomaton.html

https://guiadoestudante.abril.com.br/estudo/conheca-john-conway-o-matematico-que-criou-o-jogo-da-vida

https://en.wikipedia.org/wiki/Cellular_automaton

https://mathworld.wolfram.com/ElementaryCellularAutomaton.html
