
def rkn(t, p):
    # put `position list` and window for text and pattern
    poslist, numt, nump = [], 0, 0
    # Loop over the text and pattern with the length of pattern to get the window for matching the first occurance of pattern at first position
    for i in range(len(p)):
        numt = numt*10 + int(t[i])
        nump = nump*10 + int(p[i])
    if numt == nump:
        poslist.append(0)
    for i in range(1, len(t)-len(p)+1):
        # remove the first occurance of word and add the next char in the window
        numt = numt - int(t[i-1])*(10**(len(p)-1)) 
        # add the next char in the window
        numt = numt * 10 + int(t[i+len(p)-1]) # from i we will add the length of pattern and remove 1 from it.
        if numt == nump:
            poslist.append(i)
    return poslist


print(rkn("1234567890123456789012345678901234567890", "1234567890"))
print(rkn('233323233454323','23'))





def rks(t, p):
    # put `position list` and window for text and pattern with prime number for hashing
    poslist, prime = [], 113
    text_hash, pattern_hash = 0, 0
    # Get the hash value of the pattern and text for the length of pattern
    for i in range(len(p)):
        pattern_hash = pattern_hash + ord(p[i])
        pattern_hash = pattern_hash % prime
    for i in range(len(p)):
        text_hash = text_hash + ord(t[i])
        text_hash = text_hash % prime
    # Match the text and pattern with the hash value and the actual string
    for i in range(len(t)-len(p)+ 1):
        if text_hash == pattern_hash and t[i:i+len(p)] == p:
            poslist.append(i)
        # remove the first occurance of word and add the next char in the window
        if i < len(t) - len(p):
            text_hash = text_hash - ord(t[i]) + ord(t[i+len(p)])
            text_hash = text_hash % prime

    return poslist

text = 'abcdbabcdb'
pattern = 'abcdb'
print(rks(text, pattern))

