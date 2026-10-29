import os
import json
import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS
import paho.mqtt.client as mqtt
import threading

app = Flask(__name__)
CORS(app)

DB_PATH = '/app/database/classroom.db'
MQTT_BROKER = os.getenv('MQTT_BROKER', 'localhost')
MQTT_PORT = int(os.getenv('MQTT_PORT', 1883))

# Initialise Database
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            node_id TEXT,
            suhu REAL,
            kelembapan REAL,
            cahaya_lux REAL,
            gerak INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT Broker with code {rc}")
    client.subscribe("ukmati/classroom/node1/sensor")

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO sensor_logs (node_id, suhu, kelembapan, cahaya_lux, gerak)
            VALUES (?, ?, ?, ?, ?)
        ''', (data.get('node_id'), data.get('suhu'), data.get('kelembapan'), data.get('cahaya_lux'), 1 if data.get('gerak') else 0))
        conn.commit()
        conn.close()
        print("Data inserted:", data)
    except Exception as e:
        print("Error processing message:", e)

def start_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()

# REST API Endpoints
@app.route('/api/readings', methods=['GET'])
def get_readings():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT node_id, suhu, kelembapan, cahaya_lux, gerak, timestamp FROM sensor_logs ORDER BY id DESC LIMIT 50')
    rows = cursor.fetchall()
    conn.close()
    
    result = []
    for r in rows:
        result.append({
            "node_id": r[0],
            "suhu": r[1],
            "kelembapan": r[2],
            "cahaya_lux": r[3],
            "gerak": bool(r[4]),
            "timestamp": r[5]
        })
    return jsonify(result)

@app.route('/api/control', methods=['POST'])
def send_control():
    body = request.json
    # Publish command to MQTT
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.publish("ukmati/classroom/node1/command", json.dumps(body))
    client.disconnect()
    return jsonify({"status": "success", "command_sent": body})

if __name__ == '__main__':
    init_db()
    # Run MQTT in background thread
    mqtt_thread = threading.Thread(target=start_mqtt, daemon=True)
    mqtt_thread.start()
    app.run(host='0.0.0.0', port=5000)
