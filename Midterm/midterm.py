import math

# Problem 1
#input percent_decrease as positive integer, r as float
#output hours as float
def next_injection(percent_decrease,r):
   i = 0
   lst = []
   initial = 100
   change = r
   amt = percent_decrease
   time = round(-((math.log((amt/initial)))/change), 3)
   return time
#input hours as float
#output tuple (x,y) where x hours, y minutes
def convert_HM(hours):
    hours1 = hours % 1
    minute = math.floor(60 * hours1)
    hours2 = str(hours)
    final = hours2.split('.')
    final1 = final[0]
    final2 = round(float(final1))
    return final2, minute

# Problem 2
#input x number and possibly empty list of numbers
#output number, sum of list, list where sum list is <= x
def m(x,lst):
    newlist = []
    sum = 0

    for i in lst:
        if i < x:
            newlist.append(i)
        elif x == []:
            sum = 0
    for x in newlist:
        sum += x
    return x, sum, lst


if __name__ == "__main__":

       ## Problem 1
    data = [[50, 0.2],[35, 0.44],[20,.01]]

    for d in data:
        hours = next_injection(*d)
        h_, m_ = convert_HM(hours)
        print(hours, h_,m_ , math.isclose(hours,h_ + m_/60,abs_tol = .1))

    # Problem 2
    data = [[0,[0,0,1]],[1,[0,0,0]],[2,[1,0,1,0,2]],
                [1,[2,1,0]],[4,[1,0,2,0,.5,.1,0,5]],
                [5,[5,5]],[2,[-1,2,0,1,-1]],[1,[]]]

    for d in data:
        print(m(*d))