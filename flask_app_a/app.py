from flask import Flask,request,render_template,jsonify

app = Flask(__name__)

@app.route("/")
def calci_Home():
    return render_template('index.html')

@app.route("/math",methods=['POST'])
def Calculator():
    if (request.method == 'POST'):
        operate = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if operate == 'add':
            res = num1 + num2
            result = "Your Entered Digit is" + ' '+ str(num1) + " and" + ' ' + str(num2) + " Additon is" + ' '+str( res)
        return render_template('results.html', result = result)

        if operate == 'subtract':
            res = num1 - num2
            result = "Your Entered Digit is" + ' '+ str(num1) + " and" + ' ' + str(num2) + " Subtraction is" + ' '+str( res)
        return render_template('results.html', result = result)

        if operate == 'multiply':
            res = num1 * num2
            result = "Your Entered Digit is" + ' '+ str(num1) + " and" + ' ' + str(num2) + " Multiplication is" + ' '+str( res)
        return render_template('results.html', result = result)

        if operate == 'divide':
            res = num1 / num2
            result = "Your Entered Digit is" + ' '+ str(num1) + " and" + ' ' + str(num2) + " Division is" + ' '+str( res)
        return render_template('results.html', result = result)



@app.route("/postman",methods=['POST'])
def API_test_Calculator():
    if (request.method == 'POST'):
        operate = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if operate == 'add':
            res = num1 + num2
            result = "Your Entered Digit is" + ' '+ str(num1) + " and" + ' ' + str(num2) + " Additon is" + ' '+str( res)

        if operate == 'subtract':
            res = num1 - num2
            result = "Your Entered Digit is" + ' '+ str(num1) + " and" + ' ' + str(num2) + " Subtraction is" + ' '+str( res)
        
        if operate == 'multiply':
            res = num1 * num2
            result = "Your Entered Digit is" + ' '+ str(num1) + " and" + ' ' + str(num2) + " Multiplication is" + ' '+str( res)
        
        if operate == 'divide':
            res = num1 / num2
            result = "Your Entered Digit is" + ' '+ str(num1) + " and" + ' ' + str(num2) + " Division is" + ' '+str( res)
        return jsonify(result)


if __name__=="__main__":
    app.run(host="0.0.0.0")
