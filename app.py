import streamlit as st
import random

st.set_page_config(page_title="Sistem Antrean KRL Transit", page_icon="🚆")

st.title("🚆 Sistem Antrean KRL Transit Stasiun")
st.markdown("Aplikasi pintar untuk mengecek antrean, estimasi kedatangan, dan posisi real-time KRL.")

# Data tujuan lengkap dengan posisi kereta terkini
data_tujuan = {
    "Manggarai": {
        "pintu": "Pintu A - Zona Peron 1 & 2",
        "deskripsi": "Arah Bogor / Jakarta Kota",
        "antrean_dasar": 45,
        "waktu_krl": 13,
        "posisi_kereta": "Sedang melintas di petak jalur Cikini – Manggarai"
    },
    "Tanah Abang": {
        "pintu": "Pintu B - Zona Peron 3 & 4",
        "deskripsi": "Arah Duri / Angke / Cikarang",
        "antrean_dasar": 68,
        "waktu_krl": 7,
        "posisi_kereta": "Berangkat dari Stasiun Karet, menuju Tanah Abang"
    },
    "Kampung Bandan": {
        "pintu": "Pintu C - Zona Peron 5",
        "deskripsi": "Arah Loop Line Utara",
        "antrean_dasar": 32,
        "waktu_krl": 4,
        "posisi_kereta": "Segera masuk jalur transit Stasiun Kampung Bandan"
    }
}

st.subheader("Pilih Rute Perjalanan Anda")
stasiun_asal = st.selectbox("Posisi Stasiun Transit Saat Ini:", ["Jatinegara", "Manggarai", "Tanah Abang", "Kampung Bandan"])
pilihan_tujuan = st.selectbox("Pilih Stasiun Tujuan Akhir:", ["Manggarai", "Tanah Abang", "Kampung Bandan"])

if st.button("Cari Pintu & Cek Posisi KRL 🔍"):
    info = data_tujuan[pilihan_tujuan]
    jumlah_antrean = info["antrean_dasar"] + random.randint(-3, 5)
    waktu_datang = info["waktu_krl"] + random.randint(-1, 3)
    
    st.success(f"Analisis untuk tujuan **{pilihan_tujuan}** berhasil!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="📍 Rekomendasi Pintu", value=info["pintu"])
        st.write(f"ℹ️ {info['deskripsi']}")
        
    with col2:
        st.metric(label="👥 Estimasi Antrean", value=f"{jumlah_antrean} orang")
        st.metric(label="🚆 KRL Tiba Dalam", value=f"{waktu_datang} menit")
        
    # Menampilkan informasi posisi kereta secara jelas
    st.markdown("---")
    st.info(f"📍 **Posisi KRL Terkini:** {info['posisi_kereta']}")
        
    if waktu_datang <= 5:
        st.warning("⚠️ **Perhatian:** Kereta sudah dekat dengan peron, bersiaplah untuk boarding!")
    else:
        st.info("💡 **Tips:** Posisi kereta masih dalam perjalanan, silakan menunggu di area ruang tunggu.")
