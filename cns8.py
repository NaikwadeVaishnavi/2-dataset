# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:48:10 2023

@author: hp
"""

# Diffie-Hellman Key Exchange Implementation with User Input

# Function to calculate power in a modular fashion (to avoid large numbers)
def power(base, exponent, modulus):
    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus

    return result

# Taking prime number and base input from the user
p = int(input("Enter a prime number (p): "))
g = int(input("Enter a base/generator (g): "))

# Taking private keys input from Alice and Bob
a_private = int(input("Alice, enter your private key: "))
b_private = int(input("Bob, enter your private key: "))

# Alice's public key calculation
A_public = power(g, a_private, p)

# Bob's public key calculation
B_public = power(g, b_private, p)

# Secret key calculation by Alice
alice_secret = power(B_public, a_private, p)

# Secret key calculation by Bob
bob_secret = power(A_public, b_private, p)

# Both Alice and Bob will have the same secret key
print("Alice's calculated secret key:", alice_secret)
print("Bob's calculated secret key:", bob_secret)
