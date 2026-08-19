import streamlit as st
import random

st.set_page_config(page_title="Sistem Antrean KRL Transit", page_icon="🚆", layout="centered")

st.title("🚆 Sistem Antrean KRL Transit Stasiun")
st.markdown("Aplikasi pintar untuk mengarahkan penumpang ke pintu peron transit yang tepat sesuai tujuan akhir.")
st.markdown("---")

data_tujuan = {
    "Manggarai": {
        "pintu": "Pintu A - Zona Peron 1 & 2",
        "deskripsi": "Arah Bogor / Jakarta Kota (Jalur Utama Sentral)",
        "antrean_dasar": 45,
        "status_krl": "Menuju Stasiun (Estimasi tiba dalam 3 menit)"
    },
    "Tanah Abang": {
        "pintu": "Pintu B - Zona Peron 3 & 4",
        "deskripsi": "Arah Duri / Angke / Kampung Bandan / Cikarang",
        "antrean_dasar": 68,
        "status_krl": "Segera Berangkat dari Stasiun Sebelumnya (Estimasi tiba dalam 5 menit)"
    },
    "Kampung Bandan": {
        "pintu": "Pintu C - Zona Peron 5",
        "deskripsi": "Arah Loop Line Utara",
        "antrean_dasar": 32,
        "status_krl": "Sedang Proses Transit di Peron (Estimasi berangkat 2 menit lagi)"
    }
}

with st.form("form_transit"):
    st.subheader("Pilih Rute Perjalanan Anda")
    stasiun_asal = st.selectbox(
        "Posisi Stasiun Transit Anda Saat Ini:",
        ["Stasiun Jatinegara", "Stasiun Manggarai", "Stasiun Duri", "Stasiun Kampung Bandan"]
    )
    
    pilihan_tujuan = st.selectbox(
        "Pilih Stasiun Tujuan Akhir:",
        ["Manggarai", "Tanah Abang", "Kampung Bandan"]
    )
    
    tombol_cek = st.form_submit_button("Cari Pintu & Cek Antrean 🔍")

if tombol_cek:
    info = data_tujuan[pilihan_tujuan]
    jumlah_antrean = info["antrean_dasar"] + random.randint(-4, 8)
    
    st.success(f"Rute berhasil dianalisis untuk tujuan **{pilihan_tujuan}**!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="📍 Rekomendasi Pintu Peron", value=info["pintu"])
        st.caption(info["deskripsi"])
        
    with col2:
        st.metric(label="👥 Jumlah Antrean di Pintu", value=f"{jumlah_antrean} orang")
        if jumlah_antrean > 60:
            st.error("Status: Padat (Disarankan menunggu di ruang tunggu)")
        elif jumlah_antrean > 40:
            st.warning("Status: Cukup Ramai")
        else:
            st.info("Status: Lancar / Lengang")

    st.markdown("---")
    st.markdown("### 🔔 Notifikasi Keberadaan KRL")
    st.warning(f"**Info Real-Time:** {info['status_krl']}")
    st.info("💡 **Tips:** Mohon berdiri di belakang garis aman peron dan dahulukan penumpang yang turun dari kereta.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Sistem Informasi KRL Transit Pintar © 2026</p>", unsafe_allow_html=True)
