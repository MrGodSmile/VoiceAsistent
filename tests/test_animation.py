from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример анимации GIF")
        self.setGeometry(100, 100, 400, 300)

        # Создаем виджет QLabel для отображения анимации
        self.label = QLabel(self)

        # Создаем кнопку для активации/деактивации анимации
        self.button = QPushButton("Запустить анимацию", self)
        self.button.clicked.connect(self.toggle_animation)

        # Создаем компоновщик QVBoxLayout для размещения виджетов
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Создаем главный виджет и устанавливаем на него компоновщик
        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        # Создаем объект QMovie для анимации
        self.movie = QMovie(r"C:\Users\mrgod\PycharmProjects\TISK.gif")  # Укажите путь к вашему анимированному GIF

        # Устанавливаем анимацию на виджет QLabel
        self.label.setMovie(self.movie)

        # Флаг для отслеживания состояния анимации
        self.is_animation_running = False

    def toggle_animation(self):
        if not self.is_animation_running:
            # Если анимация не активна, запускаем ее
            self.start_animation()
            self.button.setText("Остановить анимацию")
        else:
            # Если анимация активна, останавливаем ее
            self.stop_animation()
            self.button.setText("Запустить анимацию")

    def start_animation(self):
        # Запускаем анимацию
        self.movie.start()
        self.is_animation_running = True

    def stop_animation(self):
        # Останавливаем анимацию
        self.movie.stop()
        self.is_animation_running = False


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()