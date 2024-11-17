import math
# import matplotlib.pyplot as plt



###########################################################################
# Functions for Problem 1
###########################################################################
#INPUT dlst = [day, month, year]
#RETURN string corresponding to the day of the week (i.e. "Mon", "Sun", etc)
week = {1:"Mon", 2:"Tue", 3:"Wed", 4:"Thu", 5:"Fri", 6:"Sat", 7:"Sun"}
def a(dlst):
    d = dlst[0]
    m = dlst[1]
    y = dlst[2]
    
    vara = y - ((14-m)/12)
    return vara


def b(dlst):
    x = a(dlst) + a(dlst)/4 - a(dlst)/100 + a(dlst)/400
    b = math.floor(x)
    return b

def c(dlst):
    m = dlst[1]
    c = m + 12*((14-m)/12) - 2
    return c
    

def day(dlst):
    d = dlst[0]
    var_day = (d + b(dlst) + (31*(c(dlst)/12)))%7
    var_day = week[var_day]
    
    
    return var_day





###########################################################################
# Functions for Problem 2
###########################################################################
#INPUT t = (a,b,c)
#RETURN return complex or real roots
def q(t):
    a = t[0]
    b = t[1]
    c = t[2]
    d = b**2 - 4*a*c
    if d >= 0:
        first_root = round((-b - math.sqrt(d))/(2*a), 2)
        second_root = round((-b + math.sqrt(d))/(2*a), 2)
    else:
        r = round(-b/(2*a),2)
        i = round(math.sqrt(-1*d)/(2*a),2)
        root1 = (r + i * 1j)  # Remove quotes around the complex number
        root2 = (r - i * 1j)
        # first_root =f"({r:.2f}+{i:.2f}j)" 
        # second_root = f"({r:.2f}-{i:.2f}j" 
    return (root1), (root2)





###########################################################################
# Functions for Problem 3
###########################################################################
#INPUT a nested list of people encoded as 0's and 1's. v0 and v1 are the respective lists respresenting the people pairs.
# You'll be comparing the smallest degree of difference between each sublist representing each person.
# RETURN person pair with the smallest degree (smallest degree of difference between the person pair lists)

def inner_prod(v0,v1):
    n = 0
    c = 0
    while n < len(v1):
        c = c + v1[n]*v0[n]
        n = n + 1
   
    return c
#print(inner_prod(v0, v1))
    
def mag(v):
    final = math.sqrt(inner_prod(v, v))
    return final

def angle(v0,v1):
    rad = math.acos(inner_prod(v0, v1)/ (mag(v0)*mag(v1)))
    deg = rad*(180/math.pi)
    return round(deg, 2)

def match(people):
    #people = [j, f, c, n]
    """
    (j, f), (j, c), (j, n), 
    (f,c), (f, n)
    (c, n)

    """

    
    i = 0
    all = []
    while i < len(people):
        j = i + 1
        while j < len(people):
            p1 = people[i]
            p2 = people[j]
            ang = angle(p1, p2)
            all.append([p1, p2, ang])
            #print("this is a person 1:", p1, "and this is person 2:", p2)
            j = j + 1
        i = i + 1


    # for p in people:
    #     print("this is a person", people)
        
    return all


def best_match(scores):
    best_v = 100  

    best_pair = scores[0]
    for s in scores:
        value = s[2]

        if best_v > value:
            best_v = value
            best_pair = s

    return best_pair





###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT tuple of quadratic (ax^2 + bx + c)
#RETURN tuple (m,n) cofficients for real solutions a(x+m)^2 + n = 0
#CONSTRAINT round to 2 places
def c_s(coefficients):
    a = coefficients[0]
    b = coefficients[1]
    c = coefficients[2]
    m = round(b/(2*a), 2)
    n = round(c - (b**2/(4*a)), 2)
    return m, n


#INPUT coefficients for quadratic ax^2 + bx + c 
#RETURN return real roots uses c_s
def q_(coefficients):
    m,n = c_s(coefficients)
    if n > 0:
        r = -m 
        i = math.sqrt(n)
        fr =(f"({r}-{i}j)")
        sr = (f"({r}+{i}j)")
    else:
        fr = round(-m + math.sqrt(-n),2)
        sr = round(-m - math.sqrt(-n), 2)
    return sr, fr
    




###########################################################################
# Functions for Problem 5
###########################################################################
# INPUT List of numbers
# RETURN Various means
def mean(lst):
    # x0 = lst[0]
    # x1 = lst[1]
    # x2 = lst[2]
   
    # n = 0
    # var_mean = 0
    # while n <= len(lst):
    #     # total = sum(lst, n)
    #     n = n + 1
    sum = 0
    for x in lst:
        sum += x
    final = round(sum/len(lst), 2)
        
  
    return final

def var(lst):
    # mu = mean(lst)
    counter = 0
    sum = 0
    for x in lst:
        

        counter += ((x- mean(lst))**2)
        
        var_var = round(counter/ len(lst), 2)
       
    return var_var 

def std(lst):
    answer = round(math.sqrt(var(lst)), 2)
    return answer

def mean_centered(lst):
    new_list = []
    n = 0
    old_list = 0
    mu = mean(lst)
    while n < len(lst):
        list = old_list + lst[n]
        n = n + 1
        new_list.append(list - mu)
    return new_list





###########################################################################
# Functions for Problem 6
###########################################################################
# INPUT supply and demand coefficients
# RETURN solution of quadratic equations
def equi(s,d):
   

    a1 = s[0]
    b1 = s[1]
    c1 = s[2]

    a2 = d[0]
    b2 = d[1]
    c2 = d[2]

    difference_a, difference_b, difference_c = a1 - a2, b1 - b2, c1 - c2

    discriminant = b1**2 - 4*a1*c1

    if discriminant < 0:
        return None  # No real roots

    x1 = (-b1 + discriminant**0.5) / (2*a1)
    x2 = (-b1 - discriminant**0.5) / (2*a1)

    if a1 * x1**2 + b1 * x1 + c1 > 0:
        return x1
    else:
        return x2
    
    # (a1 - a2)x^2 + (b1- b2)x + (c1-c2)= 0
   




###########################################################################
# Functions for Problem 7
###########################################################################
#INPUT parameters to LV model
#OUTPUT two lists history_rabbit, history_fox of populations
def rabbit_fox(br, dr, df, bf, rabbit, fox, time_limit):
    i = 0
    history_rabbit = []
    history_fox = []
    
    while i < time_limit:
        history_rabbit.append(rabbit)
        history_fox.append(fox)
        
        # Calculate the population changes using Lotka-Volterra equations
        next_rabbit = rabbit + (rabbit * br - rabbit * fox * dr)
        next_fox = fox + (bf * dr * rabbit * fox - fox * df)
        
        # Apply the ceiling function to ensure populations are non-negative integers
        rabbit = math.ceil(next_rabbit)
        fox = math.ceil(next_fox)
        
        i += 1
        
    return history_rabbit, history_fox



###########################################################################
# Functions for Problem 8
###########################################################################
# INPUT container, sample size n
# OUTPUT random selection of size n in any order
# CONSTRAINT uses random
# This is with replacement
def sub_strings(str,cnt):
   
    for i in range(len(str)):
        for x in range(i+1, len(str) + 1):
            string = str[i:x]
            if string != '':
                if string in cnt:
                    cnt[string] += 1
                else:
                    cnt[string] = 1

    return cnt
 
    
        


    



###########################################################################
# Functions for Problem 9
###########################################################################
#INPUT values for annuity
#OUTPUT deposit amount needed
def deposit(S,i,n):
    ann = (((1+i)**n)-1)/(i)
    output = round(S/ann,2)
    return output




#INPUT sinking fund values except deposit
#OUTPUT a list of period, deposit, interest, accrued total fund
def sinking_fund(final_amt, r, m, y):
    d = deposit(final_amt, r/m, m*y )
    pcnt = m*y
    amt = 0 
    interest = 0
    all = []
    for i in range(pcnt): 
        interest = round(amt*(r/m), 2)
        amt = round(amt + interest + d, 2)
        period = [i, d, interest, amt]
        all.append(period)
    return all
        



###########################################################################
# Functions for Problem 10
###########################################################################
#INPUT list of numbers
#OUTPUT Boolean if geometric series
def is_geometric_sequence(lst):
    #lst is a tuple with multiple elements inside of it
    # print("is geometric", lst)
    i = 1
    ratio = lst[1]/lst[0]
    # print("this is my ration", ratio)
    while i < len(lst):
        j = i - 1
        first = lst[i]
        second = lst[j]
        i = i + 1
        # print("elements", element_1, element_2)
        if ratio != first/second:
            return False
    return True
            


        




###########################################################################
# Functions for Problem 11
###########################################################################
#INPUT portfolio of stock price, shares, market
#OUTPUT current total value
def value(portfolio, market):
    totalp = 0
    totalv = 0

    for stock, (purchase_price, num_shares) in portfolio['stock'].items():
        market_price = market[stock]
        stock_value = market_price * num_shares
        totalv += stock_value

        purchase_value = purchase_price * num_shares
        totalp += purchase_value

    percentage_change = ((totalv - totalp) / totalp) * 100
    final = round(percentage_change)
    return float(final)



if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here
    """

    #problem 1
    # print(day([14,2,2000]))
    # print(day([14,2,1963]))
    # print(day([14,2,1972]))

    # #problem 2
    # print(q((3,4,2)))
    # print(q((1,3,-4)))
    # print(q((1,-2,-4)))

    # #problem 3
    # people0 = [[0,1,1],[1,0,0],[1,1,1]]
    # print(match(people0))
    # print(best_match(match(people0)))

    # people1 = [[0,1,1,0,0,0,1],
    #            [1,1,0,1,1,1,0],
    #            [1,0,1,1,0,1,1],
    #            [1,0,0,1,1,0,0],
    #            [1,1,1,0,0,1,0]]
    # print(best_match(match(people1)))
    # #output is ([1, 1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0, 0], 39.23)

    # v0,v1 = (2,3,-1), (1,-3,5)
    # print(angle(v0,v1)) #122.83

    # v0,v1 = (3,4,-1),(2,-1,1)
    # print(angle(v0,v1)) #85.41

    # v0,v1 = (5,-1,1),(1,1,-1)
    # print(angle(v0,v1)) #70.53


    # #problem 4 pairs should be identical
    # print(q((1,-4,-8)), q_((1,-4,-8)))
    # print(q((1,3,-4)),q_((1,3,-4)))
   
    
    # #problem 5
    # lst = [1,3,3,2,9,10]

    # print(mean(lst))
    # print(var(lst))
    # print(std(lst))
    # print(mean(mean_centered(lst)))

    # #problem 6
    # s = (-.025,-.5,60)
    # d = (0.02,.6,20)
    # print(equi(s,d))
    
    # s = (5,7,-350)
    # d = (4,-8,1000)

    # print(equi(s,d))

    #problem 7
    # br = 0.03
    # dr = 0.0004
    # df = 0.25
    # bf = 0.11
    # rabbit = 3000  #initial population size
    # fox = 200  #initial population size
    # time_limit = 2000
    # history_rabbit, history_fox = rabbit_fox(br,dr,df,bf,rabbit,fox, time_limit)

    # # #uncomment to see time, rabbit, fox populations
    # for j in range(0,2000,200):
    #     print(j, history_rabbit[j], history_fox[j])


    # plt.plot(list(range(0,time_limit)),history_rabbit)
    # plt.plot(list(range(0,time_limit)),history_fox)
    # plt.xlabel("Time")
    # plt.ylabel("Population Size")
    # plt.legend(["Rabbit","Fox"])
    # plt.title("Lotka-Volterra Model for Rabbit & Fox")
    # plt.show()

    
    # #problem 8
    # data = ["abcabc","ccccc",""]
    # for d in data:
    #     cnt = {}
    #     sub_strings(d,cnt)
    #     print(cnt)

    # #problem 9
    # S = 30000
    # m = 4
    # r = 10/100
    # y = 2
    # for i in sinking_fund(S,r,m,y):
    #     print(i)


    #problem 10
    # data = [[1,2,4,6],[2,4,8,16],[10,30,90,270,810,2430]]
    # for d in data:
    #     print(is_geometric_sequence(d))


    #problem 11
    # portfolios =  {'A':{'stock':{'x':(41.45,45),'y':(22.20,1000)}},
    # 'B':{'stock':{'x':(33.45,15),'y':(12.20,400)}}}
    # market = {'x':43.00, 'y':22.50}


    # for name, portfolio in portfolios.items():
    # print(f"{name} {value(portfolio,market)}")