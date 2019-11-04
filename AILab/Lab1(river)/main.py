import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

r_x = np.load("RiverY.npy")
r_y = np.load("RiverX.npy")
nr_x = np.load("nonRiverY.npy")
nr_y = np.load("nonRiverX.npy")

test_arr  = np.ndarray(shape=(512,512,4), dtype=np.uint8)
test_arr[:,:,0] = np.asarray(Image.open('band1.gif'))
test_arr[:,:,1] = np.asarray(Image.open('band2.gif'))
test_arr[:,:,2] = np.asarray(Image.open('band3.gif'))
test_arr[:,:,3] = np.asarray(Image.open('band4.gif'))

# print(test_arr.shape)
# plt.subplot(2,2,1)
# plt.imshow(test_arr[:,:,0],cmap='gray')
# plt.subplot(2,2,2)
# plt.imshow(test_arr[:,:,1],cmap='gray')
# plt.subplot(2,2,3)
# plt.imshow(test_arr[:,:,2],cmap='gray')
# plt.subplot(2,2,4)
# plt.imshow(test_arr[:,:,3],cmap='gray')
# plt.show()
T1 = [0, 0, 0, 0]
T2 = [0, 0, 0, 0]
for i in range(50):
    for j in range(4):
        T1[j] = T1[j] + test_arr[r_x[i],r_y[i],j]
for i in range(4):
    T1[i] = T1[i] / 50

a = np.ndarray((50,4))
for i in range(50):
    a[i] = np.subtract(test_arr[r_x[i],r_y[i]], T1)

for i in range(100):
    for j in range(4):
        T2[j] = T2[j] + test_arr[nr_x[i],nr_y[i],j]
for i in range(4):
    T2[i] = T2[i] / 100

b = np.ndarray((100,4))
for i in range(100):
    b[i] = np.subtract(test_arr[nr_x[i],nr_y[i]], T2)

print(T1)
print(T2)

cov_r = np.ndarray(shape=(4, 4), dtype=np.float64)
cov_nr = np.ndarray(shape=(4, 4), dtype=np.float64)

for i in range(4):
    for j in range(4):
        cov_r[i][j]=np.dot(a[:,i],a[:,j])/50
        
print('Covariance of River class')
print(cov_r)

for i in range(4):
    for j in range(4):
        cov_nr[i][j]=np.dot(b[:,i],b[:,j])/100
print('\nCovariance of Non-river class')
print(cov_nr)



inverse_cov_r = np.linalg.inv(cov_r)
inverse_cov_nr = np.linalg.inv(cov_nr)

def cal(i,j):
    r = np.subtract(test_arr[i,j,:],T1)
    nr = np.subtract(test_arr[i,j,:],T2)

    river_class = np.dot(np.dot(r.T,inverse_cov_r), r)
    non_river_class = np.dot(np.dot(nr.T,inverse_cov_nr), nr)
    
    # density functions

    det_cov_r = np.linalg.det(cov_r)
    p1 = (-0.5) * 1/np.sqrt(det_cov_r) * np.exp(river_class)

    det_cov_nr = np.linalg.det(cov_nr)
    p2 = (-0.5) * 1/np.sqrt(det_cov_nr) * np.exp(non_river_class)
    return p1,p2



def bayes(P1, P2):
    out_image=np.ndarray(shape=(512, 512), dtype = np.integer)
    for i in range(512):
        for j in range(512):
            p1,p2 = cal(i,j)
            if((P1 * p1) >= (P2 * p2)):
                out_image[i,j]=255
            else:
                out_image[i,j]=0
                
    return out_image

out_image1 = bayes(P1=0.5,P2=0.5)
out_image2 = bayes(P1=0.3,P2=0.7)
out_image3 = bayes(P1=0.7,P2=0.3)
out_image4 = bayes(P1=0.1,P2=.9)

plt.subplot(2,2,1)
plt.imshow(out_image1, cmap='gray')
plt.subplot(2,2,2)
plt.imshow(out_image2, cmap='gray')
plt.subplot(2,2,3)
plt.imshow(out_image3, cmap='gray')
plt.subplot(2,2,4)
plt.imshow(out_image4, cmap='gray')
plt.show()

