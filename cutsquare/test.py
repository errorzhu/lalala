# -*- coding=utf-8 -*-

import itertools
import os


#加载数据，得到大矩形组合sl[]，小矩形组合 l[]
def loaddata():

     data=open('data.txt','r+')
     lines=data.readlines()
     for line in lines:
         t=(float(line.split()[0]),float(line.split()[1]),float(line.split()[2]))

         l.append(t)
     data.close()

     datas = open('datas.txt', 'r+')
     lines = datas.readlines()
     for line in lines:
         t = (float(line.split()[0]), float(line.split()[1]))

         sl.append(t)
     datas.close()

#元组排序，统一元组第一位为长，第二位为宽
def tup_sort(tup):

    if tup[0]>tup[1]:
        t=(tup[0],tup[1])
    else:
        t=(tup[1],tup[0])

    return t

#分割，传入大矩形，得到两种裁剪的小矩形
def dived(S,s):
    l1=[]
    l2=[]
    X=S[0]
    Y=S[1]
    x=s[0]
    y=s[1]
    suba1=(x,Y-y)
    suba2=(Y,X-x)
    subb1=(X,Y-y)
    subb2=(y,X-x)
    l1.append(tup_sort(suba1))
    l1.append(tup_sort(suba2))
    l2.append(tup_sort(subb1))
    l2.append(tup_sort(subb2))
    return l1,l2
#裁剪，传入大矩形，得到挖出的拼接矩形，和长宽数量
def cut(S,s):
    X = S[0]
    Y = S[1]
    x = s[0]
    y = s[1]
    if(x==0 or y==0):
        return (0,0,0,0)
    xr=s[1]
    yr=s[0]
    nx=int(X/x)
    ny=int(Y/y)
    sx=nx*x
    sy=ny*y
    nxr = int(X / y)
    nyr = int(Y / x)
    sxr = nxr * xr
    syr = nyr * yr

    if((sx*sy)>(sxr*syr)):
        t=(sx,sy,nx,ny)
    else:
        t=(sxr,syr,nxr,nyr)

    if(t[2]>0 and t[3] >0 ):
        return t
    else:
        return (0,0,0,0)

#排列出小矩形的组合方式
def combine(l):

    s=list(itertools.permutations(l, 3))


    return s


#生成小矩形map，用来查找二维数组位置
def genmap(l):
    i = 0
    for ll in l:
        map[ll] = i
        i = i + 1

#生成全零的二维矩阵
def genarray(m,n):

    arr=[]


    for i in range(m):
        a=[0 for i in range(n)]
        arr.append(a)
    return arr

#填入二维矩阵
def fillarray(s):
    n = 0

    for ss in s:
        k1 = ss[0].split(':')[0]
        v1 = ss[0].split(':')[1]
        k2 = ss[1].split(':')[0]
        v2 = ss[1].split(':')[1]
        k3 = ss[2].split(':')[0]
        v3 = ss[2].split(':')[1]
        n1 = map[eval(k1)]
        n2 = map[eval(k2)]
        n3 = map[eval(k3)]
        arr[n][n1] = eval(v1)
        arr[n][n2] = eval(v2)
        arr[n][n3] = eval(v3)
        n = n + 1


# def search(n):
#     s=0
#     for k in map:
#         if(map[k]==n):
#             s=k[2]
#             break
#     return s

#得到lingo语句
def genexpression(nnnn):
    sr=''
    for i in range(nnnn):
        bd = ''
        x = 0
        num=l[i][2]
        for a in arr:

            if(a[i]!=0):
                bd=bd+str(a[i])+'*'+'p'+str(x)+'+'
            x=x+1
        bd=bd[:-1]+'>='+str(num)
        bdl.append(bd)
    n=0

    for mm in sl:
        sss = ''
        bs=float(mm[0])*float(mm[1])
        if (n+1<=len(pn)):
            for i in range(pn[n], pn[n + 1]):
                sss = sss + 'p' + str(i) + '+'
            sr=sr+ '(' + sss[:-1] + ')' + '*' + str(bs)+'+'
            #sr = sr+'(' + sss[:-1] + ')' + '+'

            n = n + 1
    genlingo(sr[:-1])
    genlingo('\r\n')
    # sss=''
    # bs=S[0]*S[1]
    # for i in range(len(s)):
    #     sss=sss+'p'+str(i)+'+'
    # print '('+sss[:-1]+')' +'*'+str(bs)

    ligo=''
    for i in range(size):
        ligo = ligo +'@bin('+ 'p' + str(i) + ');'
    genlingo(ligo)
    genlingo('\r\n')

    ppp=''
    for i in range(size):
        ppp = ppp +'p' + str(i) + '+'
    genlingo(ppp[:-1])
    genlingo('\r\n')


#写入文件
def genlingo(s,filename="lingo.txt"):

    w = open(filename, "a")
    w.write(s)
    w.close()

#核心：裁剪递归算法，得到组合
def getrur(S,sg,n,rresult):


    r=cut(S,sg[n])
    l1,l2=dived(S,r)
    rresult=rresult+str(sg[n])+":"+str(r[2])+"*"+str(r[3])+'+'

    if (n > 1):
        ans.append(rresult[:-1])
        return rresult
    getrur(l1[0],sg,n+1,rresult)
    getrur(l1[1], sg, n + 1,rresult)

    getrur(l2[0], sg, n + 1,rresult)
    getrur(l2[1], sg, n + 1,rresult)

#生成组合表达式
def genc(l1,l2,l3,l4):
    s1 = l1.split('+')
    s2 = l2.split('+')
    s3 = l3.split('+')
    s4 = l4.split('+')
    t = (s1[0], s1[1].split(":")[0] + ":" + s1[1].split(":")[1] + "+" + s3[1].split(":")[1],
         s1[2].split(":")[0] + ":" + s1[2].split(":")[1] + "+" + s2[2].split(":")[1] + "+" + s3[2].split(":")[1] + "+" +
         s4[2].split(":")[1])
    return t


#对递归解组合
def combineans(ans):
    ll=[]
    t1=genc(ans[0],ans[1],ans[4],ans[5])
    t2=genc(ans[0],ans[1],ans[6],ans[7])
    t3=genc(ans[2],ans[3],ans[4],ans[5])
    t4=genc(ans[2],ans[3],ans[6],ans[7])
    t5=genc(ans[8],ans[9],ans[12],ans[13])
    t6=genc(ans[8],ans[9],ans[14],ans[15])
    t7=genc(ans[10],ans[11],ans[12],ans[13])
    t8=genc(ans[10],ans[11],ans[14],ans[15])
    ll.append(t1)
    ll.append(t2)
    ll.append(t3)
    ll.append(t4)
    ll.append(t5)
    ll.append(t6)
    ll.append(t7)
    ll.append(t8)
    return ll



if __name__ == "__main__":


    f1= 'array.txt'
    f2='lingo.txt'
    if os.path.exists(f1):
        os.remove(f1)
    if os.path.exists(f2):
        os.remove(f2)


    #小矩形索引
    map={}
    #结果拼接
    rresult=''
    #大矩形
    sl=[]
    #小矩形
    l = []
    #约束条件
    bdl=[]
    ss=[]
    #返回的一组解
    ans = []
    #一个大矩形拼接的所有组合
    ans2=[]
    #二维数组总行数
    size=0
    #所有大矩形下所有解的组合
    zy = []
    #每种矩形对应行数
    pn=[]
    loaddata()
    genmap(l)
    sort_group = combine(l)

######################################################################################################
    # S=(5000,1450)
    # r=cut(S,(3862.0, 143.0))
    # #print r
    # r1,r2=dived(S,r)
    # # print r1
    # # print r2
    # rr=cut(r2[1],(63.0, 60.0))
    # print rr
    # rr1,rr2=dived(r2[1],rr)
    # print rr1
    # print rr2
    # rrr=cut(rr1[1],(130.0, 33.0))
    # print rrr
    #
    #
    # print rr1[1]


#####################################################################################################
    nnnnn = len(l)
    for S  in  sl:
        ans2 = []
        for sg in sort_group:
            ans = []

            getrur(S, sg, 0, rresult)
            llll = combineans(ans)
            ans2 = ans2 + llll

        s = set(ans2)

        #print len(s)
        size = size + len(s)
        pn.append(size)
        #print size

        for sss in s:
            zy.append(sss)

#####################################################################################



 ############################################################################################################
                     ##### test
#13	34	36	47	50	54	57	62	64	70	72	75	76	78	80
#176	7989	8021	8379	8831	8876	8965	11562	12103	12261	13095	13537	15455	15644	16040	17379	18162	21013	21931	22327	22422	23088	23200	23950	24550	26554	28388	29042	29804	30328	33561	34108	34740


    # llss = [47	,50	,54	,57	,62	,64	,70	,72	,75	,76	,78	,80	,81]
    #
    # for l in llss:
    #     print  zy[l]

#################################################################################################################


    # print nnnnn
    #
    #
    pn.insert(0, 0)
    print pn


###########################################################################################################
    arr=genarray(size,nnnnn)
    fillarray(zy)


    genlingo(str(arr),'array.txt')

    ###############################################################
    print pn
    print size
    genexpression(nnnnn)
    for b in bdl:
        sr= b+';'
        genlingo(sr)
        genlingo('\r\n')






































