#  When pass a negative index like text[-i], Python translates it mathematically
#  by adding the length of the string to the negative index: text[len(text) - i].
#  For example, text[-1] becomes text[6 - 1], which evaluates to text[5]

txt = "RikustoMadika"
print(txt[::-1])    #[start : stop : step]
print(txt[8:2:-2])  #here print the value with 1 step jump because i put -2
