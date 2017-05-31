import random
primeList = [23, 29, 31, 37, 41]
basesList = [3, 5, 7, 11, 13]         #Actually primes too

index = random.randrange(5)

sharedPrime = primeList[index]        # p
sharedBase = basesList[index]         # g
 
aliceSecret = 6                       # a
bobSecret = 15                        # b

print "The \"secret\" of Alice is: ", aliceSecret
print "The \"secret\" of Bob is: ", bobSecret
print "You must never share any of these!!!"

print "\n************************************************\n"
 
print  "Publicly shared variables: (no need to hide this info)"
print  "    Shared prime: " , sharedPrime 
print  "    Shared base:  ", sharedBase 

print "\n************************************************\n"

# Alice sends Bob A = g^a mod p
A = (sharedBase**aliceSecret) % sharedPrime
print "Alice computes A = {}^{} mod {}".format(sharedBase, aliceSecret, sharedPrime)
print "Step 1: {}^{} = {}".format(sharedBase, aliceSecret, sharedBase**aliceSecret)
print "Step 2: {} mod {} = {}".format(sharedBase**aliceSecret, sharedPrime, A)
print "Alice sends via a public channel: " , A
print
 
# Bob sends Alice B = g^b mod p
B = (sharedBase ** bobSecret) % sharedPrime
print "Bob computes B = {}^{} mod {}".format(sharedBase, bobSecret, sharedPrime)
print "Step 1: {}^{} = {}".format(sharedBase, bobSecret, sharedBase**bobSecret)
print "Step 2: {} mod {} = {}".format(sharedBase**bobSecret, sharedPrime, B)
print "Bob sends via a public channel: ", B 
 
print "\n***********************************************\n"
print "Both computes shared key on its own" 
# Alice computes shared key: K = B^a mod p
aliceSharedSecret = (B ** aliceSecret) % sharedPrime
print "Alice computes K = {}^{} mod {}".format(B, aliceSecret, sharedPrime)
print "Step 1: {}^{} = {}".format(B, aliceSecret, B**aliceSecret)
print "Step 2: {} mod {} = {}".format(B**aliceSecret, sharedPrime, aliceSharedSecret)
print "    Shared key (i.e. symmetric) Alice computed: ", aliceSharedSecret
print
 
# Bob computes shared key: K = A^b mod p
bobSharedSecret = (A**bobSecret) % sharedPrime
print "Bob computes K = {}^{} mod {}".format(A, bobSecret, sharedPrime)
print "Step 1: {}^{} = {}".format(A, bobSecret, A**bobSecret)
print "Step 2: {} mod {} = {}".format(A**bobSecret, sharedPrime, bobSharedSecret)
print "    Shared key (i.e. symmetric) Bob computed: ", bobSharedSecret
print
print "\nEnd of algorithm, now both can encrypt using that last key."
