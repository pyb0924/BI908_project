import numpy as np


def region_growing(im, t, threshold, seed,abs_flag,tail_max=500000): 
    # abs_flag=True: traditional False: new
    n, m, l = im.shape
    xlist = [seed[0]]
    ylist = [seed[1]]
    zlist = [seed[2]]
    ifsearch = np.zeros(im.shape)
    ifsearch[xlist[0], ylist[0], zlist[0]] = 1
    head = 0
    tail = 0
    while head <= tail:
        #print(head,tail)
        if tail>tail_max:
            #print('force quit')
            break
        x = xlist[head]
        y = ylist[head]
        z = zlist[head]
        for i in range(-t, t + 1):
            for j in range(-t, t + 1):
                for k in range(-t, t + 1):
                    xx = x + i
                    yy = y + j
                    zz = z + k
                    if (xx >= 0) and (xx < n) and (yy >= 0) and (yy < m) and (zz >= 0) and (zz < l):
                        if abs_flag:
                            if (ifsearch[xx][yy][zz] == 0) and (int(im[x, y, z]) - int(im[xx, yy, zz]) <= threshold):
                                tail = tail + 1
                                ifsearch[xx][yy][zz] = 1
                                xlist.append(xx)
                                ylist.append(yy)
                                zlist.append(zz)
                        else:
                            if (ifsearch[xx][yy][zz] == 0) and (abs(int(im[x, y, z]) - int(im[xx, yy, zz])) <= threshold):
                                tail = tail + 1
                                ifsearch[xx][yy][zz] = 1
                                xlist.append(xx)
                                ylist.append(yy)
                                zlist.append(zz)
        head = head + 1
    for index in range(head,tail):
        x=xlist[index]
        y=ylist[index]
        z=zlist[index]
        ifsearch[x][y][z]=1
    print(head,tail)
    return ifsearch
