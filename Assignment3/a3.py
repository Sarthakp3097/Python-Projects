import math

#Problem 1

#INPUT n0 start colony size, m growth rate, t time
#RETURN final colony size
def N(n_0, m, t):
    return1 = 0
    return1 = n_0*math.exp(m*t)
    return math.ceil(return1)

#INPUT t days
#RETURN number of teeth
def N_t(t):
    return2 = 0
    return2 = 71.8*math.exp(-8.96*math.exp(-0.0685*t))


    return math.ceil(return2)


#INPUT pressures Pi, Pf 
#RETURN work joules
def W(P_i, P_f):
    return3 = 0
    return3 = 8.314*300*(math.log(P_i/P_f))
    return math.ceil(return3)



#INPUT V miles per hour, A area, C_l lift coefficient
#RETURN lbs 
def L(V,A,C_l):
    return4 = 0
    return4 = 0.0033*(V**2)*A*C_l
    return math.ceil(return4)



###########################################################################
# Functions for Problem 2
###########################################################################
#INPUT coef = (a,b,c)
#RETURN tuple ('up'|'down', (vertex, y-value of vertex))
###########################################################################
def q(coef):
    a = coef[0]
    b = coef[1]
    c = coef[2]
    v = -b/(2*a)
    y = round(a*(v**2)+b*v+c,2)
    x = round(v,2)
    if a < 0:
        up_down = "down"
    if a > 0:
        up_down = "up"
    vertex = [x, y]
   
    return up_down, vertex

# print(q((97, 90, 62)))
# print(q((1,-10.2,26.01)))

#q(97,90,62) returned [ "up", [ -0.46, 41.13 ] ], but expected [ "up", [ -0.46, 41.12 ] ].


    


    




###########################################################################
# Functions for Problem 3
###########################################################################
#INPUT object x and list lst
#RETURN True if object occurs in the list
#CONSTRAINT You cannot use 'x in y' -- must use bounded looping
def m(x,lst):
    
    position = 0
    while position < len(lst):
        
        if lst[position] == x:
            return True
        position = position +1

    return False

receipt = [[1,1.45],[3,10.00],[2,1.45],[5,2.00]]
tax_rate,no_tax = 7/100, [33,5,2]


#INPUT receipt= [[x0,y0],[x1,y1],...,[xn,yn]]
# x is item, y is cost
# tax_rate is the tax on taxable items
# no_tax is a list of items not taxable
#RETURN total amount owed (round values to 2 nearest decimal places)
def amt(reciept, tax_rate, no_tax):
    
    amt = 0
    index = 0
    max = len(reciept)
    no_tax_length = len(no_tax)
    while index < max:
        price = reciept[index][1]
        
        if m(reciept[index][0], no_tax):
            amt = amt + price
            #print("non-taxable", reciept[index][0])
        else:
            amt = amt + price*(1+tax_rate)      
        index = index+1

    print(amt(receipt,tax_rate, no_tax))
    return round(amt,2)

# reciept = [[1,1.45],[3,10.00],[2,1.45],[5,2.00]]
# tax_rate,no_tax = 7/100, [33,5,2]
# print(amt(reciept,tax_rate, no_tax))



###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT p0 = (x0,y0) p1 = (x1,y1)
#RETURN dictionary y = mx + b
def make_line(p0,p1):
    x0,y0,x1,y1 = *p0,*p1
  
    x = round((y1 - y0)/(x1 - x0),2)
    y = round(y0 - (m*x0),2)
    return {'x':x, 'y':y}
# x = 0
# x = input()
# y = m*x +b

# pass

#INPUT two lines as dictionary
#RETURN a point (x,y) of intersection or "same line", "parallel lines" 
#rounded to two places
def intersection(l0,l1): 
    if l0["m"]  == l1["m"] and l0["b"] ==l1["b"]:
        return ("same line")
    elif l0["m"]  == l1["m"] and l0["b"] !=l1["b"]:
        return ("parallel lines")
    else: 

        x = (l1["b"]-l0["b"])/(l0["m"]-l1["m"])
        y = x * l1["m"] + l1["b"]
        x = round(x,2)
        y = round(y,2)
        return (x ,y)
   
   
   
    



    






# p0 = (32,32)
# p1 = (29,5)
# p2 = (15,10)
# p3 = (49,25)
# p4 = (15,30)
# p5 = (50,15)

# l0,l1 = make_line(p0,p1),make_line(p2,p3)

# print(intersection(l0,l1))
# l0 = make_line(p4,p5)
# print(intersection(l0,l1))

# p6,p7,p8 = (0,0),(1,1),(2,2)
# p9,p10 = (0,1),(1,2)
# print(intersection(make_line(p6,p7),make_line(p7,p8))) # same line
# print(intersection(make_line(p6,p7),make_line(p9,p10))) # parallel lines



###########################################################################
# Functions for Problem 5
###########################################################################
#INPUT List of numbers
#RETURN Various means or error message

def arithmetic_mean(nlst):
    nlst1 = len(nlst)
    if nlst1 == 0:
        return "Data Error: 0 values"
    sum = 0
    index = 0
    while index < nlst1:
        sum = sum + nlst[index]
        index = index + 1
    mean = sum/nlst1
    return mean
    

def geo_mean(nlst):
    len_nlst = len(nlst)
    if len_nlst == 0:
        return "Data Error: 0 values"
    sum = 0
    index = 0
    while index < len_nlst:
        sum = sum + math.log(nlst[index])
        index = index + 1
    final = math.e**(sum/len_nlst)
    return final

def har_mean(nlst):
    len_nlst = len(nlst)
    if len_nlst == 0:
        return "Data Error: 0 values"
    sum = 0
    index = 0
    while index < len_nlst:
        if nlst[index] == 0:
            return "Data Error: 0 in data"
        sum = (1/(nlst[index]))+ sum
        index = index + 1
    mean = len_nlst/sum
    return mean

def RMS_mean(nlst):
    len_nlst = len(nlst)
    if len_nlst == 0:
        return "Data Error: 0 values"
    sum = 0
    index = 0
    while index < len_nlst:
        sum = sum + (nlst[index])**2
        index = index + 1
    mean = math.sqrt(sum/len_nlst)
    return mean
#har_mean(1,3,10,3,6,7,5,2) returned 0.34702380952380957, but expected 2.8816466552315605.

# nlst = [1,3,10,3,6,7,5,2]
# print(har_mean(nlst))

###########################################################################
# Function for Problem 6
###########################################################################
#INPUT x object, list of objects, integer y
#RETURN true if x occurs at least y times, false otherwise
def occur_at_least(x,y,lst):
    #[1, [1, 2, 1, 2, 1, 1], 4]
    lst_len = len(lst)
    index = 0
    counter = 0
    while index < lst_len:
        if lst[index] == x:
            counter = counter + 1
        #index = index + 1
        index += 1
    if counter >= y:  
        return True
    else:
        return False



###########################################################################
# Functions for Problem 7
###########################################################################
#input two objects x,y and list
#returns True if x occurs strictly more than y in lst, False otherwise
def occurs_more(x,y,lst):
   
    
    x1 = lst.count(x)
    y1 = lst.count(y)
    if lst == []:
        return True
    elif y1 < x1:
        return True
    
    else:
        return False
    



#occurs_more(2,2,2,2,2,6,3,2,2,3,6,6,2,5,2,8,2,6,2)
   
    #print(occurs_more(lst[1]))

    
    
# lst = [2,2,2,2,2,6,3,2,2,3,6,6,2,5,2,8,2,6,2]
# print("this is my list", occurs_more(5,8, lst))

# print(occurs_more(1,2,lst))
# print(occurs_more(2,3,lst))
# print(occurs_more(2,3,[]))




#input two objects x, y and list
#return if the number of times x,y occur in list are equal, then return the list
#if x occurs more than y, then remove the occurrences from the left side until
#their counts are equal, then return the list
#if y occurs more than x, the same procedure
def equal_remove(x,y,lst):
    index = 0
    new_list_y = []
    new_list_x = []
    skipcount = 0
    new_list = []
    length_list = len(lst)
    while index < length_list:
        if y == lst[index]:
            new_list_y.append(index)
        if x == lst[index]:
            new_list_x.append(index)  
            
        index = index + 1
    

    # print("my new list is", new_list_y, "and my positions for x are", new_list_x)
    length_new_list_y = len(new_list_y)
    length_new_list_x = len(new_list_x)
    delta_y = length_new_list_y - length_new_list_x
    delta_x = length_new_list_x - length_new_list_y

    if length_new_list_y > length_new_list_x:
        #print("I am going to be reducing", delta_y, "y's")
        index = 0
        while index < length_list:
            if lst[index] == y and skipcount < delta_y:
               skipcount = skipcount + 1
               index = index +1
               continue
            new_list.append(lst[index])
                            
            index = index + 1
    elif length_new_list_x > length_new_list_y:
        #print("I am going to be reducing", delta_x, "x's")
        index = 0
        while index < length_list:
            if lst[index] == x and skipcount < delta_x:
                skipcount = skipcount + 1
                index = index + 1
                continue
            else:
                new_list.append(lst[index])
            index = index + 1
    else:
        index = 0
        while index < length_list:
            new_list.append(lst[index])
            index = index + 1



    
    #print("length of y list is", length_new_list_y, "and the length of the x's is", length_new_list_x)
    #print(" my new new list is", new_list)
    #equal_remove(2,1,7,6,4,3,5,5,4,3,8,3,8,5,8,7,6,3,5,4,3,3) returned [], but expected [ 7, 6, 4, 3, 5, 5, 4, 3, 8, 3, 8, 5, 8, 7, 6, 3, 5, 4, 3, 3 ].
          #expected [ 7, 6, 4, 3, 5, 5, 4, 3, 8, 3, 8, 5, 8, 7, 6, 3, 5, 4, 3, 3 ]
    # lst = [2,1,7,6,4,3,5,5,4,3,8,3,8,5,8,7,6,3,5,4,3,3]

    # print(equal_remove(1,2,lst))

    
    #print("original list", lst)
    #print("update list", new_list)
    return new_list

# lst = [2,1,7,6,4,3,5,5,4,3,8,3,8,5,8,7,6,3,5,4,3,3]

# print(equal_remove(1,2,lst))
    
   
# def my_test():
#     listX = []
#     listX.append(1)
#     listX.append(99)
#     print ("list X ", listX)

    


        
            
    

        

    

    
    
    # things = lst
    # apples = x
    # oranges = y
    # number_apples = lst.count(apples)
    # number_oranges = lst.count(oranges)
    # if number_apples > number_oranges:
    #     number_apples.remove(apples) == number_oranges
    #     return number_apples
    # if number_oranges > number_apples:
    #     number_oranges.remove(oranges) == number_apples
    #     return number_oranges
    


###########################################################################
# Functions for Problem 8
###########################################################################
#INPUT list of numbers
#RETURN True if geometric series, False otherwise
def is_geo(xlst):
    for i in range(len(xlst) - 2):
        if xlst[i] * xlst[i + 2] != xlst[i + 1] ** 2:
            return 0
    for i in range(len(xlst) - 1):
        if xlst[i] == 0 and xlst[i + 1] != 0:
            return 0
        if len(xlst) == 2:
            return 0
    return 1

###########################################################################
# Functions for Problem 9
###########################################################################
#INPUT pair of points in 2D
#RETURN distance round to two decimal places
def net_displacement(p0,p1):
        calcDist =0 
       
        x_1 = p0[0]
        x_2 = p1[0]
        y_1 = p0[1]
        y_2 = p1[1]
        calcDist = math.sqrt(((x_1 - x_2)**2)+((y_1-y_2)**2))


        return round(calcDist,2)
        

#INPUT starting position (x,y) and list of one step directions w,e,s,n that move the positon
#of x,y
#RETURN a tuple final destination, distance, distance from start
def track(start_pos, movement):
    
    end_pos = [start_pos[0], start_pos[1] ]
 

    count  =0 
    m = len(movement)
    
    while count < m:
        m  = movement[i]
        if m == 's':
            end_pos[1] = end_pos[1] -1
        elif m == 'n':
            end_pos[1] = end_pos[1] +1  
        elif m == 'e':
            end_pos[0] = end_pos[0] +1
        elif m == 'w':
            end_pos[0] = end_pos[0]-1

        i = i + 1

    displaceVal = net_displacement(start_pos, end_pos)
    total_movements = len(movement)

    return end_pos, total_movements, displaceVal
# lst = ['n','e','e','w','s']
# print(track([7,8],lst))

# data_m9 = [[(0,0), list(10*'n' + 15*'e' + 10*'s'+15*'w')],
#       [(0,0), list(3*'n' + 4*'e')],
#       [(1,2), list(3*'s' + 4*'w')]]

# for d in data_m9:
#     #print(*d)
#     print(track(*d))






###########################################################################
# Functions for Problem 10
###########################################################################
#INPUT pair of tuples from tracking
#RETURN distance betweem two ending places 
def final_distance(m0,m1):
    # print("these are my thingies", m0, m1)
    end_point_0 = m0[0]
    end_point_1 = m1[0]

    value = net_displacement(end_point_0, end_point_1)
    return round(value,2)



    

    
    
    


# print("problem 10 ")
# data_m10 = [[(0,0), list(10*'n' + 15*'e' + 10*'s'+15*'w')],
#          [(0,0), list(3*'n' + 4*'e')],
#           [(1,2), list(3*'s' + 4*'w')]]     
# print(final_distance(track(*data_m10[1]),track(*(data_m10[2]))))     



###########################################################################
# Functions for Problem 11
###########################################################################
#INPUT conference and game
#RETURN the dictionary conference after changing wins,losses, percentages of teams (there are no ties)
def update(conference, game):
   
    
    val = list(game)
    
    player1 = list(game.keys())[0]
    player2 = list(game.keys())[1]
    score1 = game[player1]
    score2 = game[player2]
    if score1 > score2:
        winner = player1
        loser = player2
        score_win = score1
        score_loss = score2
    elif score2 > score1:
        winner = player2
        loser = player1
        score_win = score2
        score_loss = score1
    
    conference[winner]['W']+=1
    conference[winner]['PCT'] = round(conference[winner]['W']/(conference[winner]['W']+conference[winner]['L']),3)

    conference[loser]['L']+= 1
   
    conference[loser]['PCT'] = round(conference[loser]['W']/(conference[loser]['W']+conference[loser]['L']),3)

    return conference
#update([object Object]) returned , but expected { "IU": { "W": 14, "L": 1, "PCT": 0.933, "Home": [ 13, 0 ] },
#  "PU": { "W": 6, "L": 6, "PCT": 0.5, "Home": [ 8, 4 ] }, 
# "IOWA": { "W": 11, "L": 3, "PCT": 0.786, 
# "Home": [ 11, 1 ] }, "NW": { "W": 1, "L": 11, "PCT": 0.083, "Home": [ 6, 6 ] } }.
# 
# 
# 
# 
# big_10_women = {'IU':{'W':12,'L':1,'PCT':.923, 'Home':(13,0)},
#                 'PU':{'W':6,'L':6,'PCT':.500, 'Home':(8,4)}, 
#                 'IOWA':{'W':11,'L':1,'PCT':.917, 'Home':(11,1)},
#                 'NW':{'W':1,'L':11,'PCT':.083,'Home':(6,6)}}
# print(big_10_women['IU'],big_10_women['IOWA'])
# update(big_10_women,{'IU':87,'IOWA':78})
# print(big_10_women['IU'],big_10_women['IOWA'])

###########################################################################
# Functions for Problem 12
###########################################################################
#INPUT amt and list of donations
#RETURN tuple: amt, donations left, the amount of the goal left
def go_fund_me(amt, donations):
    #print(donations)
    total_sum = 0
    extra = []

    for d in donations:
        if total_sum < amt:
            total_sum = total_sum + d
        
        else: 
            extra.append(d)

    extra_amount = total_sum - amt
    return amt, extra, extra_amount


# data12 = [[100,[10,15,20,30,29,13,15,40]],
#         [100,[]],
#         [100,[30,4]]]

# for d in data12:
#     print(go_fund_me(*d))
# print(go_fund_me(50, [45,47,78]))


###########################################################################
# Functions for Problem 13
###########################################################################
#INPUT credit score cr and list of potential clients [[n0,cd0],[n1,cd1],...,[nm,cdm]] where n is name, cd is unweighted dictionary of credit values
#RETURN list of people and their score that is strictly greater than cr; if nobody qualifies, then return empty list
def loan(cr, lst):
    candidates = []
    for l in lst:
        name = l[0]
        dict = l[1]
        score = dict['P']*0.35+dict['A']*0.3+dict['L']*0.15+dict['N']*0.10+dict['C']*0.10
        if score >= cr:
    
            candidates.append([name, score])
    return candidates



# data = [['x',{'P':600, 'L':700,'A': 500, 'N': 170, 'C': 250}],
#         ['y',{'P':550, 'L':720,'A': 500, 'N': 230, 'C': 250}],
#         ['b',{'P':560, 'L':710,'A': 500, 'N': 221, 'C': 250}],
#         ['c',{'P':800, 'L':700,'A': 200, 'N': 100, 'C': 150}],
#         ['a',{'P':800, 'L':800,'A': 600, 'N': 250, 'C': 150}],
#         ['z',{'P':800, 'L':800,'A': 500, 'N': 250, 'C': 150}]]
# print(loan(550,data))


#  (.35) P (Payment History)
# • (.30) A (Amounts Owed)
# • (.15) L (Length of Credit History)
# • (.10) N (New Credit)
# • (.10) C (Credit Mix)






    # a_c =[]
    # for n, dets in lst:
    #     sum = a_c.append_sum(n, sum)
    #     if cr<= sum:
    #         a_c.append(n, sum)
    #     return a_c
    # def calculate_weighted_sum(applicant):
    #     weight = 0



#Problem 14
#INPUT current temperature T(t) of fish (T_t, environment T_e, temperature of fish and lst of what dogs were doing hours ago]
#OUTPUT The time (in hours) that elapsed after the murder reported as a float
#you must determine k from problem and formula from description
def time(T_t, T_e, T_0):
    k = 0.28768
    t = math.log((T_t - T_e)/(T_0 - T_e))/(-k)
    return t

# no_alibis = {"Ursala":[3,4],"Shilah":[2,2.5],"Kaiser":[1,2]}
# T_t = 81
# T_e = 65
# T_0 = 85
# time_discovered = 4 #PM Dr. D's living room
# suspects = []

# time_of_murder = time_discovered - time(T_t, T_e, T_0)
# for name,times in no_alibis.items():
#     start,end = times
#     if start <= time_of_murder <= end:
#         suspects.append(name)

# print(f"The suspect(s) {suspects}")



# def equal_remove(x,y,lst):
#     index = 0
#     new_list_y = []
#     new_list_x = []
#     skipcount = 0
#     new_list = []
#     length_list = len(lst)
#     while index < length_list:
#         if y == lst[index]:
#             new_list_y.append(index)
#         if x == lst[index]:
#             new_list_x.append(index)

#         #if y != lst[index]:
#          #   new_list.append(lst[index])


            
            
#             #print( f"value {y} in position/index {index}" )

#         index = index + 1

#     print("my new list is", new_list_y, "and my positions for x are", new_list_x)
#     length_new_list_y = len(new_list_y)
#     length_new_list_x = len(new_list_x)
#     delta_y = length_new_list_y - length_new_list_x
#     delta_x = length_new_list_x - length_new_list_y

#     if length_new_list_y > length_new_list_x:
#         print("I am going to be reducing", delta_y, "y's")
#         index = 0
#         while index < length_list:
#             if lst[index] == y and skipcount < delta_y:
#                skipcount = skipcount + 1
#                index = index +1
#                continue
#             new_list.append(lst[index])
                            
#             index = index + 1
#     elif length_new_list_x > length_new_list_y:
#         print("I am going to be reducing", delta_x, "x's")
#         index = 0
#         while index < length_list:
#             if lst[index] == x and skipcount < delta_x:
#                 skipcount = skipcount + 1
#                 index = index + 1
#                 continue
        


#             else:
#                 new_list.append(lst[index])
#             index = index + 1

    
#     #print("length of y list is", length_new_list_y, "and the length of the x's is", length_new_list_x)
#     #print(" my new new list is", new_list)
    
#     print("original list", lst)
#     print("update list", new_list)
#     return new_list
    
   
# def my_test():
#     listX = []
#     listX.append(1)
#     listX.append(99)
#     print ("list X ", listX)

    






# index = 0



# lst = [1,2,2,1,2,1,2,2,2,1,1,1,1,1,1,1,1,1,1]
# print(my_function(1,2,lst))
#my_test()


 





if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here
    """
    # #problem 1
    # print(N(500,100,4)) 
    # print(N_t(1000))
    # print(W(10,1))
    # print(L(33.8,512,0.515))

    #problem 2
    # print(q((-2.6,7.6,-10)))
    # print(q((1,-10.2,26.01)))

    #problem 3
    # receipt = [[1,1.45],[3,10.00],[2,1.45],[5,2.00]]
    # tax_rate,no_tax = 7/100, [33,5,2]
    # print(amt(receipt,tax_rate, no_tax))
    # print(amt(receipt,10/100,[]))

    # #problem 4
    # p0 = (32,32)
    # p1 = (29,5)
    # p2 = (15,10)
    # p3 = (49,25)
    # p4 = (15,30)
    # p5 = (50,15)
 
    # l0,l1 = make_line(p0,p1),make_line(p2,p3)
    # print(intersection(l0,l1))
    # l0 = make_line(p4,p5)
    # print(intersection(l0,l1))
    
    # p6,p7,p8 = (0,0),(1,1),(2,2)
    # p9,p10 = (0,1),(1,2)
    # print(intersection(make_line(p6,p7),make_line(p7,p8))) # same line
    # print(intersection(make_line(p6,p7),make_line(p9,p10))) # parallel lines

    #problem 5
    # print(arithmetic_mean([1,2,3]))
    # print(geo_mean([2,4,8]))
    # print(geo_mean([]))
    # print(har_mean([1,2,3]))
    # print(RMS_mean([1,3,4,5,7]))

    #problem 6
    # data6 = [[1,[1,2,1,2,1,1],4], [1,[1,2,1,2,1,1],3],
    #     [1,(1,2,1,2,1,0),4], ]

    # for d in data6:
    #     print(d)
    #     print(occur_at_least(*d))

    #problem 7
    # lst = [2,2,3,1,2,1,1,2]
    # print(occurs_more(1,2,lst))
    # print(occurs_more(2,3,lst))
    # print(occurs_more(2,3,[]))
 
    #lst = [0, 0, 1,10, 1, 0, 3,1,1,1,1,2]
    #(equal_remove(1,2,lst))
    
    # print(equal_remove(1,3,lst))
    # print(equal_remove(2,3,lst))
    # print(occurs_more(2,3,(equal_remove(2,3,lst))))

    #problem 8
    # xlst = [1/2,1/4,1/8,1/16,1/32]
    # print(is_geo(xlst))
    # xlst = [1,-3,9,-27]
    # print(is_geo(xlst))
    # xlst = [625,125,25]
    # print(is_geo(xlst))
    # xlst = [1/2,1/4,1/8,1/16,1/31]
    # print(is_geo(xlst))
    # xlst = [1,-3,9,-26]
    # print(is_geo(xlst))
    # xlst = [625,125,24]
    # print(is_geo(xlst))
    # print(is_geo([1/2,1/4]))

    # #problem 9
    # data_m9 = [[(0,0), list(10*'n' + 15*'e' + 10*'s'+15*'w')],
    #       [(0,0), list(3*'n' + 4*'e')],
    #       [(1,2), list(3*'s' + 4*'w')]]

    # for d in data_m9:
    #     print(track(*d))

    #problem 10
    # data_m10 = [[(0,0), list(10*'n' + 15*'e' + 10*'s'+15*'w')],
    #       [(0,0), list(3*'n' + 4*'e')],
    #       [(1,2), list(3*'s' + 4*'w')]]

    # print(final_distance(track(*data_m10[1]),track(*(data_m10[2]))))

    # #problem 11
    # big_10_women = {'IU':{'W':12,'L':1,'PCT':.923, 'Home':(13,0)},
    #             'PU':{'W':6,'L':6,'PCT':.500, 'Home':(8,4)}, 
    #             'IOWA':{'W':11,'L':1,'PCT':.917, 'Home':(11,1)},
    #             'NW':{'W':1,'L':11,'PCT':.083,'Home':(6,6)}}
    
    # print(big_10_women['IU'],big_10_women['IOWA'])
    # update(big_10_women,{'IU':87,'IOWA':78})
    # print(big_10_women['IU'],big_10_women['IOWA'])
    
    # update(big_10_women, {'IU':8,'IOWA':7})
    # print(big_10_women)
    
    # update(big_10_women, {'PU':87,'NW':91})
    # print(big_10_women)
    
    # update(big_10_women, {'IOWA':89,'PU':75})
    # print(big_10_women)
    

    # #problem 12
    # data12 = [[100,[10,15,20,30,29,13,15,40]],
    #     [100,[]],
    #     [100,[30,4]]]

    # for d in data12:
    #     print(go_fund_me(*d))
    # print(go_fund_me(50, [45,47,78]))

    #Problem 13
    # data = [['x',{'P':600, 'L':700,'A': 500, 'N': 170, 'C': 250}],
    #     ['y',{'P':550, 'L':720,'A': 500, 'N': 230, 'C': 250}],
    #     ['b',{'P':560, 'L':710,'A': 500, 'N': 221, 'C': 250}],
    #     ['c',{'P':800, 'L':700,'A': 200, 'N': 100, 'C': 150}],
    #     ['a',{'P':800, 'L':800,'A': 600, 'N': 250, 'C': 150}],
    #     ['z',{'P':800, 'L':800,'A': 500, 'N': 250, 'C': 150}]]
    # print(loan(550,data))

    #problem 14
    #initial scene of the crime data
   
    # no_alibis = {"Ursala":[3,4],"Shilah":[2,2.5],"Kaiser":[1,2]}
    # T_t = 81
    # T_e = 65
    # T_0 = 85
    # time_discovered = 4 #PM Dr. D's living room
    # suspects = []

    # time_of_murder = time_discovered - time(T_t, T_e, T_0)
    # for name,times in no_alibis.items():
    #     start,end = times
    #     if start <= time_of_murder <= end:
    #         suspects.append(name)

    # print(f"The suspect(s) {suspects}")