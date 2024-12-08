"""
--- Day 8: Resonant Collinearity ---

You find yourselves on the roof of a top-secret Easter Bunny installation.

While The Historians do their thing, you take a look at the familiar huge antenna. Much to your surprise, it seems to have been reconfigured to emit a signal that makes people 0.1% more likely to buy Easter Bunny brand Imitation Mediocre Chocolate as a Christmas gift! Unthinkable!

Scanning across the city, you find that there are actually many such antennas. Each antenna is tuned to a specific frequency indicated by a single lowercase letter, uppercase letter, or digit. You create a map (your puzzle input) of these antennas. For example:

............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............

The signal only applies its nefarious effect at specific antinodes based on the resonant frequencies of the antennas. In particular, an antinode occurs at any point that is perfectly in line with two antennas of the same frequency - but only when one of the antennas is twice as far away as the other. This means that for any pair of antennas with the same frequency, there are two antinodes, one on either side of them.

So, for these two antennas with frequency a, they create the two antinodes marked with #:

..........
...#......
..........
....a.....
..........
.....a....
..........
......#...
..........
..........

Adding a third antenna with the same frequency creates several more antinodes. It would ideally add four antinodes, but two are off the right side of the map, so instead it adds only two:

..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......#...
..........
..........

Antennas with different frequencies don't create antinodes; A and a count as different frequencies. However, antinodes can occur at locations that contain antennas. In this diagram, the lone antenna with frequency capital A creates no antinodes but has a lowercase-a-frequency antinode at its location:

..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......A...
..........
..........

The first example has antennas with two different frequencies, so the antinodes they create look like this, plus an antinode overlapping the topmost A-frequency antenna:

......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#.

Because the topmost A-frequency antenna overlaps with a 0-frequency antinode, there are 14 total unique locations that contain an antinode within the bounds of the map.

Calculate the impact of the signal. How many unique locations within the bounds of the map contain an antinode?

"""


data = open('input','r').readlines()
data = [x.strip() for x in data]

rows = len(data)
cols = len(data[0])
output = [['.' for _ in range(len(data[j]))] for j in range(len(data))]

def isInside(x, y):
    return x >= 0 and x < rows and y >= 0 and y < cols
    

for i in range(rows):
    for j in range(cols):
        if data[i][j] != '.':
            symbol = data[i][j]
            for k in range(rows):
                for l in range(cols):
                    if data[k][l] == symbol and (i != k or j != l):
                        delta_x = i -k
                        delta_y = j - l
                        try:
                            new_x1 = i + delta_x
                            new_y1 = j + delta_y
                            new_x2 = k - delta_x
                            new_y2 = l - delta_y
                            if isInside(new_x1, new_y1):
                                output[new_x1][new_y1] = '#'
                            if isInside(new_x2, new_y2):
                                output[new_x2][new_y2] = '#'
                        except IndexError:
                            continue
                        
total_ones = 0
for i in range(rows):
    for j in range(cols):
        if output[i][j] == '#':
            total_ones += 1
        print(output[i][j], end='')
    print()
print(f"part1: {total_ones}")


"""
--- Part Two ---

Watching over your shoulder as you work, one of The Historians asks if you took the effects of resonant harmonics into your calculations.

Whoops!

After updating your model, it turns out that an antinode occurs at any grid position exactly in line with at least two antennas of the same frequency, regardless of distance. This means that some of the new antinodes will occur at the position of each antenna (unless that antenna is the only one of its frequency).

So, these three T-frequency antennas now create many antinodes:

T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
..........

In fact, the three T-frequency antennas are all exactly in line with two antennas, so they are all also antinodes! This brings the total number of antinodes in the above example to 9.

The original example now has 34 antinodes, including the antinodes that appear on every antenna:

##....#....#
.#.#....0...
..#.#0....#.
..##...0....
....0....#..
.#...#A....#
...#..#.....
#....#.#....
..#.....A...
....#....A..
.#........#.
...#......##

Calculate the impact of the signal using this updated model. How many unique locations within the bounds of the map contain an antinode?

"""

output = [['.' for _ in range(len(data[j]))] for j in range(len(data))]


for i in range(rows):
    for j in range(cols):
        if data[i][j] != '.':
            symbol = data[i][j]
            for k in range(rows):
                for l in range(cols):
                    if data[k][l] == symbol and (i != k or j != l):
                        delta_x = i -k
                        delta_y = j - l
                        d = 0
                        while d < rows:
                            new_x1 = i + d*delta_x
                            new_y1 = j + d*delta_y
                            new_x2 = k - d*delta_x
                            new_y2 = l - d*delta_y
                            if isInside(new_x1, new_y1):
                                output[new_x1][new_y1] = '#'
                            if isInside(new_x2, new_y2):
                                output[new_x2][new_y2] = '#'
                            d += 1
total_ones = 0
for i in range(rows):
    for j in range(cols):
        if output[i][j] == '#':
            total_ones += 1
        print(output[i][j], end='')
    print()
print(f"part2: {total_ones}")
