import math
Locations=tuple()
MyList=list()
(x1,y1)=(37.575869, 126.973548)
Locations=[(37.576501, 126.985436),(37.571618, 126.976551),(37.576501, 126.985436),(37.570171, 126.982905
),(37.565798, 126.977068)]
for i in Locations:
    MyList.append (math.sqrt((x1-i[0])**2+(y1-i[1])**2))   
print min(MyList)
    