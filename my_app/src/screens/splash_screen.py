import flet as ft
import os
import time
from flet import Colors

# ฟังก์ชัน Splash Screen
def splash_screen(page: ft.Page, navigate_to):
    page.title = "Splash Screen"
    page.padding = 0
    page.bgcolor = Colors.WHITE

    # ตรวจสอบไฟล์โลโก้
    logo_path = os.path.join(os.path.dirname(__file__), "../assets/logo_siet.png")
    if not os.path.exists(logo_path):
        raise FileNotFoundError(f"The file {os.path.abspath(logo_path)} does not exist.")

    # องค์ประกอบโลโก้
    logo = ft.Image(
        src=logo_path,
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )

    # องค์ประกอบข้อความใต้โลโก้
    text = ft.Text(
        value="Graduate Student Tracking System\nMobile Application",
        size=18,
        weight=ft.FontWeight.BOLD,
        color=Colors.PINK,
        text_align=ft.TextAlign.CENTER
    )

    # จัดเรียงองค์ประกอบในหน้า
    container = ft.Column(
        controls=[logo, text],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

    # เพิ่มองค์ประกอบลงในหน้า
    page.add(container)
    page.update()

    # เพิ่มดีเลย์ 3 วินาที
    time.sleep(3)

    # เปลี่ยนไปหน้า Sign In
    page.controls.clear()
    navigate_to(page, "signin")
