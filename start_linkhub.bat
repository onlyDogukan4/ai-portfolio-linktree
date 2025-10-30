@echo off
:: Bu script, Streamlit Link Hub uygulamasını başlatır.

:: 1. Uygulamanın bulunduğu klasöre geçiş yap
cd personal_website_linkhub

:: 2. Streamlit'i Python modülü olarak çalıştırmayı dene
echo Streamlit uygulamasi baslatiliyor...

:: Python -m ile çalıştırmak, streamlit komutu PATH'te olmasa bile çalışmasını sağlar.
python -m streamlit run app_linkhub.py

:: Hata durumunda bilgilendirme
if %errorlevel% neq 0 (
    echo.
    echo HATA: Uygulama baslatilamadi.
    echo Lutfen 'pip install streamlit' komutunun calistigindan emin olun.
    echo Terminal penceresi otomatik kapanmayacaktir.
    pause
)