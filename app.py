from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return ('''<html>
    <h1>Hello, here's pictures of food, an animal and outer space</h1> 

    <img width="500px" src="https://thecozycook.com/wp-content/uploads/2022/04/Lasagna-Recipe-f.jpg">
    <img width="500px" src="https://media.wired.com/photos/593261cab8eb31692072f129/master/pass/85120553.jpg">
    <img width="500px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Webb%27s_First_Deep_Field.jpg/310px-Webb%27s_First_Deep_Field.jpg">


    </html>''')




if __name__ == '__main__':
    app.run(debug=True)
