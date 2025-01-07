#!/usr/bin/python3
""" This code is for the prime game """


def is_winner(x, nums):
    prime_numbers = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
        109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
        173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
        233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
        293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
        367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431,
        433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499
    ]

    players = {"Maria": 0, "Ben": 0}

    for n in nums:
        all_numbers = [1] * n
        if n > prime_numbers[-1]:
            # add more prime numbers
            for i in range(prime_numbers[-1], n + 1):
                is_prime = True
                for j in range(2, i):
                    if i % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_numbers.append(i)
        game_count = 0
        for i in prime_numbers:
            if i > n:
                break
            for j in range(i, n + 1, i):
                if all_numbers[j - 1] == 1:
                    all_numbers[j - 1] = 0
                    game_count += 1
        if game_count % 2 == 0:
            players["Ben"] += 1
        else:
            players["Maria"] += 1

    if players["Maria"] > players["Ben"]:
        return "Maria"
    elif players["Maria"] < players["Ben"]:
        return "Ben"
    else:
        return None
