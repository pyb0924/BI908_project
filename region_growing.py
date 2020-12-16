import numpy as np
seed = [100, 82, 94]  # 区域扩增的起始种子


def region_growing(im, t, threshold, seed,abs_flag): # abs_flag=True: traditional False: new
    n, m, l = im.shape
    xlist = [seed[0]]
    ylist = [seed[1]]
    zlist = [seed[2]]
    ifsearch = np.zeros(im.shape)
    ifsearch[xlist[0], ylist[0], zlist[0]] = 1
    head = 0
    tail = 0
    while head <= tail:
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
    return ifsearch


# def deal(imgsource, labelsource, t1, t2, threshold, seed):
#     img = read_img(imgsource)
#     n, m, l = img.shape
#     label = read_img(labelsource)
#     for i in range(m):
#         for j in range(l):
#             if (img[100, i, j] > 870):
#                 print(100, i, j, img[100, i, j])
#     print('now region_growing')
#     img_region = region_growing(img, t1, threshold, seed)
#     print('now closing-opperation')
#     newimg = closing(img_region, t2)
#     print('the region-growing img shows as listed:')
#     show2D(img_region, l)
#     print('the closing-operation img shows as listed:')
#     show2D(newimg, l)
#     print('the label shows as listed:')
#     show2D(label, l)
#     im1 = label * newimg
#     im2 = label + newimg
#     I = np.sum(im1 != 0)
#     U = np.sum(im2 != 0)
#     print('IOU=', I / U)
#     print('the size of labels is ', np.sum(label != 0))
#     print('the size of newimg is ', np.sum(newimg != 0))
#     return newimg, I / U


#    print(I,U,I/U,np.sum(label!=0),np.sum(newimg!=0))

# newimg, IoU = deal(imgsource, labelsource, t1, t2, threshold, seed)
# 用来找种子
"""

for i in range(m):
    for j in range(l):
        if (img[100,i,j]>880):
            print(100,i,j,img[100,i,j])

print(np.argmax(img))"""
