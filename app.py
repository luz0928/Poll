from flask import Flask, render_template, request, json
from flask.ext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ormuco1'
app.config['MYSQL_DATABASE_DB'] = 'Results'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/sendData',methods=['POST'])
def sendData():
    try:
        _name = request.form['inputName']
        _color = request.form['inputColor']
        _pet = request.form['inputPet']

        if _name and _color and _pet:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('createResults',(_name,_color,_pet))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'Data sent succesfully'})
            else:
                return json.dumps({'error':str(data[0])})

        else:
            return json.dumps({'html':'<span>Please complete all fields.</span>'})

    except Exception as e:
         return json.dumps({'error':str(e)})
    finally:
        cursor.close() 
        conn.close()

if __name__ == "__main__":
    app.run()
