import streamlit as st
import base64
from pathlib import Path

# --- Konfigürasyon ve Sayfa Ayarları ---
st.set_page_config(
    page_title="Doğukan Şark | AI & Computer Vision Engineer", 
    page_icon="🤖", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- FOTOĞRAFI BASE64'E ÇEVİRME FONKSİYONU ---
def img_to_base64(image_path):
    """Yerel görüntüyü Base64'e çevirir ve Streamlit HTML'ine gömer."""
    try:
        with open(image_path, "rb") as img_file: 
            base64_data = base64.b64encode(img_file.read()).decode()
            mime_type = "image/png" if image_path.lower().endswith(".png") else "image/jpeg"
            return f"data:{mime_type};base64,{base64_data}"
    except FileNotFoundError:
        st.error(f"Hata: '{image_path}' dosyası bulunamadı. Lütfen dosya yolunu kontrol edin.")
        return "https://via.placeholder.com/200/667eea/ffffff?text=PROFIL" 

# --- BİLGİLERİNİZ VE LİNKLERİNİZ ---
ISIM = "DOĞUKAN ŞARK"
UNVAN = "AI Engineer | Computer Vision Specialist"
PROFIL_OZETI = """ 
Kod ve kahve arasında geçen bir hayatın mimarı.
"""
EMAIL = "dogukansark44@gmail.com"
KONUM = "Türkiye"

PROFILE_PIC_PATH = "assets/foto.png"
PROFILE_PIC_URL = img_to_base64(PROFILE_PIC_PATH)
PROFILE_ALT_TEXT = "Doğukan Şark Profil Fotoğrafı"

# --- Bağlantılar Sözlüğü ---
LINK_BUTONLARI = {
    "🚀 Canlı AI Projelerim (Streamlit)": {
        "url": "https://share.streamlit.io/user/onlydogukan4",
        "logo": "https://streamlit.io/images/brand/streamlit-mark-color.png",
    },
    "💻 Tüm Kodlarım (GitHub)": {
        "url": "https://github.com/onlyDogukan4", 
        "logo": "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
    },
    "💼 LinkedIn Profilim": {
        "url": "https://www.linkedin.com/in/do%C4%9Fukan-%C5%9Fark-95658327a/",
        "logo": "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg",
    },
    "📊 Kaggle Profilim": {
        "url": "https://www.kaggle.com/work",
        "logo": "https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/189_Kaggle_logo_logos-512.png",
    },
    "📝 Teknik Blog": {
        "url": "https://medium.com/@dogukansark44",
        "logo": "https://miro.medium.com/v2/resize:fit:1128/1*s986xIGqhfsN8U--09_AdA.png",
    },
    "📩 E-posta Gönder": {
        "url": f"mailto:{EMAIL}?subject=AI Collaboration&body=Merhaba Doğukan,",
        "logo": "https://cdn4.iconfinder.com/data/icons/social-media-logos-6/512/112-gmail_email_mail-512.png",
    }
}

# --- PROFESYONEL CSS TASARIMI ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * { 
        font-family: 'Inter', sans-serif; 
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
        min-height: 100vh;
    }
    
    .main {
        background: transparent;
        padding: 2rem 1rem;
        max-width: 900px;
        margin: 0 auto;
    }
    
    /* YENİ PROFİL LAYOUTU - MODERN TASARIM */
    .profile-container {
        display: flex;
        align-items: center;
        gap: 3rem;
        background: linear-gradient(135deg, rgba(255,255,255,0.98) 0%, rgba(248,250,252,0.98) 100%);
        border-radius: 32px;
        padding: 3rem;
        margin-bottom: 2rem;
        box-shadow: 
            0 25px 50px rgba(0, 0, 0, 0.15),
            0 0 0 1px rgba(255,255,255,0.1);
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(20px);
    }
    
    .profile-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2, #667eea);
    }
    
    /* PROFİL FOTOĞRAFI STİLİ */
    .profile-image-container {
        flex-shrink: 0;
        position: relative;
    }
    
    .profile-avatar {
        width: 220px;
        height: 220px;
        border-radius: 50%;
        object-fit: cover;
        border: 6px solid #ffffff;
        box-shadow: 
            0 20px 40px rgba(0, 0, 0, 0.25),
            0 0 0 1px rgba(102, 126, 234, 0.1);
        transition: all 0.4s ease;
    }
    
    .profile-avatar:hover {
        transform: scale(1.05) rotate(2deg);
        box-shadow: 
            0 25px 50px rgba(0, 0, 0, 0.35),
            0 0 0 2px rgba(102, 126, 234, 0.3);
    }
    
    /* PROFİL BİLGİLERİ */
    .profile-info {
        flex: 1;
        text-align: left;
    }
    
    .name-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        line-height: 1.1;
        letter-spacing: -0.5px;
    }
    
    .subtitle {
        font-size: 1.3rem;
        font-weight: 600;
        color: #475569;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #475569 0%, #334155 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .location-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.7rem 1.5rem;
        border-radius: 25px;
        font-size: 0.95rem;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
        margin-bottom: 2rem;
    }
    
    .bio-text {
        font-size: 1.15rem;
        color: #374151;
        line-height: 1.6;
        font-weight: 500;
        background: rgba(248, 250, 252, 0.9);
        padding: 1.8rem;
        border-radius: 20px;
        border-left: 5px solid #667eea;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
        font-style: italic;
        text-align: center;
    }
    
    /* YETKİNLİK KARTLARI */
    .expertise-section {
        background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(248,250,252,0.95) 100%);
        border-radius: 28px;
        padding: 3rem 2.5rem;
        margin: 2.5rem 0;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.12);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .section-title {
        font-size: 2rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 2.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        position: relative;
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 60px;
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        border-radius: 2px;
    }
    
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1.5rem;
        margin-top: 2rem;
    }
    
    .skill-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        padding: 2rem;
        border-radius: 20px;
        border-left: 5px solid #667eea;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        text-align: center;
    }
    
    .skill-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.05), transparent);
        transition: left 0.6s;
    }
    
    .skill-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
    }
    
    .skill-card:hover::before {
        left: 100%;
    }
    
    .skill-card h3 {
        color: #1e293b;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
    }
    
    .skill-card p {
        color: #64748b;
        line-height: 1.6;
        font-size: 0.95rem;
        margin: 0;
    }
    
    /* BUTON STİLLERİ */
    .link-button {
        display: flex;
        align-items: center;
        width: 100%;
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        color: #1e293b;
        padding: 1.3rem 2rem;
        margin: 0.8rem 0;
        border-radius: 20px;
        text-decoration: none !important;
        font-weight: 700;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
        border: 2px solid transparent;
        position: relative;
        overflow: hidden;
    }
    
    .link-button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.1), transparent);
        transition: left 0.5s;
    }
    
    .link-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
        border-color: #667eea;
        color: #667eea;
        text-decoration: none !important;
    }
    
    .link-button:hover::before {
        left: 100%;
    }
    
    .platform-logo {
        width: 32px;
        height: 32px;
        margin-right: 15px;
        border-radius: 8px;
        object-fit: contain;
        flex-shrink: 0;
    }
    
    /* FOOTER */
    .footer {
        text-align: center;
        color: rgba(255, 255, 255, 0.7);
        margin-top: 4rem;
        padding: 2rem 1rem;
        font-size: 0.9rem;
    }
    
    .footer p {
        margin: 0.3rem 0;
    }
    
    /* RESPONSIVE TASARIM */
    @media (max-width: 768px) {
        .profile-container {
            flex-direction: column;
            text-align: center;
            gap: 2rem;
            padding: 2rem;
        }
        
        .profile-info {
            text-align: center;
        }
        
        .profile-avatar {
            width: 180px;
            height: 180px;
        }
        
        .name-title {
            font-size: 2.2rem;
        }
        
        .skills-grid {
            grid-template-columns: 1fr;
        }
        
        .bio-text {
            font-size: 1.1rem;
            padding: 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# --- ARAYÜZ OLUŞTURMA ---

with st.container():
    
    # 1. YENİ PROFİL BÖLÜMÜ - YAN YANA LAYOUT
    st.markdown('<div class="profile-container">', unsafe_allow_html=True)
    
    # Sol Taraf - Profil Fotoğrafı
    st.markdown('<div class="profile-image-container">', unsafe_allow_html=True)
    st.markdown(f'<img src="{PROFILE_PIC_URL}" alt="{PROFILE_ALT_TEXT}" class="profile-avatar">', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Sağ Taraf - Bilgiler
    st.markdown('<div class="profile-info">', unsafe_allow_html=True)
    st.markdown(f'<div class="name-title">{ISIM}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="subtitle">{UNVAN}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="location-badge">📍 {KONUM}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="bio-text">{PROFIL_OZETI}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. TEKNİK YETKİNLİKLER BÖLÜMÜ - 2x3 GRID
    st.markdown('<div class="expertise-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🚀 Technical Expertise</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="skills-grid">
        <div class="skill-card">
            <h3>🧠 Neural Networks</h3>
            <p>ANN, CNN, RNN, LSTM architectures with PyTorch & TensorFlow. Building intelligent systems from scratch.</p>
        </div>
        <div class="skill-card">
            <h3>🤖 Advanced AI Models</h3>
            <p>U-Net, ResNet-50, RAG Chatbots. State-of-the-art architectures for complex problem solving.</p>
        </div>
        <div class="skill-card">
            <h3>👁️ Computer Vision</h3>
            <p>OpenCV, Image Classification, Object Detection. Turning pixels into intelligent insights.</p>
        </div>
        <div class="skill-card">
            <h3>🚀 Live Deployment</h3>
            <p>Streamlit apps, GitHub repositories. See my code in action with real-world applications.</p>
        </div>
        <div class="skill-card">
            <h3>🔬 Research & Development</h3>
            <p>Mitacs Accelerate alumni. Industrial AI solutions with academic rigor and practical impact.</p>
        </div>
        <div class="skill-card">
            <h3>💡 End-to-End Solutions</h3>
            <p>From data to deployment. Full-stack AI development with measurable results.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 3. BAĞLANTILAR BÖLÜMÜ - TÜM LİNKLER GERİ EKLENDİ
    st.markdown('<div class="expertise-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📬 Explore My Work</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <p style="color: #64748b; font-size: 1.1rem; font-weight: 500;">
            Check out my live AI applications on Streamlit and explore the code on GitHub. 
            Every project tells a story of problem-solving and innovation.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tüm bağlantı butonları geri eklendi
    for metin, bilgi in LINK_BUTONLARI.items():
        st.markdown(
            f'''
            <a href="{bilgi['url']}" target="_blank" class="link-button">
                <img src="{bilgi['logo']}" class="platform-logo" alt="{metin} Logo">
                {metin}
            </a>
            ''',
            unsafe_allow_html=True
        )
    
    st.markdown('</div>', unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
    <p><strong>Doğukan Şark | Building Intelligent Systems</strong></p>
    <p>From code to coffee, from neural networks to real-world solutions</p>
    <p style="margin-top: 1rem; font-size: 0.8rem; opacity: 0.6;">Crafted with precision using Streamlit</p>
</div>
""", unsafe_allow_html=True)
