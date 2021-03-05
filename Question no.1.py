from flask import Flask,jsonify,request 
import re
app = Flask(__name__)  
  
@app.route('/find_symbols_in_names', methods = ['POST']) 
def home():
    request_data = request.get_json()
    if 'chemicals' in request_data:
        chemicals = request_data['chemicals']

    if 'symbols' in request_data:
        symbols = request_data['symbols']
       
    res = []
    for symbol in symbols:
        for chemical in chemicals:
            search = re.search(symbol, chemmical)
            if search:
                res.append(re.sub(symbol, "[{}]".format(symbol), chemical))
    result=", ".join(res)
    return jsonify({"result":result})
  
if __name__ == '__main__': 
  
    app.run(debug=True)
