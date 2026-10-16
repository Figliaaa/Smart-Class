# 🏫 Smart Classroom IoT Project

[![Project Status: Active](https://img.shields.io/badge/Project-Active-brightgreen.svg)]()
[![Division: IoT UKM](https://img.shields.io/badge/UKM-IoT%20Division-blue.svg)]()
[![Hardware: ESP32](https://img.shields.io/badge/Hardware-ESP32-red.svg)]()
[![Frontend: React.js](https://img.shields.io/badge/Frontend-React.js-61DAFB.svg)]()

Selamat datang di repositori utama **Proyek Smart Classroom**! Proyek ini dirancang sebagai proyek kolaboratif untuk anggota baru UKM dalam membangun sistem pemantauan dan otomasi ruang kelas berbasis *Internet of Things* (IoT) secara *end-to-end*.

---

## 📌 1. Tentang Proyek

Sistem **Smart Classroom** bertujuan untuk memantau kondisi lingkungan ruang kelas secara *real-time* (suhu, kelembapan, intensitas cahaya, dan keberadaan orang) serta melakukan kontrol otomasi terhadap perangkat elektrik (seperti AC dan lampu). Selain itu, seluruh data akan ditayangkan secara interaktif pada *dashboard* berbasis React.js.

### 🎯 Fitur Utama
1. **Monitoring Real-time:** Pengukuran suhu, kelembapan udara, tingkat pencahayaan, dan deteksi gerakan.
2. **Otomasi Lokal (Edge Logic):** Kontrol otomatis Relay (AC/Lampu) berdasarkan batas ambang (*threshold*) sensor.
3. **Pusat Komunikasi Data:** Mengirim dan menerima data menggunakan protokol MQTT.
4. **Web Dashboard (React):** Tampilan grafik histori, indikator status *real-time*, serta tombol kontrol manual remote.
5. **Sistem Alerting:** Notifikasi otomatis jika kondisi ruangan berada di luar batas ideal.

---

## 🏗️ 2. Arsitektur Sistem & Kontrak Data

Agar Tim Elektrik dan Tim Server/React dapat bekerja secara independen tanpa saling menunggu, berikut adalah gambaran arsitektur sistem dan **Kontrak Format Data MQTT**.

### Arsitektur Ringkas
```text
[ Sensor Node (ESP32) ] 
     │ 
     ├── (Sensors: DHT22, BH1750, PIR) ──> Publish Sensor Data
     └── (Actuators: Relay AC/Lampu)    <── Subscribe Command
     │
     ▼ (Protokol MQTT via WiFi)
[ MQTT Broker ]
     │
     ├──> [ Backend Server & Database ] (Log Data & API Service)
     └──> [ React Web Dashboard ]       (Tampilan UI Real-time & Manual Control)
```

### 📑 Kontrak Format JSON & Topik MQTT

#### 1. Data Sensor (ESP32 ──> Broker ──> Server/Web)
* **Topik:** `ukmati/classroom/node1/sensor`
* **Format Payload (JSON):**
```json
{
  "node_id": "ruang_301",
  "suhu": 28.5,
  "kelembapan": 65.0,
  "cahaya_lux": 350,
  "gerak": true,
  "timestamp": 1725302400
}
```

#### 2. Perintah Kontrol Manual (Web/Server ──> Broker ──> ESP32)
* **Topik:** `ukmati/classroom/node1/command`
* **Format Payload (JSON):**
```json
{
  "relay_ac": "ON",
  "relay_lamp": "OFF",
  "timestamp": 1725302400
}
```

---

## 👥 3. Pembagian Tim & Tugas Kerja

Repositori ini berstatus **kosong (0 file)** pada awalnya. Tugas kalian adalah membangun struktur folder dan kode sesuai divisi masing-masing.

```text
smart-classroom-iot/
├── elektrik/           # Workdir Tim Elektrik (Firmware & Circuit Diagram)
│   ├── src/            # Kode Program Arduino / PlatformIO
│   ├── docs/           # Diagram Skematik Pin & Dokumentasi Komponen
│   └── README.md       # Panduan khusus setup Hardware
│
├── server/             # Workdir Tim Server Backend
│   ├── src/            # Service MQTT Logger, Database, & REST API
│   └── README.md       # Panduan khusus Backend & Database
│
├── web/                # Workdir Tim Frontend (React.js)
│   ├── src/            # Komponen & Page React.js
│   └── README.md       # Panduan khusus Running Web App
│
└── README.md           # Dokumentasi Utama Repo Ini
```

---

### ⚡ Tim Elektrik (Hardware & Firmware)
**Fokus Utama:** Merakit sensor/aktuator ke ESP32 dan menyusun program untuk membaca data serta berkomunikasi via MQTT.

* **Daftar Komponen:**
  * **ESP32 DevKit V4** (Microcontroller Utama)
  * **DHT22** (Sensor Suhu & Kelembapan)
  * **BH1750** (Sensor Intensitas Cahaya I2C)
  * **PIR HC-SR501** (Sensor Gerak)
  * **Relay Module 2-Channel** (Simulasi AC & Lampu)
* **Target Pengerjaan:**
  1. [ ] Buat program pembacaan tiap sensor secara terpisah.
  2. [ ] Gabungkan pembacaan seluruh sensor tanpa menggunakan `delay()` berlebihan (gunakan `millis()`).
  3. [ ] Hubungkan ESP32 ke WiFi dan MQTT Broker.
  4. [ ] Menerapkan format JSON sesuai **Kontrak Data**.
  5. [ ] Tambahkan alur logika otomasi lokal (*thresholding*) & *auto-reconnect* WiFi/MQTT.

---

### 💻 Tim Server & Frontend (Backend, Broker & React Web)
**Fokus Utama:** Mengelola lalu lintas data, menyimpan histori ke database, dan menampilkan *dashboard* web yang responsif.

* **Target Backend / Server:**
  1. [ ] Setup MQTT Broker (misal: Mosquitto atau broker publik untuk *testing* awal seperti `broker.hivemq.com`).
  2. [ ] Buat service *subscriber* (Node.js/Python) untuk menyimpan data ke Database (SQLite / PostgreSQL / MongoDB).
  3. [ ] Buat REST API atau WebSocket endpoint untuk kebutuhan data historis web.
* **Target Frontend React:**
  1. [ ] Setup *project* React (menggunakan Vite / Create React App) di folder `web/`.
  2. [ ] Buat *dashboard layout* (Card Stat, Status Indicator, Toggle Switch Relay).
  3. [ ] Integrasikan koneksi MQTT over WebSocket atau polling REST API.
  4. [ ] Tambahkan grafik interaktif (menggunakan Recharts / Chart.js) untuk histori suhu dan cahaya.

---

## 🚀 4. Alur Kerja Git & Kolaborasi

Sebagai anggota baru, ikuti panduan *workflow* Git berikut agar kode tidak saling bertabrakan:

### Step-by-Step Alur Kontribusi:

1. **Clone Repositori ini:**
   ```bash
   git clone https://github.com/USERNAME/REPO_NAME.git
   cd REPO_NAME
   ```

2. **Buat Branch Baru** sesuai divisi dan fitur yang kamu kerjakan:
   * Format nama branch: `nama-divisi/nama-fitur`
   * *Contoh Elektrik:*
     ```bash
     git checkout -b elektrik/baca-sensor-dht22
     ```
   * *Contoh React:*
     ```bash
     git checkout -b web/setup-dashboard-ui
     ```

3. **Lakukan Pekerjaan & Commit:**
   Gunakan pesan commit yang jelas dan deskriptif.
   ```bash
   git add .
   git commit -m "feat(elektrik): menambahkan pembacaan sensor DHT22 pada ESP32"
   ```

4. **Push Branch ke GitHub:**
   ```bash
   git push origin nama-divisi/nama-fitur
   ```

5. **Buat Pull Request (PR):**
   * Buka repositori di browser GitHub.
   * Pilih tombol **Compare & Pull Request**.
   * Jelaskan perubahan yang kamu buat, lalu mita koordinator divisi untuk meminjau (*review*) sebelum di-*merge* ke branch `main`.

---

## 📅 5. Timeline Pengerjaan (8 Minggu)

| Minggu | Agenda Utama | Output |
| :---: | :--- | :--- |
| **W1** | Onboarding, Pembagian Tim, & Initial Setup Repo | Folder direktori terbentuk, tools terinstall |
| **W2** | **Elektrik:** Tes Sensor Mandiri <br> **Server/Web:** Setup Base React & Backend Skeleton | Kode tes sensor & layout UI awal |
| **W3** | **Elektrik:** Kirim Data MQTT JSON <br> **Server/Web:** Database Logger & Integrasi Broker | Data ESP32 masuk ke Broker/Database |
| **W4** | **Elektrik:** Terima Command Relay <br> **Server/Web:** Fitur Control Remote di React | Control relay via Web Dashboard berhasil |
| **W5** | Testing End-to-End & Penanganan Error (*Auto-reconnect*) | Sistem stabil dari Hardware ke Web |
| **W6** | Optimalisasi UI Web (Grafik/Histori) & Otomasi Lokal ESP32 | Dashboard lengkap & fitur otomasi aktif |
| **W7** | Pengujian Durabilitas (Burn-in Test) & *Bug Fixing* | Sistem berjalan 24 jam tanpa error |
| **W8** | Dokumentasi Akhir, Pembuatan Video Demo, & Presentasi | Proyek Selesai & Siap Di-demo! |

---

## ❓ 6. Frequently Asked Questions (FAQ) & Troubleshooting

<details>
<summary><b>Q: Saya anggota baru dan belum paham betul React / ESP32, harus mulai dari mana?</b></summary>
<br>
Jangan khawatir! Mulailah dari file-file contoh kecil terlebih dahulu. 
* Tim Elektrik: Coba jalankan contoh program bawaan Arduino IDE seperti <i>Blink</i> dan <i>DHTtester</i>.
* Tim Server/React: Pelajari dasar React Hook (`useState`, `useEffect`) dan coba buat tampilan statis terlebih dahulu.
</details>

<details>
<summary><b>Q: Apa yang harus dilakukan jika data dari sensor di Web tidak muncul?</b></summary>
<br>
Gunakan <b>MQTTX</b> (Aplikasi MQTT Client GUI) sebagai "wasit". 
1. Cek apakah ESP32 berhasil publish data ke Broker melalui MQTTX.
2. Jika di MQTTX data masuk tetapi di React tidak muncul, berarti masalah ada pada koneksi WebSocket/API Web.
</details>

---

💡 *'The best way to learn IoT is to build IoT.'* Selamat berproses, jangan ragu untuk bertanya di grup diskusi UKM jika mengalami kendala! 🚀
