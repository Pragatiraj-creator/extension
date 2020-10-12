#l=["py" : "python" , "txt" : "text" , "c" : "C" ]
fname = input("Enter the filename")
f =fname.split(".")
print("Extension of the file is : " + f[-1])
