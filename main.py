
# Question 1

print("Question 1 ")
print("*************************************************************************** \n")

# text to be used from encryption/decryption
text = "As I walk"

# list for register
register = []

# method for transforming string to int
def CreateRegister(lfsr):
    register = []
    for i in lfsr:
        register.append(int(i))
    return register

# method for LFSR algorithm
# pops from end of register and inserts to start of register
# takes in register and int as inputs , int represents the increments
def LFSR(register, numb):
    for k in range(numb):
        xorA = register[5] ^ register[9]
        xorB = register[2] ^ xorA
        register.pop(31)
        register.insert(0, xorB)
    return register

# method for A51 algorithm
# takes in both registers and an int as inputs
# XOR's both registers and outputs the result
def A51(registerA, regesterB, numb):
    A51 = []
    for i in range(numb):
        A51.append(registerA[i] ^ regesterB[i])
    return A51

# method for encryption/decryption
# loops through the key
# takes in text to be encrypted/decrypted as well as Key
def ExclusiveOR(text,key):
    key_string = ""
    for v in key:
        key_string += str(v)
    return "".join(chr(ord(x) ^ ord(y)) for (x, y) in zip(text, key_string))

# registers to be used by above methods
lfsr =  "11001010110011001010011010110010"
lfsrB = "00110110111100101001010010011010"

# Random Binary Registers for Question 2
random_Binary = ["01000101000011000011100111001111",
                 "01010101101110000100011000001111",
                 "01100010111000110101101110010100",
                 "01100001010011111101001101101100",
                 "10110110001100000010110010101011"]

# prints registers as ints
crA = CreateRegister(lfsr)
A = LFSR(crA, 20)
print("Stream 1: ", A)

crB = CreateRegister(lfsrB)
B = LFSR(crB, 20)
print("Stream 2: ", B)

# prints output of A51 Algorithm
crC = A51(A, B, 20)
print("Output Stream is : ", crC)

# prints plaintext and ciphertext
crD = ExclusiveOR(text,crC)
print("PlainText is :",text)
print("Ciphertext is :",crD)

# prints decrypted text
crE = ExclusiveOR(crD,crC)
print("Decrypted PlainText is :",crE)
print("*************************************************************************** \n")

# Question 2

print("Question 2")
print("*************************************************************************** \n")

# part 1
# method for counting 0's and 1's
# takes in lfsr object as input
# loops through register and counts each occurrence
# then prints the count on each
def Count_Binary(lfsr):
    count0 = 0
    count1 = 0
    for i in lfsr:
        if (i == 0):
            count0 += 1
        else:
            count1 += 1
    print("Part 1: Number of 0's is ", count0)
    print("Part 1: Number of 1's is ", count1)
    print("\n")


# part 2
# method that coungs the longest sequence for 0's and 1's
# takes in an int and an object as inputs
def Longest_Sequence(number, lfsr):
    sequence = 0
    longest = 0
    for s in lfsr:
        if (s == number):
            sequence += 1
        else:
            sequence = 0
        if (sequence > longest):
            longest = sequence
    return longest

# Part 3
# method that counts the number of 0's or 1's
# (only if they are above 3 and less than 7 in the sequence)
# takes in an int and an object as inputs
# returns the number of sequences that match the above conditions
def Estamations(number, lfsr):
    output = 0
    # current count of the analysed sequence
    count = 0
    for s in lfsr:
        if (s == number):
            count = count + 1
            if (count < 7 and count > 3):
                output = output + 1
        else:
            count = 0
    return output

# loops through the random binary list
# then runs andd prints the above methods for Question 2
for r in random_Binary:
    reg = CreateRegister(r)
    lfsr = LFSR(reg, 10000)
    print("Stream: ", lfsr)
    Count_Binary(lfsr)
    l = Longest_Sequence(1, lfsr)
    print("Part 2 : The longest Sequence of 1's is ", l)

    lb = Longest_Sequence(0, lfsr)
    print("Part 2 : The longest Sequence of 0's is ", lb)
    print("\n")

    estA = Estamations(0, lfsr)
    print("Part 3 : Estimations Greater than 3 and less than 7 for 0's is ", estA)

    estB = Estamations(1, lfsr)
    print("Part 3 : Estimations Greater than 3 and less than 7 for 1's is ", estB)
    print("\n")

print("*************************************************************************** \n")
