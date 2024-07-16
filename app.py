from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return ('''<html>
    <h1>Hello, here's pictures of food, an animal and outer space</h1> 

    <img wdith="500px" src="https://thecozycook.com/wp-content/uploads/2022/04/Lasagna-Recipe-f.jpg"></html>''')




if __name__ == '__main__':
    app.run(debug=True)
