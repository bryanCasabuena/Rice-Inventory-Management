from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QWidget, QPushButton, QMainWindow, QTableWidget, \
    QTableWidgetItem, QDialog, QVBoxLayout, QComboBox, QToolBar, QStatusBar, QMessageBox
from PyQt6.QtGui import QAction, QIcon, QIntValidator

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
        add_inventory_action.triggered.connect(self.insert)
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

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

# Insert Dialog Box inserting data
class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        
        layout = QVBoxLayout()
        
        # Add rice name comboBox
        self.rice_name = QComboBox()
        rice = ["Pandoy", "Coco Pandan", "MCL", "Buco Pandan", "Sweet Jasmine Blue" \
            "Sweet Jasmine Yellow", "Laon"]
        self.rice_name.addItems(rice)
        layout.addWidget(self.rice_name)
        self.setLayout(layout)
        
        # Add Quantity
        self.quantity = QLineEdit()
        self.quantity.setPlaceholderText("Enter Quanity")
        int_validator = QIntValidator(0, 100,self)
        self.quantity.setValidator(int_validator)
        layout.addWidget(self.quantity)
        
        # Add Price
        self.price = QLineEdit()
        self.price.setPlaceholderText("Price in PHP")
        int_validator = QIntValidator(0, 1000, self)
        self.price.setValidator(int_validator)
        layout.addWidget(self.price)
        
        # Add a submit Button
        button = QPushButton()
            
        
# Opening of app
app = QApplication(sys.argv)            
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())