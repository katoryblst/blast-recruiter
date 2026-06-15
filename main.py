import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QProgressBar
)

from PyQt6.QtCore import (
    Qt,
    QTimer
)

from PyQt6.QtGui import (
    QPixmap,
    QIcon
)

from ui.main_window import MainWindow


class SplashScreen(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedSize(700, 450)

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
        )

        self.setStyleSheet("""
            QWidget {
                background-color: #080808;
            }

            QLabel {
                color: white;
            }

            QProgressBar {
                border: none;
                border-radius: 10px;
                background-color: #151515;
                height: 18px;
                text-align: center;
                color: white;
                font-weight: bold;
            }

            QProgressBar::chunk {
                background-color: #c1121f;
                border-radius: 10px;
            }
        """)

        layout = QVBoxLayout(self)

        layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.setSpacing(20)

        # =====================================
        # ЛОГОТИП
        # =====================================

        self.logo = QLabel()

        pixmap = QPixmap(
            "assets/logo.png"
        )

        if not pixmap.isNull():

            pixmap = pixmap.scaled(
                220,
                220,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )

            self.logo.setPixmap(
                pixmap
            )

        self.logo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        # =====================================
        # ТЕКСТ
        # =====================================

        self.title = QLabel(
            "Добро пожаловать!"
        )

        self.title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.title.setStyleSheet("""
            font-size: 34px;
            font-weight: bold;
            color: white;
        """)

        self.subtitle = QLabel(
            "Blast Recruiter"
        )

        self.subtitle.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.subtitle.setStyleSheet("""
            font-size: 18px;
            color: #a0a0a0;
        """)

        # =====================================
        # ПРОГРЕСС
        # =====================================

        self.progress = QProgressBar()

        self.progress.setFixedWidth(
            420
        )

        self.progress.setValue(0)

        layout.addStretch()

        layout.addWidget(
            self.logo
        )

        layout.addWidget(
            self.title
        )

        layout.addWidget(
            self.subtitle
        )

        layout.addSpacing(
            15
        )

        layout.addWidget(
            self.progress,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout.addStretch()

        self.value = 0

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_progress
        )

        self.timer.start(
            20
        )

    def update_progress(self):

        self.value += 1

        self.progress.setValue(
            self.value
        )

        if self.value >= 100:

            self.timer.stop()

            self.open_main_window()

    def open_main_window(self):

        self.window = MainWindow()

        self.window.show()

        self.close()


def main():

    app = QApplication(
        sys.argv
    )

    app.setWindowIcon(
        QIcon(
            "assets/icon.ico"
        )
    )

    splash = SplashScreen()

    splash.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    main()