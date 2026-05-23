class solution:
    def nextWarmerDays(self, temperatures):
        n = len(temperatures)
        answer = [0] * n # initialze the result array with 0s
        stack = [] #stack to store the indices
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index # calculate the diffrences
            stack.append(i) # push current index onto the stack
                
        return answer