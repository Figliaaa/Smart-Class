# 🚀 Panduan Lengkap Git & GitHub untuk Proyek Tim

Panduan ini berisi kumpulan perintah Git dan alur kerja (*workflow*) yang wajib diketahui oleh anggota tim selama mengerjakan proyek.

---

## 📑 Daftar Isi
1. [Konfigurasi Awal (Sekali di Awal)](#1-konfigurasi-awal-sekali-di-awal)
2. [Memulai Pekerjaan (Clone & Branch)](#2-memulai-pekerjaan-clone--branch)
3. [Alur Kerja Harian (Add, Commit, Push)](#3-alur-kerja-harian-add-commit-push)
4. [Mengambil Update Terbaru (Pull & Sync)](#4-mengambil-update-terbaru-pull--sync)
5. [Membuat Pull Request (PR) di GitHub](#5-membuat-pull-request-pr-di-github)
6. [Perintah Berguna Lainnya (Utilitas)](#6-perintah-berguna-lainnya-utilitas)
7. [Penanganan Masalah Umum (Troubleshooting)](#7-penanganan-masalah-umum-troubleshooting)

---

## 1. Konfigurasi Awal (Sekali di Awal)

Sebelum melakukan commit, pastikan identitas akun Git kamu sudah terpasang di komputer/laptop:

```bash
# Atur nama lengkap kamu
git config --global user.name "Nama Lengkap Kamu"

# Atur email yang terhubung dengan akun GitHub
git config --global user.email "emailkamu@gmail.com"

# Verifikasi konfigurasi
git config --list
```

---

## 2. Memulai Pekerjaan (Clone & Branch)

### a. Mengunduh Repositori dari GitHub (Clone)
Jalankan perintah ini **hanya satu kali** di awal proyek untuk mengunduh kode ke komputer lokal:

```bash
git clone https://github.com/USERNAME/NAMA-REPO.git
cd NAMA-REPO
```

### b. Membuat dan Beralih ke Branch Baru
**Aturan Utama:** Jangan pernah melakukan koding langsung di branch `main`. Selalu buat branch baru untuk tiap fitur/tugas!

```bash
# Format nama branch: divisi/nama-fitur
# Contoh Tim Elektrik:
git checkout -b elektrik/baca-dht22

# Contoh Tim Web/Server:
git checkout -b web/layout-dashboard

# Mengecek kamu sedang berada di branch mana:
git branch
```

---

## 3. Alur Kerja Harian (Add, Commit, Push)

Setiap kali selesai menambah, mengubah, atau menghapus kode, lakukan langkah-langkah ini secara berurutan:

### Step 1: Cek Perubahan
```bash
git status
```
*Perintah ini menampilkan file mana saja yang telah kamu ubah.*

### Step 2: Masukkan Perubahan ke Staging Area
```bash
# Memasukkan SEMUA file yang diubah
git add .

# Atau memasukkan file spesifik saja
git add elektrik/src/main.cpp
```

### Step 3: Simpan Perubahan (Commit)
Buat pesan commit yang singkat dan jelas menggambarkan perubahan yang dibuat.
```bash
git commit -m "feat(elektrik): menambahkan pembacaan sensor DHT22"
```

### Step 4: Unggah ke GitHub (Push)
```bash
# Format: git push origin NAMA_BRANCH_KAMU
git push origin elektrik/baca-dht22
```

---

## 4. Mengambil Update Terbaru (Pull & Sync)

Agar kodingan di komputermu tidak tertinggal dengan perubahan yang dibuat oleh anggota tim lain:

### a. Berpindah Kembali ke Branch Utama
```bash
git checkout main
```

### b. Mengunduh Perubahan Terbaru dari GitHub
```bash
git pull origin main
```

### c. Menggabungkan Update `main` ke Branch Kamu
Setelah branch `main` lokal kamu terbarui, gabungkan ke branch fitu yang sedang kamu kerjakan:
```bash
git checkout elektrik/baca-dht22
git merge main
```

---

## 5. Membuat Pull Request (PR) di GitHub

Setelah pekerjaan di branch kamu selesai dan sudah di-`push` ke GitHub:

1. Buka repositori proyek di browser web GitHub.
2. Kamu akan melihat banner kuning bertuliskan **"Compare & pull request"**. Klik tombol tersebut.
3. Berikan judul yang jelas dan deskripsi singkat tentang apa yang telah kamu selesaikan.
4. Pilih **Reviewer** (misalnya Koordinator Divisi atau Ketua Tim).
5. Klik **Create Pull Request**.
6. Tunggu hingga kode kamu direview dan di-*merge* ke branch `main`.

---

## 6. Perintah Berguna Lainnya (Utilitas)

### Menyimpan Pekerjaan Sementara (Stash)
Gunakan ini jika kamu harus berpindah branch secara mendadak tetapi kodingan saat ini belum siap di-commit:
```bash
# Simpan perubahan sementara
git stash

# Pindah ke branch lain, lalu kembali lagi...
# Buka kembali simpanan sementara tadi:
git stash pop
```

### Melihat Riwayat Commit
```bash
# Melihat log riwayat commit
git log --oneline

# Melihat log dalam bentuk grafik visual sederhana
git log --graph --oneline --all
```

### Membatalkan Perubahan Lokal
```bash
# Membatalkan perubahan pada satu file sebelum di-add/commit
git checkout -- nama_file.cpp

# Membatalkan staging (git add) pada file
git restore --staged nama_file.cpp
```

---

## 7. Penanganan Masalah Umum (Troubleshooting)

### 🔴 Problem 1: Conflict saat `git pull` atau `git merge`
**Penyebab:** Kamu dan anggota tim lain mengubah baris kode yang sama pada file yang sama.
**Solusi:**
1. Buka file yang bermasalah di Text Editor (VS Code / Arduino IDE).
2. Cari tanda `<<<<<<<`, `=======`, dan `>>>>>>>`.
3. Pilih baris kode mana yang ingin dipertahankan dan hapus penanda konflik tersebut.
4. Simpan file, lalu jalankan:
   ```bash
   git add .
   git commit -m "fix: menyelesaikan merge conflict"
   git push origin NAMA_BRANCH
   ```

### 🔴 Problem 2: `push rejected (non-fast-forward)`
**Penyebab:** Ada pembaruan di GitHub yang belum ada di komputer lokal kamu.
**Solusi:**
```bash
git pull origin NAMA_BRANCH
# Selesaikan konflik jika ada, lalu push kembali:
git push origin NAMA_BRANCH
```

### 🔴 Problem 3: Salah Nulis Pesan Commit
```bash
git commit --amend -m "pesan commit baru yang benar"
```

---

💡 **Tips Penting:**
* Lakukan `git push` secara berkala (minimal 1x sehari) agar progres pekerjaanmu aman dan tidak hilang jika laptop bermasalah.
* Jangan malu bertanya di grup jika menemukan error Git!