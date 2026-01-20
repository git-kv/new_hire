import os, sys, logging, csv
import pandas as pd

from datetime import datetime, timedelta, time
from PyQt6.QtCore import Qt, QCoreApplication, QDate
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QLineEdit, QPushButton, QSpacerItem, QCalendarWidget, QCheckBox, QMessageBox

today = datetime.today().strftime('%Y-%m-%d')
log_path = '\\\\eocservices\\apps$\\programs\\scripts\\logs\\employee_account_creation_' + today + '.log'
logging.basicConfig(filename=log_path, level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')