from flask import Flask, render_template, request

app = Flask(__name__)

usuarios = {}

@app.route('/')
def home():
    return render_template("index.html")  # Carga el archivo en /templates/index.html

@app.route('/login/<rol>', methods=['GET', 'POST'])
def login(rol):
    if request.method == 'POST':
        correo = request.form['correo_electronico']
        password = request.form['password']

        # Verificación de usuario
        for user in usuarios():
            if user["email"] == correo and user["password"] == password and user["rol"].upper() == rol.upper():
                return f"Bienvenido {user['nombre']} ({user['rol']}) - Página en construcción"

        return render_template("login.html", rol=rol, error="Credenciales incorrectas")

    return render_template("login.html", rol=rol)

if __name__ == '__main__':
    app.run(debug=True)

