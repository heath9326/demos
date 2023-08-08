stack = []
symbols = []
vvod = input().split()

for symbol in vvod:
    if symbol.isdigit():
        stack.append(int(symbol))
    else:
        # Если бинарные:
        if symbol in ["+", "-", "*", "/"]:
            y = stack.pop(len(stack) - 1)
            x = stack.pop(len(stack) - 1)
            if symbol == "+":
                stack.append(x + y)
            elif symbol == "-":
                stack.append(x - y)
            elif symbol == "*":
                stack.append(x * y)
            else:
                stack.append(x // y)
        # Если унарные:            
        elif symbol in ["~", "!", "#"]:
            y = stack.pop(len(stack) - 1)     
            if symbol == "~":
                stack.append(-y)
            elif symbol == "!":
                fact = 1
                for i in range(1, y + 1):
                    fact = fact * i
                stack.append(fact)
            else:
                stack.append(y)
                stack.append(y)
        # Если тернарные:                
        else:
            y = stack.pop(len(stack) - 1)
            x = stack.pop(len(stack) - 1)
            z = stack.pop(len(stack) - 1)
            stack.append(x)
            stack.append(y)
            stack.append(z)

print(stack[0])