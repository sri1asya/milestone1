def s(dna):
    dna = dna.upper() #makes it uppercase in case we get it in lower
    dict = {} #opens a dictionary
    count_A = dna.count('A') #counts A
    count_C = dna.count('C') #counts C
    count_G = dna.count('G') #counts G
    count_T = dna.count('T') #counts T

    dict['A'] = count_A #adds A count to dict
    dict['C'] = count_C #adds C count to dict
    dict['G'] = count_G #adds G count to dict
    dict['T'] = count_T #adds T count to dict

    return dict

print (s(dna))

def fibonacci_rabbits(n, k):
    if n<=2:
        return 1
    else:
        return (fibonacci_rabbits(n-1, k)  + fibonacci_rabbits(n-2, k)*k) #the math stuff
    print(fibonacci_rabbits(n,k))

def hamming_dist (dna1, dna2):
    count = 0 #resets count
    for index in range(len(dna1)): 
        if dna1[index] != dna2[index]: #checks for when they're not equal
            count = count + 1 #adds a tally for each time it isn't equal
    return count
print(hamming_dist (dna1, dna2))
