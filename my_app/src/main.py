import sys
import os

# เพิ่ม Path ไปยังโฟลเดอร์ src
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import flet as ft
from screens.splash_screen import splash_screen

# ฟังก์ชันสำหรับเปลี่ยนหน้า
def navigate_to(page: ft.Page, screen: str):
    if screen == "home":
        from screens.home_screen import home_screen
        page.controls.clear()
        home_screen(page)
    elif screen == "signin":
        from screens.signin_screen import signin_screen
        page.controls.clear()
        signin_screen(page, navigate_to)

# ฟังก์ชันหลัก
def main(page: ft.Page):
    page.title = "Graduate Student Tracking System"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    splash_screen(page, navigate_to)

if __name__ == "__main__":
    ft.app(target=main)
