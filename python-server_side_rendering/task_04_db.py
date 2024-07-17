from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def read_csv(file_path):
    products = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sqlite(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    products = [
        {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
        for row in cursor.fetchall()
    ]
    conn.close()
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    try:
        if source == 'json':
            products = read_json('products.json')
        elif source == 'csv':
            products = read_csv('products.csv')
        elif source == 'sql':
            products = read_sqlite('products.db')
        else:
            return render_template('product_display.html', error="Wrong source")
    except Exception as e:
        return render_template('product_display.html', error=str(e))

    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
