import sys

from PyQt5.QtWidgets import QApplication

from apps.windows.w_principal import W_Main
from config import BASE_PATH

print("Ruta: "+ BASE_PATH)
app = QApplication(sys.argv)
ventana = W_Main()
ventana.show()
sys.exit(app.exec_())