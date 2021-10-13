from flask import Flask, request, jsonify
from blood_calculator import hdl_analysis

app = Flask(__name__)

@app.route("/", methods=["GET"]) # Empty/base route
@app.route("/index", methods=["GET"])
def server_status():
    return "Server is ON"


@app.route("/info", methods=["GET"]) 
def info():
    my_output = "This server is for BME 547"
    return my_output


@app.route("/hdl", methods=["POST"])
def hdl_analysis_server():
    """
    Input should look like {"hdl": 58, "patient_id": 200}

    :return:
    """
    in_data = request.get_json()
    hdl_value = in_data["hdl"]
    print("The hdl value is {}".format(hdl_value))
    answer = hdl_analysis(hdl_value)
    return jsonify(hdl_value), 201

@app.route("/hdl/<hdl_value>", methods=["GET"])
def hdl_analysis_servers(hdl_value):
    """
    Input should look like {"hdl": 58, "patient_id": 200}

    :return:
    """
    # in_data = request.get_json()
    # hdl_value = in_data["hdl"]
    hdl_value = int(hdl_value)
    print("The hdl value is {}".format(hdl_value))
    answer = hdl_analysis(hdl_value)
    return jsonify(answer), 201


@app.route("/say_hello/<input_name>", methods=["GET"])
def say_hello(input_name):
    return "Hello, {}".format(input_name)

if __name__ == '__main__':
    app.run()