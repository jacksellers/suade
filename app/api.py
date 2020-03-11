import flask
import sqlite3

from flask import request, jsonify

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/api/v1/report', methods=['GET'])
def report():
    args = request.args
    if 'date' in args:
        date = args['date']
        with sqlite3.connect('app.db') as con:
            cur = con.cursor()
            customers = cur.execute(
                'SELECT COUNT(DISTINCT customer_id) FROM orders '
                'WHERE date(created_at)={}'.format(date)
            ).fetchone()[0]
            total_discount_amount = cur.execute(
                'SELECT SUM(discounted_amount) FROM order_lines '
                'INNER JOIN orders ON order_lines.order_id=orders.id '
                'WHERE date(created_at)={}'.format(date)
            ).fetchone()[0]
            items = cur.execute(
                'SELECT COUNT(*) FROM order_lines '
                'INNER JOIN orders ON order_lines.order_id=orders.id '
                'WHERE date(created_at)={}'.format(date)
            ).fetchone()[0]
            order_total_avg = cur.execute(
                'SELECT AVG(total_amount) FROM order_lines '
                'INNER JOIN orders ON order_lines.order_id=orders.id '
                'WHERE date(created_at)={}'.format(date)
            ).fetchone()[0]
            discount_rate_avg = cur.execute(
                'SELECT AVG(discount_rate) FROM order_lines '
                'INNER JOIN orders ON order_lines.order_id=orders.id '
                'WHERE date(created_at)={}'.format(date)
            ).fetchone()[0]
        con.close()
        return jsonify(
            {
                'customers': customers,
                'total_discount_amount': round(total_discount_amount, 2),
                'items': items,
                'order_total_avg': round(order_total_avg, 2),
                'discount_rate_avg': round(discount_rate_avg, 2)
            }
        )
    else:
        return jsonify(
            {
                'error': 'Please include a date in the request parameters.'
            }
        )

app.run()