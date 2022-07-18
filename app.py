from flask import Flask
from flask import render_template
from flask import Flask,request
import sqlite3
# from instamojo_wrapper import Instamojo
# API_KEY = "aef7265f4ea64c280a85c4936e4fcf28"
# AUTH_TOKEN = "59ce92abe04fde4c46b61d896d06a432"

# api = Instamojo(api_key=API_KEY,auth_token=AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1')

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/success")
# def sucess_pay():
#     return render_template('success.html')

@app.route("/",methods = ["GET", "POST"])
def world():
    #getting the data from html form
    if request.method == "POST":
        first_name = request.form.get("name")
        first_mail = request.form.get("e_mail")
        first_mob = request.form.get("mob_no")
        first_domain = request.form.get("domain")
        first_college = request.form.get("coll_name")
        first_branch = request.form.get("branch")
        first_month = request.form.get("month")
        first_gender = request.form.get("gender")
        first_add = request.form.get("address")
        first_trans_id = request.form.get("trans_id")

        #converting dropdown into value
        internship_domain = ["Internship", "Frontend web development", "Backend web development",
        "Full stack web development","Software development","UI/UX design","Data Science","IOT","Digital Marketing",
        "content Writing","Human Resource","Business development","Law","Machine Learning","Cloud Computing","Cyber security","Artificial intelligence","Android App Development",
        "Robotics","VLSI","Hybrid & Electric Vehicle","IC Engine","Auto CAD","Construction Planning","Nano science & nano technology","Genetic Engineering","Finance"]
        month = ["Month","July","August","September"]
        gender = ["gender","Male","Female","others"]

        #replacing the value from original one
        first_domain = internship_domain[int(first_domain)]
        first_month = month[int(first_month)]
        first_gender = gender[int(first_gender)]

        #making connection with database
        conn = sqlite3.connect("registration_entry.db")

        #firing the insert query
        ins=f'''
            INSERT INTO registred_Students(name,email,mob_number,domain,college_name,branch,month,gender,address,Transaction_ID)
             VALUES ('{first_name}','{first_mail}','{first_mob}','{first_domain}','{first_college}','{first_branch}','{first_month}','{first_gender}','{first_add}', '{first_trans_id}')
        '''
        conn.execute(ins)
        conn.commit()
        conn.close()


        #executing and commiting the changes then closing the connection
        print("success")
        if(bool("success")):
            return render_template('success.html')
    return render_template('index.html')




@app.route("/success")
def sucess_pay():
    return render_template('success.html')


if __name__ == "__main__":
    app.run(debug=True)

# DEFAULT PAYMENT LINK ->  https://instamojo.com/@Scibiscus
