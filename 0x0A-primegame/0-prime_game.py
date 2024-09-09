#!/usr/bin/python3
'''Prime game between Maria and Ben'''


def isWinner(x: int, nums: list) -> str:
    ''' The prime game between Maria and Ben
    Parameters:
    x (Integer): the number of rounds
    nums (List): List of numbers to pick from
    Return:
        Name of the player that won the most rounds
    '''

    def get_primes_up_to(n):
        '''Helper function to generate list of
        primes up to n using Sieve of Eratosthenes'''
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for start in range(2, int(n**0.5) + 1):
            if sieve[start]:
                for multiple in range(start*start, n + 1, start):
                    sieve[multiple] = False
        return [num for num, is_prime in enumerate(sieve) if is_prime]

    def determine_winner(n):
        '''Determine the winner for a given value of n'''
        primes = get_primes_up_to(n)
        is_maria_turn = True
        numbers = set(range(1, n + 1))

        while primes:
            prime = primes.pop(0)
            if prime in numbers:
                numbers -= {i for i in range(prime, n + 1, prime)}
                is_maria_turn = not is_maria_turn

        return 'Maria' if is_maria_turn else 'Ben'

    win_counts = {'Maria': 0, 'Ben': 0}

    for n in nums:
        winner = determine_winner(n)
        win_counts[winner] += 1

    if win_counts['Maria'] > win_counts['Ben']:
        return 'Maria'
    elif win_counts['Ben'] > win_counts['Maria']:
        return 'Ben'
    else:
        return None
