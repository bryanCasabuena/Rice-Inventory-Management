from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QWidget, QPushButton, QMainWindow, QTableWidget, \
    QTableWidgetItem, QDialog, QVBoxLayout, QComboBox, QToolBar, QStatusBar, QMessageBox
from PyQt6.QtGui import QAction, QIcon, QIntValidator

import sys
import mysql.connector

class DatabaseConnection():
    def __init__(self, host = "localhost", user="root", password = "!Walalng28", database = "inventory"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        
    def connect(self):
        connection = mysql.connector.connect(host = self.host, user=self.user, password=self.password, database = self.database)
        return connection
        

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
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM  inventory")
        result = cursor.fetchall()
        self.table.setRowCount(0)                                                               # Resets the table and loads the data
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)                                                    #Use to insert an empty row to row number
            #print(row_number)
            #print(row_data)
            for column_number, data in enumerate(row_data):                                     #Populate cells of that row with actual data
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))      # Secify row and which column
        connection.close()
    
    # Instatiate an insert dialogue box
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
        button = QPushButton("Submit")
        button.clicked.connect(self.add_inventory)
        layout.addWidget(button)
        
        self.setLayout(layout)

    #Insert Add Inventory function
    def add_inventory(self):
        rice = self.rice_name.itemText(self.rice_name.currentIndex())
        rice_quantity = self.quantity.text()
        rice_price = self.price.text() 
        
        # Making SQL Connection and Inserting data
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("Insert INTO inventory (name, quantity, price) VALUES (%s, %s, %s)", (rice, rice_price, rice_quantity))

        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()
    

        
# Opening of app
app = QApplication(sys.argv)            
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())