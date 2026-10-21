import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time

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
# 2. INJEKSI CSS KUSTOM (UNTUK UI YANG LUAR BIASA)
# ==========================================
st.markdown("""
<style>
    /* Global Font & Background */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Custom Gradient Text */
    .gradient-text {
        background: linear-gradient(135deg, #059669 0%, #10b981 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 3rem;
    }
    
    /* Card Styles */
    .glass-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        border: 1px solid rgba(16, 185, 129, 0.2);
        transition: transform 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(16, 185, 129, 0.1);
    }
    
    /* Founder Section Style */
    .founder-name {
        color: #064e3b;
        font-weight: 800;
        font-size: 2.5rem;
        margin-bottom: 0px;
    }
    .founder-title {
        color: #059669;
        font-weight: 600;
        font-size: 1.2rem;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. DATA DUMMY UNTUK DASHBOARD
# ==========================================
@st.cache_data
def load_map_data():
    # Simulasi titik persebaran limbah kelapa di Sulawesi Barat
    np.random.seed(42)
    lat = np.random.uniform(-3.5, -2.5, 100)
    lon = np.random.uniform(118.8, 119.5, 100)
    volume = np.random.randint(500, 5000, 100) # dalam kg
    return pd.DataFrame({'Latitude': lat, 'Longitude': lon, 'Volume (Kg)': volume})

@st.cache_data
def load_impact_data():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun']
    emisi = [120, 105, 90, 75, 55, 40] # Emisi menurun
    pendapatan = [15, 22, 35, 48, 65, 85] # Pendapatan petani naik (Juta Rupiah)
    return pd.DataFrame({'Bulan': months, 'Emisi Karbon (Ton)': emisi, 'Pendapatan Petani (Juta)': pendapatan})


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
        * 🌍 **Zero Waste Integration:** Mencegah pembakaran terbuka dengan mendistribusikan limbah ke industri bio-energi.
        * 🤖 **AI Logistics:** Memetakan titik kumpul secara presisi untuk menekan biaya transportasi.
        * 💰 **Circular Economy:** Memberikan insentif langsung (E-Wallet) kepada petani yang menyetorkan limbahnya.
        """)
        
    with col2:
        st.image("https://images.unsplash.com/photo-1596704017254-9b121068fb31?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="Potensi Biomassa Kelapa (Ilustrasi)", use_container_width=True)

    st.write("### 📈 Pencapaian Platform (Live Metrics)")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="Total Biomassa Terselamatkan", value="1,245 Ton", delta="↑ 12% bulan ini")
    m2.metric(label="Reduksi Jejak Karbon", value="450 Ton CO2e", delta="-5% dibanding pembakaran")
    m3.metric(label="Mitra Pengepul Desa", value="128 Titik", delta="15 Desa Terintegrasi")
    m4.metric(label="Sirkulasi Ekonomi Lokal", value="Rp 850 Juta", delta="↑ Rp 45 Juta")


def page_teknologi():
    st.markdown('<h1 class="gradient-text">Geo-AI & Optimasi Rantai Pasok</h1>', unsafe_allow_html=True)
    st.write("Memonitor dan memetakan potensi energi biomassa secara *real-time* menggunakan algoritma *routing* pintar.")
    st.write("---")
    
    df_map = load_map_data()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🗺️ Peta Potensi Biomassa (Sulawesi Barat)")
        # Plotly Mapbox
        fig = px.scatter_mapbox(df_map, lat="Latitude", lon="Longitude", size="Volume (Kg)",
                                color="Volume (Kg)", color_continuous_scale=px.colors.sequential.Greens,
                                size_max=15, zoom=7, mapbox_style="carto-positron")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.markdown("### ⚙️ Sistem Kerja SCH-Hub")
        st.markdown("""
        <div class="glass-card">
            <h4>1. Koleksi Data (IoT & Mobile)</h4>
            <p style='font-size: 14px;'>Petani memindai berat limbah via aplikasi. Data masuk ke cloud secara real-time.</p>
            <hr>
            <h4>2. Clustering AI</h4>
            <p style='font-size: 14px;'>Sistem mengelompokkan titik pengangkutan terdekat untuk memastikan truk selalu muat penuh (Efisiensi 30%).</p>
            <hr>
            <h4>3. Distribusi P2P</h4>
            <p style='font-size: 14px;'>Pabrik briket/bio-pelet langsung menerima pasokan tanpa perantara panjang.</p>
        </div>
        """, unsafe_allow_html=True)


def page_dampak():
    st.markdown('<h1 class="gradient-text">Dampak Lingkungan & Ekonomi</h1>', unsafe_allow_html=True)
    st.write("Harmonisasi antara *Profit* (Keuntungan), *People* (Masyarakat), dan *Planet* (Bumi).")
    st.write("---")
    
    df_impact = load_impact_data()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📉 Tren Penurunan Emisi Karbon")
        fig1 = px.line(df_impact, x="Bulan", y="Emisi Karbon (Ton)", markers=True, 
                       line_shape='spline', color_discrete_sequence=['#ef4444'])
        fig1.update_traces(line=dict(width=4))
        fig1.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig1, use_container_width=True)
        
    with col2:
        st.markdown("### 📈 Tren Peningkatan Ekonomi Petani")
        fig2 = px.bar(df_impact, x="Bulan", y="Pendapatan Petani (Juta)", text_auto=True,
                      color="Pendapatan Petani (Juta)", color_continuous_scale="Greens")
        fig2.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig2, use_container_width=True)


def page_founder():
    st.markdown('<h1 class="gradient-text">Visioner di Balik Inovasi</h1>', unsafe_allow_html=True)
    st.write("Membangun masa depan digital yang berkelanjutan dari Sulawesi Barat untuk Nusantara.")
    st.write("---")
    
    col_img, col_text = st.columns([1, 2.5])
    
    with col_img:
        # Placeholder untuk foto (Bisa diganti dengan URL foto asli Pak Armil jika ada)
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
        <br>
        """, unsafe_allow_html=True)
        
        st.write("""
        Sebagai seorang *Data Scientist* dan teknolog yang tersertifikasi BNSP, **Muh. Armil Syam, S.T.** melihat ketimpangan besar antara inovasi teknologi di kota besar dan pemanfaatan sumber daya di daerah.
        
        Melalui **PT. Boyang Digital Nusantara**, beliau memelopori pendekatan *Climate Technopreneurship*. Beliau percaya bahwa menyelesaikan masalah lingkungan lokal—seperti pembakaran limbah kelapa di Sulawesi Barat—membutuhkan lebih dari sekadar sosialisasi; membutuhkan intervensi sistemik berbasis **Data, Kecerdasan Buatan (AI), dan Bisnis Sirkular**.
        """)
        
        st.markdown("""
        <div class="glass-card" style="margin-top: 20px; border-left: 5px solid #059669;">
            <i>"Teknologi tidak berguna jika hanya menjadi pajangan akademis. Teknologi harus turun ke desa, menyentuh tangan petani, menaikkan taraf hidup mereka, sekaligus menyembuhkan bumi yang kita tinggali."</i> 
            <br><br><b>— Muh. Armil Syam, S.T.</b>
        </div>
        """, unsafe_allow_html=True)
        
    st.write("---")
    st.markdown("### Tentang PT. Boyang Digital Nusantara")
    st.write("""
    Berpusat di Sulawesi Barat, perusahaan ini berfokus pada pengembangan *software*, analitik data, dan integrasi *Internet of Things (IoT)* untuk memecahkan masalah industri riil. **SCH-Hub** adalah salah satu portofolio unggulan yang menyatukan misi pelestarian lingkungan dengan pertumbuhan ekonomi mikro.
    """)


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
    
    # Menu Navigasi
    menu = st.sidebar.radio(
        "Navigasi Platform",
        ["🏠 Beranda & Visi Utama", "⚙️ Teknologi Geo-AI", "📊 Dampak Ekonomi & Karbon", "👨‍💼 Profil Founder & Tim"]
    )
    
    st.sidebar.write("---")
    st.sidebar.info("💡 **Aplikasi Interaktif:** Coba arahkan kursor pada peta atau grafik untuk melihat detail data.")
    st.sidebar.write("© 2026 PT. Boyang Digital Nusantara")
    
    # Routing Halaman
    if menu == "🏠 Beranda & Visi Utama":
        page_beranda()
    elif menu == "⚙️ Teknologi Geo-AI":
        page_teknologi()
    elif menu == "📊 Dampak Ekonomi & Karbon":
        page_dampak()
    elif menu == "👨‍💼 Profil Founder & Tim":
        page_founder()

# ==========================================
# 6. EKSEKUSI UTAMA
# ==========================================
if __name__ == "__main__":
    main()
