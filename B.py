import cv2
import numpy as np

# 读取图像
img = cv2.imread("picture.jpg")  # 替换为你的图一路径
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转为灰度图

# 二值化：将亮度高于200的区域设为白色，其余为黑色（可根据实际图像调整阈值）
_, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

result = img.copy()  # 复制原图用于绘制结果
min_area = 500   # 最小面积阈值（根据蓝色角实际大小调整）
max_area = 5000  # 最大面积阈值（根据蓝色角实际大小调整）

for contour in contours:
    area = cv2.contourArea(contour)
    if min_area < area < max_area:
        # 获取轮廓的最小外接矩形
        x, y, w, h = cv2.boundingRect(contour)
        # 绘制红色矩形框
        cv2.rectangle(result, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imwrite("result2.jpg", result)  # 保存结果图
cv2.imshow("Result2", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
