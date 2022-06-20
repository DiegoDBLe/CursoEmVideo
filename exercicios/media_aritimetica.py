''' Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''

# a = {1:9, 2:8, 3:7, 4:6, 5:5}
#
# print(a.items())

# try:
#     [1,2,3][4]
# except IndexError:
#     print("IndexErro raised")
# except:
#     print("Exception raised")
# else:
#     print("Sommething else ")
# finally:
#     print("Cleaning up")


# a = 7
# a.__str__()
#
# print(a)


# a = {1:9,2:8,3:7,4:6,5:5}
# print(a.get(6))

# def f():
#     f()
#     return 42
#
# f()


# class test():
#     id = 0
#
#     def __init__(self):
#         self.id = id
#         id = 2
#         t = test(1)
#         t.id
#
#
# print(id)
# import re
#
# m = re.search(r'(ab[cd]?)',"acdeabdabcde")
# print(m.groups())
# from datetime import datetime
#
# type(datetime.date(201, 0o1, 01) - datetime.date(2011, 01, 0o1))



# # Somando dois digitos maneira 1
# def solution(n):
#     sum = 0
#     for digit in str(n):
#       sum += int(digit)
#     return sum
#
# # Somando dois digitos maneira 2
# def getSum(n):
#     sum = 0
#     for digit in str(n):
#         sum += int(digit)
#     return sum
#
#
# n = 12345
# print(getSum(n))

#
# def isBalanced(s):
#     st = list()
#
#     n = len(s)
#
#     for i in range(n):
#
#         # If current bracket is an opening
#         # bracket push it to stack.
#         # Se o colchete atual for uma abertura
#         # colchete empurre-o para empilhar.
#         if s[i] == '(':
#             st.append(s[i])
#
#         # If current bracket is a closing
#         # bracket then pop from stack if
#         # it is not empty. If stack is empty
#         # then sequence is not balanced.
#
#         # Se o colchete atual for um fechamento
#         # colchete, em seguida, pop da pilha se
#         # não está vazio. Se a pilha estiver vazia
#         # então a sequência não está balanceada.
#         else:
#             if len(st) == 0:
#                 return False
#             else:
#                 st.pop()
#
#     # If stack is not empty, then sequence
#     # is not balanced.
#
#     # Se a pilha não estiver vazia, então a sequência
#     # não está balanceado.
#     if len(st) > 0:
#         return False
#
#     return True
#
#
#
# print(isBalanced("{}[]{}"))
#
#
# def isBalancedSeq(s1, s2):
#     # Check if s1 + s2 is balanced or not.
#     if (isBalanced(s1 + s2)):
#         return True
#
#     # Check if s2 + s1 is balanced or not.
#     return isBalanced(s2 + s1)
#
#
# import Jython
#
# import math
#
#
# def distancia2d(x1, y1, x2, y2):
#     a = x2 - x1
#     b = y2 - y1
#     c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
#     return c
#
#
# def countStrUtil(dp, n, bCount=1, cCount=2):
#     # Base cases
#     if (bCount < 0 or cCount < 0):
#         return 0
#     if (n == 0):
#         return 1
#     if (bCount == 0 and cCount == 0):
#         return 1
#
#     # if we had saw this combination previously
#     if (dp[n][bCount][cCount] != -1):
#         return dp[n][bCount][cCount]
#
#     # Three cases, we choose, a or b or c
#     # In all three cases n decreases by 1.
#     res = countStrUtil(dp, n - 1, bCount, cCount)
#     res += countStrUtil(dp, n - 1, bCount - 1, cCount)
#     res += countStrUtil(dp, n - 1, bCount, cCount - 1)
#
#     dp[n][bCount][cCount] = res
#     return dp[n][bCount][cCount]
#
#
# # A wrapper over countStrUtil()
# def countStr(n):
#     dp = [[[-1 for x in range(n + 2)] for y in range(3)] for z in range(4)]
#     return countStrUtil(dp, n)
#
#
# # Driver code
# if __name__ == "__main__":
#     n = 3  # Total number of characters
#     print(countStr(n))
#







def abc (a,b):
    letra = str(a,b)
    print(type(letra))


abc("a","b")



