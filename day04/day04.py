"""
--- Day 4: Ceres Search ---

"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:

..X...
.SAMX.
.A..A.
XMAS.S
.X....

The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

Take a look at the little Elf's word search. How many times does XMAS appear?

Your puzzle answer was 2591.
--- Part Two ---

The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S

Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........

In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?

"""


lines = [line.strip() for line in open("day04/input", 'r').readlines()]
xmas_count = 0
rows = len(lines)
cols = len(lines[0])  

for i in range(rows):
    for j in range(cols):
        if lines[i][j] == 'X':
            if j + 3 < cols and lines[i][j + 1] == 'M' and lines[i][j + 2] == 'A' and lines[i][j + 3] == 'S':
                xmas_count += 1
            if j - 3 >= 0 and lines[i][j - 1] == 'M' and lines[i][j - 2] == 'A' and lines[i][j - 3] == 'S':
                xmas_count += 1
            if i + 3 < rows and lines[i + 1][j] == 'M' and lines[i + 2][j] == 'A' and lines[i + 3][j] == 'S':
                xmas_count += 1
            if i - 3 >= 0 and lines[i - 1][j] == 'M' and lines[i - 2][j] == 'A' and lines[i - 3][j] == 'S':
                xmas_count += 1
            if i + 3 < rows and j + 3 < cols and lines[i + 1][j + 1] == 'M' and lines[i + 2][j + 2] == 'A' and lines[i + 3][j + 3] == 'S':
                xmas_count += 1
            if i - 3 >= 0 and j - 3 >= 0 and lines[i - 1][j - 1] == 'M' and lines[i - 2][j - 2] == 'A' and lines[i - 3][j - 3] == 'S':
                xmas_count += 1
            if i + 3 < rows and j - 3 >= 0 and lines[i + 1][j - 1] == 'M' and lines[i + 2][j - 2] == 'A' and lines[i + 3][j - 3] == 'S':
                xmas_count += 1
            if i - 3 >= 0 and j + 3 < cols and lines[i - 1][j + 1] == 'M' and lines[i - 2][j + 2] == 'A' and lines[i - 3][j + 3] == 'S':
                xmas_count += 1

print(f"part 1: {xmas_count}")


xmas_count= 0
for i in range(rows):
    for j in range(cols):
        if lines[i][j] == 'A':
            if j+1 < cols and j-1 >= 0 and i+1 < rows and i-1 >= 0:
                if (lines[i+1][j+1] == 'S' and lines[i-1][j-1] == 'M') or (lines[i+1][j+1] == 'M' and lines[i-1][j-1] == 'S'):
                    if (lines[i+1][j-1] == 'S' and lines[i-1][j+1] == 'M') or (lines[i+1][j-1] == 'M' and lines[i-1][j+1] == 'S'):
                        xmas_count += 1
                
print(f"part 2: {xmas_count}")