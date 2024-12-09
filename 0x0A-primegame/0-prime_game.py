#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """Returns a list of primes up to n using the Sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]

def isWinner(x, nums):
    """Returns the name of the player who won the most rounds."""
    # Count of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = sieve_of_eratosthenes(n)
        turn = 0  # Maria starts, so turn = 0 for Maria, 1 for Ben
        
        # We simulate the game for this round
        available_numbers = [True] * (n + 1)
        
        for prime in primes:
            if available_numbers[prime]:
                # Mark the multiples of the prime number as unavailable
                for multiple in range(prime, n + 1, prime):
                    available_numbers[multiple] = False
                
                # Switch turns: 0 for Maria, 1 for Ben
                turn = 1 - turn
        
        # If turn is 0, Maria had the last move, otherwise Ben did
        if turn == 0:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
