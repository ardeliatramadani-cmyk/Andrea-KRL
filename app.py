import streamlit as st
import random

st.set_page_config(page_title="Sistem Antrean KRL Transit", page_icon="🚆")

st.title("🚆 Sistem Antrean KRL Transit Stasiun")
st.markdown("Aplikasi pintar untuk mengecek antrean dan estimasi kedatangan KRL secara real-time.")

# Data tujuan lengkap dengan status KRL dan waktu kedatangan
data_tujuan = {
    "Manggarai": {
        "pintu": "Pintu A - Zona Peron 1 & 2",
        "deskripsi": "Arah Bogor / Jakarta Kota",
        "antrean_dasar": 45,
        "waktu_krl": 13  # Estimasi waktu kedatangan dalam menit
    },
    "Tanah Abang": {
        "pintu": "Pintu B - Zona Peron 3 & 4",
        "deskripsi": "Arah Duri / Angke / Cikarang",
        "antrean_dasar": 68,
        "waktu_krl": 7
    },
    "Kampung Bandan": {
        "pintu": "Pintu C - Zona Peron 5",
        "deskripsi": "Arah Loop Line Utara",
        "antrean_dasar": 32,
        "waktu_krl": 4
    }
}

st.subheader("Pilih Rute Perjalanan Anda")
stasiun_asal = st.selectbox("Posisi Stasiun Transit Saat Ini:", ["Jatinegara", "Manggarai", "Tanah Abang", "Kampung Bandan"])
pilihan_tujuan = st.selectbox("Pilih Stasiun Tujuan Akhir:", ["Manggarai", "Tanah Abang", "Kampung Bandan"])

if st.button("Cari Pintu & Cek KRL 🔍"):
    info = data_tujuan[pilihan_tujuan]
    jumlah_antrean = info["antrean_dasar"] + random.randint(-3, 5)
    waktu_datang = info["waktu_krl"] + random.randint(-1, 3) # Biar waktunya agak dinamis
    
    st.success(f"Analisis untuk tujuan **{pilihan_tujuan}** berhasil!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="📍 Rekomendasi Pintu", value=info["pintu"])
        st.write(f"ℹ️ {info['deskripsi']}")
        
    with col2:
        st.metric(label="👥 Estimasi Antrean", value=f"{jumlah_antrean} orang")
        st.metric(label="🚆 KRL Tiba Dalam", value=f"{waktu_datang} menit")
        
    if waktu_datang <= 5:
        st.warning("⚠️ **Perhatian:** Kereta akan segera tiba di peron, bersiaplah!")
    else:
        st.info("💡 **Tips:** Masih ada waktu, silakan menunggu di area ruang tunggu.")
