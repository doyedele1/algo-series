class Solution:
    def simplifyPath(self, path: str) -> str:
        # Initialize a stack that helps pop when we encounter double dots
        stack = []
        print(path.split("/"))
        
        for char in path.split("/"):
            if char == "..":
                if len(stack) != 0: stack.pop()
            elif char != "" and char != ".":
                stack.append(char)
            else: 
                char = ""

        return "/" + "/".join(stack)
        
        
        '''
            Example 1:
                Input = "/../abc//./def/"
                Simplified =  "/abc/def"

            Example 2:
                Input = "/a/b/c/../.."
                Simplified = "/abc"

                Time complexity - O(N) - where N is the length of the path
                Space complexity - O(N) - memory needed to create the simplified list
        '''