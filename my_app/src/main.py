import flet as ft

# พยายามนำเข้า splash_screen จาก screens.splash_screen
# หากไม่พบโมดูลหรือฟังก์ชันจะเกิด ImportError พร้อมแสดงข้อความแนะนำ
try:
    from screens.splash_screen import splash_screen
except ImportError as e:
    raise ImportError("Failed to import 'splash_screen' from 'screens.splash_screen'. Please ensure the module and function are correctly implemented and available.") from e

# ฟังก์ชันหลักของแอปพลิเคชัน
# Parameters:
# - page: Flet Page ที่ใช้แสดงเนื้อหาในแอป

def main(page: ft.Page):
    page.title = "Graduate Student Tracking System"  # ตั้งชื่อหน้าจอหลัก
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # จัดเนื้อหาให้อยู่กึ่งกลางแนวตั้ง
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # จัดเนื้อหาให้อยู่กึ่งกลางแนวนอน

    # เรียกหน้าจอ Splash Screen พร้อมกำหนดชื่อและสีพื้นหลัง
    splash_screen(page, title="Graduate Student Tracking System", bgcolor=ft.colors.WHITE)

# จุดเริ่มต้นของแอปพลิเคชัน
# ใช้ flet.app เพื่อรันแอปพลิเคชันโดยกำหนด target เป็นฟังก์ชัน main
if __name__ == "__main__":
    ft.app(target=main)
