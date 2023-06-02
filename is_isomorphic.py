


import time
def isIsomorphic(s,t):
    print(set(s))
    print(set(t))
    print(set(zip(s,t)))
  



    

start = time.time()
#nums = [2,1,-1]
# s = "egg"
# t = "add"
# s = "paper"
# t = "title"
s = "foo"
t = "bar"
#nums = [1,2,3]
print(isIsomorphic(s,t))
end = time.time()
print(f"Code execution time : {(end-start)*1000}ms")
