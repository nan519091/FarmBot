import numpy as np
from scipy.spatial.transform import Rotation as R

# ฟังก์ชันสำหรับเคลื่อนที่ไปยังตำแหน่งที่กำหนด
def move_to_position(current_position, target_position):
    """
    คำนวณเวกเตอร์การเคลื่อนที่จากตำแหน่งปัจจุบันไปยังตำแหน่งเป้าหมาย
    """
    movement_vector = np.array(target_position) - np.array(current_position)
    return movement_vector

# ฟังก์ชันสำหรับสร้าง quaternion จากมุมหมุน
def create_quaternion(rotation_angle):
    """
    สร้าง quaternion จากมุมหมุนรอบแกน Z
    """
    quaternion = R.from_euler('z', rotation_angle, degrees=True).as_quat()
    return quaternion

# ฟังก์ชันควบคุม FarmBot ให้เคลื่อนที่และหมุนไปยังตำแหน่งเป้าหมาย
def control_farmbot(current_position, target_position):
    """
    ควบคุม FarmBot ให้เคลื่อนที่ไปยังตำแหน่งเป้าหมายและหมุนให้ตรงตามเป้าหมาย
    """
    movement = move_to_position(current_position, target_position)
    print(f"Moving to: {target_position} with vector {movement}")

    # คำนวณมุมหมุนที่ต้องการ
    rotation_angle = calculate_rotation_angle(current_position, target_position)
    quaternion = create_quaternion(rotation_angle)
    print(f"Rotating with quaternion: {quaternion}")

# ฟังก์ชันคำนวณมุมระหว่างตำแหน่งปัจจุบันและตำแหน่งเป้าหมาย
def calculate_rotation_angle(current_pos, target_pos):
    """
    คำนวณมุมระหว่างตำแหน่งปัจจุบันและตำแหน่งเป้าหมายในระนาบ XY
    """
    angle = np.arctan2(target_pos[1] - current_pos[1], target_pos[0] - current_pos[0]) * (180 / np.pi)
    return angle

# ตัวอย่างการใช้งานฟังก์ชัน
current_position = [0, 0, 0]  # ตำแหน่งเริ่มต้น (x, y, z)
target_position = [5, 3, 0]   # ตำแหน่งเป้าหมาย (x, y, z)

# เรียกใช้งานฟังก์ชันควบคุม FarmBot
control_farmbot(current_position, target_position)



# ------------------------------------------------------------------------------------------------------
