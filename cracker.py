
"""
*       This statement is a one-liner that cycles through every possible combination of characters within a possible
*       password and compares them to md5 hashes that are given as input in the file "hashes.txt" in order to crack the
*       passwords in the file.
*
*
*       How to run the cracker:
*           Create a file called "hashes.txt" that contains md5 hashes you want to crack separated by a newline
*           Type and replace: python3 /PATH/TO/FILE/cracker.py
*
*       Output: The program will print the cracked word(s) with a given length next to each other, starting from
*               length 1 going up until length 8. The time it took to crack the word(s) will be on the same line as
*               the word(s) themselves.
*               Example format:
*                   AD TE   0.021890878677368164
*                   BR9 1.749272108078003
*
"""

# (lambda file: (lambda hashlib: __import__('functools').reduce(lambda passLenMinusOne, passLen: ((lambda timerStart: print(" ".join((possiblePass for possiblePass in (m for n in ((''.join(tmp) for tmp in ((__import__('itertools').product([chr(i) for i in range(32, 127)],repeat=num_chars)))) for num_chars in range(passLen, passLen + 1)) for m in n) if __import__('hashlib').md5(possiblePass.encode('utf-8')).hexdigest()+'\n' in file))+'\t'+str(__import__("time").time()-timerStart)))(__import__("time").time())),range(0,8+1))) (__import__("hashlib")))(open('hashes.txt','r').readlines())





"""
*       This statement is the same statement as the one-liner, but it is broken up into different lines for readability 
*       and for commenting.
"""

(lambda file:
    (lambda hashlib:
     (lambda itertools:
        __import__('functools').reduce(
            lambda passLenMinusOne, passLen:  # Gives the password length as 2 parameters to the function
            (
                (lambda time:  # Declares lambda function timerStart
                 (lambda timerStart:
                    print(  # Prints the string surrounded by the parentheses
                        " ".join(  # Joins each of the parts of the array within its parentheses by a space
                            (possiblePass for possiblePass in  # declares variable possiblePass to the md5 function below
                             (m for n in  # Flattens the list inside it
                                (
                                    (  # Declares what is inside the parentheses as a list
                                        ''.join(tmp)  # Joins each character in array tmp, to make it a string
                                        for tmp in (  # cycles through the map and stores the result in tmp
                                            (  # cycles through each of the characters
                                                itertools.product(
                                                    [chr(i) for i in range(32, 127)] # creates permutations with range of characters
                                                    ,  # separates parameters
                                                    repeat=num_chars # sets parameter variable as num_chars to specify length of permutation
                                                )  # returns a permutation set of length (127-32)^num_chars
                                            )
                                        )  # map returns an iterable object, and j cycles through it
                                    ) for num_chars in range(passLen, passLen + 1)  # captures the list and sets variable num_chars
                                )  # Separates the previous for loop with the next
                                for m in n)  # Helps flatten the list
                             if  # (the possiblePass variable holds an actual password)
                             hashlib.md5(
                                 possiblePass  # uses md5 from hashlib package to hash the possPass
                                 .encode('utf-8'))  # just encodes the string to allow md5 to use it
                                 .hexdigest()  # gets the actual string version of the md5 hash
                             + '\n'  # adds an endline because each of the hashes in the following array have it
                             in
                             file
                            )  # Now contains the passwords that actually contained a real password
                        )  # Contains a list of actual passwords with passLen number of characters
                    +
                        '\t'  # Adds a tab
                    +
                        str(  # converts the following into a string
                            time.time()  # gets the current time
                            -
                            timerStart  # Subtracts the time when it started
                        )
                    )  # Gets the password(s) followed by a space followed by the time to crack
                ) (time.time())
                 )
                (
                __import__("time")
                )
            )
            ,
            range(0,8+1)
        )
      ) (__import__('itertools'))
     ) (__import__("hashlib"))
 )  (open(  # Opens parameter 1 as file
    'hashes.txt',
    'r'  # Opens it with 'r'ead flag to make the file read only
    ).readlines())  # Adds each of the lines in the file to an array)
