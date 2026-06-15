import json
import requests

url = "https://github.com/katoryblst/blast-recruiter.git"

news = requests.get(url).json()

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QFrame,
    QScrollArea
)


class NewsPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(
            QFrame.Shape.NoFrame
        )

        container = QWidget()

        self.container_layout = QVBoxLayout(
            container
        )

        self.container_layout.setSpacing(
            15
        )

        title = QLabel("НОВОСТИ")
        title.setObjectName(
            "PageTitle"
        )

        self.container_layout.addWidget(
            title
        )

        self.load_news()

        self.container_layout.addStretch()

        scroll.setWidget(container)

        layout.addWidget(scroll)

    def load_news(self):

        try:

            with open(
                "data/news.json",
                "r",
                encoding="utf-8"
            ) as file:

                news = json.load(
                    file
                )

        except Exception:

            news = [

                {
                    "title":
                    "Добро пожаловать",

                    "text":
                    "Приложение Blast Recruiter успешно запущено.",

                    "date":
                    "16.06.2026",

                    "important":
                    True
                }
            ]

        for item in news:

            card = QFrame()

            card.setObjectName(
                "NewsCard"
            )

            card_layout = QVBoxLayout(
                card
            )

            if item.get(
                "important",
                False
            ):

                badge = QLabel(
                    "ВАЖНО"
                )

                badge.setObjectName(
                    "ImportantBadge"
                )

                card_layout.addWidget(
                    badge
                )

            title = QLabel(
                item["title"]
            )

            title.setObjectName(
                "NewsTitle"
            )

            text = QLabel(
                item["text"]
            )

            text.setWordWrap(
                True
            )

            date = QLabel(
                item["date"]
            )

            date.setObjectName(
                "NewsDate"
            )

            card_layout.addWidget(
                title
            )

            card_layout.addWidget(
                text
            )

            card_layout.addWidget(
                date
            )

            self.container_layout.addWidget(
                card
            )

    def search_text(self, query):

        query = query.lower()

        try:

            with open(
                "data/news.json",
                "r",
                encoding="utf-8"
            ) as file:

                news = json.load(
                    file
                )

        except Exception:

            return False

        for item in news:

            if query in item[
                "title"
            ].lower():

                return True

            if query in item[
                "text"
            ].lower():

                return True

        return False