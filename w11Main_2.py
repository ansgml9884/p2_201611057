def Survey():
    Data_Satis=[
        [13.1, 37.1],
        [10.6, 34.6],
        [27.1, 40.0],
        [16.2, 37.8],
        [11.4, 29.8],
        [12.2, 26.5],
        [13.5, 29.7],
        [13.7, 37.6]]
    Data_unSatis=[
        [8.7, 1.5],
        [13.4, 1.9],
        [2.9, 1.5],
        [6.8, 0.8],
        [14.8, 4.9],
        [14.9, 4.4],
        [11.1, 2.4],
        [4.1, 1.2]]

    sum_Satis=0
    sum_unSatis=0

    for i in Data_Satis:
        sum_Satis=i[0]+i[1]

    for e in Data_unSatis:
        sum_unSatis=e[0]+e[1]


    print "sum of Satisfaction :",sum_Satis
    print "sum of Unsatisfaction :",sum_unSatis
    print "average of Satisfaction :",float(sum_Satis/len(Data_Satis))
    print "average of Satisfaction :",float(sum_unSatis/len(Data_unSatis))

def lab11_2():
    Survey()

def main(): 
    lab11_2()

if __name__=="__main__":
    main()

input()
