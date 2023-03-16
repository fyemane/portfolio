from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# create a new function to store sent messages in txt file
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


# create a new function to store sent messages in csv file
def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


# requesting data
# POST and GET are defualt
# wrap in try block
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            # turn all data into dictionary
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            # redirect to thank you page
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. try again!'
