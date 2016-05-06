my2dlist=[
[74425, 76326],
[61164, 61636],
[109688, 115744],
[144796, 146776],
[174996, 181676],
[177841, 177434],
[204630, 205980],
[223373, 232245],
[161055, 166130],
[171576, 176735],
[279169, 293772],
[239450, 251066],
[148690, 156510],
[182977, 196992],
[237792, 242641],
[283869, 296762],
[209344, 210282],
[118965, 114441],
[186503, 186856],
[195734, 203014],
[254381, 249472],
[212401, 229111],
[271654, 295354],
[319197, 335045],
[229829, 231671]]
#리스트의 리스트
Gu=['Jongno','Jung','Yongsan','Seongdong',
    'Gwangjin','Dongdaemun', 'Jungnang', 
    'Seongbuk','Gangbuk','Dobong','Nowon',
    'Eunpyeong','Seodaemun','Mapo','Yangcheon',
    'Gangseo','Guro','Geumcheon','Yeongdeungpo',
    'Dongjak','Gwanak','Seocho','Gangnam',
    'Songpa', 'Gangdong']

sum_m=0
sum_w=0
sum=0
for i in my2dlist:
    sum_m=sum_m+i[0]
print "남자합계:",sum_m
for i in my2dlist:
    sum_w=sum_w+i[1]
print "여자합계:",sum_w

average_m=sum_m/25
print "남자평균:",average_m

average_w=sum_w/25
print "여자평균:",average_w


"""구별합계"""

print "구별합계:"
for i in my2dlist:
    sum_gu=i[0]+i[1]
    print sum_gu,
    

"""구별 평균"""
print "구별평균:"
for i in my2dlist:
    average_gu=(i[0]+i[1])/2
    print average_gu,
    
"""구별 총인구 그래프로 나타내기"""
d=dict()
for i in range(25):
    d.update({Gu[i]:my2dlist[i][0]+my2dlist[i][1]})
    
import matplotlib 
import matplotlib.pyplot as plt 
plt.bar(range(len(d)),d.values(), align='center') 
plt.xticks(range(len(d)), d.keys()) 
plt.show() 

 
plt.show()
