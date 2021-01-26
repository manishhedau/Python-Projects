from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world !"

@app.route('/isprime/<int:n>')
def isPrime(n): 
      
    # Corner case 
    if (n <= 1): 
        result = {
            "Number":n,
            "IsPrime":False,
            'name':"Manish hedau",
            'list':[1,2,3,4,5]
        }
  
    # Check from 2 to n-1 
    for i in range(2, n): 
        if (n % i == 0): 
             result = {
            "Number":n,
            "IsPrime":False,
            'name':"Manish hedau",
            'list':[1,2,3,4,5]
        }
    else:
        result = {
            "Number":n,
            "IsPrime":True,
            'name':"Manish hedau",
            'list':[1,2,3,4,5]
        }

  
    return jsonify(result)
        


if __name__ == "__main__":
    app.run(debug = True)