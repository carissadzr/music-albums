### Carissa Aida Zahra (2206082543) - PBP D

- Adaptable : https://musicalbumapp.adaptable.app
- Current README.md : Tugas 2, 3, dan 4 

### 
## TUGAS INDIVIDU 2

1. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)**
- Selain mengikuti tutorial 0 dan 1, dalam implementasi pengerjaan tugas individu 2 ini saya merujuk pada materi powerpoint yang dijelaskan di kelas dan membaca referensi dari beberapa website mengenai proses deployment dan penggunaan GitHub. Di samping itu, saya mencoba mencari referensi beberapa contoh unit testing yang sekiranya bisa saya implementasikan di project ini.

2. **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**

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

3. **Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
- Virtual environment akan mengisolasi dependencies dan packages secara terpisah dari dari lingkungan Python global, seperti aplikasi dan project lainnya dalam sistem operasi atau komputer yang digunakan. Virtual Environment dinyalakan di antaranya untuk menghindari konflik antar proyek karena menggunakan versi paket yang berbeda, meningkatkan keamanan data proyek, dan mengelola packages yang digunakan dalam proyek.

4. **Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.**

**a. MVC (Model-View-Controller)** : MVC adalah pola desain perangkat lunak yang membagi aplikasi menjadi tiga komponen utama, yaitu 
- Model = menyimpan data dan mengimplementasikan logika aplikasi
- View = menampilkan data yang berasal dari Model dan mengintegrasikannya dengan template
- Controller = mengendalikan alur aplikasi dan menghubungkan Model dan View

**b. MVT (Model-View-Template)** : MVT adalah suatu prinsip desain yang diterapkan dalam pengembangan web dengan tujuan memisahkan komponen-komponen kunci dari sebuah aplikasi. Prinsip ini membantu pengembang web dalam pengorganisasian dan pengelolaan kode dengan lebih terstruktur. Pola desain perangkat lunak MVT ini adalah desain yang digunakan oleh Django.
- Model = menyimpan data dan mengimplementasikan logika aplikasi
- View = menampilkan data yang berasal dari Model dan mengintegrasikannya dengan template
- Template = menyusun tampilan antarmuka pengguna dengan menentukan struktur dan tampilan elemen-elemen antarmuka

**c. MVVM (Model-View-ViewModel)** : MVVM umumnya diterapkan dalam pengembangan aplikasi antarmuka pengguna atau user interface (UI).
- Model = menyimpan data dan mengimplementasikan logika aplikasi
- View = menampilkan data yang berasal dari Model dan mengintegrasikannya dengan template
- ViewModel = memuat logika presentasi serta menyiapkan data yang akan ditampilkan di View

Perbedaan pokok antara ketiganya terletak pada cara setiap pola desain perangkat lunak mengatur struktur komponen dalam sebuah aplikasi dan mengelola interaksi antar komponen. Django memanfaatkan MVT untuk mencapai pemisahan logika aplikasi, MVC merupakan pola desain yang umum digunakan dalam pengembangan perangkat lunak, sedangkat MVVM digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI) yang mengandalkan banyak interaksi dari pengguna.


###
## TUGAS INDIVIDU 3

**1. Apa perbedaan antara form POST dan form GET dalam Django?**
- Form POST pada Django mengirim data melalui badan request HTTP sehingga cocok untuk mengirim data - data yang lebih sensitif dalam jumlah banyak. Hal ini bisa dilakukan sebab form POST tidak dibatasi oleh kapasitas atau panjang URL. Selain itu, data yang dikirm melalui form POST adalah tipe data yang akan diproses oleh server.
- Form GET pada Django mengirim data dalam bentuk parameter query string yang bisa terlihat dalam URL, maka dalam prosesnya lebih mudah bagi pengguna untuk membagikan data tersebut karena cukup melalui URL. Di sisi lain, dengan kemudahan membagikan data ini, tingkat keamanan data yang dikirim melalui form GET tidak lebih aman dari form POST. Form GET biasa digunakan untuk mengirim data yang akan diambil dari server, dan data yang akan dikirim lebih mudah diproses browser dan dianalisis pengguna karena data tercantum langsung pada URL.

**2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?**

**- XML (Extensible Markup Language)** mengadopsi konsep markup tags seperti <nama_tag>nilai</nama_tag>. Ini cenderung menghasilkan file dengan ukuran yang lebih besar dan umumnya digunakan dalam konteks yang lebih formal. XML memiliki kapasitas untuk mendukung berbagai jenis tipe data. Biasanya XML digunakan dalam situasi yang memerlukan struktur data yang kompleks dan memerlukan validasi data.

**- JSON (JavaScript Object Notation)** menggunakan format pasangan nama-nilai seperti "nama": "nilai". JSON lebih mudah dibaca oleh manusia dan menghasilkan file dengan ukuran yang lebih kecil serta menggunakan format yang umum digunakan dalam pengembangan web dan aplikasi modern. Di sisi lain, JSON memiliki keterbatasan dalam mendukung berbagai jenis tipe data. JSON biasa digunakan untuk proses pertukaran data yang lebih ringan serta lebih mudah dibaca.
- HTML merupakan bahasa yang biasa digunakan ketika akan membuat tampilan sebuah web dan interaksi pada tampilan pengguna. HTML mengatur elemen - elemen seperti gambar, tombol, teks, dan lain - lain dengan format <tag>konten</tag> 
- Secara singkat, XML berfokus representasi struktur data, JSON berfokus pada pengiriman data antar sistem, dan HTML digunakan untuk merancang tampilan halaman web.

**3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?**
- JSON sering digunakan dalam pertukaran data antara aplikasi web modern sebab data yang dikirim melalui JSON menggunakan format yang sederhana sehingga lebih mudah dibaca dan ditransfer, memiliki ukuran file yang lebih ringan, serta lebih fleksibel karena dapat digunakan dengan berbagai bahasa pemrograman. 

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
- Pertama, saya mereview kembali apa saja yang sudah dilakukan di tutorial 2 saat lab. Mulai dari materinya, implementasi yang terjadi pada program sebelum dan sesudah dilakukan suatu perubahan, serta mencoba lebih familiar dengan penggunaan XML, JSON, dan Postman
- Selanjutnya. selain dari tutorial, dalam pengerjaan tugas 3 ini saya melakukan beberapa modifikasi dalam kode yang sudah dibuat pada repo music-albums sebelumnya. Penyesuaian ini saya lakukan agar beberapa kode yang dijelaskan pada tutorial 2 kompatibel dengan kode yang sudah saya kerjakan di tugas 2
- Terakhir, saya menanyakan dan meminta penjelasan kepada asisten dosen ketika menemukan kendala dalam proses pengkodean atau membutuhkan penjelasan mengenai materi yang belum saya kuasai

**Berikut screenshot dari hasil akses URL pada Postman**

![image](https://github.com/carissadzr/music-albums/assets/124969497/b9d6f392-ec73-4489-8f04-52d38e58b193)
![image](https://github.com/carissadzr/music-albums/assets/124969497/7a8cc898-d718-4c1e-8d23-267366c7db5a)
![image](https://github.com/carissadzr/music-albums/assets/124969497/0353d344-c7e1-4824-b252-9a30d3145c8c)
![image](https://github.com/carissadzr/music-albums/assets/124969497/0ad1a114-4973-4b79-ad26-332560ca1291)
![image](https://github.com/carissadzr/music-albums/assets/124969497/4fd8b073-96a9-4370-aeb7-6a568479ad22)


###
## TUGAS INDIVIDU 4

 **1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?**
 - UserCreationForm dalam Django adalah sebuah formulir bawaan dalam kerangka kerja Django yang digunakan untuk membuat formulir pendaftaran pengguna dan merupakan bagian dari sistem otentikasi Django dan menyediakan cara mudah untuk membuat formulir pendaftaran yang mencakup bidang seperti nama pengguna, kata sandi, dan konfirmasi kata sandi
 - Keuntungan : menyediakan validasi bawaan untuk memastikan bahwa kata sandi yang dimasukkan oleh pengguna sesuai dan memungkinkan integrasi yang mudah dengan model pengguna Django
 - Kelemahan : sangat mendasar dan memerlukan penyesuaian tambahan jika ingin menambahkan fungsionalitas dan fitur tambahan

 **2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?**
 - Autentikasi adalah proses verifikasi identitas pengguna yang mengakses project Django, misalnya dari aspek username dan password ketika melakukan login akun
 - Otorisasi adalah penentuan hak akses pengguna yang telah melalui proses autentikasi atau yang biasa diatur dalam "access permissions" dengan tujuan untuk mengendalikan akses pengguna ke tindakan atau data tertentu dalam aplikasi
 - Kedua proses ini penting untuk memastikan bahwa pengguna yang mengakses aplikasi merupakan pihak yang berwenang dan keamanan berbagai data dalam aplikasi tetap terjaga

 **3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?**
 - Dalam lingkup aplikasi web, cookies merujuk pada berkas kecil yang disimpan di pihak user, umumnya di dalam peramban (browser), dan digunakan sebagai wadah penyimpanan informasi sesi pengguna atau data lain yang relevan. Django memanfaatkan cookies untuk mengelola data sesi pengguna, di antaraanya penyimpanan ID sesi, token otentikasi, atau preferensi user. Tujuannya adalah untuk melacak pengguna yang telah diotentikasi dan mempertahankan keadaan sesi ketika permintaan HTTP dilakukan

 **4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**
 - Beberapa manfaat cookies dalam pengembangan web meliputi personalisasi preferensi pengguna, pengelolaan keadaan status pengguna (state management), otentikasi akses pengguna, dan mengumpulkan data seperti aktivitas pengguna
 - Terdapat tantangan terkait penggunaan cookies meliputi masalah privasi, keamanan, serta beberapa batasan. Penggunaan cookies dapat menimbulkan masalah privasi dan keamanan jika tidak dikelola dengan baik (melacak aktivitas pengguna, mengambil data pribadi) serta memiliki keterbatasan dalam hal ukuran penyimpanan dan waktu kadaluwarsa
 - Untuk mengelola risiko potensial terkait privasi dan keamanan, praktik terbaik melibatkan penggunaan protokol HTTPS dan memberikan opsi kepada pengguna untuk mengontrol cookies yang mereka terima, seperti melalui pengaturan privasi di browser pengguna

 **5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
 
 Pertama, sebelum membuat perubahan dari tugas sebelumnya kita menjalankan virtual environment terlebih dahulu

 ``````
 env\Scripts\activate.bat
 ``````

### Membuat Method dan Form Register

Selanjutnya di file `views.py` kita akan menambahkan beberapa import berikut untuk membuat UserCreationForm,

```
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
```

Kita akan membuat method `register` untuk menghasilkan form bagi pengguna yang akan membuat akun baru.

```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

Untuk membuat tampilan registrasi akun baru, kita akan membuat berkas HTML baru bernama `register.html` yang meng-_extend_ berkas `base.html` pada folder `main/templates` dengan isi berkas sebagai berikut

```
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

Untuk mengimplementasikan tampilan dan method register yang sudah kita buat, kita akan melakukan import path fungsinya ke berkas `urls.py`

```
from main.views import register 

...
path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
...
```

### Membuat Method Login

Pada step ini, kita akan membuat form login untuk kepentingan autentikasi akun. Pertama kita akan mengimport dan membuat fungsi `login_user` pada file `views.py` yang berada pada subdirektori `main`.

```
from django.contrib.auth import authenticate, login

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

Untuk membuat tampilan pengisian data registrasi akun baru, kita akan membuat berkas HTML baru bernama `login.html` yang meng-_extend_ berkas `base.html` pada folder `main/templates` dengan isi berkas sebagai berikut

```
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```

Lalu, kita akan kembali menambahkan method dan pathnya ke dalam `urls.py` pada subdirektori `main`.

```
from main.views import login_user 

...
path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
...
```

### Membuat Method dan Tombol Logout

Pada step ini kita akan membuat mekanisme _logout_ dan menambahkan tombolnya pada halaman utama. Pertama kita akan mengimport dan membuat fungsi `logout_user` pada file `views.py` yang berada pada subdirektori `main`.

```
from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    return redirect('main:login')
```

Selanjutnya, pada file `main.html` kita akan menambahkan potongan kode ini untuk memunculkan tombol logout

```
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
```

Untuk mengimplementasikan tampilan dan method logout yang sudah kita buat, kita akan melakukan import path fungsinya ke berkas `urls.py`

```
from main.views import logout_user

...
path('logout/', logout_user, name='logout'),
...
```

### Restriksi Akses Halaman Utama

Step ini dilakukan agar pengguna perlu melakukan proses login dan autentikasi untuk mengakses halaman web. Pertama, kita harus menambahkan import `login_required` pada file `views.py`.

```
from django.contrib.auth.decorators import login_required
```

Lalu menambahkan potongan kode berikut sebelum method `show_main` agar halaman web terestriksi.

```
...
@login_required(login_url='/login')
def show_main(request):
...
```

Setelah tahap ini dilakukan, coba jalankan web menggunakan perintah `python manage.py runserver` dan buka http://localhost:8000/ untuk memunculkan halaman login yang sudah dibuat.

### Menggunakan Data dari _Cookies_

Sebelum memulai, pastikan bahwa tidak ada akun yang sedang login selama proses ini berjalan. Buka kembali `views.py` dan tambahkan tiga _import_ berikut.

```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

Pada method `login_user` sebelumnya, kita akan menambahkan method cookie untuk melihat aktivitas login terbaru pengguna. Hal ini bisa dilakukan dengan **mengganti** kode pada blok `if user is not None` menjadi kode berikut.

```
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```

Lalu, pada method `show_main` tambahkan kode `last_login` berikut ke dalam variabel `context` untuk menambahkan informasi aktivitas login terakhir di halaman utama web.

```
context = {
    'name': 'Pak Bepe',
    'class': 'PBP A',
    'products': products,
    'last_login': request.COOKIES['last_login'],
}
```

Kemudian, ubah potongan kode pada method `logout_user` seperti kode berikut untuk menghapus _cookie_ `last_login`` saat pengguna melakukan logout.

```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

Buka kembali file `main.html` dan tambahkan potongan kode berikut di antara tabel dan tombol logout untuk menampilkan data last login.

```
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```

Setelah menyelesaikan step ini, coba lakukan _refresh_ halaman login atau jalankan projek Django untuk melihat informasi `last_login` akun pada halaman utama. Sebelum melanjutkan ke tutorial berikutnya, diharapkan untuk *membuat minimal satu akun lain baru* pada halaman web.

### Menghubungkan Model `Product` dengan `User`
Terakhir, kita akan menghubungkan setiap objek Product yang akan dibuat dengan pengguna yang membuatnya. Untuk melakukan tahap ini, pastikan bahwa step - step sebelumnya dilakukan secara terurut.

Mulai dengan membuka `models.py` lalu impor model dengan menambahkan potongan kode berikut. Fungsinya untuk memastikan bahwa sebuah produk pasti terasosiasikan dengan seorang user.

```
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```

Selanjutnya, buka file `views.py` dan ubah potongan kode pada method `create_product`. Bagian ini dilakukan untuk memungkinkan kit amelakukan modifikasi terhadap objek yang sudah dibuat sebelum disimpan ke database.

```
def create_product(request):
 form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
 ...
```

Kemudian, ubah method `show_main` menjadi kode berikut agar web yang kita buat akan menampilkan objek Product yang terasosiasikan dengan pengguna yang sedang login dan menampilkan username pengguna yang login pada halaman utama.

```
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
    ......
```

Setelah semua langkah dilakukan, simpan perubahan dan lakukan migrasi model dengan perintah `python manage.py makemigrations`. 

Pada langkah ini akan muncul error saat melakukan migrasi, kita akan memilih opsi `1` sebanyak dua kali (satu untuk menetapkan default value untuk field user pada semua row yang telah dibuat pada basis data dan satu lagi untuk menetapkan user dengan ID 1 untuk model yang sudah dibuat sebelumnya). 

Jalankan `python manage.py migrate` untuk mengaplikasikan migrasi yang dilakukan pada poin sebelumnya lalu jalankan project Django dengan membuka link http://localhost:8000/  di browser atau menjalankan perintah `python manage.py runserver`. Hasil akhir yang benar akan membuat produk yang tadi telah dibuat dengan akun sebelumnya tidak akan ditampilkan di halaman pengguna akun yang baru saja dibuat.

###
## TUGAS INDIVIDU 5

### 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
**- ID Selector (#id):** Memilih elemen berdasarkan ID unik, memungkinkan pemberian gaya khusus pada elemen tertentu dalam dokumen
**- Universal Selector (*):** Memilih semua elemen di dokumen untuk memberikan gaya secara global dan berdampak pada seluruh elemen
**- Type Selector (element):** Mengidentifikasi dan memilih semua elemen dari jenis tertentu, seperti paragraf (p), untuk menerapkan gaya yang seragam pada elemen-elemen sejenis
**- Class Selector (.class):** Menentukan dan memilih semua elemen yang memiliki kelas tertentu, memungkinkan penerapan gaya yang konsisten pada beberapa elemen tanpa memperhatikan jenis elemen
**- Descendant Selector (ancestor descendant):** Memilih semua elemen yang merupakan turunan dari elemen tertentu, seperti anak atau cucu, berguna untuk membatasi pemilihan pada elemen yang berada dalam hierarki tertentu
**- Child Selector (parent > child):** Memilih elemen anak langsung dari elemen induk tertentu, membatasi pemilihan hanya pada elemen anak yang langsung berada di bawah elemen induk
**- Adjacent Sibling Selector (prev + next):** Memilih elemen sejajar yang berada setelah elemen tertentu, memungkinkan pemberian gaya pada elemen yang berdekatan secara langsung

### 2. Jelaskan HTML5 Tag yang kamu ketahui
- article : Memberikan penanda untuk konten yang berdiri sendiri sebagai artikel independen.
- section : Digunakan untuk mengumpulkan bersama konten yang terkait dalam suatu topik tertentu, membantu dalam mengorganisir halaman.
- nav : Menandakan area navigasi, seperti menu, mempermudah pengguna untuk berpindah antarhalaman atau bagian dalam situs.
- header dan footer: Memberi penanda pada bagian atas (header) dan bawah (footer) dari halaman atau bagian, memberikan struktur yang jelas pada dokumen.
- aside : Digunakan untuk konten yang terkait dengan konten di sekitarnya, seperti sidebar, menambahkan informasi tambahan atau terkait.
- figure dan figcaption: Diterapkan untuk menyertakan gambar dan keterangan gambar, membantu menyajikan informasi visual dengan lebih kontekstual.
- main : Menandai konten utama dalam sebuah dokumen, memberikan fokus pada isi utama halaman.
- mark : Digunakan untuk menyoroti atau menandai teks tertentu, menonjolkan bagian teks yang memiliki arti atau penting dalam konteks dokumen.

### 3. Jelaskan perbedaan antara margin dan padding
**Margin:**
- menciptakan ruang kosong di luar elemen.
- mengatur jarak antara elemen.
- tidak memiliki warna atau background.
- dapat memiliki nilai negatif -> elemen akan tumpang tindih dengan elemen lain

**Padding:**
- menciptakan ruang kosong di dalam elemen.
- mengatur jarak antara konten dan tepi dalam elemen.
- dapat memiliki warna atau background.
- tidak dapat memiliki nilai negatif.

### 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
**Tailwind CSS:**
1. Menyajikan kelas utilitas yang mencakup berbagai properti CSS, memberikan fleksibilitas maksimal bagi pengembang untuk menyesuaikan desain secara detail.
2. Memungkinkan pengembang membuat desain yang lebih kustom dan sesuai dengan kebutuhan proyek tanpa terbatas oleh komponen siap pakai.
3.  Menawarkan tingkat fleksibilitas tinggi dalam mengontrol gaya elemen sesuai preferensi pengembang.
4. Tailwind CSS memiliki file CSS yang lebih ringan dibandingkan dengan Bootstrap, hanya memuat kelas-kelas utilitas yang digunakan.
5. Tailwind CSS mengonstruksi antarmuka dengan menggabungkan kelas-kelas utilitas yang telah ditetapkan sebelumnya.

**Kapan Menggunakan Tailwind**
1. Saat ingin mencapai fleksibilitas maksimal dalam desain dan mengendalikan setiap detail secara spesifik.
2. Jika proyek membutuhkan desain yang sangat spesifik yang sulit dicapai dengan menggunakan komponen siap pakai.

**Bootstrap:**
1. Menyediakan rangkaian komponen UI yang telah dipersiapkan, memudahkan pembangunan cepat tanpa perlu merancang elemen dari awal.
2. Menyuguhkan struktur terstruktur dan konsisten, menjadikan desain antar proyek memiliki gaya yang seragam.
3. Meminimalkan kebutuhan penulisan CSS khusus karena komponen sudah memiliki gaya yang telah ditentukan.
4. Bootstrap memiliki file CSS yang lebih besar dibandingkan dengan Tailwind CSS karena mencakup banyak komponen yang sudah ditetapkan.
5. Untuk pemula, Bootstrap menawarkan pembelajaran yang lebih cepat karena dapat memulai dengan menggunakan komponen yang sudah ditetapkan.

**Kapan Menggunakan Bootstrap**
1. Saat memerlukan pengembangan yang cepat dengan komponen yang siap pakai.
2. Jika konsistensi antar proyek menjadi prioritas untuk mempertahankan tampilan yang serupa.
3. Jika tujuannya adalah meminimalkan penulisan CSS khusus dengan mengandalkan desain yang sudah ada.


### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).