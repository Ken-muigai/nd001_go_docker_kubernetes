import json
import logging

from flask import Flask

app = Flask(__name__)

number = 1234578
num = [x for x in str(number)]
first_set = "".join(num[:3])
rest_of_the_set = str(num[3:])
for i in rest_of_the_set % 3:
    print(int(first_set))
    print(rest_of_the_set)



@app.route("/")
def hello():
    app.logger.info('Metrics request successfull')
    return "Hello World!"


@app.route("/status")
def status_check():
    response = app.response_class(
        response=json.dumps({"Result": "Ok - healthy"}), status=200, mimetype='application/json'
    )
    app.logger.info("Success")
    return response


@app.route("/metrics")
def metrics_check():
    metric_response = app.response_class(
        response=json.dumps({"status": "Success", "code": 0, "data": {"UserCount": 140, "UserCountActive":23}}),
        status=200,
        mimetype="application/json"
    )
    app.logger.info("Thats how its done man")
    return metric_response

@app.route("/something")
def funct():
    jsoresp = app.response_class(
        onet  = json.dumps(

        )

    )



if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
