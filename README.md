**Carissa Aida Zahra (2206082543)**
**PBP D**

- Adaptable : https://musicalbumapp.adaptable.app
- Current README.md : Tugas 2 dan 3



**TUGAS INDIVIDU 2**

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
- Selain mengikuti tutorial 0 dan 1, dalam implementasi pengerjaan tugas individu 2 ini saya merujuk pada materi powerpoint yang dijelaskan di kelas dan membaca referensi dari beberapa website mengenai proses deployment dan penggunaan GitHub. Di samping itu, saya mencoba mencari referensi beberapa contoh unit testing yang sekiranya bisa saya implementasikan di project ini.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

```````
                                         http request -> urls.py
                                                    |
                                                    v
                                        melakukan forward request
                                                    |                            
                                                    v                          
      models.py --> membaca/menambahkan data --> views.py --> http response (html file)
                                                    ^
                                                    |
                                             template (html)
```````

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
- Virtual environment akan mengisolasi dependencies dan packages secara terpisah dari dari lingkungan Python global, seperti aplikasi dan project lainnya dalam sistem operasi atau komputer yang digunakan. Virtual Environment dinyalakan di antaranya untuk menghindari konflik antar proyek karena menggunakan versi paket yang berbeda, meningkatkan keamanan data proyek, dan mengelola packages yang digunakan dalam proyek.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

a. MVC (Model-View-Controller) : MVC adalah pola desain perangkat lunak yang membagi aplikasi menjadi tiga komponen utama, yaitu 
- Model = menyimpan data dan mengimplementasikan logika aplikasi
- View = menampilkan data yang berasal dari Model dan mengintegrasikannya dengan template
- Controller = mengendalikan alur aplikasi dan menghubungkan Model dan View

b. MVT (Model-View-Template) : MVT adalah suatu prinsip desain yang diterapkan dalam pengembangan web dengan tujuan memisahkan komponen-komponen kunci dari sebuah aplikasi. Prinsip ini membantu pengembang web dalam pengorganisasian dan pengelolaan kode dengan lebih terstruktur. Pola desain perangkat lunak MVT ini adalah desain yang digunakan oleh Django.
- Model = menyimpan data dan mengimplementasikan logika aplikasi
- View = menampilkan data yang berasal dari Model dan mengintegrasikannya dengan template
- Template = menyusun tampilan antarmuka pengguna dengan menentukan struktur dan tampilan elemen-elemen antarmuka

c. MVVM (Model-View-ViewModel): MVVM umumnya diterapkan dalam pengembangan aplikasi antarmuka pengguna atau user interface (UI).
- Model = menyimpan data dan mengimplementasikan logika aplikasi
- View = menampilkan data yang berasal dari Model dan mengintegrasikannya dengan template
- ViewModel = memuat logika presentasi serta menyiapkan data yang akan ditampilkan di View

Perbedaan pokok antara ketiganya terletak pada cara setiap pola desain perangkat lunak mengatur struktur komponen dalam sebuah aplikasi dan mengelola interaksi antar komponen. Django memanfaatkan MVT untuk mencapai pemisahan logika aplikasi, MVC merupakan pola desain yang umum digunakan dalam pengembangan perangkat lunak, sedangkat MVVM digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI) yang mengandalkan banyak interaksi dari pengguna.



**TUGAS INDIVIDU 3**

1. Apa perbedaan antara form POST dan form GET dalam Django?
- Form POST pada Django mengirim data melalui badan request HTTP sehingga cocok untuk mengirim data - data yang lebih sensitif dalam jumlah banyak. Hal ini bisa dilakukan sebab form POST tidak dibatasi oleh kapasitas atau panjang URL. Selain itu, data yang dikirm melalui form POST adalah tipe data yang akan diproses oleh server.
- Form GET pada Django mengirim data dalam bentuk parameter query string yang bisa terlihat dalam URL, maka dalam prosesnya lebih mudah bagi pengguna untuk membagikan data tersebut karena cukup melalui URL. Di sisi lain, dengan kemudahan membagikan data ini, tingkat keamanan data yang dikirim melalui form GET tidak lebih aman dari form POST. Form GET biasa digunakan untuk mengirim data yang akan diambil dari server, dan data yang akan dikirim lebih mudah diproses browser dan dianalisis pengguna karena data tercantum langsung pada URL.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
- XML (Extensible Markup Language) mengadopsi konsep markup tags seperti <nama_tag>nilai</nama_tag>. Ini cenderung menghasilkan file dengan ukuran yang lebih besar dan umumnya digunakan dalam konteks yang lebih formal. XML memiliki kapasitas untuk mendukung berbagai jenis tipe data. Biasanya XML digunakan dalam situasi yang memerlukan struktur data yang kompleks dan memerlukan validasi data.
- JSON (JavaScript Object Notation) menggunakan format pasangan nama-nilai seperti "nama": "nilai". JSON lebih mudah dibaca oleh manusia dan menghasilkan file dengan ukuran yang lebih kecil serta menggunakan format yang umum digunakan dalam pengembangan web dan aplikasi modern. Di sisi lain, JSON memiliki keterbatasan dalam mendukung berbagai jenis tipe data. JSON biasa digunakan untuk proses pertukaran data yang lebih ringan serta lebih mudah dibaca.
- HTML merupakan bahasa yang biasa digunakan ketika akan membuat tampilan sebuah web dan interaksi pada tampilan pengguna. HTML mengatur elemen - elemen seperti gambar, tombol, teks, dan lain - lain dengan format <tag>konten</tag> 
- Secara singkat, XML berfokus representasi struktur data, JSON berfokus pada pengiriman data antar sistem, dan HTML digunakan untuk merancang tampilan halaman web.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- JSON sering digunakan dalam pertukaran data antara aplikasi web modern sebab data yang dikirim melalui JSON menggunakan format yang sederhana sehingga lebih mudah dibaca dan ditransfer, memiliki ukuran file yang lebih ringan, serta lebih fleksibel karena dapat digunakan dengan berbagai bahasa pemrograman. 

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Pertama, saya mereview kembali apa saja yang sudah dilakukan di tutorial 2 saat lab. Mulai dari materinya, implementasi yang terjadi pada program sebelum dan sesudah dilakukan suatu perubahan, serta mencoba lebih familiar dengan penggunaan XML, JSON, dan Postman
- Selanjutnya. selain dari tutorial, dalam pengerjaan tugas 3 ini saya melakukan beberapa modifikasi dalam kode yang sudah dibuat pada repo music_albums sebelumnya. Penyesuaian ini saya lakukan agar beberapa kode yang dijelaskan pada tutorial 2 kompatibel dengan kode yang saya kerjakan di tugas 2
- Terakhir, saya menanyakan dan meminta penjelasan kepada asisten dosen ketika menemukan kendala dalam proses pengkodean atau membutuhkan penjelasan mengenai materi yang belum saya kuasai

**Berikut screenshot dari hasil akses URL pada Postman**

<img width="960" alt="image" src="https://github.com/carissadzr/music-albums/assets/124969497/8bdc1e4a-5c9e-4bad-ab15-634d50fcd96a">
![image](https://github.com/carissadzr/music-albums/assets/124969497/7a8cc898-d718-4c1e-8d23-267366c7db5a)
![image](https://github.com/carissadzr/music-albums/assets/124969497/0353d344-c7e1-4824-b252-9a30d3145c8c)
![image](https://github.com/carissadzr/music-albums/assets/124969497/0ad1a114-4973-4b79-ad26-332560ca1291)
![image](https://github.com/carissadzr/music-albums/assets/124969497/4fd8b073-96a9-4370-aeb7-6a568479ad22)

