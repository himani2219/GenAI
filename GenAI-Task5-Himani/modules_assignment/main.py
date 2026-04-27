import Math_utils

print(Math_utils.add(5, 3))        
print(Math_utils.subtract(5, 3))   
print(Math_utils.square(4))        


from Math_utils import add, subtract, square
print(add(9, 3))
print(subtract(8, 3))
print(square(9))


import strings_utils
print(strings_utils.capitalize_text("Hello senior!"))
print(strings_utils.reverse_string("Hello how are you doing"))
print(strings_utils.word_count("Hello welcome to my space"))


import shop_package.discount as dis
print(dis.apply_discount(1000, 10))

from shop_package.billing import total_price, apply_tax
print(total_price([100, 200, 300]))