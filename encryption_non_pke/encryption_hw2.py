# Name: Ed Hawkins
# Encryption (non-PKE) Homework
# Starter code is from Wayne Tobias in-class code along
# Modified to create a symmetric cipher other than shift/caesar cipher.
# Algorithm substitutes A for Z, B for Y, C for X, etc (first/last, second/next to last...).

def encrypt(message):
  message = message.upper()
  alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  result = ""
  for letter in message:
    if letter in alpha:
      #substitute based on index of original letter (A for Z, B for Y, C for X, etc.)
      letter_index = len(alpha) - (alpha.find(letter) % len(alpha))
      result = result+alpha[letter_index-1]
    else:
      result = result + letter
  return result

def decrypt(message):
  message = message.upper()
  alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  result = ""
  for letter in message:
    if letter in alpha:
      #substitute based on index of encoded letter (A for Z, B for Y, C for X, etc.)
      letter_index = len(alpha) - (alpha.find(letter) % len(alpha))
      result = result +alpha[letter_index-1]
    else:
      result = result + letter
  return result

def main():
  word = "This message will be encrypted and decrypted using a symmetric substitution cypher. The quick brown fox jumps over the lazy dog."
  print()
  print('Original Message: ' + word)
  print()
  #encrypt original message
  encrypted = encrypt(word)
  print('Encrypted Message: ' + encrypted)
  print()
  #decrypt encrypted message
  decrypted=decrypt(encrypted)
  print('Decrypted Message: ' + decrypted)
  print()

if __name__ == "__main__":
  main()