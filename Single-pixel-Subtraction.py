import cv2
import numpy as np
import time

start = time.time()

#def splitFrames():
video = input('请输入待检测视频:')
cap = cv2.VideoCapture(video)
ret, frame = cap.read()
num = 1
while True:
    success,frame = cap.read()
    if not success:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   #灰度化处理
    np_img = np.array(gray)                          #重建图像
    
    if num == 1 :                                    #第一帧
        video_array = np_img
    elif num == 2 :
        video_array = np.array([video_array, np_img])       #第二帧
    else:                                                   #重建为三维数组
        data = np.append(video_array,np_img)
        dim = video_array.shape
        video_array = data.reshape(dim[0]+1,dim[1],dim[2])
    num = num + 1
cap.release()





print('视频维数：',video_array.shape)
picture = video_array[0,:,:]
print('单帧维数：',picture.shape)

i=0
diff = np.array(picture)
while i != video_array.shape[1] :               #遍历数组
    j=0
    while j != video_array.shape[2] :
        max_final = np.max(video_array[:,i,j])
        mean_final = np.mean(video_array[:,i,j])
        diff[i,j] = max_final-mean_final            #最大值-平均值
        j = j+1
    i = i+1

diff = np.array(diff,dtype='uint8')

end = time.time()
print('处理时间：',end - start)
cv2.imshow('picture',diff)
cv2.waitKey(0)
cv2.destroyAllWindows()