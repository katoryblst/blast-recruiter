from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QFrame,
    QScrollArea
)


class RulesPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)

        container = QWidget()

        container_layout = QVBoxLayout(container)
        container_layout.setSpacing(15)

        title = QLabel("ПРАВИЛА СЕМЬИ")
        title.setObjectName("PageTitle")

        container_layout.addWidget(title)

        # ======================
        # МОЖНО
        # ======================

        allow_card = QFrame()
        allow_card.setObjectName("AllowCard")

        allow_layout = QVBoxLayout(allow_card)

        allow_title = QLabel("МОЖНО")
        allow_title.setObjectName("AllowTitle")

        allow_text = QLabel(
            "• Жить дружно\n"
            "• Поддерживать участников семьи\n"
            "• Помогать новичкам"
        )

        allow_text.setWordWrap(True)

        allow_layout.addWidget(allow_title)
        allow_layout.addWidget(allow_text)

        container_layout.addWidget(allow_card)

        # ======================
        # ЗАПРЕЩЕНО
        # ======================

        forbidden_title = QLabel("ЗАПРЕЩЕНО")
        forbidden_title.setObjectName("ForbiddenTitle")

        container_layout.addWidget(forbidden_title)

        rules = [

            "1.1 Запрещено оскорбление любых участников дискорд-сервера.",

            "1.2 Запрещено спамить упоминаниями (@).",

            "1.3 Запрещён флуд (частая отправка однотипных сообщений).",

            "1.4 Запрещены угрозы в любой форме участникам сервера.",

            "1.5 Запрещены провокации администрации и участников сервера, а также токсичное поведение.",

            "1.6 Запрещены дискриминация, расизм, ксенофобия, издевательства и всё связанное с этим.",

            "1.7 Запрещены политические лозунги, высказывания и агитация.",

            "1.8 Запрещено выдавать себя за руководство семьи.",

            "1.9 Запрещено злоупотребление функционалом Discord-сервера."
        ]

        for rule in rules:

            card = QFrame()
            card.setObjectName("RuleCard")

            card_layout = QVBoxLayout(card)

            text = QLabel(rule)
            text.setWordWrap(True)

            card_layout.addWidget(text)

            container_layout.addWidget(card)

        container_layout.addStretch()

        scroll.setWidget(container)

        layout.addWidget(scroll)

    def search_text(self, query):

        searchable_text = """
        правила
        оскорбление
        спам
        флуд
        угрозы
        провокации
        токсичность
        дискриминация
        политика
        руководство
        """

        return query.lower() in searchable_text.lower()