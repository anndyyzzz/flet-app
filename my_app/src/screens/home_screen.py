import flet as ft
from flet import Colors

def home_screen(page: ft.Page):
    page.title = "Home"
    page.padding = 10
    page.bgcolor = Colors.WHITE

    header = ft.Row(
        controls=[
            ft.Container(
                content=ft.Text(
                    "N",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=Colors.WHITE
                ),
                bgcolor=Colors.PINK,
                width=50,
                height=50,
                border_radius=25,
                alignment=ft.alignment.center
            ),
            ft.Column(
                controls=[
                    ft.Text("ID : 65030226", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("STATUS : out of condition", size=14, color=Colors.BLACK54)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10
    )

    form_section = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("แบบฟอร์มเอกสารทางการศึกษา", size=18, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.Container(
                    content=ft.Image(
                        src="/path/to/image_placeholder.png",
                        width=100,
                        height=100,
                        fit=ft.ImageFit.CONTAIN
                    ),
                    alignment=ft.alignment.center,
                    bgcolor=Colors.BLACK12,
                    border_radius=10,
                    height=150,
                    width=150
                ),
                ft.Text(
                    "แบบฟอร์มขอรับรองการเป็นอาจารย์ที่ปรึกษาวิทยานิพนธ์ หลัก/ร่วม",
                    size=14,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.ElevatedButton(
                    text="Download PDF",
                    on_click=lambda e: print("Downloading PDF..."),
                    bgcolor=Colors.PINK,
                    color=Colors.WHITE
                )
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        padding=20,
        border=ft.border.all(1, Colors.BLACK12),
        border_radius=10
    )

    nav_bar = ft.Row(
        controls=[
            ft.Icon(name=ft.icons.HOME, color=Colors.PINK),
            ft.Icon(name=ft.icons.CONTACT_PAGE, color=Colors.BLACK54),
            ft.Icon(name=ft.icons.NOTIFICATIONS, color=Colors.BLACK54),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND
    )

    page.add(
        ft.Column(
            controls=[header, form_section, nav_bar],
            spacing=20,
            alignment=ft.MainAxisAlignment.START
        )
    )
    page.update()
