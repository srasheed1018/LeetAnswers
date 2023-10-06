class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map: # if c is not ) ] or }, it must be ( [ or {, so add it to stack and continue loop
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]: # if the stack doesn't exist (no opening character detected) or the corresponding opening character was not the last thing in the stack (to preserve order), then this is not a valid input
                return False
            stack.pop() # at this point, the input must've been a valid ending character, so take it out the stack

        return not stack # if the stack exists, the input is invalid
                