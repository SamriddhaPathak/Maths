def Sieve_of_Eratosthenes(n):
    # Create a list called 'prime' with all elements initialized to 0.
    # This list will help us keep track of whether a number is prime.
    # We are assuming the maximum number we need to check is 100.
    prime = [0 for i in range(101)]  # 0 means the number is initially assumed to be prime.

    # Start with the first prime number, 2, and check each number up to 'n'.
    for i in range(2, n+1):
        # If prime[i] is 0, it means 'i' is still considered a prime number.
        if prime[i] == 0:
            # Mark all multiples of 'i' as not prime (set to 1), starting from i*i.
            # We start from i*i because all smaller multiples of 'i' would have
            # already been marked by smaller primes.
            for j in range(i*i, n+1, i):
                prime[j] = 1  # Mark 'j' as not prime.
    
    # Now, we loop through the list again to find and print all prime numbers.
    for i in range(2, n+1):
        if prime[i] == 0:  # If prime[i] is still 0, it means 'i' is a prime number.
            print(i, end=" ")  # Print the prime number.

def main():
    # Ask the user to enter a number 'n'.
    n = int(input("Enter a number: "))
    # Call the Sieve_of_Eratosthenes function with the user's input.
    Sieve_of_Eratosthenes(n)

# This ensures that the main function runs only when the script is executed directly.
if __name__ == "__main__":
    main()
