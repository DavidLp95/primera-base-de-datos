from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configura la ruta de la carpeta estática
app.config['STATIC_FOLDER'] = 'static'  # Suponiendo que tus archivos estáticos estén en una carpeta llamada 'static'

# Configura la conexión a la base de datos MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',       # Reemplaza con tu usuario de MySQL
    'password': '1015451473', # Reemplaza con tu contraseña de MySQL
    'database': 'aprendiendo',
    'port': 3307
}

# se modifica el pueto raiz html----------
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    celular = request.form['celular']
    genero = request.form['genero']
    correo = request.form['correo']
    direccion = request.form['direccion']


    # Conectar a la base de datos y guardar los datos
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO usuarios (nombre, apellido, celular, genero, correo, direccion)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (nombre, apellido, celular, genero, correo, direccion))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
