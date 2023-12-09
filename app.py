from flask import Flask, render_template, request
import mysql.connector
import tensorflow as tf

model = tf.keras.models.load_model('model_2.h5')


db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '1234',
    'port':3306

}

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():    
    image_file = request.files['image']    
    image = image_file.read()
    image = tf.image.decode_png(image, channels=1)
    image = tf.image.resize(image, [28, 28])
    image = image / 255.0    
    prediction = model.predict(tf.expand_dims(image, axis=0)).argmax(axis=1)[0]
    prediction = int(prediction)    
    log_request_and_result(image_file.filename, prediction)
    return render_template('index.html', prediction=prediction)



def log_request_and_result(filename, prediction):
    prediction = int(prediction)
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS mnist")
    cursor.execute("USE mnist")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            filename VARCHAR(255) NOT NULL,
            prediction INT NOT NULL
        )
    """)    
    sql = "INSERT INTO predictions (filename, prediction) VALUES (%s, %s)"
    values = (filename, prediction)
    cursor.execute(sql, values)

    db.commit()
    cursor.close()
    db.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
