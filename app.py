from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return ('''<html>
    <a href="/food1">Go to the page for food1</a>
    <a href="/food3">Go to the page of food3 here</a>
    <a href="/pet2">Go to the page of pet2 here</a>
    <a href="/space1">Go to the page of space1 here</a>
    <body>
    <h1>Hello, here are pictures of food, animals and outer space</h1>
    </body>
    </html>''')

@app.route('/food1')
def food1():
    return ('''<html>
    <body>    
    <h1>Here's a picture of food</h1>
    <img src="https://thecozycook.com/wp-content/uploads/2022/04/Lasagna-Recipe-f.jpg">
    <a href="/home"> Click here to go back to the home page</a>
    <a href="/food2"> Click here for another picture of food (food2)</a>
    </body>
    </html>''')

@app.route('/food2')
def food2():
    return ('''<html>
        <body>
        <h1>Hi here's another picture of food</h1>
        <img src="https://www.onceuponachef.com/images/2023/10/smores.jpg">
        <a href="/food1"> Click here to go back to the page of food1</a>
        <a href="/food3"> Click here to go to the picture of food3</a> 
        </body>
        </html>''')

@app.route('/food3')
def food3():
    return ('''<html>
    <body>    
    <h1>Here's another picture of food</h1>
    <img src="https://hungrybynature.com/wp-content/uploads/2017/09/pinch-of-yum-workshop-19.jpg">
    <a href="/home"> Click here to go back to the home page</a>
    <a href="/food2"> Click here to go back to the page of food2</a>
    </body>
    </html>''')

@app.route('/pet1')
def pet1():
    return ('''<html>
    <body>
    <h1>Here's a picture of a pet</h1>
    <img src="https://t4.ftcdn.net/jpg/01/99/00/79/360_F_199007925_NolyRdRrdYqUAGdVZV38P4WX8pYfBaRP.jpg">
    <a href="/pet2"> Click here to go the page of pet2</a>
    </body>
    </html>''')

@app.route('/pet2')
def pet2():
    return('''<html>
    <body>
    <h1>Here's a picture of another pet (pet2)</h1>
    <img src="https://www.usatoday.com/money/blueprint/images/uploads/2023/06/27134316/best-pet-insurance-scaled-e1687873423254.jpg">
    <a href="/home"> Click here to go back to the home page</a>
    <a href="/pet1"> Click here to go to pet1</a>
    <a href="/pet3"> Click here to go to pet3</a>
    </body>
    </html>''')

@app.route('/pet3')
def pet3():
    return('''<html>
    <body>
    <h1>here's a picture of even another pet (pet3)</h1>
    <img src="https://images.saymedia-content.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:eco%2Cw_1200/MTk3NTc0OTQ3OTk5MDY1Mzg5/how-to-be-a-good-owner-of-a-headgehog.jpg">
    <a href="/pet2">Click here to go back to pet2</a>
    </body>
    </html>''')

@app.route('/space1')
def space1():
    return('''<html>
    <body>
    <h1>Here's a picture of space!</h1>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/LH_95.jpg/1200px-LH_95.jpg">
    <a href="/space2">Click here to acces another picture of space (space2)</a>
    <a href="/space3">Click on here to acces even another picture of space (space3)</a>
    <a href="/home">Click here to go back to the home page</a>
    </body>
    </html>''')


@app.route('/space2')
def space2():
    return('''<html>
    <body>
    <h1>Here's a picture of space!</h1>
    <img src="https://c02.purpledshub.com/uploads/sites/48/2020/04/Things-never-knew-astronomy-e454e5d.jpg">
    <a href="/space1">Click here to acces another picture of space (space2)</a>
    <a href="/space3">Click on here to acces even another picture of space (space3)</a>
    <a href="/home">Click here to go back to the home page</a>
    </body>
    </html>''')


@app.route('/space3')
def space3():
    return('''<html>
    <body>
    <h1>Here's a picture of space!</h1>
    <img src="https://t4.ftcdn.net/jpg/03/86/82/73/360_F_386827376_uWOOhKGk6A4UVL5imUBt20Bh8cmODqzx.jpg">
    <a href="/space1">Click here to acces another picture of space (space2)</a>
    <a href="/space2">Click on here to acces even another picture of space (space3)</a>
    <a href="/home">Click here to go back to the home page</a>
    </body>
    </html>''')


if __name__ == '__main__':
    app.run(debug=True)
