import streamlit as st
import random

st.set_page_config(page_title="Sistem Antrean KRL Transit", page_icon="🚆")

st.title("🚆 Sistem Antrean KRL Transit Stasiun")

# Data lengkap dengan 3 tujuan
data_tujuan = {
    "Manggarai": {
        "pintu": "Pintu A - Zona Peron 1 & 2",
        "deskripsi": "Arah Bogor / Jakarta Kota",
        "antrean_dasar": 45
    },
    "Tanah Abang": {
        "pintu": "Pintu B - Zona Peron 3 & 4",
        "deskripsi": "Arah Duri / Angke / Kampung Bandan / Cikarang",
        "antrean_dasar": 68
    },
    "Kampung Bandan": {
        "pintu": "Pintu C - Zona Peron 5",
        "deskripsi": "Arah Loop Line Utara",
        "antrean_dasar": 32
    }
}

st.subheader("Pilih Rute Perjalanan Anda")
stasiun_asal = st.selectbox("Posisi Stasiun Transit Saat Ini:", ["Jatinegara", "Manggarai", "Tanah Abang", "Kampung Bandan"])
pilihan_tujuan = st.selectbox("Pilih Stasiun Tujuan Akhir:", ["Manggarai", "Tanah Abang", "Kampung Bandan"])

if st.button("Cari Pintu & Cek Antrean 🔍"):
    info = data_tujuan[pilihan_tujuan]
    jumlah = info["antrean_dasar"] + random.randint(-4, 8)
    
    st.success(f"Analisis untuk tujuan **{pilihan_tujuan}** berhasil!")
    st.write(f"📍 **Rekomendasi Pintu:** {info['pintu']}")
    st.write(f"ℹ️ **Info Jalur:** {info['deskripsi']}")
    st.metric(label="👥 Estimasi Antrean", value=f"{jumlah} orang")

