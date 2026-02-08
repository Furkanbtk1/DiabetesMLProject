# Diabetes & Obesity Risk Prediction Project 🩺

Bu proje, bireylerin fiziksel özelliklerine ve günlük yaşam alışkanlıklarına dayanarak obezite seviyelerini ve dolaylı sağlık risklerini (diyabet risk faktörleri gibi) tahmin etmek amacıyla geliştirilmiştir.

## 🚀 Proje Hakkında
Makine öğrenmesi odaklı bu çalışma, veri setindeki 17 farklı parametreyi (yaş, boy, kilo, beslenme alışkanlıkları, fiziksel aktivite vb.) analiz ederek kullanıcıyı uygun bir sağlık kategorisine yerleştirir. Model, modern bir web arayüzü ile entegre edilerek son kullanıcıya sunulmuştur.

## 📊 Model Performansı
Projede **Random Forest Classifier** kullanılmış olup, yapılan testler sonucunda aşağıdaki başarı metrikleri elde edilmiştir:
- **Doğruluk (Accuracy):** %96
- **Model:** Rastgele Orman (Random Forest)
- **Veri Seti:** 2111 kayıt ve 17 öznitelik.

## 🛠️ Kullanılan Teknolojiler
- **Python** (Veri işleme ve Model eğitimi)
- **Pandas & NumPy** (Veri manipülasyonu)
- **Matplotlib & Seaborn** (Veri görselleştirme)
- **Scikit-learn** (Makine öğrenmesi algoritmaları)
- **Web Framework:** [Buraya kullandığın aracı yaz: Flask / Streamlit]

## 📋 Veri Seti Parametreleri
Tahmin yapılırken kullanılan bazı temel özellikler:
- **FAVC:** Sık yüksek kalorili yiyecek tüketimi.
- **FCVC:** Sebze tüketme sıklığı.
- **NCP:** Ana öğün sayısı.
- **CAEC:** Öğünler arasında yemek yeme.
- **CH2O:** Günlük su tüketimi.
- **FAF:** Fiziksel aktivite sıklığı.
