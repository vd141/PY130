'''
The diamond exercise takes as its input a letter, and outputs it in a diamond
shape. Given a letter, it prints a diamond starting with 'A', with the supplied
letter at the widest point.

The first row contains one 'A'.
The last row contains one 'A'.
All rows, except the first and last, have exactly two identical letters.
The diamond is horizontally symmetric.
The diamond is vertically symmetric.
The diamond has a square shape (width equals height).
The letters form a diamond shape.
The top half has the letters in ascending order.
The bottom half has the letters in descending order.
The four corners (containing the spaces) are triangles.
'''

'''
Diamond has one class method make_diamond()

it takes a letter as input and makes a diamond out of the letters

for A:
A

for B:
 A 
B B
 A

for C:
  A  
 B B 
C   C
 B B 
  A

for D
   A   
  B B  
 C   C 
D     D
 C   C 
  B B  
   A   

width of the diamond is twice the position of the target letter minus 1

could use an dict to store letter/position, or use the ASCII alphabet (each char
already has a position associated)


'''

class Diamond:
    pass