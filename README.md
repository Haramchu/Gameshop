Nama        : Clement Samuel Marly
NPM         : 2206082114
Kelas       : PBP C
Adaptable   : https://gamestock.adaptable.app/main/

[Tugas 2](#-membuat-sebuah-proyek-django-baru)
[Tugas 3](#-perbedaan-antara-form-post-dan-form-get-dalam-django)

# Membuat sebuah proyek Django baru
1. Membuat direktori baru untuk proyek Django baru.
2. Buka command prompt di direktori tersebut dan jalankan perintah `python -m venv env` untuk membuat virtual environment untuk Python. Environment akan mengisolasi package dan *dependencies* dari aplikasi sehingga tidak konflik dengan versi lain.
3. Mengaktifkan virtual environment dengan menjalankan perintah `env\Scripts\activate.bat` (windows).
4. Buat file dengn nama `requirements.txt` di direktori yang sama dan isi dengan *dependencies* berikut:
`django`
`gunicorn`
`whitenoise`
`psycopg2-binary`
`requests`
`urllib3`
5. Install *dependencies* dengan perintah `pip install -r requirements.txt` dengan virtual environment menyala.
6. Membuat proyek Django dengan nama yang diinginkan melalui perintah `django-admin startproject shopping_list .`
7. Buka file settings.py yang ada di dalam folder yang telah dibuat dan tambahkan '*' pada `ALLOWED_HOSTS` untuk mengizinkan akses dari semua *host*.
8. Buka kembali command prompt dan jalankan perintah `python manage.py runserver` (windows) dan buka http://localhost:8000 untuk melihat apakah aplikasi Django berhasil dibuat.
9. Hentikan server dengan menekan `Ctrl+C` di command prompt dan jalankan perintah `deactivate` untuk mematikan virtual environment. Push hasil perubahan ke GitHub.

# Membuat aplikasi dengan nama main pada proyek tersebut.
1. Mengaktifkan virtual environment dengan perintah `env\Scripts\activate.bat` (windows).
2. Jalankan perintah `python manage.py startapp main` untuk membuat aplikasi baru dengan nama main.
3. Buka berkas settings.py di dalam proyek Django yang dibuat dan tambahkan `'main'` di variabel `INSTALLED_APPS`. 

# Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
1. Membuat berkas dengan nama `urls.py` di dalam direktori `main` dan isi dengan kode berikut untuk mengatur rute URL:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
show_main digunakan sebagai tampilan ketika URL yang terkait diakses dan app_name sebagai nama unik pada pola URL aplikasi.
2. Buka berkas `urls.py` di direktori proyek Django dan bukan `urls.py` di direktori `main` dan tambahkan rute URL seperti berikut:
```python
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```
*Path* `main/` akan diarahkan ke rute yang didefinisikan dalam berkas `urls.py` pada aplikasi `main`.

# Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
1. Buka file `models.py` dan isi file dengan nama dan atribut yang diminta.
2. Berdasarkan ketentuan soal, file minimal harus memiliki isi sebagai berikut:
```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
```
3. Jalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk mengaplikasikan perubahan model.

# Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
1. Buka file `views.py` di dalam direktori `main`.
2. Tambahkan kode berikut ke dalam file.
```python 
from django.shortcuts import render
``` 
3. Tambahkan fungsi berikut ke dalam file.
```python
def show_main(request):
    context = {
        'name': 'nama',
        'class': 'kelas'
    }

    return render(request, "main.html", context)
```
4. Buat direktori dengan nama `templates` di dalam direktori main dan buat file dengan nama `main.html` kemudian isi dengan kode html untuk menampilkan data yang ada di file sebelumnya.
```html
<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}<p>
```

# Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
1. Membuat berkas dengan nama `urls.py` di dalam direktori `main` dan isi dengan kode berikut untuk mengatur rute URL:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```


# Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
1. Buka web Adaptable.io dan buat akun melalui akun GitHub. 
2. Setelah login, tekan tombol `New APP`dan pilih `Connect an Existing Repository`.
3. Pilih `All Repositories` untuk memberikan akses kepada semua repository di akun GitHUB.
4. Pilih repository yang berisi aplikasi yang ingin di-*deploy*.
5. Pilih `Pyhon App Template` sebagai *template deployment*.
6. Pilih `PostgreSQL` sebagai tipe basis data.
7. Sesuaikan versi Python dan masukkan perintah `python manage.py migrate && gunicorn (nama direktori utama).wsgi.` di bagian `Start Command`.
8. Tulis nama aplikasi yang diinginkan dan centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai *deployment*.

# *Request client* ke web aplikasi berbasis Django beserta responnya
![DJango Framework](https://github.com/Haramchu/Tugas-2/blob/main/PBP-Tugas%202.png)
Pertama, *user* atau *client* akan meminta akses atau *resource*. Django akan kemudian akan memproses URL dari *client* dan menyesuaikannya sesuai dengan file `urls.py` (URL Mapping).
Kedua, Django akan akan membuka file `views.py` dan meminta tampilan. 
File `models.py` kemudian menangani data yang terkait permintaan pengguna dan folder `template` akan berisi file dengan ekstension html. File yang berisi ekstension html tersebut akan berisi kode-kode html untuk mengatur tulisan, tabel, ukuran, dan lainnya. Setelah selesai diproses, tampilan akan diberikan ke *client* atau *user*.
*Source*: https://intellipaat.com/blog/tutorial/python-django-tutorial/

# Fungsi Virtual Environment
Isolasi *Dependencies*
Virtual environment memungkinkan untuk mengisolasi dependensi proyek sehingga proyek tidak akan saling mengganggu proyek lain.

Mencegah konflik
Virtual environment membantu mencegah masalah yang mungkin muncul ketika berbagi proyek dengan orang lain.

Keamanan
Virtual environment memungkinkan untuk mencoba berbagai konfigurasi dan versi python tanpa merusak instalasi Python global pada komputer kita. Virtual environment membatasi akses proyek terhadap instalasi Python global sehingga mencegah perubahan tidak terduga di berbagai proyek python.

Menyesuaikan Versi Python 
Pneggunaan virtual environment memungkinkan untuk menggunakan versi Python yang berbeda untuk berbagai proyek.

*Source*: https://csguide.cs.princeton.edu/software/virtualenv#:~:text=In%20a%20nutshell%2C%20Python%20virtual,or%20used%20by%20other%20projects.

# Apakah proyek Django tetap bisa dibuat tanpa Virtual Environment
Proyek Django masih bisa dibuat tanpa menggunakan virtual environment, namun virtual environment disarankan untuk tetap digunakan untuk mencegah berbagai konflik yang bisa terjadi tanpa adanya virtual environment.

*Source*: https://www.w3schools.com/django/django_create_virtual_environment.php#:~:text=It%20is%20suggested%20to%20have,we%20will%20call%20it%20myworld%20.

# MVC, MVT, dan MVVM
MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah tiga pola arsitektur perangkat lunak yang berbeda dalam pengembangan aplikasi web. Ketiga pola arsitektur tersebut memiliki konsep yang mirip dalam memisahkan visualisasi, pemrosesan, dan manajemen data. Ketiga pola arsitektur tersebut bertujuan untuk meningkatkan fleksibilitas, kemudahan pengujian, dan pemeliharaan aplikasi yang mudah.

### MVC (Model-View-Controller):
**Model:** komponen yang mengelola data dan logika aplikasi. Model berisi struktur data dan operasi terkait data.
**View:** komponen yang mengatur tampilan antarmuka pengguna. View mengambil data dari Model dan menampilkannya kepada pengguna.
**Controller:** komponen yang mengelola aliran kontrol dalam aplikasi. *Controller* menerima input dari pengguna, memprosesnya, dan berinteraksi dengan Model dan View sesuai dengan instruksi yang diberikan.

MVC biasanya digunakan dalam pengembangan aplikasi desktop, web, dan mobile.
Controller bertanggung jawab untuk menerima dan mengirimkan input dari pengguna, mengambil tindakan yang sesuai, dan memperbarui Model dan View sesuai kebutuhan.

### MVT (Model-View-Template):
**Model:** komponen yang mengelola data dan logika.
**View:** Tidak seperti *View* dalam MVC, *View* dalam MVT hanya bertanggung jawab untuk mengatur tampilan dan tidak memiliki logika.
**Template:** komponen yang mengatur cara data ditampilkan. Template menggabungkan data dari Model dengan tampilan.

MVT adalah varian dari MVC dan umumnya digunakan dalam kerangka kerja web yang didasarkan pada Python seperti Django.
Perbedaan utama adalah penggunaan Template, yang memisahkan tampilan dari logika sehingga memudahkan pengembangan dan pemeliharaan.

### MVVM (Model-View-ViewModel):
**Model:** komponen yang mengelola data dan logika.
**View:** komponen yang mengatur tampilan antarmuka pengguna.
**ViewModel:** komponen yang bertindak sebagai perantara antara *Model* dan *View*. *ViewModel* mengambil data dari *Model* dan mengubahnya menjadi format yang sesuai untuk ditampilkan *View*.

MVVM biasanya digunakan dalam pengembangan aplikasi berbasis data.
ViewModel memungkinkan binding dua arah antara Model dan View, yang memungkinkan perubahan data secara otomatis dalam tampilan.

*Source*: https://agus-hermanto.com/blog/detail/mvc-vs-mvp-vs-mvvm-apa-perbedaannya-mana-yang-terbaik-diantara-ketiganya-a

# Perbedaan antara form POST dan form GET dalam Django