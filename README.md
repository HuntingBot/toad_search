# toad_search

A methuselah search Golly script, in other words, enumerate all patterns inside a bounding box and detect its lifespan (very crudely)

## toad_search.py

Original version for Life-like rules, detect periodicity after killing gliders at the corner. It will do nothing with xWSS or other spaceships, or glider flotillas.

## random.py

toad_search but with random soup.

## tribute_search.py

Improved version. Finds lifespan with a binary approach, but only detects period 2.
