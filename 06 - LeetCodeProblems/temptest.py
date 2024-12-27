class Solution:
    def romanToInt(self, s):
        # Hardcoded dictionary with direct integer mapping
        roman_values = {
            b'I': 1, b'V': 5, b'X': 10, 
            b'L': 50, b'C': 100, b'D': 500, 
            b'M': 1000
        }
        
        # Pre-allocate result variable
        result = 0
        
        # Use range-based iteration with explicit indexing
        for i in range(len(s) - 1, -1, -1):
            # Convert to bytes for potentially faster lookup
            current_char = s[i].encode('ascii')
            current_value = roman_values[current_char]
            
            # Use explicit comparison without else
            if i < len(s) - 1:
                prev_char = s[i + 1].encode('ascii')
                prev_value = roman_values[prev_char]
                
                if current_value < prev_value:
                    result -= current_value
                else:
                    result += current_value
            else:
                result += current_value
        
        return result