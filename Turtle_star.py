#Uma forma de brincar com pycharm

#veja uma estrela feita por uma tartaruga
import turtle
star = turtle.Turtle()
star.shape('turtle')
for i in range (60):
 star.forward(i)
 star.forward(150)
 star.right(144)
turtle.done()