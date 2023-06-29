from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/k1/')
def k1():
  return render_template('k1.html')
if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/k2/')
def k2():
  return render_template('k1.html')
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/k3/')
def k3():
  return render_template('k1.html')
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/k4/')
def k4():
  return render_template('k1.html')
if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/k5/')
def k5():
  return render_template('k1.html')
if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/k6/')
def k6():
  return render_template('k1.html')
if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/k7/')
def k7():
  return render_template('k1.html')
if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/k8/')
def k8():
  return render_template('k1.html')
if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/k9/')
def k9():
  return render_template('k1.html')
if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/k10/')
def k10():
  return render_template('k1.html')
if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/k11/')
def k11():
  return render_template('k1.html')
if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/k12/')
def k12():
  return render_template('k1.html')
if __name__ == '__main__':
    app.run(debug=True)