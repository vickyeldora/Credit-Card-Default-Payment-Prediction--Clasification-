import eda, predict
import streamlit as st

navigation = st.sidebar.selectbox('Navigation',['EDA','Predict Default'])

st.sidebar.markdown('# About')
st.sidebar.write("Kartu kredit memberikan kenyamanan dan fleksibilitas dalam bertransaksi, memungkinkan Anda untuk membeli barang dan layanan dengan mudah tanpa harus membawa uang tunai.Namun, penting untuk diingat bahwa menggunakan kartu kredit juga membawa tanggung jawab. Melakukan pembayaran tepat waktu adalah kunci untuk memanfaatkan kartu kredit dengan bijaksana dan menghindari beban finansial yang tidak perlu.Default payment atau keterlambatan pembayaran dapat mengakibatkan denda dan bunga yang tinggi, serta berdampak negatif pada skor kredit Anda. Oleh karena itu, disiplin dalam membayar tagihan kartu kredit sesuai dengan jadwal yang ditetapkan sangatlah penting.Dengan membayar tagihan tepat waktu, Anda dapat membangun reputasi keuangan yang baik, meningkatkan skor kredit Anda, dan memperoleh manfaat tambahan seperti penawaran kartu kredit dengan suku bunga yang lebih rendah dan limit yang lebih tinggi.Jadi, selalu prioritaskan untuk melakukan pembayaran tepat waktu agar Anda dapat menikmati manfaat kartu kredit secara maksimal tanpa khawatir terjebak dalam utang yang tidak terkendali.")

if navigation == 'EDA':
    eda.run()
else:
    predict.run()

#