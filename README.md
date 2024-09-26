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
