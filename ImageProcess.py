import cv2
# อ่านภาพจากไฟล์
image = cv2.imread('path/to/image.jpg')

# ตรวจสอบว่าภาพถูกโหลดสำเร็จหรือไม่
if image is None:
    print("Error: Unable to load image. Please check the file path.")
else:
    # แสดงผลภาพต้นฉบับ
    cv2.imshow('Original Image', image)

    # แปลงภาพเป็นระดับสีเทา
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # ใช้ Canny Edge Detection
    edges = cv2.Canny(gray_image, 100, 200)

    # แสดงผลขอบที่ตรวจจับได้
    cv2.imshow('Edges', edges)

    # รอให้ผู้ใช้กดปุ่มก่อนปิดหน้าต่างทั้งหมด
    cv2.waitKey(0)
    cv2.destroyAllWindows()
