
Input = input("Input:")
stack=[]
def maching(Input):
    for ch in Input:
        if ch in ["(", "{", "["]:  
            stack.append(ch) 
        else:     
            current = stack.pop() 
            if current == "[": 
                if ch != "]": 
                    return False
            if current == "{": 
                if ch != "}": 
                    return False
            if current == "(": 
                if ch != ")": 
                    return False
  
    if stack: 
        return False
    return True
print(f'Output:{maching(Input)}')
