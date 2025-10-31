from flask import Flask, request, jsonify
import os

app = Flask(__name__)
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    datos = request.data.decode('utf-8')
    if not datos:
        return jsonify({"error": "No data received"}), 400
    
    ip_cliente = request.remote_addr.replace(":", "_") #replace ':' to avoid issues in filenames
    archivo_ip = f"{ip_cliente}.txt"
    filepath = os.path.join(LOG_DIR, archivo_ip)

    linea = f"{datos}\n"
    
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(linea)

    return jsonify({"message": "Data saved successfully", "file": archivo_ip}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
