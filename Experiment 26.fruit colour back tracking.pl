% Facts
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(kiwi, green).
fruit_color(watermelon, green).
fruit_color(cherry, red).

% Rule to get fruit by color
fruit_by_color(Color, Fruit) :-
    fruit_color(Fruit, Color).

% Rule to get color by fruit
color_by_fruit(Fruit, Color) :-
    fruit_color(Fruit, Color).
