# Rabin-Karp Pattern Matching Algorithm

* This function finds all positions where the pattern 'p' appears in the text 't'
* poslist is a list to store the positions where the pattern is found
* numt and nump store the numeric value of the current window in text and the pattern

* Convert the first part of the text and the pattern into numbers for easy comparison
* Build the number for the first window in text and the pattern by treating digits as numbers

* If the first window matches the pattern, record position 0

* Slide the window over the text one digit at a time
* Remove the leftmost digit and add the new rightmost digit to the window to update the number efficiently
* If the current window matches the pattern, record the position

* Return all positions where the pattern was found

* Example usage: find all positions of '23' in '233323233454323'





# Rabin-Karp String Matching Algorithm (with Simple Hash)

* Initialize an empty list to store the starting indices where the pattern is found in the text

* Get the lengths of the text and the pattern

* Choose a prime number to use in the hash function to reduce hash collisions

* Calculate the initial hash value for the pattern by summing the ASCII values of its characters
* Take modulo with the prime to keep the hash value manageable

* Calculate the hash value for the first substring of the text (of the same length as the pattern)
* Again, sum the ASCII values and take modulo with the prime

* Loop through each possible starting position in the text where the pattern could fit

    * If the hash values of the current substring and the pattern match,
    * check the actual substring to confirm if it matches the pattern
    * If it matches, record the starting index

    * If not at the end, update the hash value for the next substring by:
        * Subtracting the ASCII value of the character going out of the window
        * Adding the ASCII value of the new character coming into the window
        * Take modulo with the prime to keep the hash value manageable

* Return the list of all starting indices where the pattern was found in the text

* Example usage: Find all positions of 'abcdb' in 'abcdbabcdb'

