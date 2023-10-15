### Carissa Aida Zahra (2206082543) - PBP D

- Link : https://carissa-aida-tugas.pbp.ui.ac.id
- Current README.md : Tugas 2, 3, 4, 5, 6

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
- **ID Selector (#id):** Memilih elemen berdasarkan ID unik, memungkinkan pemberian gaya khusus pada elemen tertentu dalam dokumen
- **Universal Selector (*):** Memilih semua elemen di dokumen untuk memberikan gaya secara global dan berdampak pada seluruh elemen
- **Type Selector (element):** Mengidentifikasi dan memilih semua elemen dari jenis tertentu, seperti paragraf (p), untuk menerapkan gaya yang seragam pada elemen-elemen sejenis
- **Class Selector (.class):** Menentukan dan memilih semua elemen yang memiliki kelas tertentu, memungkinkan penerapan gaya yang konsisten pada beberapa elemen tanpa memperhatikan jenis elemen
- **Descendant Selector (ancestor descendant):** Memilih semua elemen yang merupakan turunan dari elemen tertentu, seperti anak atau cucu, berguna untuk membatasi pemilihan pada elemen yang berada dalam hierarki tertentu
- **Child Selector (parent > child):** Memilih elemen anak langsung dari elemen induk tertentu, membatasi pemilihan hanya pada elemen anak yang langsung berada di bawah elemen induk
- **Adjacent Sibling Selector (prev + next):** Memilih elemen sejajar yang berada setelah elemen tertentu, memungkinkan pemberian gaya pada elemen yang berdekatan secara langsung

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

### Menambahkan Bootstrap ke Aplikasi

Pertama, buka proyek Django, dalam hal ini saya menggunakan `music_albums`, akses file `base.html` yang sudah ada di dalam folder "templates" di direktori proyek utama. Pada file `templates/base.html`, tambahkan elemen tag `<meta name="viewport">` untuk memastikan halaman web dapat menyesuaikan ukuran dan responsif terhadap perangkat mobile jika belum dilakukan sebelumnya.

```
<head>
    {% block meta %}
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
    {% endblock meta %}
</head>
```

Lalu, tambahkan Bootstrap CSS dan JS sebagai berikut :

**CSS**
```
<head>
    {% block meta %}
        ...
    {% endblock meta %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
```

**JS**
```
<head>
    ...
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
</head>
```

Karena saya berniat menggunakan dropdowns, popover, atau tooltips dari framework Bootstrap, maka saya menambahkan dua baris skrip JavaScript di bawah skrip JavaScript sebagai berikut.

```
<head>
    ...
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
</head>
```

### Tutorial: Menambahkan navbar pada Aplikasi

Untuk menambahkan navbar pada aplikasi web, saya meambahkan navigation bar (Bootstrap) pada halaman `main.html` dengan bentuk berikut.

```
<nav class="navbar" style="background-color: #78C1F3; color: #4ea1d3; text-align: center;">
    <div class="container-fluid">
        <div class="user-info">
            <a class="navbar-brand" style="color: #Ffffff; font-size: 42px;">Music Albums</a>
            <p>{{name}} - {{class}}</p>
        </div>

        <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit" style="border-color: #edf5e1; color: #ffffff;">Search</button>
        </form>

        <style>
            button.btn-outline-success:hover {
                background-color: #a7afe9;
                color: #6474e5;
            }
        </style>

        <ul class="navbar-nav ml-auto">
            <li class="nav-item">
                <a class="btn btn-outline-light" href="{% url 'main:logout' %}">Logout</a>
            </li>
        </ul>
    </div>
</nav>
```

### Tutorial: Menambahkan Fitur Edit pada Aplikasi

Untuk menambahkan fitur ini, buka berkas `views.py` yang terletak dalam subdirektori `main` dan membuat sebuah fungsi baru yang dinamai `edit_product` yang menerima parameter request dan id. Lalu, tambahkan bagian kode berikut ke dalam fungsi edit_product.

```
def edit_product(request, id):
    # Get product berdasarkan ID
    product = Product.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
```

Kemudian, buat berkas HTML baru dengan nama `edit_product.html` pada subdirektori `main/templates` lalu mengisi berkas tersebut dengan potongan kode berikut

```
{% extends 'base.html' %}

{% load static %}

{% block content %}

<h1>Edit Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Edit Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

Buka urls.py yang berada pada direktori `main` dan import fungsi `edit_product` yang sudah dibuat.

```
from main.views import edit_product

```

Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.

```
...
path('edit-product/<int:id>', edit_product, name='edit_product'),
...

```

Buka main.html yang berada pada subdirektori main/templates. Tambahkan potongan kode berikut sejajar dengan elemen `<td>` terakhir agar terlihat tombol edit pada setiap baris tabel.

```
...
<tr>
    ...
    <td>
        <a href="{% url 'main:edit_product' product.pk %}">
            <button>
                Edit
            </button>
        </a>
    </td>
</tr>
...

```

Kemudian jalankan proyek Django dengan perintah `python manage.py runserver`` dan bukalah http://localhost:8000 di browser untuk melihat hasilnya.

### Membuat Fungsi untuk Menghapus Data Produk

Untuk menambahkan fitur ini, buat fungsi baru dengan nama `delete_product` yang menerima parameter request dan id pada `views.py` di folder `main` 

```
def delete_product(request, id):
    # Get data berdasarkan ID
    product = Product.objects.get(pk = id)
    # Hapus data
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))
```

Kemudian, buka `urls.py` yang ada pada folder `main` dan impor fungsi `delete_product`

```
from main.views import delete_product
```


Lalu saya akan menambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimport

```
...
path('delete/<int:id>', delete_product, name='delete_product'), # sesuaikan dengan nama fungsi yang dibuat
...

```

Buka file `main.html` yang terdapat di direktori  `main/templates` dan modifikasi kode yang sudah ada agar setiap produk memiliki tombol delete

```
...
<tr>
    ...
    <td>
        <a href="{% url 'main:edit_product' product.pk %}">
            <button>
                Edit
            </button>
        </a>
        <a href="{% url 'main:delete_product' product.pk %}">
              <button>
                  Delete
              </button>
          </a>
    </td>
</tr>
...
```

Kemudian jalankan kembali proyek Django dengan perintah `python manage.py runserver`` dan bukalah http://localhost:8000 di browser untuk melihat hasilnya.


###
## TUGAS INDIVIDU 6

### 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

**Asynchronous**

- Komunikasi terjadi secara tertunda tanpa ketergantungan pada waktu.
- Contoh media: e-mail, forum, membaca/menulis dokumen online.
- Tidak terikat pada kecepatan waktu tetap; fleksibilitas dalam transformasi data.
- Menggunakan metode serial, satu karakter/bit dikirim pada satu waktu.
- Start bit dan stop bit untuk menyinkronkan perangkat pengirim dan penerima.
- Variabilitas interval waktu memberikan fleksibilitas dalam kecepatan transmisi data.

**Synchronous**

- Komunikasi langsung, contohnya video call dan chatting.
- Terjadi secara waktu nyata dengan keselarasan dan prediktabilitas.
- Mengutamakan kecepatan tinggi dalam pengiriman data.
- Data dikirim dalam blok, diperiksa ulang dengan Block Check Character (BCC).

### 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

**Paradigma Event-Driven Programming:**

Paradigma event-driven programming adalah suatu paradigma pemrograman di mana alur eksekusi program ditentukan oleh terjadinya kejadian atau peristiwa tertentu. Pada dasarnya, program ini berinteraksi dengan peristiwa (events) yang terjadi, dan tugas-tugas atau fungsi-fungsi tertentu dijalankan sebagai respons terhadap peristiwa tersebut. Konsep ini sangat relevan dalam pengembangan antarmuka pengguna (UI) pada aplikasi web atau desktop.

**Contoh Penerapan pada JavaScript dan AJAX:**

Misalkan kita memiliki tombol di halaman web kita, dan kita ingin sesuatu terjadi ketika tombol tersebut diklik. Dalam paradigma event-driven, kita akan menetapkan suatu fungsi atau aksi untuk dijalankan ketika event "click" pada tombol itu terjadi.

Contoh kode menggunakan JavaScript dan AJAX:

```
html
<!DOCTYPE html>
<html>
<head>
  <title>Contoh Event-Driven Programming dengan JavaScript dan AJAX</title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script>
    $(document).ready(function(){
      // Menetapkan fungsi yang akan dijalankan ketika tombol di klik
      $("#myButton").click(function(){
        // Melakukan AJAX request ketika tombol diklik
        $.ajax({
          url: "example.php", // Contoh URL untuk AJAX request
          success: function(result){
            // Menangani hasil dari AJAX request
            $("#output").html(result); // Menampilkan hasil di elemen dengan ID "output"
          }
        });
      });
    });
  </script>
</head>
<body>

<button id="myButton">Klik Saya</button>
<div id="output">Hasil AJAX akan muncul di sini.</div>

</body>
</html>
```

Pada contoh ini, fungsi yang ditetapkan akan dijalankan ketika tombol dengan ID "myButton" diklik. Fungsi tersebut melakukan AJAX request ke server (contoh URL "example.php") dan menanggapi hasilnya dengan memperbarui elemen dengan ID "output". Ini adalah contoh konkret dari paradigma event-driven programming di dalam konteks JavaScript dan AJAX.

### 3. Jelaskan penerapan asynchronous programming pada AJAX.
Asynchronous programming pada AJAX memungkinkan pengguna untuk berinteraksi dengan halaman web secara dinamis tanpa perlu memuat ulang seluruh halaman. Ini berarti bahwa kode JavaScript dapat mengirim permintaan ke server dan menerima respons tanpa mengganggu pengalaman pengguna.

Berikut adalah cara kerja AJAX secara asynchronous:

1. **Membuat objek XMLHttpRequest**: Objek ini digunakan untuk berkomunikasi dengan server.

2. **Mengirim permintaan ke server**: Dengan menggunakan metode `open()` dan `send()` dari objek XMLHttpRequest, kita dapat mengirim permintaan ke server. Metode `open()` digunakan untuk menentukan jenis permintaan (GET, POST, dll.), URL tujuan, dan apakah permintaan harus asynchronous atau tidak. Metode `send()` digunakan untuk mengirim permintaan.

3. **Menangani respons dari server**: Kita dapat menentukan fungsi callback yang akan dipanggil ketika respons diterima dari server. Fungsi ini akan dipanggil setiap kali properti `readyState` dari objek XMLHttpRequest berubah. Ketika `readyState` bernilai 4, itu berarti respons telah diterima dan siap untuk diproses.

4. **Memproses respons**: Setelah respons diterima, kita dapat memproses data yang dikembalikan oleh server dan memperbarui halaman web sesuai kebutuhan.

Berikut adalah contoh kode AJAX asynchronous:

```
javascript
var xhr = new XMLHttpRequest();
xhr.open("GET", "https://api.example.com/data", true);
xhr.onreadystatechange = function () {
  if (xhr.readyState == 4 && xhr.status == 200)
    console.log(JSON.parse(xhr.responseText));
}
xhr.send();
```

Dalam contoh ini, kita membuat permintaan GET ke "https://api.example.com/data" secara asynchronous. Ketika respons diterima (yaitu, `readyState` adalah 4 dan `status` adalah 200), kita mencetak respons ke konsol. Dengan pendekatan ini, kita dapat membuat aplikasi web yang responsif dan cepat, karena kita tidak perlu menunggu server merespons sebelum kita dapat melanjutkan dengan tugas lain.

### 4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan

Fetch API dan jQuery AJAX adalah dua teknologi yang digunakan untuk membuat permintaan HTTP asynchronous dalam pengembangan web. 

**Fetch API** adalah teknologi modern yang dibangun ke dalam JavaScript ES6 dan merupakan bagian dari spesifikasi browser web standar.
- (+) FMenggunakan Promises yang membuat penanganan respons asynchronous lebih mudah dan lebih intuitif.
- (+) Memberikan kontrol lebih besar atas permintaan HTTP, seperti mendukung operasi baca/tulis pada objek Request dan Response.
- (+) Mendukung service workers, yang penting untuk fitur offline dan push notifications.
- (-) Fetch API belum didukung oleh semua browser (meskipun sudah didukung oleh sebagian besar browser modern).
- (-)  Fetch API tidak secara otomatis mengirim atau menerima cookies, harus diatur secara manual.

**jQuery** AJAX adalah bagian dari library jQuery yang telah ada sejak lama dan telah terbukti stabil dan dapat diandalkan.
- (+) jQuery AJAX memiliki dukungan browser yang luas, termasuk browser lama.
- (+) jQuery AJAX secara otomatis mengirim dan menerima cookies.
- (+) Jika Anda sudah menggunakan jQuery di situs Anda, menggunakan jQuery AJAX tidak memerlukan dependensi tambahan.
- (-) jQuery AJAX didasarkan pada callback, yang bisa menjadi rumit untuk dikelola jika Anda memiliki banyak operasi asynchronous.
- (-) Jika Anda tidak menggunakan fitur lain dari jQuery, memuat seluruh library hanya untuk AJAX bisa menjadi pemborosan.

Untuk mengembangkan aplikasi modern dengan banyak fitur asynchronous dan/atau offline, Fetch API mungkin pilihan yang lebih baik. Namun, jika pada situs yang perlu mendukung berbagai macam browser (termasuk browser lama) atau jika Anda sudah menggunakan jQuery, maka jQuery AJAX mungkin pilihan yang lebih baik.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Membuat Fungsi untuk Mengembalikan Data JSON

Pertama, saya membuat fungsi `get_product_json` yang menerima parameter `request` pada `views.py`

```
def get_product_json(request):
    product_item = Product.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))
```

### Membuat Fungsi untuk Menambahkan Produk dengan AJAX

Pada berkas `views.py` tambahkan import `from django.views.decorators.csrf import csrf_exempt`. Lalu buatlah fungsi baru pada dengan nama `add_product_ajax` yang menerima parameter `request`. Jangan lupa tambahkan dekorator `@csrf_exempt` di atas fungsi tersebut

```
...
@csrf_exempt
def add_product_ajax(request):
if request.method == 'POST':
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    user = request.user

    new_product = Product(name=name, price=price, description=description, user=user)
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

return HttpResponseNotFound()

```

### Menambahkan Routing Untuk Fungsi get_product_json dan add_product_ajax

Pada berkas `urls.py` pada folder `main`, impor fungsi `get_product_json` serta `add_product_ajax`. Lalu tambahkan kode berikut.

```
...
path('get-product/', get_product_json, name='get_product_json'),
path('create-product-ajax/', add_product_ajax, name='add_product_ajax')
```

### Menampilkan Data Product dengan Fetch() API
Pertama, bukalah main.html pada main/templates dan hapus bagian kode table yang sudah ada. Tambahkan kode berikut sebagai struktur table (jika menggunakan table)

```
<table id="product_table"></table>
```

Selanjutnya, buat block `<Script>` di bagian bawah berkas dan buat fungsi baru pada block `<Script>` tersebut dengan nama `getProducts()`.

```
<script>
    async function getProducts() {
        return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
    }
</script>
```

Buat fungsi baru pada block `<Script>` dengan nama refreshProducts() yang digunakan untuk me-refresh data produk secara asynchronous.

```
<script>
    ...
    async function refreshProducts() {
        document.getElementById("product_table").innerHTML = ""
        const products = await getProducts()
        let htmlString = `<tr>
            <th>Name</th>
            <th>Price</th>
            <th>Description</th>
            <th>Date Added</th>
        </tr>`
        products.forEach((item) => {
            htmlString += `\n<tr>
            <td>${item.fields.name}</td>
            <td>${item.fields.price}</td>
            <td>${item.fields.description}</td>
            <td>${item.fields.date_added}</td>
        </tr>` 
        })
        
        document.getElementById("product_table").innerHTML = htmlString
    }

    refreshProducts()
</script>
```

### Membuat Modal Sebagai Form untuk Menambahkan Produk

Untuk melakukan stel ini, tambahkan kode berikut untuk mengimplementasikan modal (Bootstrap) pada aplikasi dan tambahkan `button` untuk menampilkan modal

```
...
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form id="form" onsubmit="return false;">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="name" class="col-form-label">Name:</label>
                        <input type="text" class="form-control" id="name" name="name"></input>
                    </div>
                    <div class="mb-3">
                        <label for="price" class="col-form-label">Price:</label>
                        <input type="number" class="form-control" id="price" name="price"></input>
                    </div>
                    <div class="mb-3">
                        <label for="description" class="col-form-label">Description:</label>
                        <textarea class="form-control" id="description" name="description"></textarea>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
            </div>
        </div>
    </div>
</div>
...

<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Product by AJAX</button>

```

### Menambahkan Data Product dengan AJAX

Buat fungsi baru pada block `<Script>` dengan nama `addProduct()` lalu isi dengan kode berikut

```
<script>
    ...
    function addProduct() {
        fetch("{% url 'main:add_product_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshProducts)

        document.getElementById("form").reset()
        return false
    }
</script>
```

Tambahkan fungsi `onclick` pada button `"Add Product"` pada modal untuk menjalankan fungsi `addProduct()` 

```
<script>
...
document.getElementById("button_add").onclick = addProduct
</script>
```

Terakhir, coba jalankan dengan mengakses http://localhost:8000/ untuk melihat perubahan dengan menggunakan AJAX