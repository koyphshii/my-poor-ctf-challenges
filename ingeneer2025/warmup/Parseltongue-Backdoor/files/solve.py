#!/usr/bin/env python3
"""
Solver for the "snake" encryption used above.
Decrypts a ciphertext produced by snake_encrypt(message, cols).
"""

def snake_decrypt(cipher: str, cols: int) -> str:
    # Determine number of rows
    rows = len(cipher) // cols
    # Fill matrix column by column
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    idx = 0
    for c in range(cols):
        for r in range(rows):
            matrix[r][c] = cipher[idx]
            idx += 1

    # Read matrix in snake (zig-zag) row order to reconstruct the message
    plaintext = []
    for r in range(rows):
        col_range = range(cols) if (r % 2 == 0) else reversed(range(cols))
        for c in col_range:
            plaintext.append(matrix[r][c])

    # Join and strip padding 'X'
    return ''.join(plaintext).rstrip('X')


def main():
    # Example usage:
    # Replace the following encrypted_text with the output you got from snake_encrypt
    encrypted_text = "OOPTUSAZUOBM"
    cols = 4

    decrypted = snake_decrypt(encrypted_text, cols)
    print("Decrypted message:", decrypted)


if __name__ == '__main__':
    main()

