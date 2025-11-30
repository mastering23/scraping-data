import os
from django.shortcuts import render
import csv

# Path to this file's directory (the app folder)
APP_DIR = os.path.dirname(os.path.abspath(__file__))

def home(request):
    quotes = []
    csv_path = os.path.join(APP_DIR, 'quotes.csv')  # points to quotes.csv in the app folder
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:
                quotes.append({'author': row[0], 'quote': row[1]})
    return render(request, 'quotes_app/app.html', {'quotes': quotes})
