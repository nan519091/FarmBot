import cv2
import numpy as np

# อ่านภาพจากไฟล์
image = cv2.imread('C:/Users/Nan/OneDrive/Pictures/IMG_20241108_170843_760.jpg')

# ขั้นที่ 1: แยกสี (Color Segmentation)
# แปลงภาพเป็นสีเทา
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# กำหนดค่า threshold เพื่อแยกภาพเป็นขาวดำ
ret, segmented_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# ขั้นที่ 2: การตรวจจับขอบ (Edge Detection)
# ใช้ Canny Edge Detection เพื่อตรวจจับขอบในภาพ
edges = cv2.Canny(segmented_image, 100, 200)

# ขั้นที่ 3: การตรวจจับขนาด (Size Detection)
# หาคอนทัวร์จากภาพที่ตรวจจับขอบแล้ว
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# วาดคอนทัวร์และแสดงขนาดของวัตถุ
for contour in contours:
    if cv2.contourArea(contour) > 500:  # กำหนดขนาดขั้นต่ำของวัตถุ
        # หาพื้นที่ของวัตถุ
        area = cv2.contourArea(contour)
        
        # หากรอบของวัตถุ
        x, y, w, h = cv2.boundingRect(contour)

        # วาดกรอบสี่เหลี่ยมรอบวัตถุ
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # แสดงพื้นที่ของวัตถุ
        cv2.putText(image, f"Area: {area}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# ขั้นที่ 4: การแสดงผลภาพ
# แสดงภาพที่แยกสี
cv2.imshow('Segmented Image', segmented_image)
# แสดงผลขอบที่ตรวจจับได้
cv2.imshow('Edges', edges)
# แสดงผลภาพที่มีการตรวจจับขนาด
cv2.imshow('Detected Objects', image)
# รอให้ผู้ใช้กดปุ่มก่อนปิดหน้าต่างทั้งหมด
cv2.waitKey(0)
cv2.destroyAllWindows()
