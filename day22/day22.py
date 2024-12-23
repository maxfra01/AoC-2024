def mix_and_prune(secret, value):
    secret ^= value
    secret %= 16777216
    return secret

def next_secret(secret):
    secret = mix_and_prune(secret, secret * 64)
    secret = mix_and_prune(secret, secret // 32)
    secret = mix_and_prune(secret, secret * 2048)
    return secret

def simulate_secrets(initial_secret, iterations):
    secret = initial_secret
    for _ in range(iterations):
        secret = next_secret(secret)
    return secret

def sum_of_2000th_secrets(initial_secrets):
    total = 0
    for secret in initial_secrets:
        total += simulate_secrets(secret, 2000)
    return total

def get_prices(initial_secret, iterations):
    prices = []
    secret = initial_secret
    for _ in range(iterations):
        secret = next_secret(secret)
        prices.append(secret % 10)
    return prices

def find_best_sequence(initial_secrets, iterations=2000):
    from itertools import product

    best_sequence = None
    max_bananas = 0

    # Generate all possible sequences of four price changes
    possible_sequences = list(product(range(-9, 10), repeat=4))

    for sequence in possible_sequences:
        total_bananas = 0
        for secret in initial_secrets:
            prices = get_prices(secret, iterations)
            changes = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
            for i in range(len(changes) - 3):
                if changes[i:i + 4] == list(sequence):
                    total_bananas += prices[i + 4]
                    break
        if total_bananas > max_bananas:
            max_bananas = total_bananas
            best_sequence = sequence

    return best_sequence, max_bananas

if __name__ == "__main__":
    with open("input.txt") as f:
        initial_secrets = [int(line.split()[-1]) for line in f]
    
    # Part 1
    print(sum_of_2000th_secrets(initial_secrets))
    
    # Part 2
    best_sequence, max_bananas = find_best_sequence(initial_secrets)
    print(f"Best sequence: {best_sequence}, Max bananas: {max_bananas}")
