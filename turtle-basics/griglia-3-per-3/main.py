# Il programma disegna un quadrato, in senso antiorario.

import turtle

pippo = turtle.Turtle(); # crea una tartaruga, chiamata pippo


# rettangolo esterno (ho modificato le dimensioni della griglia perchè non riuscivo a visualizzare l'intero disegno nella finestra)
pippo.forward(99);
pippo.left(90);
pippo.forward(99);
pippo.left(90);
pippo.forward(99);
pippo.left(90);
pippo.forward(99);

#rettangolo interno
pippo.left(90);
pippo.forward(33);
pippo.left(90);
pippo.forward(99);
pippo.right(90);
pippo.forward(33);
pippo.right(90);
pippo.forward(99);
pippo.left(90);
pippo.forward(33);
pippo.left(90);
pippo.forward(33);
pippo.left(90);
pippo.forward(99);
pippo.right(90);
pippo.forward(33);
pippo.right(90);
pippo.forward(99);
turtle.done()
