# suade

### Description
A simple REST API using Flask and SQLite that creates reports based on sales data

### Installation

```
git clone https://github.com/jackwsellers/suade.git
cd suade
virtualenv appenv
source appenv/bin/activate
pip install -r requirements.txt
python db_setup.py
python app/api.py
```

### Testing
Example:
```
curl -X GET 'http://127.0.0.1:5000/api/v1/report?date="2019-08-01"'
```
Response:
```
{
  "customers": 9,
  "discount_rate_avg": 0.13,
  "items": 121,
  "order_total_avg": 1182286.1,
  "total_discount_amount": 130429980.26
}
```
