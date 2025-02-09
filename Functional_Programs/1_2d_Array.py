
no_rows=int(input("enter the number of rows: "))
no_columns=int(input("enter the number of columns: "))


"""def PrintArray(array):
    print(array)       

array=[[0 for i in range(no_columns)] for i  in range(no_rows)]
PrintArray(array)"""

array=[]
for i in range(no_columns):
    rows=[]
    for j in range(no_rows):
        element=int(input(f"enter the element at ({i},{j}) position: "))
        rows.append(element)
    array.append(rows)
   
   
print("2D-array is: ")
for row in array:
    print(row)    
        
        


