def string_reverse(s: str)-> str: 
   new_string = ""
   n = len(s)
   for i in range(n):
      new_string = new_string + s[n-i-1]
   return new_string

B = "NAIDESU"
print(string_reverse(B))
