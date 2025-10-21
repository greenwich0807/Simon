import cv2
import numpy as np

# 读取图像
img_bgr = cv2.imread("minecraft bed.png")
# 转换为HSV色彩空间
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

# 定义粉色的HSV范围
lower_hsv = np.array([150, 50, 50])
upper_hsv = np.array([180, 255, 255])

# 生成掩码：筛选出HSV在范围内的像素
mask = cv2.inRange(img_hsv, lower_hsv, upper_hsv)

# 用掩码提取目标区域（黑色背景保留目标粉色）
img_out = cv2.bitwise_and(img_bgr, img_bgr, mask=mask)

# 显示、保存结果
cv2.imshow("img_out", img_out)
cv2.imwrite("img_out.png", img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()