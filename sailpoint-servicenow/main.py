from flask import Flask,request,json,render_template 
import requests

app = Flask(__name__)


@app.route('/raiseincident',methods=["POST"])
def raiseIncident():
    category = request.form['category']
    impact = request.form['impact']
    urgency = request.form['urgency']
    address = request.form['address']
    message = "Sorry! Request Not Submitted."

    data = {"caller_id":"System Administrator","impact":impact,"urgency":urgency,"short_description":address,"category":category}
    result = firedApi(json.dumps(data))
    if result:
        message = "Request Submitted!, Incident No. "+result
        return render_template('nextpage.html',message=message)




   # return "Hello World!" + category +" " + impact + " "+ urgency + " " +address

def firedApi(data):
    url = 'https://dev63380.service-now.com/api/now/table/incident'
    user = 'admin'
    pwd = 'Pass@123'
    headers = {"Content-Type":"application/json","Accept":"application/json"}
    response = requests.post(url, auth=(user, pwd), headers=headers ,data=data)

    # if response.status_code != 200:
    #     print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    #     return response.json()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    print(type(data))
    print(data.keys())
    print(data['result']['number'])
    return data['result']['number']


if __name__ == '__main__':
    app.run(debug=True)