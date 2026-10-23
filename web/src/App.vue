<template>
  <div class="min-h-screen bg-gray-100 p-6">
    <header class="mb-6">
      <h1 class="text-3xl font-bold text-gray-800">
        🏫 Smart Classroom Dashboard
      </h1>
      <p class="text-gray-600">Monitoring & Kontrol Ruang Kelas Real-time</p>
    </header>

    <!-- Stat Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
      <div class="bg-white p-4 rounded-lg shadow">
        <h3 class="text-sm font-semibold text-gray-500">Suhu</h3>
        <p class="text-2xl font-bold text-red-500">{{ latest.suhu || 0 }} °C</p>
      </div>
      <div class="bg-white p-4 rounded-lg shadow">
        <h3 class="text-sm font-semibold text-gray-500">Kelembapan</h3>
        <p class="text-2xl font-bold text-blue-500">
          {{ latest.kelembapan || 0 }} %
        </p>
      </div>
      <div class="bg-white p-4 rounded-lg shadow">
        <h3 class="text-sm font-semibold text-gray-500">Intensitas Cahaya</h3>
        <p class="text-2xl font-bold text-yellow-500">
          {{ latest.cahaya_lux || 0 }} Lux
        </p>
      </div>
      <div class="bg-white p-4 rounded-lg shadow">
        <h3 class="text-sm font-semibold text-gray-500">Status Keberadaan</h3>
        <span
          :class="
            latest.gerak
              ? 'bg-green-100 text-green-800'
              : 'bg-gray-100 text-gray-800'
          "
          class="px-2 py-1 text-xs font-bold rounded"
        >
          {{ latest.gerak ? "ADA ORANG" : "KOSONG" }}
        </span>
      </div>
    </div>

    <!-- Control Section -->
    <div class="bg-white p-6 rounded-lg shadow mb-6">
      <h2 class="text-xl font-bold text-gray-800 mb-4">
        Remote Control Actuator
      </h2>
      <div class="flex gap-4">
        <button
          @click="toggleRelay('ac')"
          class="px-4 py-2 bg-blue-600 text-white font-semibold rounded shadow hover:bg-blue-700"
        >
          Toggle AC Status
        </button>
        <button
          @click="toggleRelay('lamp')"
          class="px-4 py-2 bg-yellow-500 text-white font-semibold rounded shadow hover:bg-yellow-600"
        >
          Toggle Lampu Status
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  setup() {
    const latest = ref({});
    const acStatus = ref(false);
    const lampStatus = ref(false);

    const fetchReadings = async () => {
      try {
        const res = await fetch("http://localhost:5000/api/readings");
        const data = await res.json();
        if (data.length > 0) {
          latest.value = data[0];
        }
      } catch (err) {
        console.error("Failed to fetch API:", err);
      }
    };

    const toggleRelay = async (type) => {
      if (type === "ac") acStatus.value = !acStatus.value;
      if (type === "lamp") lampStatus.value = !lampStatus.value;

      await fetch("http://localhost:5000/api/control", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          relay_ac: acStatus.value ? "ON" : "OFF",
          relay_lamp: lampStatus.value ? "ON" : "OFF",
        }),
      });
    };

    onMounted(() => {
      fetchReadings();
      setInterval(fetchReadings, 3000); // Polling interval
    });

    return { latest, toggleRelay };
  },
};
</script>
