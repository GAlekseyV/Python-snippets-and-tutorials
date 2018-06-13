# First application using PySide2 and QtQuick/QML
import os
from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl

app = QApplication([])
view = QQuickView()
url = QUrl(os.path.join("QML_Tutorials", "2_components.qml"))

view.setSource(url)
view.show()
app.exec_()
