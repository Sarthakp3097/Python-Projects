import math
import random as rn
import numpy as np
# import matplotlib.pyplot as plt
import os 
import csv


print(os.getcwd())

# PROBLEM ONE

data = []
#INPUT path and filename
#OUTPUT list of parent, child pairs
#CONSTRAINT use csv reader
def get_data(path, filename):
    content = open('Assignment6/family.txt', 'r')
    a = csv.reader(content)
    my_data = []
    for line in a:
        my_data.append(line)
    return my_data

#input parent name
#output children
#constraint using comprehension
def get_child(name):
    return [child for parent, child in data if parent == name]


#input parent name
#output true if has children
#constraint using comprehension
def has_children(name):
    return bool(get_child(name))

#input child name
#output parent of child
#constraint using comprehension
def get_parent(name):
    parents = [parent for parent, child in data if child == name]
    return parents


#input child name1, child name2
#output true if children have same parent
#constraint using comprehension
def siblings(name1,name2):
    p1 = get_parent(name1)
    p2 = get_parent(name2)
    return (bool(p1 == p2))
 
 
#input grandparent name1, grandchild name2
#output true if name1 is grandparent to name2
#constraint using comprehension 
def grandparent(name1, name2):
    children = get_child(name1)
    gkids = [child for child in children if name2 in get_child(child)]

    return bool(gkids)

#input nothing
#output all names
#constraint list comprehension only
def get_all():
    return [k for k in [i for i,j in data] + [j for i,j in data]]

#input name1, name2
#output true if name1 and name 2 are cousins, i.e., have the same grandparents
def cousins(name1,name2):
    gp1 = get_parent(get_parent(name1)[0])
    gp2 = get_parent(get_parent(name2)[0])
    # print("1st grandparent", gparent_1, "this is second gparent", gparent_2)
    return (bool(gp1 == gp2))


# Problem 2
# input n: total space (size), v: tiles and 
# output all possible patterns where the tiles add exactly to the the space (n)
def tiles(n, v, lst):
    if sum(lst[-1]) > n:
        return []
    if sum(lst[-1]) == n:
        return [lst[-1]]
    patterns = []
    for x in v:
        for pattern in lst:

            temp = pattern + [x]
            patterns.extend(tiles(n, v, [temp]))

    final = [list(x) for x in set(tuple(x) for x in patterns)]
    
    return final




#problem 3
# input: a list of numbers
# output: a pair containing the sum and boolean vector (see PDF for sample output)
def max_adjacent(nums):
    
    if len(nums) == 0:
        return [0, []]
    elif len(nums) == 1:
        return [nums[0], [1]]
    elif len(nums) == 2:
        return [max(nums), [1 if nums[0] > nums[1] else 0, 1 if nums[1] >= nums[0] else 0]]

    mlist = [0] * len(nums)
    mlist[0] = nums[0]
    mlist[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        mlist[i] = max(mlist[i - 1], mlist[i - 2] + nums[i])

    p = [0] * len(nums)
    x = len(nums) - 1
    while x >= 0:
        if mlist[x] == mlist[x - 1]:
            x -= 1
        else:
            p[x] = 1
            x -= 2  
    return [mlist[-1], p]
    # example = nums
    

    # a = example[::2]
    # b = example[1::2]
    # c = example[:1]
    # d = example[1:]
    # final = c + d
    
    # index_a = [1 if (i % 2 == 0) else 0 for i in range(len(example))]
    # index_b = [1 if (i % 2 == 1) else 0 for i in range(len(example))]
    


    
    # sum_a = np.sum(a)
    # sum_b = np.sum(b)
    # if len(nums) > 3:
    #     final = []
    # return final

    
    # if sum_a >= sum_b:
    #     return [sum_a, index_a]
    # else:
    #     return [sum_b, index_b]

    



########################
# PROBLEM 4
########################


# INPUT path and filename (payrollwins.txt)
# OUTPUT payroll and number of wins as a list
# Ouptut example: [[209,89], [139,74]]
# CONSTRAINT use csv reader
def get_data_1(path, filename):
    lst = []
    f = ('Assignment6/payrollwins.txt')  # Construct the full file path

    with open(f, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            payroll = int(row[0])
            wins = int(row[1])
            lst.append([payroll, wins])
           

    return lst
        


#INPUT data points (x0,y0),...,(xn,yn)
#OUTPUT best regression slope m_hat, intercept b_hat, and R_sq
def std_linear_regression(data):
    n = len(data)
    xyp = sum([x*y for x,y in data])
    xs = sum([x for x,_ in data])
    ys = sum([y for _,y in data])
    xsq = sum([x**2 for x,_ in data])
    ysq = sum([y**2 for _,y in data])
    Sxy = xyp - ((xs*ys)/n)
    Sxx = xsq - (xs**2/n)
    
    m = round(Sxy/Sxx, 3)
    b = round(((ys - m*xs)/n), 3)
    for x, y in data:
        x_val = int(x)
        y_val = int(y)
        y_val_2 = int(y**2)
        sst = (ysq) - ((ys**2)/n)
        sse = ysq - (b * ys) - (m * xyp)
        final = round((sst - sse)/sst, 3)
    
    return m, b, final





#### Problem 5

# INPUT path and filename (fish_data.txt)
# OUTPUT two separate lists, first one containing the age and second containing 
# the length as given in the fish_data.txt file 
# Ouptut example: [1,2,3, ...], [4.8, 8.8, 8.0, ...]
# CONSTRAINT use csv reader
# make sure to get rid of the first line that just contains the column names (we don't want that)
def get_fish_data(path, name):
    x = []
    y = []

    with open(path, 'r') as fish:
        content = fish.readlines()
        for line in content[1:]:
            s = line.strip().split(',')
            x.append(float(s[0]))
            y.append(float(s[1]))
    return x, y

#INPUT lists X values, Y values of data and degree of the polynomial
#RETURN a polynomial of degree three
def make_function(X,Y,degree):
    nums = np.polyfit(X, Y, degree)
    graphyy = np.poly1d(nums)

    return graphyy



#### Problem 6*
#input string and positive integer n
#output a list of the longest string that have no more than n distinct symbols
#Doesn't work
def max_n(str, n):
   
    b = 0
    maximum = 0
    final = ""
    c = {}
    t = str
    for x in range(len(t)):
        char = t[x]
        c[char] = c.get(char, 0) + 1
        while len(c) > n:
            start_char = t[b]
            c[start_char] -= 1
            if c[start_char] == 0:
                del c[start_char]
            b += 1
        if x - b + 1 > maximum:
            maximum = x - b + 1
            final = t[b:x+1]
    return [final]



#problem 7

#input a tuple of model parameters, second parameter is the number of trials
#output the percent success rounded to two decimal places
def simulation(model_parameters, num_trials):
    b, p, m = model_parameters
    g = num_trials
    final = 0
    for x in range(g):
        money = b
        while money > 0 and money < m:
            outcome = np.random.binomial(1, p, 1)[0]
            if outcome == 1:
                money += 1
            else:
                money -= 1
        if money == m:
            final += 1

    perc = (final / num_trials) 
    return round(perc, 2)





if __name__ == '__main__':
    
    # uncomment to test
    # Before sbmitting to the Autograder: 
    # Make sure to comment the code for plotting graph in P4 and also the import of matplotlib on the top of this file
    # You can use that code to make the graph on your system and test but comment it before the submission

    # problem 1
    # data = get_data('Assignment6/family.txt', "family.txt")
    # print(data)
    # print(has_children('0')) #true
    # print(has_children('7')) #false
    # print(get_child('6'))
    # print(get_parent('g'))
    # print(siblings('7','A')) #true
    # print(siblings('2','7')) #false
    # print(grandparent('0','3')) #true
    # print(grandparent('0','7')) #false
    # print(get_all())
    # print(cousins('3','6')) #true
    # print(cousins('3','5')) #false


    #problem 2
    # n = 6
    # v = [1,2,3]
    # print(tiles(n,v,[[i] for i in v]))
    # for i in tiles(n,v,[[i] for i in v]):
    #     print(sum(i), end="")
    # n = 4
    # v = [1,2]
    # print(tiles(n,v,[[i] for i in v]))
    # for i in tiles(n,v,[[i] for i in v]):
    #     print(sum(i), end="")    

    #problem 3
    # data = [[5,1,4,1,5],[5,6,2,4],[4,5,1,1],[1,5,10,4,1],[1,1,1,1,1]]
    # for d in data:
    #     print(max_adjacent(d))

    #problem 4

    # data6 = get_data_1("provide path", "payrollwins.txt")
    # m_hat, b_hat, R_sq  = std_linear_regression(data6)
    # print(m_hat,b_hat,R_sq)
    
    # Comment the code for plotting (and the import of matplotlib up top) before you submit to the Autograder.
    # You can test as much as you want on your system but before the submission - please comment the code for
    # plotting.
    # plt.plot([x for x,_ in data6],[y for _,y in data6],'ro')
    # plt.plot([x for x,_ in data6],[m_hat*x + b_hat for x,_ in data6],'b')
    # plt.xlabel("$M Payroll")
    # plt.ylabel("Season Wins")
    # plt.title(f"Least Squares: m = {m_hat}, b = {b_hat}, R^2 = {R_sq} ")
    # plt.ylabel("Y")
    # plt.show()

    # #problem 5
    # name = "fish_data.txt"
    # X,Y = get_fish_data("Assignment6/fish_data.txt", name)
    # data5 = [[i,j] for i,j in zip(X,Y)]
    # print(data5)
      
    # plt.plot(X,Y,'ro')
    # xp = np.linspace(1,14,10)
    # degree = 3
    # p3 = make_function(X,Y,degree)
    # plt.plot(xp,p3(xp),'b')
    # plt.xlabel("Age (years)")
    # plt.ylabel("Length (inches)")
    # plt.title("Rock Bass Otolith")
    # plt.show()

    #problem 6
    # data = ["aaaba", "abcba", "abbcde","aaabbbaaaaaac","abcdeffg"]
    # for d in data:
    #     for i in range(1,7):
    #         print(f"{d} with {i} max is\n {max_n(d,i)}")
    
    
    #problem 7
    # model_parameters = (2,.6,4) #starting amount, probablity of win, goal
    # print(simulation(model_parameters,100000))
    
    print()