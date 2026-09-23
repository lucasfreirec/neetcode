class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == '+' or c == '-' or c == '*' or c == '/':
                n2 = stack.pop()
                n1 = stack.pop()
                if c == '+':
                    stack.append(n1+n2)
                elif c == '-':
                    stack.append(n1-n2)
                elif c == '*':
                    stack.append(n1*n2)
                else:
                    stack.append(int(n1 / n2))
            else:
                stack.append(int(c))
        
        return stack[0]
            
