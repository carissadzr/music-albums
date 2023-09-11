Carissa Aida Zahra (2206082543)
PBP D

Tautan menuju aplikasi Adaptable : https://musicalbumapp.adaptable.app

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
- 

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
- 

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

c. MVVM (Model-View-ViewModel): MVVVM umumnya diterapkan dalam pengembangan aplikasi antarmuka pengguna atau user interface (UI).
- Model = menyimpan data dan mengimplementasikan logika aplikasi
- View = menampilkan data yang berasal dari Model dan mengintegrasikannya dengan template
- ViewModel = memuat logika presentasi serta menyiapkan data yang akan ditampilkan di View

Perbedaan pokok antara ketiganya terletak pada cara setiap pola desain perangkat lunak mengatur struktur komponen dalam sebuah aplikasi dan mengelola interaksi antar komponen. Django memanfaatkan MVT untuk mencapai pemisahan logika aplikasi, MVC merupakan pola desain yang umum digunakan dalam pengembangan perangkat lunak, sedangkat MVVM digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI) yang mengandalkan banyak interaksi dari pengguna.