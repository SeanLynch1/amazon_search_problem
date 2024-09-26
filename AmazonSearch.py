'''
"You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have a common prefix with searchWord.
If there are more than three products with a common prefix, return the three lexicographically minimum products.

Return a list of lists of the suggested products after each character of searchWord is typed."


Example:

Input word: "mouse"

Step 1:
Search for "m"
Output = ["mobile", "moneypot", "monitor"]

Step 2:
Search for "mo"
Output = ["mobile", "moneypot", "monitor"]

Step 3:
Search for "mou"
Output = ["mouse", "mousepad"]

Step 4:
Search for "mous"
Output = ["mouse", "mousepad"]

Step 5:
Search for "mouse"
Output = ["mouse", "mousepad"]

Algorithm finished.
Final Output = [
  ["mobile", "moneypot", "monitor"],
  ["mobile", "moneypot", "monitor"],
  ["mouse", "mousepad"],
  ["mouse", "mousepad"],
  ["mouse", "mousepad"]
]
'''

class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str):
        
        if len(searchWord) == 0:
            return []
        
        # ant, bat, fridge, mobile, moneypot, monitor, mouse, mousepad
        products.sort()
        
        final_output = []
        
        base=0
        

        for i in list(range(len(searchWord))):
            
            searched_items = 0
            temp_output = []
            
            while base < len(products) and searched_items < 3:
                if products[base][:i + 1] != searchWord[:i + 1]:
                    print("word or char not found : ", products[base][:i + 1])
                    base += 1
                elif products[base + searched_items][:i + 1] == searchWord[:i + 1]:
                    print("word or char found! : ", products[base][:i + 1])
                    temp_output.append(products[base + searched_items])
                    searched_items +=1
                else:
                    break
                    
            final_output.append(temp_output)
            
        return final_output
        
        
data = ["ant","bat","fridge","mobile","mobby","mobbed","moniscule","monecule","mouse","moneypot","monitor","mousepad"]

solution = Solution()

print(solution.suggestedProducts(data, "monis"))