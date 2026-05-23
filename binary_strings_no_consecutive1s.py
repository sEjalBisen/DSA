def generate_binary_strings(n, current, prev, result):
        if len(current) == n:
            result.append(current)
            return
        generate_binary_strings(n, current + '0', 0, result)
        
        if prev != 1:
            generate_binary_strings(n, current + '1', 1, result )
        
        
    
    
class solution:
    def get_binary_strings(self, n):
        result=[]
        generate_binary_strings(n,"", 0, result)
        return result