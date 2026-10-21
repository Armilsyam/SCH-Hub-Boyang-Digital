import streamlit as st
import pandas as pd
import numpy as np

# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="SCH-Hub | PT Boyang Digital Nusantara",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. INJEKSI CSS KUSTOM (UNTUK UI)
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .gradient-text {
        background: linear-gradient(135deg, #059669 0%, #10b981 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 3rem;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        border: 1px solid rgba(16, 185, 129, 0.2);
    }
    .founder-name { color: #064e3b; font-weight: 800; font-size: 2.5rem; margin-bottom: 0px; }
    .founder-title { color: #059669; font-weight: 600; font-size: 1.2rem; text-transform: uppercase; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. DATA DUMMY UNTUK DASHBOARD
# ==========================================
@st.cache_data
def load_map_data():
    # Streamlit map membutuhkan kolom bernama 'lat' dan 'lon'
    np.random.seed(42)
    lat = np.random.uniform(-3.5, -2.5, 100)
    lon = np.random.uniform(118.8, 119.5, 100)
    return pd.DataFrame({'lat': lat, 'lon': lon})

@st.cache_data
def load_impact_data():
    # Menggunakan index untuk sumbu X pada chart bawaan Streamlit
    data = {
        'Emisi Karbon (Ton)': [120, 105, 90, 75, 55, 40],
        'Pendapatan Petani (Juta)': [15, 22, 35, 48, 65, 85]
    }
    return pd.DataFrame(data, index=['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'])

# ==========================================
# 4. FUNGSI HALAMAN (PAGES)
# ==========================================

def page_beranda():
    st.markdown('<h1 class="gradient-text">Strategic Coconut Hilirization Hub (SCH-Hub)</h1>', unsafe_allow_html=True)
    st.markdown("### Ekosistem Climate Technopreneurship oleh **PT. Boyang Digital Nusantara**")
    st.write("---")
    
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("""
        ### Mengubah Ancaman Ekologi Menjadi Nilai Ekonomi
        Sulawesi Barat memiliki potensi perkebunan kelapa yang masif. Namun, sisa panen seperti sabut dan batok kelapa seringkali hanya dibakar, menghasilkan emisi **Gas Rumah Kaca (GRK)** yang tinggi.
        
        **SCH-Hub hadir sebagai jembatan digital:**
        * 🌍 **Zero Waste Integration:** Mencegah pembakaran terbuka.
        * 🤖 **AI Logistics:** Memetakan titik kumpul secara presisi.
        * 💰 **Circular Economy:** Memberikan insentif langsung (E-Wallet).
        """)
    with col2:
        st.image("https://images.unsplash.com/photo-1596704017254-9b121068fb31?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)

    st.write("### 📈 Pencapaian Platform (Live Metrics)")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Biomassa", "1,245 Ton", "↑ 12%")
    m2.metric("Reduksi Jejak Karbon", "450 Ton CO2e", "-5%")
    m3.metric("Mitra Pengepul Desa", "128 Titik", "15 Desa")
    m4.metric("Sirkulasi Ekonomi Lokal", "Rp 850 Juta", "↑ Rp 45 Jt")

def page_teknologi():
    st.markdown('<h1 class="gradient-text">Geo-AI & Optimasi Rantai Pasok</h1>', unsafe_allow_html=True)
    st.write("Memonitor potensi energi biomassa menggunakan algoritma *routing* pintar.")
    st.write("---")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### 🗺️ Peta Potensi Biomassa (Sulawesi Barat)")
        # Menggunakan peta bawaan Streamlit (Tidak butuh Plotly)
        st.map(load_map_data(), zoom=6, use_container_width=True)
        
    with col2:
        st.markdown("### ⚙️ Sistem Kerja SCH-Hub")
        st.markdown("""
        <div class="glass-card">
            <h4>1. Koleksi Data (IoT & Mobile)</h4>
            <p>Petani memindai berat limbah via aplikasi. Data masuk ke cloud secara real-time.</p>
            <hr>
            <h4>2. Clustering AI</h4>
            <p>Sistem mengelompokkan titik pengangkutan terdekat (Efisiensi 30%).</p>
            <hr>
            <h4>3. Distribusi P2P</h4>
            <p>Pabrik langsung menerima pasokan tanpa perantara panjang.</p>
        </div>
        """, unsafe_allow_html=True)

def page_dampak():
    st.markdown('<h1 class="gradient-text">Dampak Lingkungan & Ekonomi</h1>', unsafe_allow_html=True)
    st.write("Harmonisasi antara *Profit*, *People*, dan *Planet*.")
    st.write("---")
    
    df_impact = load_impact_data()
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📉 Tren Penurunan Emisi Karbon")
        # Menggunakan line chart bawaan Streamlit
        st.line_chart(df_impact['Emisi Karbon (Ton)'])
        
    with col2:
        st.markdown("### 📈 Tren Peningkatan Ekonomi Petani")
        # Menggunakan bar chart bawaan Streamlit
        st.bar_chart(df_impact['Pendapatan Petani (Juta)'])

def page_founder():
    st.markdown('<h1 class="gradient-text">Visioner di Balik Inovasi</h1>', unsafe_allow_html=True)
    st.write("Membangun masa depan digital yang berkelanjutan dari Sulawesi Barat untuk Nusantara.")
    st.write("---")
    
    col_img, col_text = st.columns([1, 2.5])
    with col_img:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #059669 0%, #10b981 100%); padding: 5px; border-radius: 20px;">
            <img src="https://ui-avatars.com/api/?name=Armil+Syam&background=ffffff&color=059669&size=512" 
                 style="width: 100%; border-radius: 15px; border: 4px solid white;">
        </div>
        """, unsafe_allow_html=True)
        
    with col_text:
        st.markdown("""
        <h2 class="founder-name">MUH. ARMIL SYAM, S.T.</h2>
        <p class="founder-title">Founder & CEO — PT. Boyang Digital Nusantara</p>
        """, unsafe_allow_html=True)
        
        st.write("""
        Sebagai seorang *Data Scientist* dan teknolog yang tersertifikasi BNSP, **Muh. Armil Syam, S.T.** memelopori pendekatan *Climate Technopreneurship*. Beliau percaya bahwa menyelesaikan masalah lingkungan lokal membutuhkan intervensi sistemik berbasis **Data, Kecerdasan Buatan (AI), dan Bisnis Sirkular**.
        """)
        
        st.markdown("""
        <div class="glass-card" style="margin-top: 20px; border-left: 5px solid #059669;">
            <i>"Teknologi harus turun ke desa, menyentuh tangan petani, menaikkan taraf hidup mereka, sekaligus menyembuhkan bumi yang kita tinggali."</i> 
            <br><br><b>— Muh. Armil Syam, S.T.</b>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 5. STRUKTUR NAVIGASI SIDEBAR
# ==========================================
def main():
    st.sidebar.markdown("""
        <div style="text-align: center; margin-bottom: 30px;">
            <h1 style="color: #059669; font-weight: 800; font-size: 2rem; margin-bottom: 0;">SCH-Hub</h1>
            <p style="color: #6b7280; font-size: 0.8rem;">by PT. Boyang Digital Nusantara</p>
        </div>
    """, unsafe_allow_html=True)
    
    menu = st.sidebar.radio(
        "Navigasi Platform",
        ["🏠 Beranda & Visi Utama", "⚙️ Teknologi Geo-AI", "📊 Dampak Ekonomi & Karbon", "👨‍💼 Profil Founder & Tim"]
    )
    
    if menu == "🏠 Beranda & Visi Utama":
        page_beranda()
    elif menu == "⚙️ Teknologi Geo-AI":
        page_teknologi()
    elif menu == "📊 Dampak Ekonomi & Karbon":
        page_dampak()
    elif menu == "👨‍💼 Profil Founder & Tim":
        page_founder()

if __name__ == "__main__":
    main()
