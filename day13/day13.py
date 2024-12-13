"""
--- Day 13: Claw Contraption ---

Next up: the lobby of a resort on a tropical island. The Historians take a moment to admire the hexagonal floor tiles before spreading out.

Fortunately, it looks like the resort has a new arcade! Maybe you can win some prizes from the claw machines?

The claw machines here are a little unusual. Instead of a joystick or directional buttons to control the claw, these machines have two buttons labeled A and B. Worse, you can't just put in a token and play; it costs 3 tokens to push the A button and 1 token to push the B button.

With a little experimentation, you figure out that each machine's buttons are configured to move the claw a specific amount to the right (along the X axis) and a specific amount forward (along the Y axis) each time that button is pressed.

Each machine contains one prize; to win the prize, the claw must be positioned exactly above the prize on both the X and Y axes.

You wonder: what is the smallest number of tokens you would have to spend to win as many prizes as possible? You assemble a list of every machine's button behavior and prize location (your puzzle input). For example:

Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279

This list describes the button configuration and prize location of four different claw machines.

For now, consider just the first claw machine in the list:

    Pushing the machine's A button would move the claw 94 units along the X axis and 34 units along the Y axis.
    Pushing the B button would move the claw 22 units along the X axis and 67 units along the Y axis.
    The prize is located at X=8400, Y=5400; this means that from the claw's initial position, it would need to move exactly 8400 units along the X axis and exactly 5400 units along the Y axis to be perfectly aligned with the prize in this machine.

The cheapest way to win the prize is y_b pushing the A button 80 times and the B button 40 times. This would line up the claw along the X axis (because 80*94 + 40*22 = 8400) and along the Y axis (because 80*34 + 40*67 = 5400). Doing this would cost 80*3 tokens for the A presses and 40*1 for the B presses, a total of 280 tokens.

For the second and fourth claw machines, there is no combination of A and B presses that will ever win a prize.

For the third claw machine, the cheapest way to win the prize is y_b pushing the A button 38 times and the B button 86 times. Doing this would cost a total of 200 tokens.

So, the most prizes you could possibly win is two; the minimum tokens you would have to spend to win all (two) prizes is 480.

You estimate that each button would need to be pressed no more than 100 times to win a prize. How else would someone be expected to play?

Figure out how to win as many prizes as possible. What is the fewest tokens you would have to spend to win all possible prizes?

"""

from fractions import Fraction


A_COST = 3
B_COST = 1

data = open('input.txt').readlines()
claw_machines = []
prizes = []
for i in range(len(data)):
    if 'Button A' in data[i]:   
        data[i] = data[i].strip()
        x_index = data[i].find('X+')
        comma_index = data[i].find(',')
        x = int(data[i][x_index+2:comma_index])
        y_index = data[i].find('Y+')
        y = int(data[i][y_index+2:])
        claw_machines.append(('A', x, y))
    elif 'Button B' in data[i]:
        data[i] = data[i].strip()
        x_index = data[i].find('X+')
        comma_index = data[i].find(',')
        x = int(data[i][x_index+2:comma_index])
        y_index = data[i].find('Y+')
        y = int(data[i][y_index+2:])
        claw_machines.append(('B', x, y))
    elif 'Prize' in data[i]:
        data[i] = data[i].strip()
        x_index = data[i].find('X=')
        comma_index = data[i].find(',')
        x = int(data[i][x_index+2:comma_index])
        y_index = data[i].find('Y=')
        y = int(data[i][y_index+2:])
        prizes.append((x, y))
    else:
        # Blank line
        continue

    
def solve(x_prize, y_prize, x_a, y_a, x_b, y_b):
    # k1 * x_a + k2 * x_b = x_prize
    # k1 * y_a + k2 * y_b = y_prize
    # k1<=100 and k2 <= 100
    # k1, k2, k3, k4 >= 0
    k1 = 0
    k2 = 0
    for i in range(100):
        for j in range(100):
            if i*x_a + j*x_b == x_prize and i*y_a + j*y_b == y_prize:
                k1 = i
                k2 = j
                break
    if k1 == 0 and k2 == 0:
        return 0
    else:
        return k1*A_COST + k2*B_COST
    
    
    
    
tokens = 0
for i in range(len(prizes)):
    x_prize = prizes[i][0]
    y_prize = prizes[i][1]
    
    x_a = claw_machines[i*2][1]
    y_a = claw_machines[i*2][2]
    x_b = claw_machines[i*2+1][1]
    y_b = claw_machines[i*2+1][2]
    
    # print(f"Button A: x+{x_a}, y+{y_a}")
    # print(f"Button B: x+{x_b}, y+{y_b}")
    # print(f"prize at: x={x_prize}, y={y_prize}")
    
    tokens += solve(x_prize, y_prize, x_a, y_a, x_b, y_b)
    
print(f"tokens (part1): {tokens}")

"""
As you go to win the first prize, you discover that the claw is nowhere near where you expected it would be. Due to a unit conversion error in your measurements, the position of every prize is actually 10000000000000 higher on both the X and Y axis!

Add 10000000000000 to the X and Y position of every prize. After making this change, the example above would now look like this:

Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=10000000008400, Y=10000000005400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=10000000012748, Y=10000000012176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=10000000007870, Y=10000000006450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=10000000018641, Y=10000000010279

Now, it is only possible to win a prize on the second and fourth claw machines. Unfortunately, it will take many more than 100 presses to do so.

Using the corrected prize coordinates, figure out how to win as many prizes as possible. What is the fewest tokens you would have to spend to win all possible prizes?
"""

for i in range(len(prizes)):
    prizes[i] = (prizes[i][0] + 10000000000000, prizes[i][1] + 10000000000000)
    
# Cannot brute force it
# No constraints on k1 and k2, so we can use matrix system to solve it

tokens = 0
for i in range(len(prizes)):
    x_prize = prizes[i][0]
    y_prize = prizes[i][1]
    
    x_a = claw_machines[i*2][1]
    y_a = claw_machines[i*2][2]
    x_b = claw_machines[i*2+1][1]
    y_b = claw_machines[i*2+1][2]
    
    # print(f"Button A: x+{x_a}, y+{y_a}")
    # print(f"Button B: x+{x_b}, y+{y_b}")
    # print(f"prize at: x={x_prize}, y={y_prize}")
    x_a, y_a, x_b, y_b, x_prize, y_prize = map(Fraction, (x_a, y_a, x_b, y_b, x_prize, y_prize))
    
    b = ((y_a * x_prize) / x_a - y_prize) / ((y_a * x_b / x_a) - y_b)
    a = (x_prize - x_b * b) / x_a
    if a.denominator == 1 and b.denominator == 1: 
        tokens += (A_COST * a + B_COST * b).numerator
    
print(f"tokens (part2): {tokens}")