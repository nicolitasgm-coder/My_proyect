from flask import Flask

# Creamos la aplicación
app = Flask(__name__)

# Definimos una ruta principal
@app.route("/")
def home():
    return "Hola, Render está funcionando 🚀"

# Esto asegura que se ejecute en Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
