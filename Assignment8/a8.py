import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import os
import math 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics.cluster import rand_score
import math
import csv


# problem 1
# The following 4 functions are filled in by us as per the HW PDF.
def cost_2(x):
    return 2000  +  500 * x

def revenue(x):
    return 2000 * x - 10 * (x **2)

def profit(x):
    return revenue(x) - cost_2(x) 

def f(x):
    return x ** 6 - x - 1


# default h = 0.00001
# input function f and small amount (h)
# output approximation of the derivative of function f
def fp(f, h = 0.00001):
    return lambda x:( (f(x + h ) - f(x - h))/ (2 * h))


# input function f, it's derivative fp, value of x and h
# ouptut: root of f using newton-raphson
def newton(f, fp, x, h):
    while abs(f(x))>h:
        x = x - f(x) / fp(x)
    return round(x, 16)



# Problem 2

# input dataframe for iris
# output: return 3 values 
# 1. a numpy array of feature values of least correlated features
# 2. pair of indices of least correlated features as tuple 
# 3. absolute value of correlation  

def lst_c_2(data):
    corr = pd.DataFrame(data.iloc[:,[0,1,2,3]]).corr()
    x = 9999999
    m = 0
    y = 0
    for i in range(len(corr)) :
        for a in range(i+ 1, len(corr)) :
            if abs(corr.iloc[ i, a]) < x :
                x = abs(corr.iloc[ i,a ])
                m = i
                y = a
                
    return data.iloc[:,[m,y]], (m,y), x
        
    




#problem 3

# determine if x is even or not and return if

# input function, a, b, and number of intervals
# ouptut area under the function
def simpson(fn, a, b, n):
    y = 0
    delta = ((b-a)/n)
    interval = lambda x: a + x * delta
    for i in range(1, n):
        if (i % 2)== 0:
            y += 2 * fn(interval(i))
        elif (i % 2 )!= 0 :
            y += 4 * fn(interval(i))         
    y += fn(interval(0))
    y += fn(interval(n))
    
    answer = ((b-a)/(3*n)) * y
    return answer
                             


# problem 4

#the correct translation
actual = "PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSELSEIERARSRDLRRGPGPPGGEAAARRPLEAAGPLAGPRRRSGVAGRGGFQRGDGAVRGGPGAGARPVEEAGQQRRRLHDRGPGKVRQAGRPRPQGPSLPKPPGRASPTFLSQDLPGFPRHEDLLLPPGPEPRLLTSQSPRPEGGGRAEPRRGAPGRPTPRAVRAEPPARVPAASGPGQLPGERLPCWAPVPGRAPAGWVRGACGAGAGE-ALSARRSSWATACW-PSPGTTPETSAPRCRRRWTSS-ATLSRRWFPSTAELWVGGRGIPRRPSPCLSKASPRSSLLAVLSRGQDARGRR"

# INPUT path and file name of amino acid file
# RETURN a dictionary 
# Key is a tuple (c0, c1, ... , cn) where ci are codons
# Value is a pair [name, abbreviation] for the amino acid
# make sure to close the file

def get_amino_acids(path, filename):
    aminoDict = {} 
    
    with open(path + filename , 'r') as myfiles:
        for line in csv.reader(myfiles , delimiter=' '):
            full , abbr = line[0].strip(',') , line[1].strip(',')
            
            codons = tuple(codon.strip(',') for codon in line[2:] if codon)
            aminoDict[codons] = [full , abbr]
            
    return aminoDict

            
            
    

#INPUT path and file name of DNA sequence file
#RETURN a list [header, DNA]
#header is first line in the file
#DNA is a string of letters from remainder of file
#no whitespace
#make sure to close the file
def get_DNA(path, filename):
    my_list = []
    with open(path+filename, 'r') as myfiles :
        
        for z in  csv.reader(myfiles):
            seq = z[1:]
            h = z[0]
            if h != '' :    
                my_list.append(h)
                
            if seq != []:
                
                my_list.append(seq)
                

    return my_list

# INPUT A list containing our FASTA file and the dictionary obtained from get_amino_acids
# RETURN a string representing the protein
# using the dictionary

def translate(DNA_d, thedict):
    x = DNA_d[1]
    
    new_strings = ''
    
    for i in range(0, len(x), 3):
        codon = x[i: i + 3]
        for codon_list, [_, aa_code] in thedict.items():
            
            if codon in codon_list:
                new_strings += aa_code
    return new_strings
        
    



# problem 5
cost = lambda x:0.0001 * (x ** 3) - 0.08 * (x ** 2) + 40 * x + 5000


#input cost function
#output derivative
def marginal_cost(cost):
    return fp(cost)





# extra credit

#input data (need to have x_{i+1} - x_i = 1) for simplest model
#output polynomial 
def build_polyonomial(D):
    def delta(lst, x):
        return lst[0] if x == 0 else lst[x] - lst[x-1]

    def Delta(lst):
        return [delta(lst, a) for a in range (1, len(lst))]

    def dtable(lst):
        thres = [lst]
        while len(thres[-1]) > 1:
            thres.append(Delta(thres[-1]))
        return thres

    def rho(lst):
        return [rowsec [0] for rowsec in dtable(lst)]

    def prod(n):
        return math.factorial(n)
    

    def build_polynomial_recursive(table, idx):
        if len(table) == 1:
            return table [0][0]
        else:
            return table[0][0] + idx * build_polynomial_recursive(table[1:], idx)
        
    return lambda p: sum(rowinval * math.prod(p - valieds) for rowinval, valieds in zip(rho(D), range(len(D))))



if __name__ == "__main__":
    
    
    # problem 1
    
    # Instructions: In this problem, please comment the plotting related code (and the import of matplotlib and seaborn) 
    # before submitting to the Autograder. 
    # You can use the plots for testing on your VSC locally.
    
    # find the root
    # print(f"f(2) = {f(2)}")
    # print(f"f(1) = {f(1)}")
    # root = newton(f,fp(f),2,.0001)
    # print(f"f({root}) = {f(root)} ~ {round(f(root),2)}")

    # #find the maximal profit
    # m = fp(profit)
    # x = newton(m, fp(m), 1, .0001)
    # print(f"x = {x}")
    # print("The maximum profit is about ${0}".format(profit(round(x, 0))))
    # print(profit(75))

    # t = np.arange(0.0, 100.0)
    # fig,ax = plt.subplots()

    # ax.plot(t, profit(t),'g')
    # ax.plot(75,profit(75), 'bo--')
    # ax.set(xlabel ="Widgets Sold", ylabel="Profit ($)",
    # title = "Maximal Profit = ${0}".format(profit(75)))
    # ax.grid()
    # plt.show()



    
    # Problem 2
    # Instructions: In this problem, please comment the plotting related code (and the import of matplotlib and seaborn) 
    # before submitting to the Autograder. 
    # You can use the plots for testing on your VSC locally.
    
    # How to install seaborn
    # Just as we installed packages during the lab, we will follow the same command. However, some students
    # reported difficulty with package installation, so we are listing the command that we have found to be
    # working consistently with most students.
    # if you can not install with the given commands, please reach out soon in OH or over InScribe
    
    # 1. Open a new Terminal in your VSC
    # On MAC, type the following command and hit enter
    # python3 -m pip install seaborn  
    
    # on Windows
    # py -m pip install seaborn
    
    # To verify the installation, open a new terminal in VSC and type python, hit enter
    # You will that the symbol in the terminla changed to >>>- this means now we are under Python's shell
    # Patse the following command and hit enter
    
    # import seaborn as sn

    # If the command is successful (you won't see any output because we are only importing) then you will see >>> again
    # If you see errors then it means that either seaborn is not installed or it could not be found by the default Python
    # that is used by VSC. In that case, the solution can involve different options,
    # so please take our help either in OH or simply write on InScribe.
        
    # The actual code starts here
    
    # iris = pd.read_csv('Assignment8\iris.csv')
    # print(iris.shape)
    # print(iris.head())
    
    # iris_features, pair, value = lst_c_2(iris)
    # print(type(iris_features))
    
    # i,j = pair
    # print(f"Least corr columns: {iris.columns[i],iris.columns[j]} with {value}")
    
    # # using scikit-learn, cluster 
    # result = KMeans(n_clusters=3, random_state=0, n_init="auto")
    # iris_cluster_labels = result.fit_predict(iris_features)

    # # information
    # print("The cluster labels:")
    # print(iris_cluster_labels)
    # print("The cluster centers:")
    # print(result.cluster_centers_)
    # rand_index = rand_score(iris_cluster_labels,iris['species'])
    # print(f"The rand index is {round(rand_index,2)}")

    # # show how pure blocks are
    # species = ['setosa', 'versicolor','virginica']
    # dsp = { j:[]  for j in species }
    # for i,j in enumerate(iris_cluster_labels):
    #     dsp[iris.species[i]].append(j)
    # print("The three clusters and counts of members:")
    # for k,v in dsp.items():
    #     print(f"{k} {v.count(0),v.count(1),v.count(2)}")

    
    # # plot k-means with actual side-by-side
    # X,Y = [i[0] for i in iris_features],[i[1] for i in iris_features]
    # colors = [['b','g','c'][i] for i in iris_cluster_labels]
    # fig, ax = plt.subplots(1, 2)
    # sc1 = sn.scatterplot(data=iris,x='petal_width',y='petal_length',hue=iris_cluster_labels,ax=ax[0])
    # sc2 = sn.scatterplot(data=iris,x='petal_width',y='petal_length',hue='species',ax=ax[1])
    # sc1.set(title="K-means")
    # sc2.set(title="Actual")
    # plt.show()


    
    # problem 3
    
    # Instructions: In this problem, please comment the plotting related code (and the import of matplotlib and seaborn) 
    # before submitting to the Autograder. 
    # You can use the plots for testing on your VSC locally.
    
    # data = [[lambda x:3*(x**2)+1, 0,6,2],[lambda x:x**2,0,5,6],
    #     [lambda x:math.sin(x), 0,math.pi, 4],[lambda x:1/x, 1, 11, 6]]


    # for d in data:
    #     f,a,b,n = d
    #     print(simpson(f,a,b,n))

    # area = simpson(lambda t: 3*(t**2) + 1,0,6,10)
    # t = np.arange(0.0, 10.0, .1)
    # fig,ax = plt.subplots()
    # s = np.arange(0,6.1,.1)
    # ax.plot(t, (lambda t: 3*(t**2) + 1)(t),'g')
    # plt.fill_between(s,(lambda t: 3*(t**2) + 1)(s)) 
    # ax.grid()
    # ax.set(xlabel ="x", ylabel=r"$f(x)=3x^2 + 1$",
    # title = r"Area under the curve $\int_0^6\,f(x)$ ~" + f"{round(area,2)}")
    # plt.show()

    # problem 4
    
    # Please revisit (if need be) the basics of File I/O form the labs and lectures.
    # For testing you code in VSC, you have to use path that works on your system.
    # But, before submitting to the Autograder, you should keep the path as "", because Autograder has 
    # it's own OS and it's own FileSystem, and the path which works on your system may not be valid on the Autograder.
    # Remember that path is a variable so it can be set to any value.
    
    # If you hard code the path - the tests will work on your system but fail on the Autograder.
    # Another common mistake we found is that several students were manually putting '/' or '\' between
    # path and filename -- again this can work on your system but may fail on Autograder because Autograder will use it's
    # own path and filename. The best way to make the correct path is to just use path + filename when reading the file.
    # Where you provide the correct path and filename outside the function.
    
    
    # path = "Assignment8/"
    # fn1, fn2 = "amino_acids.txt", "DNA.txt"
    # aa_d = get_amino_acids(path, fn1)
    # DNA_d = get_DNA(path, fn2)
    # protein = translate(DNA_d, aa_d)

    # # print("Dictionary")
    # print(aa_d)
    # print("FASTA file")
    # print(DNA_d)
    # print("Translations match:", str(protein == actual))

    # #should return "PLHS"    
    # print(translate(["nothing", "CCACTGCACTCA"], aa_d))

    # #should returns "D-"
    # print(translate(["nothing", "GACTAA"], aa_d))

    #problem 5
    # U,C = [],[]
    # for unit in range(200,650,50):
    #     U.append(unit)
    #     mc = round(marginal_cost(cost)(unit),0)
    #     C.append(mc)
    #     print(f"For {unit} marginal cost is {mc}")
        
    # plt.plot(U,C,'b-')
    # plt.plot(300,round(marginal_cost(cost)(300)),'ro')
    # plt.xlabel("Units of Production")
    # plt.ylabel("Cost $")
    # plt.title(r"Marginal cost Cost(x) =  $0.0001x^3 - 0.08x^2 + 40x + 5000$")
    # plt.show()



    #extra credit
    # Only attempt if other functions are done.

    # D = [(0,-2),(1,5),(2,7),(3,10)]
    # pf = lambda x:x**3 - (11/2)*(x**2) + (23/2)*x - 2
    # f = build_polyonomial(D)
    # for i in range(7):
    #     print(i,pf(i),f(i))


    # x = np.linspace(0,6,100)
    # X,Y = [x for x,_ in D],[y for _,y in D]
    # plt.plot(X,Y,'ro')
    # plt.plot(x,f(x),'b-')
    # plt.title("Newton Binomial Interpolation Formula")
    # plt.show()
    
    print()