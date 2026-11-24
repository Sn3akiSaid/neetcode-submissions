class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numberstack = []

        for i in tokens:
            if i == "+":
                a, b = numberstack.pop(), numberstack.pop()
                numberstack.append(a + b)
            elif i == "-":
                a, b = numberstack.pop(), numberstack.pop()
                numberstack.append(b - a)
            elif i == "*":
                a, b = numberstack.pop(), numberstack.pop()
                numberstack.append(a * b)
            elif i == "/":
                a, b = numberstack.pop(), numberstack.pop()
                numberstack.append(int(float(b) / a))
            else:
                numberstack.append(int(i))
        return numberstack[0]