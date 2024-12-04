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