import flet as ft
import os

# ฟังก์ชัน splash_screen สำหรับแสดงหน้าจอ Splash Screen
# Parameters:
# - page: หน้าจอ Flet Page ที่กำลังแสดงผล
# - title: ชื่อหน้าจอที่จะแสดงในแอป (ค่าเริ่มต้น: "Splash Screen")
# - bgcolor: สีพื้นหลังของหน้าจอ (ค่าเริ่มต้น: ft.colors.WHITE)
def splash_screen(page: ft.Page, title="Splash Screen", bgcolor=ft.colors.WHITE):
    page.title = title  # ตั้งชื่อหน้าจอ
    page.padding = 1  # ตั้งค่าขอบ Padding ของหน้าจอ
    page.bgcolor = bgcolor  # ตั้งค่าสีพื้นหลังของหน้าจอ

    # เส้นทางไปยังโลโก้
    logo_path = os.path.join(os.path.dirname(__file__), "../assets/logo_siet.png")
    if not os.path.exists(logo_path):  # ตรวจสอบว่าไฟล์โลโก้มีอยู่หรือไม่
        raise FileNotFoundError(f"The file {os.path.abspath(logo_path)} does not exist. Please check the path and try again.")

    # องค์ประกอบภาพโลโก้
    logo = ft.Image(
        src=logo_path,  # เส้นทางโลโก้
        width=150,  # ความกว้างของภาพ
        height=150,  # ความสูงของภาพ
        fit=ft.ImageFit.CONTAIN  # การจัดขนาดภาพให้พอดีกับพื้นที่
    )

    # องค์ประกอบข้อความใต้โลโก้
    text = ft.Text(
        value="Graduate Student Tracking System\nMobile Application",  # ข้อความที่จะแสดง
        size=18,  # ขนาดตัวอักษร
        weight=ft.FontWeight.BOLD,  # น้ำหนักตัวอักษรแบบหนา
        color=ft.colors.PINK,  # สีของตัวอักษร
        text_align=ft.TextAlign.CENTER  # จัดข้อความให้อยู่กึ่งกลาง
    )

    # ฟังก์ชันสร้าง Container สำหรับรวมโลโก้และข้อความ
    def create_container():
        return ft.Column(
            controls=[logo, text],  # เพิ่มโลโก้และข้อความในคอลัมน์
            alignment=ft.MainAxisAlignment.CENTER,  # จัดให้อยู่กึ่งกลางแนวตั้ง
            horizontal_alignment=ft.CrossAxisAlignment.CENTER  # จัดให้อยู่กึ่งกลางแนวนอน
        )

    # เพิ่ม Container ลงในหน้าจอ
    page.add(create_container())
