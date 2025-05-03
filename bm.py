


def bm(t, p):
    # Generate the last occurrence table for the pattern
    last = {}
    for i in range(len(p)):
        last[p[i]]  = i
    # Initialize the position list and the index
    poslist, i = [], 0
    # Start the search for the pattern in the text
    while i < (len(t) - len(p) + 1):
        matched, j = True, len(p) - 1
        while matched and j >= 0:
            if t[i+j] != p[j]:
                matched = False
            j = j - 1
        # If a match is found, add the position to the list 
        if matched: 
            poslist.append(i)
            # Move the index to the next position
            i = i + 1
        # If no match is found, use the last occurrence table to skip ahead
        else:
            j = j + 1 
            if t[i+j] in last.keys(): # if the character is in the pattern
                i = i + max(j - last[t[i+j]],1)   # skip ahead from current position...
            else:
                # if the character is not in the pattern
                i = i + j + 1
    return poslist




t="werwerwerwerrterdfgdfdfhgghdf"
p="erd"
print(bm(t,p))
print(bm('abababbababbbbababab','abab'))
print(bm('abcaaacabc','abc'))
 
