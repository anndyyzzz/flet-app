import flet as ft
import os
from flet import Colors

def signin_screen(page: ft.Page, navigate_to):
    page.title = "Sign In"
    page.padding = 0
    page.bgcolor = Colors.WHITE

    logo_path = os.path.join(os.path.dirname(__file__), "../assets/logo_siet.png")
    if not os.path.exists(logo_path):
        raise FileNotFoundError(f"The file {os.path.abspath(logo_path)} does not exist.")

    logo = ft.Image(
        src=logo_path,
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )

    signin_button = ft.ElevatedButton(
        text="Sign in",
        on_click=lambda e: navigate_to(page, "home"),
        bgcolor=Colors.PINK,
        color=Colors.WHITE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=10
        )
    )

    text = ft.Text(
        value="Graduate Student Tracking System\nMobile Application",
        size=18,
        weight=ft.FontWeight.BOLD,
        color=Colors.PINK,
        text_align=ft.TextAlign.CENTER
    )

    container = ft.Column(
        controls=[logo, signin_button, text],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

    page.add(container)
    page.update()
