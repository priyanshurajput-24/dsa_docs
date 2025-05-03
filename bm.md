# Boyer-Moore String Search Algorithm (Simplified Version)

This function `bm(t, p)` implements a simplified version of the Boyer-Moore string search algorithm to find all occurrences of a pattern `p` in a text `t`.

## Parameters:
- `t` (string): The text in which to search for the pattern.
- `p` (string): The pattern to search for in the text.

## Returns:
- `poslist` (list of int): A list containing the starting indices of all occurrences of the pattern `p` found in the text `t`.

## How it works:
1. **Preprocessing (Last Occurrence Table):**  
   The function creates a dictionary `last` that maps each character in the pattern `p` to its last occurrence index within the pattern. This helps determine how far to shift the pattern when a mismatch occurs.

2. **Searching:**  
   - The search starts with the pattern aligned at the beginning of the text (`i = 0`).
   - For each alignment, it compares characters from the end of the pattern moving backward.
   - If all characters match, the current index `i` is added to `poslist`.
   - If a mismatch occurs, the function uses the last occurrence table to decide how far to shift the pattern to the right, skipping unnecessary comparisons.

3. **Shifting the Pattern:**  
   - If the mismatched character in the text exists in the pattern, shift the pattern so that this character aligns with its last occurrence in the pattern.
   - If the character does not exist in the pattern, shift the pattern past the mismatched character.

## Notes:
- This implementation only uses the "bad character" heuristic of the Boyer-Moore algorithm.
- It does not implement the "good suffix" heuristic, so performance may not be optimal for all inputs.
- The function returns all starting indices where the pattern is found in the text.
