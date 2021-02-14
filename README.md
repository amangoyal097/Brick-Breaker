# Brick-Breaker

The game is made using python and is a normal terminal game which involves breaking all the bricks using the ball and the paddle with lot's of power ups and more

## Instructions

1. Open terminal and run

```
pip3 install numpy
pip3 install colorama
```

2. In the game folder run

```
python3 main.py
```

## Game Instructions

- Use A and D to move the paddle left and right respectively
- Use Space to release the ball from the paddle
- Initially 2 lives is given to the player
- Hitting the ground will result in loss of a life
- For every brick destroyed 10 points is added to the score
- Power Ups are dropped when certain bricks are destroyed
- Every power up lasts 5 seconds
- Type of Bricks

  1. <span style="color:green">#</span> Green Brick has strength 1
  2. <span style="color:yellow">#</span> Yellow Brick has strength 2
  3. <span style="color:red">#</span> Red Brick has strength 3
  4. <span style="color:cyan">#</span> Cyan Brick is the unbreakable brick
  5. <span style="color:blue">#</span> Blue Brick is the exploding brick which destroys all adjacent bricks

- Power Ups include
  1. \+ : Expand the paddle by 2 units
  2. \- : Shrink the paddle by 2 units
  3. x : Every ball present will be divided into 2
  4. F: Increases the speed of the ball
  5. G: Paddle grabs the ball and releases at will
  6. T: Through ball in which ball destroys every brick in it's path
