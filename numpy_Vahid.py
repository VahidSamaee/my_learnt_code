import numpy as np 

#####<<<<< np array   >>>>>#####

# my_list=[[1, 2, 3, 4],[5,6,7,8]]
# my_array= np.array(my_list) # to convert a list to ndarray
# print (type(my_array))


# my_array=np.arange(0,11, 2) # to make a ndarray , here 2 is the step size
# print (my_array)


# my_array=np.linspace(0, 5, 10)  # her 10 is the numeber of the elements
# print (my_array)


# my_array=np.zeros(3) # to make ndarray with zeros
# print (my_array)
# my_array=np.zeros((2,5)) # to make ndarray with zeros 2 dimensional
# print (my_array)
# my_array=np.ones((2,5)) # to make ndarray with ones 2 dimensional
# print (my_array)


# my_array=np.eye(4) # to make identity matrix 
# print (my_array)


# my_array=np.random.rand(5)  # to make a randome 1D matrix 0-1
# my_array=np.random.rand(5,3)  # to make a randome 1D matrix
# print (my_array)


# my_array=np.random.randn(11)  # to make a randome 1D matrix normal distribution funtion around 0
# my_array=np.random.randn(5,3)  # to make a randome 1D matrix normal distribution funtion around 0
# print (my_array)


# my_array=np.random.randint(1,100, 9)  # to make a randome 9 integer number between 1-100 
# print (my_array)


# my_array=np.arange(1,11,1)
# my_array=my_array.reshape(5,2) # reshaping a matrix
# print (my_array)


# my_array=np.random.randint(1,100, 9)
# my_max=my_array.max() #finding maximum of elements of in an array
# maxlocation= my_array.argmax() #the location of the max
# my_min=my_array.min() #finding minimum of elements of in an array
# minlocation= my_array.argmin() # the location of the minumum
# print (my_max, maxlocation, my_min, minlocation)


# my_array=np.random.randint(1,100, 25)  
# my_array=my_array.reshape(5,5)
# arrayshape=my_array.shape  # the shape of the array
# arraytype= my_array.dtype # the type of the array
# print (arrayshape, arraytype)









#####<<<<< np indexing and selection   >>>>>#####

# arr=np.arange(0,11)
# element8=arr[8]  # selectring one element 
# partarray=arr[2:5]  # selecting a part of the element
# frombiginto=arr[:3]
# arr[7:]=100 # all the elements become 100
# frombiginto[:]=200  # be carefor like this, all the first elements of arr also change to 200
# print(arr, frombiginto)

# arr=np.arange(0,11)
# new_arr=arr.copy()  # to make a copy from an array, then if you change it this will not affc=ect the original one


# arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
# num=arr_2d[1][1] # for selecting one part of an array
# num2=arr_2d[1,1]
# partarr=arr_2d[1:,1:]
# print(arr_2d, partarr, num, num2)



# arr= np.arange(1,11)
# result= arr > 5 # comparing the elements of the array with
# selected_arr= arr[result] #conditional selection
# #or
# selected_arr2= arr[arr>5] #conditional selection 
# print(arr, result, selected_arr, selected_arr2)








#####<<<<< np operations  >>>>>#####
# arr=np.arange(0,10)
# arr=arr+arr # operation (+-* **) of element by element 
# arr=arr+10 # operation (+-* **) of a number (scalar) to all elements 
# print(arr)


# arr=np.arange(0,10)
# arr1=arr/arr # deviding is tricky
# arr2=1/arr # deviding is tricky
# print(arr1,arr2)


#universal functions (google it ti find more about it , SciPy.org) 
# arr=np.arange(0,10)
# arr_sqrt=np.sqrt(arr) 
# arr_exp=np.exp(arr)
# np.max(arr)
# np.min(arr)
# np.sin(arr)
# np.log(arr)
# print(arr_sqrt)










# excersice


import numpy as np
print(np.zeros(10))
print(np.ones(10))
print(np.ones(10)+4)
print(np.arange(10,51,1))
print(np.arange(10,51,2))
print(np.arange(0,9,1).reshape(3,3))
print(np.eye(3))
print(np.random.rand(1))
print(np.random.randn(25))
print(np.arange(0.01,1.01,0.01).reshape(10,10))
example=np.linspace(0,1,20)
print(example)
print(np.sum(example))  # sumation of all columns
print(example.sum()) # sum of all elements
print(np.std(example))
