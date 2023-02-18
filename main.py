from pyarray import Array

myarray=Array(12)
print("We create an array of 12 elements")
myarray.traverse()
for i in range(8):
 myarray[i]=i+2
print("this is how it looks...")
myarray.traverse()
print("x=", myarray[3])
myarray.delete(2)
print("after deleting at 2...")
myarray.traverse()
myarray.insert(5, 1)
print("after inserting 1 at 5...")
myarray.traverse()


from array2d import Array2D
mat1=Array2D(3, 3)
for i in range(3):
 for j in range(3):
   mat1[i,j]=2*i+3*j+4
mat1.traverse()
