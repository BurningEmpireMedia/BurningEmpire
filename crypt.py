# Practical Cryptography in Python
# Nielson & Monson (2019)
# Basic Shift Encoder Decoder - The BS_ED

import string

def create_shift_substitutions(n):
    encoding = {}
    decoding = {}
    alphabet_size = len(string.ascii_uppercase)
    for i in range(alphabet_size):
        letter = string.ascii_uppercase[i]
        subst_letter = string.ascii_uppercase[(i+n)%alphabet_size]

        encoding[letter] = subst_letter
        decoding[subst_letter] = letter
    return encoding, decoding

''' Function is parameterized on n, the shift parameter. No error checking.
For encoding and decoding each letter in a message is substituted by one
in the dictionary '''

def encode(message, subst):
    cipher = " "
    for letter in message:
        if letter in subst:
            cipher += subst[letter]
        else:
            cipher += letter
    return cipher
    
def decode(message, subst):
    return encode(message, subst)

''' Quote from book: An idiomatic function body would probably be a one-liner:
def encode(message, subst):
return "".join(subst.get(x, x) for x in message)
That’s a lovely bit of Python if you’re used to it, but we’re trying not to make too
many assumptions here.
In our implementation, the encode function takes an incoming message and a
substitution dictionary. For each letter in the message, we replace it if a substitution
is available. Otherwise, we just include the character itself with no transformation
(preserving spaces and punctuation). '''

def printable_substitution(subst):
    mapping = sorted(subst.items())
    alphabet_line = " ".join(letter for letter, _ in mapping)
    cipher_line = " ".join(subst_letter for _, subst_letter in mapping)
    return "{}\n{}".format(alphabet_line, cipher_line)

if __name__ =="__main__":
    n = 1
    encoding, decoding = create_shift_substitutions(n)
    while True:
        print("\nShift Encoder Decoder")
        print("--------------------")
        print("\tCurrent Shift: {}\n".format(n))
        print("\t1. Print Tables")
        print("\t2. Encoder")
        print("\t3. Decoder")
        print("\t4. Cipher Shift")
        print("\t5. Quit SED \n")
        choice = input(">> ")
        print()

        if choice == '1':
            print("Encoding Table:")
            print(printable_substitution(encoding))
            print("Decoding Table:")
            print(printable_substitution(decoding))

        elif choice == '2':
            message = input("\nMessage to encode: ")
            print("Encoded Message: {}".format(
                encode(message.upper(),encoding)))

        elif choice == '3':
            message = input("\nMessage to decode: ")
            print("Decoded Message: {}".format(
                decode(message.upper(), decoding)))

        elif choice == '4':
            new_shift = input("\nNew shift (concurrently{}): ".format(n))
            try:
                new_shift = int(new_shift)
                if new_shift < 1:
                    raise Exception("Shift must be greater than 0")
            except ValueError:
                print("shift{} is not a valid number.".format(new_shift))
            else:
                n = new_shift
                encoding, decoding = create_shift_substitutions(n)

        elif choice == '5':
            print("Terminating... This program will self-destruct now! \n")

            break
        
        else:
            print("Unknown option {}.".format(choice))

# This is the end
