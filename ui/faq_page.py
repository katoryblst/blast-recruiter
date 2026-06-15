from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QFrame,
    QScrollArea
)

from PyQt6.QtCore import (
    QPropertyAnimation
)


class FAQItem(QFrame):

    opened_item = None

    def __init__(self, question, answer):
        super().__init__()

        self.setObjectName("FAQCard")

        self.animation = None

        layout = QVBoxLayout(self)

        layout.setSpacing(0)

        self.button = QPushButton(question)
        self.button.setObjectName("FAQButton")

        self.answer = QLabel(answer)
        self.answer.setWordWrap(True)
        self.answer.setObjectName("FAQAnswer")

        self.answer.setMaximumHeight(0)

        layout.addWidget(self.button)
        layout.addWidget(self.answer)

        self.button.clicked.connect(
            self.toggle
        )

    def toggle(self):

        if (
            FAQItem.opened_item
            and FAQItem.opened_item != self
        ):
            FAQItem.opened_item.close_item()

        if self.answer.maximumHeight() == 0:

            self.open_item()
            FAQItem.opened_item = self

        else:

            self.close_item()
            FAQItem.opened_item = None

    def open_item(self):

        height = self.answer.sizeHint().height()

        self.animation = QPropertyAnimation(
            self.answer,
            b"maximumHeight"
        )

        self.animation.setDuration(200)

        self.animation.setStartValue(0)
        self.animation.setEndValue(height)

        self.animation.start()

    def close_item(self):

        self.animation = QPropertyAnimation(
            self.answer,
            b"maximumHeight"
        )

        self.animation.setDuration(200)

        self.animation.setStartValue(
            self.answer.maximumHeight()
        )

        self.animation.setEndValue(0)

        self.animation.start()


class FaqPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        container = QWidget()

        container_layout = QVBoxLayout(
            container
        )

        title = QLabel("ВОПРОСЫ")
        title.setObjectName("PageTitle")

        container_layout.addWidget(title)

        faq_data = [

            (
                "Что делать если у человека нет койнов?",
                "Выдать роль trainee."
            ),

            (
                "Когда повышать на 2 ранг?",
                "Только после смены фамилии на Blast."
            ),

            (
                "Как заработать в семье?",
                "Выполнять контракты и отправлять отчёт в канал 'Отчетность контрактов'."
            ),

            (
                "Есть ли у вас офис или дом?",
                "Да."
            ),

            (
                "А если я хочу убивать госников?",
                "Создавай второй аккаунт и играй на нём в рамках правил сервера."
            )

        ]

        for question, answer in faq_data:

            item = FAQItem(
                question,
                answer
            )

            container_layout.addWidget(
                item
            )

        container_layout.addStretch()

        scroll.setWidget(container)

        layout.addWidget(scroll)

    def search_text(self, query):

        text = """
        койны
        trainee
        фамилия
        blast
        контракт
        офис
        дом
        госники
        """

        return query.lower() in text.lower()