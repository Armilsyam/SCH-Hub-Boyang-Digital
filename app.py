import streamlit as st
import streamlit.components.v1 as components

# Mengatur konfigurasi halaman Streamlit
st.set_page_config(
    page_title="SCH-Hub | Climate Technopreneurship",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Menyimpan kode HTML ke dalam variabel string
html_content = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SCH-Hub | Climate Technopreneurship by Boyang Digital Nusantara</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        body { font-family: 'Inter', sans-serif; scroll-behavior: smooth; margin: 0; padding: 0; }
        .bg-gradient-green { background: linear-gradient(135deg, #047857 0%, #10b981 100%); }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">

    <!-- Navigation -->
    <nav class="bg-white shadow-sm fixed w-full z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16 items-center">
                <div class="flex-shrink-0 flex items-center">
                    <span class="font-bold text-2xl text-emerald-700">SCH-Hub</span>
                    <span class="ml-2 text-xs text-gray-500 hidden sm:block">by Boyang Digital</span>
                </div>
                <div class="hidden md:flex space-x-8">
                    <a href="#masalah" class="text-gray-600 hover:text-emerald-600 font-medium">Masalah</a>
                    <a href="#solusi" class="text-gray-600 hover:text-emerald-600 font-medium">Solusi</a>
                    <a href="#teknologi" class="text-gray-600 hover:text-emerald-600 font-medium">Teknologi</a>
                </div>
                <div>
                    <a href="mailto:contact@boyangdigital.my.id" class="bg-emerald-600 text-white px-5 py-2 rounded-full font-medium hover:bg-emerald-700 transition">Hubungi Kami</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="pt-32 pb-20 bg-gradient-green text-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h1 class="text-4xl md:text-6xl font-bold tracking-tight mb-6">
                Mengubah Limbah Kelapa Menjadi <br> <span class="text-emerald-200">Energi Masa Depan</span>
            </h1>
            <p class="mt-4 text-xl md:text-2xl font-light mb-10 max-w-3xl mx-auto">
                Platform optimasi logistik dan pemetaan potensi bio-energi berbasis Artificial Intelligence untuk Ekonomi Sirkular di Sulawesi Barat dan sekitarnya.
            </p>
            <div class="flex justify-center gap-4">
                <a href="#solusi" class="bg-white text-emerald-700 px-8 py-3 rounded-full font-bold text-lg hover:bg-gray-100 transition shadow-lg">Pelajari Inovasi Kami</a>
            </div>
        </div>
    </section>

    <!-- Problem Section -->
    <section id="masalah" class="py-20">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-3xl font-bold text-gray-900 mb-4">Tantangan Iklim Saat Ini</h2>
                <div class="w-24 h-1 bg-emerald-500 mx-auto rounded"></div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
                <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 text-center">
                    <div class="text-red-500 text-4xl mb-4"><i class="fas fa-smog"></i></div>
                    <h3 class="text-xl font-bold mb-3">Emisi Karbon Tinggi</h3>
                    <p class="text-gray-600">Praktik pembakaran terbuka limbah sisa panen kelapa (sabut dan batok) menghasilkan Gas Rumah Kaca yang signifikan.</p>
                </div>
                <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 text-center">
                    <div class="text-yellow-500 text-4xl mb-4"><i class="fas fa-route"></i></div>
                    <h3 class="text-xl font-bold mb-3">Logistik Tidak Efisien</h3>
                    <p class="text-gray-600">Rantai pasok terfragmentasi membuat biaya angkut biomassa dari desa ke pabrik pengolahan menjadi sangat mahal.</p>
                </div>
                <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 text-center">
                    <div class="text-blue-500 text-4xl mb-4"><i class="fas fa-hand-holding-usd"></i></div>
                    <h3 class="text-xl font-bold mb-3">Potensi Ekonomi Hilang</h3>
                    <p class="text-gray-600">Petani kehilangan peluang untuk mendapatkan nilai tambah ekonomi dari limbah yang sebenarnya bernilai tinggi.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Solution Section -->
    <section id="solusi" class="py-20 bg-gray-100">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row items-center gap-12">
                <div class="md:w-1/2">
                    <h2 class="text-3xl font-bold text-gray-900 mb-6">Solusi Kami: SCH-Hub</h2>
                    <p class="text-lg text-gray-600 mb-6">
                        Strategic Coconut Hilirization Hub bertindak sebagai jembatan digital. Kami memetakan titik limbah secara geospasial dan menghubungkan pengepul lokal langsung dengan industri bio-energi.
                    </p>
                    <ul class="space-y-4">
                        <li class="flex items-start">
                            <i class="fas fa-check-circle text-emerald-500 mt-1 mr-3 text-xl"></i>
                            <div>
                                <h4 class="font-bold text-gray-800">Menekan Biaya Transportasi</h4>
                                <p class="text-sm text-gray-600">Memanfaatkan algoritma *routing* AI untuk efisiensi logistik biomassa hingga 30%.</p>
                            </div>
                        </li>
                        <li class="flex items-start">
                            <i class="fas fa-check-circle text-emerald-500 mt-1 mr-3 text-xl"></i>
                            <div>
                                <h4 class="font-bold text-gray-800">Sistem Transaksi Terintegrasi</h4>
                                <p class="text-sm text-gray-600">Distribusi insentif langsung ke petani dan pengepul desa melalui E-Wallet/QRIS.</p>
                            </div>
                        </li>
                    </ul>
                </div>
                <div class="md:w-1/2 bg-white p-6 rounded-2xl shadow-lg border border-gray-200">
                    <div class="aspect-w-16 aspect-h-9 bg-gray-200 rounded-lg flex items-center justify-center text-gray-400 py-20">
                        <div class="text-center">
                            <i class="fas fa-chart-line text-5xl mb-3"></i>
                            <p class="font-medium">Prototipe Dashboard Streamlit</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Team/Founder Section -->
    <section class="py-20">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h2 class="text-3xl font-bold text-gray-900 mb-10">Tim Pengembang</h2>
            <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 inline-block text-left">
                <div class="flex items-center gap-6">
                    <div class="w-24 h-24 bg-emerald-100 rounded-full flex items-center justify-center text-emerald-600 text-3xl">
                        <i class="fas fa-user-tie"></i>
                    </div>
                    <div>
                        <h3 class="text-2xl font-bold text-gray-900">Muh. Armil Syam</h3>
                        <p class="text-emerald-600 font-medium mb-2">Founder & Director</p>
                        <p class="text-gray-600 text-sm">BNSP Certified Data Scientist & Web Developer.<br>Membangun inovasi dari Pandeglang hingga Sulawesi Barat.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row justify-between items-center">
            <div class="mb-6 md:mb-0 text-center md:text-left">
                <span class="font-bold text-2xl text-emerald-400">SCH-Hub</span>
                <p class="text-gray-400 text-sm mt-2">Inisiatif inovasi iklim oleh PT. Boyang Digital Nusantara</p>
            </div>
            <div class="text-gray-400 text-sm">
                &copy; 2026 PT. Boyang Digital Nusantara. All rights reserved.
            </div>
        </div>
    </footer>

</body>
</html>
"""

# Render HTML di dalam Streamlit menggunakan components.html
components.html(html_content, height=2500, scrolling=True)
