from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QWidget, QPushButton, QMainWindow, QTableWidget, \
    QTableWidgetItem, QDialog, QVBoxLayout, QComboBox, QToolBar, QStatusBar, QMessageBox
from PyQt6.QtGui import QAction, QIcon
import sys
import mysql.connector

# Making of Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Store Inventory")
        self.setMinimumSize(800,600)

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        
        add_inventory_action = QAction("Add Rice", self)
        file_menu_item.addAction(add_inventory_action)
        
        about_action = QAction("About", self)
        help_menu_item.addAction("about_action")
        
        # Create Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Rice Name", "Quantity", "Price"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)
        
    def load_data(self):
        self.table

# Opening of app
app = QApplication(sys.argv)            
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())