import sys

from PyQt5.QtWidgets import QApplication

from apps.windows.w_principal import W_Main

app = QApplication(sys.argv)
ventana = W_Main()
ventana.show()
sys.exit(app.exec_())