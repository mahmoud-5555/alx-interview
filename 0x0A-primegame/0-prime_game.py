#!/usr/bin/python3
""" This code is for the prime game """


def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    The game is played for `x` rounds, where for each round `n`
    (given in the `nums` list), players alternate choosing a prime
    number and removing that prime and its multiples from the set
    of integers [1, n]. The player who cannot make a move loses.

    The winner of each round is determined by the number of moves
    made. If the number of moves is even, Ben wins; otherwise, Maria wins.
    The player with the most wins after `x` rounds isdeclared the overall
    winner.

    Args:
        x (int): The number of rounds to be played.
        nums (list of int): A list of integers, where each integer represents
            the upper limit for the set of integers [1, n] in a given round.

    Returns:
        str: The name of the player with the most wins ("Maria" or "Ben").
        None: If the number of wins is the same for both players.

    Examples:
        >>> is_winner(3, [4, 5, 6])
        'Maria'

        >>> is_winner(2, [7, 10])
        'Ben'

        >>> is_winner(1, [2])
        'Maria'

        >>> is_winner(2, [1, 3])
        None

    Notes:
        - This function assumes the `nums` list contains positive integers.
        - If `nums` contains values greater than the predefined prime list,
          it dynamically calculates additional prime numbers.

    Limitations:
        - Performance may degrade for very large values of
        `n` in the `nums` list due to the dynamic calculation
        of primes.

    """
    # Predefined list of prime numbers
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
    # Initialize player scores
    players = {"Maria": 0, "Ben": 0}
    # Play the game for each round
    for n in nums:
        all_numbers = set(range(1, n + 1))
        if n > prime_numbers[-1]:
            # Extend the prime numbers list to cover the range
            for i in range(prime_numbers[-1] + 1, n + 1):
                is_prime = True
                for j in range(2, int(i ** 0.5) + 1):
                    # Optimized prime check
                    if i % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_numbers.append(i)

        game_count = 0
        for i in prime_numbers:
            if i > n:
                break
            multiples = set(range(i, n + 1, i))
            all_numbers -= multiples
            game_count += len(multiples)

        # Determine winner of the round
        is_ben_winner = (game_count % 2 == 0)
        if is_ben_winner:
            players["Ben"] += 1
        else:
            players["Maria"] += 1

    # Determine overall winner
    if players["Maria"] > players["Ben"]:
        return "Maria"
    elif players["Maria"] < players["Ben"]:
        return "Ben"
    else:
        return None
