from flask import Flask, request,render_template
from app import app

@app.route('/reverse',methods=['GET','POST'])
def reverse_string():
    if request.method=='POST':
        input_string = request.form['input_string']
        output_string = input_string[::-1]
        return render_template('index.html',output_string=output_string)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
