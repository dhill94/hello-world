"""
Updated version of the ccurve program
where it will draw using random colors
"""

from turtle import Turtle, tracer, update
import random # Added to give the random colors

"""Adding a list of colors to randomize from"""
colors = ["red","blue","green","purple","orange","black","cyan","maroon"]

def cCurve(t, x1, y1, x2, y2, level):
   
   def drawLine(x1, y1, x2, y2):
      """Draws a line segment between the endpoints."""
      # Adding the segments needed for color randomization
      color = random.choice(colors)
      t.color(color)
      
      t.up()
      t.goto(x1, y1)
      t.down()
      t.goto(x2, y2)
      
   if level == 0:
      drawLine(x1, y1, x2, y2)
   else:
      xm = (x1 + x2 + y1 - y2) // 2
      ym = (x2 + y1 + y2 - x1) // 2
      cCurve(t, x1, y1, xm, ym, level - 1)
      cCurve(t, xm, ym, x2, y2, level - 1)

def main():
   level = int(input("Enter the level (0 or greater): "))
   t = Turtle()
   if level > 8:
      tracer(False)
   t.pencolor("blue")
   t.speed(0)
   t.hideturtle()
   cCurve(t, 50, -50, 50, 50, level)
   if level > 8:
      update()

if __name__ == "__main__":
   main()

