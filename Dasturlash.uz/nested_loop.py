#1 
# a = int(input("number = "))
# s = 0
# for i in range(1,a+1):
#     s = s + (1/i)
# print(s)

#2
# a = int(input("n = "))
# for i in range(a):
#     print(a*"*")
    
#3
# n = int(input("n = "))
# for i in range(n+1):
#     for j in range(n+1):
#         print(f"({i},{j})", end = " ")
#     print("\n")

#4 
# n  =  int(input("n = "))
# for i in range(n+1):
#     for j in range(n+1):
#         if i == 0 or j == 0 or i == 9:
#             print(f"({i},{j})", end=" ")
#     print()

#5 
# n=int(input("n - "))
# for i in range(n+1):
#     for j in range(n+1):
#         if i == 0 or i ==9 or j%2 == 0:
#             print(f"({i},{j})", end=" ")
#         else:
#             print(end="      ")
#     print()

#6 List of numbers
# n = int(input("n = "))
# s = 0
# l = []
# for i in range(1,(n*n + 1)):
#     print(f"{s}\t", end=" ")
#     s +=1
#     l.append(s)
#     if len(l)%10 == 0:
#         print()

#7 Dioganal
# n = int(input("n = "))
# for i in range(n):
#     print("*")
#     for j in range(n):
#         print(" "*i, end = " ")

#8 numbers dioganali 
# n = int(input("n = "))
# for i in range(n+1):
#     print(f"({i},{i})")
#     for j in range(n+1):
#         print(i*" ", end = " ")
        
#9 inverted dioganal
# n = int(input("n = "))
# for i in range(n):
#     print(n*" ","*")
#     n -=1
  
#10 Right-angled triangle
# n = int(input("n - "))
# for i in range(n+1):
#     print("*"*i)

#11 Inverted right-angled triangle
# n = int(input("n = "))
# for i in range(n+1):
#     print(n*"*")
#     n -=1

#12 Number triangle
# n = int(input("n = "))
# for i in range(1, (n+1)):
#     for j in range(1, i+1):
#         print(j, end = "")
#     print()

#13 triangle of numbers options
# n = int(input("n = "))
# for i in range(n+1):
#     print(str(i)*i)
