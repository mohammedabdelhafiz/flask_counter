from flask import Flask, render_template, redirect, request , jsonify
app = Flask(__name__)   



counter = 1

@app.route("/")
def main():
    global counter
    counter += 1
    return render_template('index.html' , countt = counter)





if __name__ == "__main__":   
    app.run(debug=True)    
