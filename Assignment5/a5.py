import math

########################
# PROBLEM 1
########################

#recursive functions
# Implement as per the directions in the PDF
def p(n):
    if n == 0:
        return 10000
    else:
        return p(n-1) + 0.02*p(n-1)


def c(n):
    if n == 1:
        return 9
    else:
       return 8*c(n-1) + 10**(n-1)

def d(n):
    
    if n == 0:
        return 1
    else:
        return 3*d(n-1) + 1
    
    

def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)
    
def e(n):
    if n == 1:
        return 12
    else:
        return -5*e(n-1)


def c_2(n, k):
    if n == 0 or n == k:
        return 1
    else:
        e1 = n - 1
        e2 = k - 1
        a_1 =  math.factorial((e1))/(math.factorial(e1-e2)*math.factorial(e2))       
        e1 = n - 1
        e2 = k 
        a_2 =  math.factorial((e1))/(math.factorial(e1-e2)*math.factorial(e2))  
        return a_1 + a_2
    #C (n , k) = n! / [ (n-k)! k! ]


def M(c,i):
    # print("function m ", c, i)

    if c == 0:
        return 1
    elif c < 0 or f(i) > 10:
        return 0
    else: 
        return M(c - f(c), i + 1) + M(c, i +1)


  


########################
# PROBLEM 2
########################

# INPUT: a list of numbers
# OUTPUT: a list containing the start of interval, end of interval and maximal sum
def msi(x):
    max= x[0] 
    current = x[0]
    start = 0
    end = 1
    current_start = 0

    for i in range(1, len(x)):
        num = x[i]
        if num > current + num:
            current = num
            current_start = i
        else:
            current += num

        if current > max:
            start = current_start
            end = i + 1
            max = current

    return [start, end, max]
   



########################
# PROBLEM 3
########################
# INPUT: list of cheese (0s or 1s)
# OUPUT: List with 0s moved to the front of the list and 1s at the back (see PDF for sample output)

def move(x):
   



       
        lo , hi = 0 , len ( x ) -1

        while lo < hi :

                    
            if (x[lo]==1 and x[hi] ==0):
                # swap the elments in index lo and index hi
                x[lo] = 0
                x[hi] = 1            
                    
            elif (x[lo]==0 and x[hi] ==1):        
                lo +=1
                hi -=1                   
                
            elif (x[lo]==1 and x[hi] ==1):
                hi -=1
            else:       
                lo +=1
                
        return x


########################
# PROBLEM 4
########################

#INPUT list of immutable objects
#RETURN probability distribution as a list



def makeProbability(xlst):
    dict = {}
    for i in xlst:
        if i in dict:
            dict[i] += 1
        else:
             dict[i] = 1




    for n in dict:
        prob = dict[n]/len(xlst)
        dict[n] = prob

    return list(dict.values())
    
    

    
def entropy(xlst):
    prob1 = makeProbability(xlst)
    sum1 = 0
    for i in prob1:
        p = i
        sum1  += -(p*math.log2(p))
    return round(sum1, 2)
      



########################
# PROBLEM 5
########################

#INPUT list of 0s 1s
#OUTPUT longest sequential run of 1s
def L(x):
    max1 = 0
    current = 0

    for num in x:
        if num == 1:
            current += 1
            maxx1 = max(max1, current)
        else:
            current = 0

    return max1


########################
# PROBLEM 6
########################
#INPUT non-negative integer
#OUTPUT True if divisible by 9, False otherwise

def div_9(x):
    n = str(x)
    length = len(n)
    first = 0

    for i in range(length):
        var = int(n[i])
        first += var
    
    first = str(first) 
    length_second = len(first)
    sum_second = 0
   
    for x in range(length_second):
        r = first[x]
        var_second = int(r)
        
        sum_second += var_second
        # if sum2/9 == 9 or 0:
        #     return True
        # else:
        #     return False
    return sum_second == 9 or sum_second == 0


########################
# PROBLEM 7
########################
#INPUT string base 17 A:10, B:11,..., F:15, G:16
#OUTPUT decimal 
def encode(msg, shift):
    alph = 'abcdefghijklmnopqrstuvwxyz{ '  
    enc = ''
    
    for i in msg:
        pos = (alph.index(i) + shift) % 28
        enc += alph[pos]
    return enc

def decode(msg, shift):
    alph = 'abcdefghijklmnopqrstuvwxyz{ '  
    dec = ''
    
    for n in msg:
        index = (alph.index(n) - shift) % 28
        dec += alph[index]
    return dec



########################
# PROBLEM 8
########################

# INPUT: integers x and y 
# OUPUT: Ouptut of recursive functions d() and e() as shown in the PDF
def d_1(x,y):
    a1 = min(x, y)
    b1 = max(x,y)
    if a1 == 1:
        return 1
    elif a1 == 0:
        return b1
    else:
        return d_1(b1%a1, a1)

def e_1(x,y):
    ans = d_1(x,y)
    if ans == 1:
        return x*y
    else:
        return ans*e_1(x//ans,y//ans)
        




########################
# PROBLEM 9
########################
# INPUT: a list of integers
# OUTPUT: As shown by the recursive function in the PDF
def m(lst):
    t = ()
    resulty = []
    final2 = []
    if len(lst) == 1:
        return []
    elif len(lst) == 2:
        # print(sum(lst))
        return [[sum(lst)]]
    
    for i in range(len(lst) - 1):
            
        pair_sum = lst[i] + lst[i + 1]
        resulty.append(pair_sum)
        
    
    final2.append(m(resulty))

    # print(result)
   
  


    return m(resulty) + [resulty]


########################
# PROBLEM 10
########################

# INPUT: list of candies
# Total empty space
# Please don't be confused by the fact that PDF shows the function accepting only one argument i.e. 'c' but here 
# we have two arguments i.e. 'c' and 'space', it will still work if you call package() with just one argument - package([3,3,3]) 
# because we have fixed space = 9, so Python will take that value as default even if you don't pass 'space' 
# explicitly in the test case (default value of space is 9).
def package(candies, space=9):
    nums = 0  
    c = space  
    
    for candy in candies:
        if candy <= c:
            c -= candy
        else:
            nums += c
            c = space - candy

    nums += c

    return nums


########################
# PROBLEM 11
########################

def encode(msg, shift):
    a = 'abcdefghijklmnopqrstuvwxyz{ '  
    
    
    
    empty = ''
    
    for i in msg:
        pos = (a.index(i) + shift) % 28
        empty += a[pos]
    return enc

def decode(msg, shift):
    a = 'abcdefghijklmnopqrstuvwxyz{ '  
    empty = ''
    
    for n in msg:
        index = (a.index(n) - shift) % 28
        empty += a[index]
    return empty




if __name__ == "__main__":


    # ## Problem 1
    # ## p(0) = 10000
    # ## p(1) = 10200.0
    # ## p(2) = 10404.0
    # ## p(3) = 10612.08
    # ## p(4) = 10824.3216
    # for i in range(5):
    #     print(p(i))
 
    
    # for i in range(2,6):
    #     print(c(i))
    # print(c(1))
    # ## c(2) = 82
    # ## c(3) = 756
    # ## c(4) = 7048
    # ## c(5) = 66384    

    # for i in range(5):
    #     print(d(i))
    # ## d(0) = 1
    # ## d(1) = 4
    # ## d(2) = 13
    # ## d(3) = 40
    # ## d(4) = 121
    
    # for i in range(6):
    #     print(f(i))
    # ## f(0) = 1
    # ## f(1) = 1
    # ## f(2) = 2
    # ## f(3) = 3
    # ## f(4) = 5
    # ## f(5) = 8

    # for i in range(1,6):
    #     print(e(i))
    # ## e(1) = 12
    # ## e(2) = -60
    # ## e(3) = 300
    # ## e(4) = -1500
    # ## e(5) = 7500

    # for i in range(1,6):
    #     for j in range(1,6):
    # #         # print("================================")
    # #         # print("calculate i and j ", i, j)
    #         print(M(i,j), " ", end="")
    # ## M((0, 0)) = 1
    # ## M((0, 1)) = 1
    # ## M((0, 2)) = 1
    # ## M((0, 3)) = 1
    # ## M((0, 4)) = 1
    # ## M((1, 0)) = 6
    # ## M((1, 1)) = 5
    # ## M((1, 2)) = 4
    # ## M((1, 3)) = 3
    # ## M((1, 4)) = 2
    # ## M((2, 0)) = 6
    # ## M((2, 1)) = 5
    # ## M((2, 2)) = 4
    # ## M((2, 3)) = 3
    # ## M((2, 4)) = 2
    # ## M((3, 0)) = 6
    # ## M((3, 1)) = 5
    # ## M((3, 2)) = 4
    # ## M((3, 3)) = 3
    # ## M((3, 4)) = 2
    # ## M((4, 0)) = 0
    # ## M((4, 1)) = 0
    # ## M((4, 2)) = 0
    # ## M((4, 3)) = 0
    # ## M((4, 4)) = 0    

    # for i in range(2,6):
    #     print(c_2(5,i))
    # ## c_2(5,2) = 10
    # ## c_2(5,3) = 10
    # ## c_2(5,4) = 5
    # ## c_2(5,5) = 1

    # #problem 2
    # x2 = [3,-6,-7,-5,-5,0,-5,3,0,-6]
    # print(msi(x2))

    # #problem 3
    # data3 = [[1,0],[0,1,0,1,0,1,0],[1,1,1,1,0,0,0,0],[0,1,0,1,1], [1,1,0,1],[0,0,1,0,1,1],[1,0,0,0,1,1,1]]
    # for d in data3:
    #     print(d)
    #     print(f"{d} => {move(d)}")
    

    # # #Problem 4
    # data1 = [["a", "b", "a", "c", "c", "a"],[1],[1,2,3,4]]
    # # # 1.46, -0.0, 2.0; 0 is minimal, log(n) is maximal
    # for d in data1:
    #     print(makeProbability(d))
   
       
    
 
 
    # # # #Problem  5
    # data2 = [[0],[1],[1,1,0,1,1,1],[0,1,1,0],[0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    # for d in data2:
    #     print(L(d))

    # # # #Problem 6
    # data3 = [99,0,18273645,22,27]
    # for d in data3:
    #     print(div_9(d), not bool(d % 9))

    # # # # Problem 7
    # data4 = ["G2","100","10","GA3","G","E2"]
    # for d in data4:
        
    #     print(secdec_dec(d), int(d,17))
    
       
    # # # problem 8
    # data = [[15,25],[6,7],[1,1],[1,2],[0,4],[210,2310]]
    # for i in data:
    #     print(e_1(*i))

    # #problem 9
    # x = [[1,2,3,4,5],[1],[3,4],[5,10,22],[1,2,3,4,5,6]]
    # for i in x:
    #     print(m(i))

    # #problem 10
    # candies = [[3,3,3],[3,1,2,2,1],[1,2,2,2,3],[3,2,2,3,1,3]]
    # for c in candies:
    #     print(package(c))
    
    # #problem 11

    # data = ["abc xyz","the cat", "i love ctwohundred"]
    # for i,j in enumerate(data,start=2):
    #     print(f"original msg {j}")
    #     print(f"encoded  msg {encode(j,i)}")
    #     print(f"decoded  msg {decode(encode(j,i),i)}")

    # secret_msg = encode("the quick brown fox jumps over the lazy dog", 24)
    # print(secret_msg)
    # print(decode(secret_msg,24))
    # print()