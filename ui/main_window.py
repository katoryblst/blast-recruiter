import webbrowser

from PyQt6.QtCore import Qt
from PyQt6.QtGui import (
    QIcon,
    QPixmap
)

from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QStackedWidget,
    QFrame
)

from ui.news_page import NewsPage
from ui.memo_page import MemoPage
from ui.rules_page import RulesPage
from ui.faq_page import FaqPage


DISCORD_LINK = "https://discord.gg/blastmjrp"


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Blast Recruiter"
        )

        self.resize(
            1600,
            900
        )

        self.setMinimumSize(
            1200,
            700
        )

        self.setWindowIcon(
            QIcon("assets/icon.ico")
        )

        self.setup_ui()

        self.load_styles()

    def setup_ui(self):

        central = QWidget()
        self.setCentralWidget(
            central
        )

        root = QHBoxLayout(
            central
        )

        root.setContentsMargins(
            0,
            0,
            0,
            0
        )

        root.setSpacing(0)

        # ---------------------------------
        # SIDEBAR
        # ---------------------------------

        sidebar = QFrame()
        sidebar.setObjectName(
            "Sidebar"
        )

        sidebar.setFixedWidth(
            340
        )

        sidebar_layout = QVBoxLayout(
            sidebar
        )

        sidebar_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )

        sidebar_layout.setSpacing(
            15
        )

        # LOGO

        self.logo = QLabel()

        self.logo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        pixmap = QPixmap(
            "assets/logo.png"
        )

        pixmap = pixmap.scaled(
            260,
            260,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        self.logo.setPixmap(
            pixmap
        )

        sidebar_layout.addWidget(
            self.logo
        )

        # КНОПКИ

        self.news_btn = QPushButton(
            "НОВОСТИ"
        )

        self.memo_btn = QPushButton(
            "ПАМЯТКА"
        )

        self.rules_btn = QPushButton(
            "ПРАВИЛА СЕМЬИ"
        )

        self.faq_btn = QPushButton(
            "ВОПРОСЫ"
        )

        buttons = [
            self.news_btn,
            self.memo_btn,
            self.rules_btn,
            self.faq_btn
        ]

        for btn in buttons:

            btn.setMinimumHeight(
                60
            )

            btn.setCursor(
                Qt.CursorShape.PointingHandCursor
            )

            sidebar_layout.addWidget(
                btn
            )

        sidebar_layout.addStretch()

        # DISCORD

        self.discord_btn = QPushButton(
            "Discord"
        )

        self.discord_btn.setObjectName(
            "DiscordButton"
        )

        self.discord_btn.setMinimumHeight(
            70
        )

        self.discord_btn.clicked.connect(
            lambda: webbrowser.open(
                DISCORD_LINK
            )
        )

        sidebar_layout.addWidget(
            self.discord_btn
        )

        version = QLabel(
            "v1.0.0"
        )

        version.setObjectName(
            "VersionLabel"
        )

        sidebar_layout.addWidget(
            version
        )

        # ---------------------------------
        # CONTENT
        # ---------------------------------

        content = QWidget()

        content_layout = QVBoxLayout(
            content
        )

        content_layout.setContentsMargins(
            25,
            20,
            25,
            20
        )

        content_layout.setSpacing(
            20
        )

        self.search = QLineEdit()

        self.search.setPlaceholderText(
            "Поиск по всему приложению..."
        )

        self.search.setFixedHeight(
            52
        )

        content_layout.addWidget(
            self.search
        )

        self.pages = QStackedWidget()

        self.news_page = NewsPage()
        self.memo_page = MemoPage()
        self.rules_page = RulesPage()
        self.faq_page = FaqPage()

        self.pages.addWidget(
            self.news_page
        )

        self.pages.addWidget(
            self.memo_page
        )

        self.pages.addWidget(
            self.rules_page
        )

        self.pages.addWidget(
            self.faq_page
        )

        content_layout.addWidget(
            self.pages
        )

        root.addWidget(
            sidebar
        )

        root.addWidget(
            content
        )

        self.news_btn.clicked.connect(
            lambda: self.switch_page(0)
        )

        self.memo_btn.clicked.connect(
            lambda: self.switch_page(1)
        )

        self.rules_btn.clicked.connect(
            lambda: self.switch_page(2)
        )

        self.faq_btn.clicked.connect(
            lambda: self.switch_page(3)
        )

        self.search.textChanged.connect(
            self.global_search
        )

        self.switch_page(0)

    def switch_page(self, index):

        self.pages.setCurrentIndex(
            index
        )

        buttons = [
            self.news_btn,
            self.memo_btn,
            self.rules_btn,
            self.faq_btn
        ]

        for btn in buttons:

            btn.setProperty(
                "active",
                False
            )

            btn.style().unpolish(
                btn
            )

            btn.style().polish(
                btn
            )

        buttons[index].setProperty(
            "active",
            True
        )

        buttons[index].style().unpolish(
            buttons[index]
        )

        buttons[index].style().polish(
            buttons[index]
        )

    def global_search(self):

        query = (
            self.search.text()
            .lower()
            .strip()
        )

        if not query:
            return

        pages = [

            (
                0,
                self.news_page
            ),

            (
                1,
                self.memo_page
            ),

            (
                2,
                self.rules_page
            ),

            (
                3,
                self.faq_page
            )
        ]

        for index, page in pages:

            if hasattr(
                page,
                "search_text"
            ):

                if page.search_text(
                    query
                ):

                    self.switch_page(
                        index
                    )

                    return

    def load_styles(self):

        try:

            with open(
                "styles/dark.qss",
                "r",
                encoding="utf-8"
            ) as file:

                self.setStyleSheet(
                    file.read()
                )

        except Exception as error:

            print(error)