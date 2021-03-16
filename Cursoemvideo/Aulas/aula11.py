"""
Como trabalhar com cores no terminal!

PADRÃO ANSI
escape sequence

\033[m = Todo código para representar cor com ANSI deve ter essa sintese.
\033[     m
style , text, background
exemplo: \033[0;33;44m
onde style é o 0
     text é o 33
     background é o 44

style:
0   none
1   Bold (Negrito)
4   Underline (sublinhado)
7   Negative (inverte as cores)

text:
30  white (branco)
31  red (vermelho)
32  green (verde)
33  yellow (amarelo)
34  blue (azul)
35  violet (roxo)
36  ciano
37  gray (cinza)

background:
tudo do text só que trocando o 30 po 40


"""