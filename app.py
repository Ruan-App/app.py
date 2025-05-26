from flask import Flask, request, jsonify

app = Flask(__name__)

scan_logs = []

@app.route('/upload_scan', methods=['POST'])
def upload_scan():
    data = request.json
    print("Received scan:", data)
    scan_logs.append(data)
    return jsonify({"status": "success", "message": "Scan received"}), 200

@app.route('/scans', methods=['GET'])
def get_scans():
    return jsonify(scan_logs), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
