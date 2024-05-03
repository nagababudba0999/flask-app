from flask import Flask, render_template, request
import boto3

# Configure DynamoDB resource

# Configure DynamoDB resource
region_name = 'us-east-1'
table_name = 'userdetailsnv'

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)
#dynamodb = boto3.resource('dynamodb')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        print(first_name,last_name)
        # Store data in DynamoDB
        table = dynamodb.Table(table_name)
        table.put_item(Item={
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number
        })
        return render_template('success.html')
    
    return render_template('index.html')

@app.route('/fetch_data', methods=['GET'])   
def fetch_data():
    response = table.scan()
    items = response.get('Items', [])
    return render_template('fetch_data.html', items=items)
    # Handle fetching DynamoDB data (GET request)
    # Add your code here to fetch data from DynamoDB
    #return "Fetching DynamoDB Data..."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)

