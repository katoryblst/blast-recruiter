from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QFrame,
    QScrollArea
)


class MemoPage(QWidget):

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)

        container = QWidget()

        container_layout = QVBoxLayout(container)
        container_layout.setSpacing(15)

        # =====================================
        # Заголовок
        # =====================================

        title = QLabel("📘 ПАМЯТКА")
        title.setObjectName("PageTitle")

        container_layout.addWidget(title)

        # =====================================
        # ВАЖНО
        # =====================================

        important_card = QFrame()
        important_card.setObjectName("ImportantCard")

        important_layout = QVBoxLayout(
            important_card
        )

        important_title = QLabel(
            "🚨 ВАЖНО"
        )

        important_title.setObjectName(
            "SectionTitle"
        )

        important_text = QLabel(
            "Во время обзвона оценивайте адекватность человека, "
            "манеру общения и готовность развиваться вместе с семьёй."
        )

        important_text.setWordWrap(True)

        important_layout.addWidget(
            important_title
        )

        important_layout.addWidget(
            important_text
        )

        container_layout.addWidget(
            important_card
        )

        # =====================================
        # Основная памятка
        # =====================================

        memo_card = QFrame()
        memo_card.setObjectName(
            "NewsCard"
        )

        memo_layout = QVBoxLayout(
            memo_card
        )

        memo_title = QLabel(
            "📋 ПАМЯТКА ДЛЯ РЕКРУТЕРА"
        )

        memo_title.setObjectName(
            "SectionTitle"
        )

        try:

            with open(
                "data/memo.txt",
                "r",
                encoding="utf-8"
            ) as file:

                memo_content = file.read()

        except Exception:

            memo_content = (
                "Файл data/memo.txt не найден.\n\n"
                "Создайте его и вставьте туда текст памятки."
            )

        memo_text = QLabel(
            memo_content
        )

        memo_text.setWordWrap(True)

        memo_layout.addWidget(
            memo_title
        )

        memo_layout.addWidget(
            memo_text
        )

        container_layout.addWidget(
            memo_card
        )

        # =====================================
        # ЕСЛИ ОТВЕТИЛ НЕТ
        # =====================================

        reject_card = QFrame()
        reject_card.setObjectName(
            "RejectCard"
        )

        reject_layout = QVBoxLayout(
            reject_card
        )

        reject_title = QLabel(
            "❌ ЕСЛИ ОТВЕТИЛ НЕТ"
        )

        reject_title.setObjectName(
            "SectionTitle"
        )

        reject_text = QLabel(
            'Отклонить заявку с причиной "отказался".'
        )

        reject_text.setWordWrap(True)

        reject_layout.addWidget(
            reject_title
        )

        reject_layout.addWidget(
            reject_text
        )

        container_layout.addWidget(
            reject_card
        )

        # =====================================
        # ЕСЛИ ОТВЕТИЛ ДА
        # =====================================

        accept_card = QFrame()
        accept_card.setObjectName(
            "AcceptCard"
        )

        accept_layout = QVBoxLayout(
            accept_card
        )

        accept_title = QLabel(
            "✅ ЕСЛИ ОТВЕТИЛ ДА"
        )

        accept_title.setObjectName(
            "SectionTitle"
        )

        accept_text = QLabel(
            "• Как тебя зовут?\n"
            "• Сколько тебе лет?\n"
            "• Как давно играешь на RP серверах?\n"
            "• Был ли опыт в гос структурах?\n"
            "• Готов ли развиваться вместе с нами?"
        )

        accept_text.setWordWrap(True)

        accept_layout.addWidget(
            accept_title
        )

        accept_layout.addWidget(
            accept_text
        )

        container_layout.addWidget(
            accept_card
        )

        # =====================================
        # ПОВЫШЕНИЕ
        # =====================================

        rank_card = QFrame()
        rank_card.setObjectName(
            "RankCard"
        )

        rank_layout = QVBoxLayout(
            rank_card
        )

        rank_title = QLabel(
            "⭐ ПОВЫШЕНИЕ НА 2 РАНГ"
        )

        rank_title.setObjectName(
            "SectionTitle"
        )

        rank_text = QLabel(
            "Повышать человека на второй ранг "
            "можно только после смены фамилии "
            "на Blast."
        )

        rank_text.setWordWrap(True)

        rank_layout.addWidget(
            rank_title
        )

        rank_layout.addWidget(
            rank_text
        )

        container_layout.addWidget(
            rank_card
        )

        container_layout.addStretch()

        scroll.setWidget(
            container
        )

        main_layout.addWidget(
            scroll
        )

    def search_text(self, query):

        query = query.lower()

        try:

            with open(
                "data/memo.txt",
                "r",
                encoding="utf-8"
            ) as file:

                text = file.read().lower()

        except Exception:

            text = ""

        return query in text