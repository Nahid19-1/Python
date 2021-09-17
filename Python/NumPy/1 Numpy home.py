#NumPy Getting Started AND Creating Arrays
import numpy as np
arr0 = np.array(42)
arr1 = np.array([1,2,3,4,5,6,7,8,])
arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
arr3 = np.array([[[1,2,3],[4,5,6]],[[11,22,33],[44,55,66]]]) #contain 2-d array as eliment

print(type(arr0))
print(np.__version__)
print('0-D array : ', arr0)
print('1-D array : ', arr1)
print('2-D array : ', arr2)
print('3-D array : ', arr3)
print("Dimention of arr3 is  : ",arr3.ndim)

arr4 = np.array([1,2,3,4],ndmin=5)
print(arr4,"\nNum of dimention : ",arr4.ndim)
print()


# NumPy Array Indexing
print("========================NumPy Array Indexing============================")
# indexing start from 0.....
print(arr1[1])
print(arr1[1] + arr1[2])
print("Indexing 2D array : ",arr2[1,0]) # arr2[dymention,elements])
print("Indexing 3D array : ",arr3[1,0,1]) # arr2[dymention,dymention,elements])
print('Last element from 2nd dim: ', arr2[1, -1])
print()



# NumPy Array Slicing
print("========================NumPy Array Slicing============================")
print("Slicing 1D array",arr1[1:7])
print("Slicing 1D array",arr1[1:len(arr1):2])
print("Slicing 2D array",arr2[1,1:5])
print("Slicing 2D array both elements, slice index 1 to index 4 ",arr2[0:2, 1:4])
print()



# NumPy Data Types
print("========================NumPy Data Types============================")
print(arr2.dtype)
arr_i = np.array([1, 2, 3, 4], dtype='i8')
arr_u = np.array([1, 2, 3, 4], dtype='u8')
arr_f = np.array([1, 2, 3, 4], dtype='f8')

print(arr_i.dtype)
print(arr_u.dtype)
print(arr_f.dtype)


arr_o = np.array([1, 2, 3, 4], dtype='O')
arr_s = np.array([1, 2, 3, 4], dtype='S')
arr_u = np.array([1, 2, 3, 4], dtype='U')

print("O - object datatype : ",arr_o.dtype)
print("O - object : ",arr_o)
print("S - string datatype : ",arr_s.dtype)
print("S - string  : ",arr_s)
print("U - unicode string datatype : ",arr_u.dtype)
print("U - unicode string  : ",arr_u)
print()



# Converting Data Type on Existing Arrays
print("------------Converting Data Type on Existing Arrays--------------")
arr_float = np.array([1.1, 2.1, 3.1])
arr_int = np.array([1, 2, 3])
arr_bool = np.array([1, 0, 3])

newarr_i = arr_float.astype('i')
newarr_f = arr_int.astype(float)
newarr_b = arr_bool.astype(bool)
print(newarr_i)
print(newarr_f)
print(newarr_b)
print(newarr_i.dtype)
print(newarr_f.dtype)
print(newarr_b.dtype)

time =np.datetime64('2005-02-25')
print(time)
print(type(time))
y=np.datetime64(20, 'Y')
print(y)
print()



# NumPy Array Copy vs View
print("============================NumPy Array Copy vs View============================")
arrcv = np.array([1, 2, 3, 4, 5])
x = arrcv.copy()
arrcv[0] = 42

print("This is view array: ",arrcv)
print("This is copy array: ",x)


arrb = np.array([1, 2, 3, 4, 5])

x = arrb.copy()
y = arrb.view()

print("copies owns the data : ",x.base) # base that returns None if the array owns the data.
print("views does not own the data:  ",y.base)