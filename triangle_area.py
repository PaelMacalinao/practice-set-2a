def triangle_area(a, b, c):
    # Calculate the semi-perimeter
    
    s = (a + b + c) // 2  # Use integer division
    
    # Calculate the area using Heron's formula
    
    term1 = s * (s - a) * (s - b) * (s - c)
    
    # Calculate square root using exponentiation
    
    area = int(term1 ** 0.5)  
    
    return area