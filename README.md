Nama        : Clement Samuel Marly

NPM         : 2206082114

Kelas       : PBP C

[Tugas 2](#tugas-2)

[Tugas 3](#tugas-3)

[Tugas 4](#tugas-4)

[Tugas 5](#tugas-5)

[Tugas 6](#tugas-6)

# Tugas 2
## Membuat sebuah proyek Django baru
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

## Membuat aplikasi dengan nama main pada proyek tersebut.
1. Mengaktifkan virtual environment dengan perintah `env\Scripts\activate.bat` (windows).
2. Jalankan perintah `python manage.py startapp main` untuk membuat aplikasi baru dengan nama main.
3. Buka berkas settings.py di dalam proyek Django yang dibuat dan tambahkan `'main'` di variabel `INSTALLED_APPS`. 

## Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
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

## Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
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

## Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
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

## Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
1. Membuat berkas dengan nama `urls.py` di dalam direktori `main` dan isi dengan kode berikut untuk mengatur rute URL:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```


## Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
1. Buka web Adaptable.io dan buat akun melalui akun GitHub. 
2. Setelah login, tekan tombol `New APP`dan pilih `Connect an Existing Repository`.
3. Pilih `All Repositories` untuk memberikan akses kepada semua repository di akun GitHUB.
4. Pilih repository yang berisi aplikasi yang ingin di-*deploy*.
5. Pilih `Pyhon App Template` sebagai *template deployment*.
6. Pilih `PostgreSQL` sebagai tipe basis data.
7. Sesuaikan versi Python dan masukkan perintah `python manage.py migrate && gunicorn (nama direktori utama).wsgi.` di bagian `Start Command`.
8. Tulis nama aplikasi yang diinginkan dan centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai *deployment*.

## *Request client* ke web aplikasi berbasis Django beserta responnya
![DJango Framework](https://github.com/Haramchu/Tugas-2/blob/main/Image/PBP-Tugas%202.png)
Pertama, *user* atau *client* akan meminta akses atau *resource*. Django akan kemudian akan memproses URL dari *client* dan menyesuaikannya sesuai dengan file `urls.py` (URL Mapping).
Kedua, Django akan akan membuka file `views.py` dan meminta tampilan. 
File `models.py` kemudian menangani data yang terkait permintaan pengguna dan folder `template` akan berisi file dengan ekstension html. File yang berisi ekstension html tersebut akan berisi kode-kode html untuk mengatur tulisan, tabel, ukuran, dan lainnya. Setelah selesai diproses, tampilan akan diberikan ke *client* atau *user*.
*Source*: https://intellipaat.com/blog/tutorial/python-django-tutorial/

## Fungsi Virtual Environment
Isolasi *Dependencies*
Virtual environment memungkinkan untuk mengisolasi dependensi proyek sehingga proyek tidak akan saling mengganggu proyek lain.

Mencegah konflik
Virtual environment membantu mencegah masalah yang mungkin muncul ketika berbagi proyek dengan orang lain.

Keamanan
Virtual environment memungkinkan untuk mencoba berbagai konfigurasi dan versi python tanpa merusak instalasi Python global pada komputer kita. Virtual environment membatasi akses proyek terhadap instalasi Python global sehingga mencegah perubahan tidak terduga di berbagai proyek python.

Menyesuaikan Versi Python 
Pneggunaan virtual environment memungkinkan untuk menggunakan versi Python yang berbeda untuk berbagai proyek.

*Source*: https://csguide.cs.princeton.edu/software/virtualenv#:~:text=In%20a%20nutshell%2C%20Python%20virtual,or%20used%20by%20other%20projects.

## Apakah proyek Django tetap bisa dibuat tanpa Virtual Environment
Proyek Django masih bisa dibuat tanpa menggunakan virtual environment, namun virtual environment disarankan untuk tetap digunakan untuk mencegah berbagai konflik yang bisa terjadi tanpa adanya virtual environment.

*Source*: https://www.w3schools.com/django/django_create_virtual_environment.php#:~:text=It%20is%20suggested%20to%20have,we%20will%20call%20it%20myworld%20.

## MVC, MVT, dan MVVM
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

# Tugas 3
## Perbedaan antara form POST dan form GET dalam Django
1. **POST** 
- Digunakan untuk mengirim data sensitif
- Lebih aman
- Nilai variabel tidak terlihat dalam URL
- Dapat mengirim data dalam berbagai format

2. **GET** 
- Digunakan untuk mengirim data - data yang kurang penting
- Kurang aman
- Nilai variabel terlihat dalam URL
- Hanya dapat mengirim data dalam format teks dengan *encoding* ASCII dengan batas maksimum 2047 karakter
- Dapat di-*cache* oleh browser
- Mengarah ke permintaan yang tidak mengubah data di server.

*Source*: https://makinrajin.com/blog/perbedaan-post-dan-get/

## Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data

# XML (EXtensible Markup Language)
Menggambarkan data dalam struktur *tree* dengan *namespace* untuk kategori data yeng berbeda.
Hanya dapat diurai (*parsed*) menggunakan pengurai XML
Mendukung semua tipe data JSON, Boolean, tanggal, gambar, dan *namespace*.

# JSON (JavaScript Object Notation)
Struktur data seperti pasangan *key-value* dan lebih mudah diurai dengan fungsi JavaScript standar.
Mendukung pengiriman data berupa angka, objek, string, array Boolean.

# HTML (Hypertext Markup Language)
Biasanya digunakan untuk mengatur halaman dan struktur halaman web, dan bukan pengiriman data

*Source*: https://aws.amazon.com/id/compare/the-difference-between-json-xml/

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern
- JSON adalah format pertukaran data yang dapat dibaca baik oleh manusia maupun mesin.  
- JSON bersifat independen dari setiap bahasa pemrograman dan merupakan turunan dari *Object* JavaScript. Hal tersebut membuat JSON banyak digunakan baik di aplikasi web maupun *mobile*.
- *Syntax* yang digunakan JSON lebih mudah untuk ditulis serta dibaca. 
- JSON didesain menyediakan format yang sederhana serta ringkas dan data pada JSON disimpan dalam bentuk *key* dan *value*.
- JSON dapat diurai menggunakan fungsi JavaScript standar yang lebih mudah diakses. Perbedaan *syntax* dan ukuran *file* JSON juga membuat penguraian (*parsing*) JSON lebih cepat dibandingkan XML.
- JSON memiliki ukuran file yang lebih kecil dan transmisi data yang lebih cepat.
- Penguraian JSON lebih aman dibandingkan XML. Struktur XML rentan terhadap *unauthorized modification* dan deklarasi tipe dokumen eksternal yang tidak terstruktur.

*Source*: https://aws.amazon.com/id/compare/the-difference-between-json-xml/

## Membuat input form untuk menambahkan objek model
1. Membuat berkas baru pada direktori `main` dengan nama `forms.py` sebagai struktur yang menerima data baru.
2. Isi `forms.py` dengan kode berikut:
```python
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
```
model menunjukkan model yang digunakan dalam *form* dan fields menunjukkan *field* dari model yang digunakan.
3. Buka `views.py` di folder main daan tambah import berikut:
```python
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
```
4. Tambahkan *function* baru dengan nama `create_product` dalam file `views.py` untuk menerima `request` melalui kode berikut:
```python
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
*function* tersebut akan memvalidasi isi form dan menyimpan data dari *form* tersebut.
5. *Function* `show_main` yang berada di dalam file `views.py` diubah sesuai kode berikut:
```python
def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'nama',
        'class': 'kelas PBP',
        'products': products
    }

    return render(request, "main.html", context)
```
`Product.objects.all()` akan mengambil seluruh *Object* Product yang ada pada *database*
6. Buka file `urls.py` di folder `main` dan *import* fungsi `create_product` melalui kode berikut:
```python
from main.views import show_main, create_product #tambahkan create_product
```
7. Tambahkan juga *path url* ke dalam `urlpattern` di file `urls.py` untuk mengakses *function* yang sudah dibuat dan di-*import* melalui kode berikut:
```python
urlpatterns = [
    ...
    path('create-product', create_product, name='create_product'), # tambahkan path ini
    ...
]
```
8. Buat file dengan nama `create_product.html` pada direktori `main/templates` dan isi dengan kode berikut:
```python
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
`<form method="POST">` sebagai *block* untuk *form* deengan metode POST.
`{% csrf_token %}` token yang di-*generate* secara otomatis oleh Django sebagai *security*
`{{ form.as_table }}` menampilkan *fields form* yang sudah dibuat di `forms.py`
`<input type="submit" value="Add Product"/>` membuat tombol *submit* untuk mengirimkan *request* ke *function* `create_product` di `views.py`
9. Buka `main.html` dan tambahkan tampilan data produk dalam bentuk tabel serta tombol untuk menambahkan produk baru yang akan *redirect* ke halaman *form* melalui penambahan kode berikut ke dalam bagian `{% block content %}`.
```python
...
<table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.price}}</td>
            <td>{{product.description}}</td>
            <td>{{product.date_added}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_product' %}">
    <button>
        Add New Product
    </button>
</a>

{% endblock content %}
```

## Membuat 5 fungsi views untuk melihat objek dalam format HTML, XML, JSON, XML by ID, dan JSON by ID dan membuat routing URL untuk masing-masing views tersebut
Buka file `views.py` di folder `main` dan *import* `HttpResponse` dan ` Serializer` melalui kode berikut:
```python
from django.http import HttpResponse
from django.core import serializers
```
*Import* ini akan digunakan untuk mendapatkan data objek dalam format XML dan JSON
### HTML
1. Buka `urls.py` yang ada pada folder admin (sesuai dengan nama folder yang dibuat dan bukan *root* folder) dan ubah *path* `main/` menjadi `''` pada `urlpatterns`.
```python
urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]
```
2. Sesuaikan *Function* `show_main` yang berada di dalam file `views.py` dengan kode berikut:
```python
def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'nama',
        'class': 'kelas PBP',
        'products': products
    }

    return render(request, "main.html", context)
```
`Product.objects.all()` akan mengambil seluruh *Object* Product yang ada pada *database*
3. Buka `main.html` dan tambahkan tampilan data produk dalam bentuk tabel melalui penambahan kode berikut ke dalam bagian `{% block content %}`.
```python
...
<table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.price}}</td>
            <td>{{product.description}}</td>
            <td>{{product.date_added}}</td>
        </tr>
    {% endfor %}
</table>

{% endblock content %}
```
Pengambilan data Product disesuaikan dengan format data yang ada di model.
{{product.name}} untuk pengambilan nama, {{product.price}} untuk harga, dan seterusnya.

### XML
1. Buat *function* yang menerima parameter *request* dengan nama `show_xml` dan buat variabel di dalam *function* tersebut yang menyimpan hasil *query* dari seluruh data Product. Tambahkan juga *return function* berupa `HttpResponse` yang berisi parameter data hasil *query* yang sudah diubah menjadi XML dan parameter `content_type="application/xml"`.
```python
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
3. Buka `urls.py` di dalam folder `main` dan *import* fungsi yang sudah dibuat.
```python
from main.views import show_main, create_product, show_xml #tambahkan show_xml
```
4. Tambahkan juga *path url* ke dalam `urlpattern` di file `urls.py` untuk mengakses *function* yang sudah dibuat dan di-*import* melalui kode berikut:
```python
urlpatterns = [
    ...
    path('xml/', show_xml, name='show_xml'), #tambahkan path ini
    ...
]
```

### XLM by ID
1. Buat *function* yang menerima parameter *request* dan id dengan nama `show_xml_by_id` dan buat variabel di dalam *function* tersebut yang menyimpan hasil *query* dari Product sesuai dengan id. Tambahkan juga *return function* berupa `HttpResponse` yang berisi parameter data hasil *query* yang sudah diubah menjadi XML dan parameter `content_type="application/xml"`.
```python
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
3. Buka `urls.py` di dalam folder `main` dan *import* fungsi yang sudah dibuat.
```python
from main.views import show_main, create_product, show_xml, show_xml_by_id #tambahkan show_xml_by_id
```
4. Tambahkan juga *path url* ke dalam `urlpattern` di file `urls.py` untuk mengakses *function* yang sudah dibuat dan di-*import* melalui kode berikut:
```python
urlpatterns = [
    ...
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'), #tambahkan path ini
    ...
]
```

### JSON
1. Buat *function* yang menerima parameter *request* dengan nama `show_json` dan buat variabel di dalam *function* tersebut yang menyimpan hasil *query* dari seluruh data Product. Tambahkan juga *return function* berupa `HttpResponse` yang berisi parameter data hasil *query* yang sudah diubah menjadi XML dan parameter `content_type="application/json"`.
```python
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
3. Buka `urls.py` di dalam folder `main` dan *import* fungsi yang sudah dibuat.
```python
from main.views import show_main, create_product, show_json #tambahkan show_json
```
4. Tambahkan juga *path url* ke dalam `urlpattern` di file `urls.py` untuk mengakses *function* yang sudah dibuat dan di-*import* melalui kode berikut:
```python
urlpatterns = [
    ...
    path('json/', show_json, name='show_json'),  #tambahkan path ini
    ...
]
```

### JSON by ID
1. Buat *function* yang menerima parameter *request* dan id dengan nama `show_json_by_id` dan buat variabel di dalam *function* tersebut yang menyimpan hasil *query* dari Product sesuai dengan id. Tambahkan juga *return function* berupa `HttpResponse` yang berisi parameter data hasil *query* yang sudah diubah menjadi XML dan parameter `content_type="application/json"`.
```python
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
3. Buka `urls.py` di dalam folder `main` dan *import* fungsi yang sudah dibuat.
```python
from main.views import show_main, create_product, show_json, show_json_by_id #tambahkan show_json_by_id
```
4. Tambahkan juga *path url* ke dalam `urlpattern` di file `urls.py` untuk mengakses *function* yang sudah dibuat dan di-*import* melalui kode berikut:
```python
urlpatterns = [
    ...
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),  #tambahkan path ini
    ...
]
```

## Screenshot hasil akses URL di Postman
### HTML
![HTML View](https://github.com/Haramchu/Tugas-2/blob/main/Image/Html%20View.png)
### JSON
![JSON View](https://github.com/Haramchu/Tugas-2/blob/main/Image/JSON%20View.png)
### JSON ID 1
![JSON View 1](https://github.com/Haramchu/Tugas-2/blob/main/Image/JSON%20view%201.png)
### JSON ID 2
![JSON View 2](https://github.com/Haramchu/Tugas-2/blob/main/Image/JSON%20View%202.png)
### XML
![XML View](https://github.com/Haramchu/Tugas-2/blob/main/Image/XML%20view.png)
### XML ID 1
![XML View 1](https://github.com/Haramchu/Tugas-2/blob/main/Image/XML%20view%201.png)
### XML ID 2
![XML View 2](https://github.com/Haramchu/Tugas-2/blob/main/Image/XML%20view%202.png)

# Tugas 4

## DJango UserCreationForm
UserCreationForm adalah form kelas bawaan Django untuk mengatur pendaftaran *user* baru. Dengan UserCreationForm, *user* atau pengguna baru dapat membuat akun secara mudah di aplikasi web tanpa harus membuat kode baru.

Kelebihan:
- Mudah digunakan
- Bisa diatur isi dari pendaftaran akun
- Integrasi langsung dengan DJango
Kekurangan:
- Kurang fleksibel apabila ada kebutuhan tertentu
- Kebutuhan pendaftaran yang sederhana terkadang tidak cocok sehingga memerlukan pengubahan lebih lanjut

## Autentikasi dan Otorisasi
1. Autentikasi / *Authenthication*
*Authenthication* atau autentikasi adalah proses verifikasi identitas pengguna yang mencoba mengakses sistem atau aplikasi.

Authenthication mengarah kepada verifikasi identitas pengguna agar pengguna yang mengakses sistem atau aplikasi bukanlah orang yang tidak berwenang.

Dalam Django, autentikasi dapat diakses melalui `from django.contrib.auth import authenticate` kemudian diisi dengan parameter username dan password untuk melakukan autentikasi pengguna.

2. Otorisasi / *Authorization*
*Authorization* atau otorisasi adalah izin atau kemampuan pengguna yang telah diautentikasi dalam melakukan berbagai tindakan di dalam sistem atau aplikasi.

Authorization membatasi akses atau izin seseorang dalam sistem atau aplikasi. Contohnya, pengguna yang bukan administrator tidak bisa mengatur aplikasi atau mengubah aplikasi. Hal ini bertujuan untuk mencegah adanya perubahan - perubahan yang tidak diinginkan oleh pihak yang tidak berwenang.

Dalam Django, ada sistem perizinan yang bisa diimplementasikan untuk memberikan izin khusus pada objek dan *user* yang telah di autentikasi. *User* yang berwenang atau memiliki izin bisa mengubah objek yang bersangkutan dan diblokir dari objek tertentu yang hanya bisa diakses *user* lain dengan tingkat otorisasi berbeda.

Otorisasi dan autentikasi berfungsi untuk menjaga aplikasi web sehingga tidak ada akses dari *user* atau entitas yang tidak berwenang. Kedua hal ini akan meningkatkan keamanan aplikasi web secara signifikan dan membuka fungsionalitas baru dalam aplikasi web. Aplikasi web dapat disesuaikan dengan otorisasi *user* dan pembagian pekerjaan di dalam perusahaan bisa lebih mudah diatur.
Melalui autentikasi, aktivitas *log in* dan *log out* pengguna juga bisa diketahui dan dicatat dalam *log* untuk keperluan tertentu. 

## *Cookies* dalam aplikasi web
*Cookies* dalam aplikasi web adalah potongan data yang disimpan di dalam komputer ketika pengguna berinteraksi dengan aplikasi web. *Cookies* berfungsi untuk menyimpan informasi khusus saat pengguna berhasil *log in* ke dalam sebuah aplikasi web untuk mempermudah pengguna dalam mengakses aplikasi web di lain waktu. *Cookies* dapat menyimpan data seperti *username*, nama, password, dan *Session ID* yang kemudian bisa digunakan saat mengakses aplikasi web yang sama.

Dalam Django, *cookies* digunakan untuk menyimpan *Session ID user*. Setiap kali user berhasil masuk ke dalam aplikasi web, *Session ID* akan dicatat dan dimasukkan ke dalam *cookies*.*Session ID* ini kemudian berfungsi untuk mengidentifikasi *user* setiap kali *user* masuk kembali ke aplikasi web. 

## Keamanan Penggunaan *Cookies*
Penggunaan *cookies* tidak sepenuhnya aman dalam aplikasi web.
Berikut adalah beberapa risiko yang dapat muncul saat menggunakan *cookies*:

- ***Cross-site scripting* (XSS)**: Penyerang mencuri cookies dari perangkat pengguna dan mengakses aplikasi web menggunakan cookies dari pengguna. Penyerang kemudian dapat melakukan berbagai hal tanpa sepengetahuan pengguna.

- ***Session Hijacking* (Peretasan Sesi)**: Penyerang yang mencuri cookie pengguna memanfaatkannya untuk mengambil alih sesi pengguna dan melakukan berbagai hal atas nama pengguna yang bersangkutan.

- ***Cookie Spoofing* (Pemalsuan *Cookie*)**: Penyerang memalsukan atau mengganti *cookie* yang sudah diautentikasi dengan *cookie* palsu atau *cookie* dimanipulasi untuk memperoleh akses ke dalam aplikasi web.

- ***Cross-Site Request Forgery* (CSRF)**: Penyerang memanipulasi atau menipu seseorang agar melakukan tindakan yang tidak diinginkan dalam aplikasi web.

Sumber : https://www-freecodecamp-org.translate.goog/news/everything-you-need-to-know-about-cookies-for-web-development/?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=tc

## Menambahkan fungsi registrasi, login, dan logout

### Registrasi
1. Jalankan *virtual environment* dengan `env\Scripts\activate.bat`.
2. Buka `views.py` di dalam subdirektori `main`
3. Tambahkan *import* `redirect`, `UserCreationForm`, dan `messages`.
```python
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
```
`UserCreationForm` sebagai import formulir untuk pengguna baru dalam aplikasi web.
4. Tambahkan fungsi `register` berikut ke dalam `views.py` untuk membuat formulir registrasi dan menghasilkan akun pengguna.
```python
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
`form.is_valid()` berfungsi untuk memvalidasi isi form dan `form.save()` digunakan untuk membuat data dan menyimpan data.
5. Buat berkas HTML baru dengan nama `register.html` pada folder `main/templates` dan isi dengan kode berikut.
```html
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
6. Buka `urls.py` pada subdirektori `main` dan impor fungsi `register`
```python
from main.views import register
```
7. Tambahkan *path url* ke dalam `urlpatterns`.
```python
path('register/', register, name='register'),
```

### Login
1. Buka `views.py` di dalam subdirektori `main`
2. Tambahkan *import* `authenticate` dan `login`.
```python
from django.contrib.auth import authenticate, login
```
`authenticate` dan `login` akan digunakan untuk melakukan autentikasi dan login pengguna.
3. Tambahkan fungsi `login_user` berikut ke dalam `views.py` untuk membuat formulir registrasi dan menghasilkan akun pengguna.
```python
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
`authenticate(request, username=username, password=password` berfungsi untuk autentikasi pengguna berdasarkan *username* dan *password* pengguna.
4. Buat berkas HTML baru dengan nama `login.html` pada folder `main/templates` dan isi dengan kode berikut.
```html
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
5. Buka `urls.py` pada subdirektori `main` dan impor fungsi `login_user`
```python
from main.views import login_user
```
6. Tambahkan *path url* ke dalam `urlpatterns`.
```python
path('login/', login_user, name='login'),
```

### Logout
1. Buka `views.py` di dalam subdirektori `main`
2. Tambahkan *import* `logout`.
```python
from django.contrib.auth import logout
```
3. Tambahkan fungsi `logout` berikut ke dalam `views.py` untuk membuat formulir registrasi dan menghasilkan akun pengguna.
```python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
`redirect` berfungsi untuk mengembalikan pengguna ke halaman awal.
4. Buka berkas `main.html` pada folder `main/templates` dan isi dengan kode berikut setelah penambahan *button* *Add New Product*.
```html
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
```
5. Buka `urls.py` pada subdirektori `main` dan impor fungsi `logout_user`
```python
from main.views import logout_user
```
6. Tambahkan *path url* ke dalam `urlpatterns`.
```python
path('logout/', logout_user, name='logout'),
```
## Merestriksi akses halaman main
1. Buka `views.py` di dalam subdirektori `main` dan tambahkan impor `login_required`
```python
from django.contrib.auth.decorators import login_required
```
2. Tambahkan `@login_required(login_url='/login')` di atas fungsi `show_main` agar halaman *main* hanya bisa diakses pengguna yang telah diautentikasi.

## Menerapkan *cookies* dan detail informasi *last login*
1. Buka `views.py` di dalam subdirektori `main` dan tambahkan impor `HttpResponseRedirect`, `reverse`, dan `datetime`.
```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
2. Mengganti fungsi pada `login_user` untuk menambahkan *cookie* untuk melihat kapan terakhir kali pengguna *login*. Kode pada blok `if user is not None` diganti menjadi kode berikut.
```python
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```
`response.setcookie('last_login', str(datetime.datetime.now()))` berfungsi untuk membuat *cookie* `last_login` dan menambahkannya ke dalam response
3. Pada fungsi `show_main`, tambahkan potongan kode `'last_login': request.COOKIES['last_login']` ke dalam `context`.
```python
context = {
    ...
    'last_login': request.COOKIES['last_login'],
    ...
}
```
4. Ubah fungsi `logout_user` sesuai dengan kode berikut.
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
`response.delete_cookie('last_login')` berfungsi untuk menghapus *cookie* `last_login` saat pengguna melakukan `logout`.
5. Buka berkas `main.html` pada folder `main/templates` dan isi dengan kode berikut di antara tabel dan tombol *logout* untuk menampilkan data *last login*
```html
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```

## Menghubungkan model Item dengan user dan menampilkan detail informasi pengguna yang sedang *logged in*
1. Buka `models.py` pada subdirektori `main` dan impor model.
```python
from django.contrib.auth.models import User
```
2. Tambahkan kode berikut pada model `Item` untuk menghubungkan produk dengan user.
```python
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
3. Buka `views.py` pada subdirektori `main` dan ubah fungsi `create_product` menjadi kode berikut:
```python
def create_product(request):
 form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
 ...
```
4. Ubah fungsi `show_main` menjadi kode berikut:
```python
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
    ...
    }
...
```
5. Simpan semua perubahan dan migrasi model dengan `python manage.py makemigrations` dan `python manage.py migrate`.

## Membuat dua akun pengguna dengan masing - masing tiga *dummy data*
1. Jalankan proyek Django dengan perintah `python manage.py runserver`, pastikan *virtual environment* sudah menyala.
2. Buka http://localhost:8000/ di browser dan tekan tombol *register now*
3. Daftarkan diri untuk membuat akun
4. Setelah membuat akun, halaman web akan kembali ke awal dan lakukan login sesuai dengan *username* dan *password* yang didaftarkan.
5. Tekan tombol `add product` untuk menambahkan produk dan lakukan tiga kali untuk menambahkan tiga produk.
6. Tekan tombol `logout` untuk kembali ke halaman awal dan daftarkan lagi satu akun sesuai dengan langkah nomor 4.
7. Ulangi langkah nomor 5 dan dua akun pengguna dengan masing - masing tiga *dummy data* sudah terbuat.

# Tugas 5

Sumber format css : https://www.w3schools.com/css/default.asp

## Manfaat setiap element selector
1. *Universal Selector*
*Universal Selector* akan mengubah semua elemen. Biasanya digunakan untuk mengatur *style* dasar web.
Contoh :
* {
    margin: 0;
    padding: 0;
}
2. *Element Selector*
*Element Selector* memungkinkan mengubah semua properti untuk elemen dengan tag HTML yang sama. Melalui format *style* suatu tag HTML di *style* CSS, semua tag HTML yang sama akan berubah mengikuti format tersebut.
Contoh :
```css
h1 {
    color: black;
}
```
```HTML
<h1>Warna Hitam</h1>
```
*Style* css diatas akan mengubah semua tag HTML h1.
*Element Selector* biasanya digunakan saat semua tag HTML yang bersangkutan ingin diubah atau memiliki format awalan. 

3. *ID Selector*
*ID Selector* menggunakan sebuah ID yang bisa ditambahkan pada tag sebagai *selector*-nya. Melalui penambahan ID pada, tiap tag bisa diatur menggunakan *style* yang diinginkan.
Contoh :
```css
#Warna {
  background-color: black;
  color: white;
}
```
```HTML
<td id = "Warna">Warna tabel hitam dan font colour putih</td>
```
*ID Selector* biasanya digunakan untuk memberikan *style* spesifik pada bagian tertentu atau memisahkan format suatu *style* dengan *style* awalan.

4. *Class Selector*
*Class Selector* akan memungkinkan untuk mengelompokkan elemen dengan karakteristik yang sama.
Contoh :
```css
.box {
    background-color: #f0f0f0;
    border: 1px solid #ddd;
    padding: 10px;
}
```
```HTML
<div class="box">Content1</div>
<div class="box">Content2</div>
<div class="box">Content3</div>
```
*Class Selector* biasanya digunakan untuk mengelompokkan elemen yang diinginkan karakteristiknya sama.

5. *Inline Styles*
*Inline Styles* lebih mengarah kepada *style* yang ada di dalam suatu tag HTML dan bukan selector karena hanya memungkinkan format suatu elemen spesifik.
Contoh:
```HTML
<img src="img_girl.jpg" width="500" height="600"/>
```
Digunakan untuk mengatur *style* suatu elemen spesifik

6. *Attribute Selector*
Selektor yang memilih elemen berdasarkan atribut. 
Contoh:
```css
input[type=text] {
    background: none;
    padding: 10px;
}
```
```HTML
<input type="text"/>
```
Biasanya digunakan untuk mengatur tampilan elemen berdasarkan nilai atributnya.

7. *Pseudo-Class Selector*
*Pseudo-Class Selector* memilih elemen berdasarkan keadaan atau posisi dalam halaman web.
Contoh:
```css
a:hover {
    color: white;
}
```
Digunakan untuk membedakan *style* elemen saat digunakan pengguna (*hover*) atau elemen dengan urutan tertentu dalam daftar (*elemen kedua*).

Terdapat beberapa *selector* lain yang bisa dilihat dalam web  berikut [Selector CSS](https://www.w3schools.com/cssref/css_selectors.php)

## HTML5 Tag
1. `<nav>`: Tag `<nav>` digunakan untuk menandai bagian dari halaman web yang berisi navigasi atau menu. 

2. `<header>`: Tag `<header>` digunakan untuk menandai bagian atas atau kepala dari sebuah halaman web. Sering digunakan untuk judul, logo, atau elemen lain yang biasanya diletakkan di bagian atas halaman.

3. `<footer>`: Tag `<footer>` digunakan untuk menandai bagian bawah atau kaki dari sebuah halaman web.  Sering digunakan untuk informasi kontak, daftar pustaka, atau elemen lainnya.

4. `<aside>`: Tag `<aside>` digunakan untuk menandai konten yang tidak terkait langsung dengan konten utama tetapi masih terkait atau mendukung konten utama. Bisa berupa tautan terkait, iklan, atau elemen samping lainnya.

5. `<article>`: Tag `<article>` digunakan untuk menandai konten yang dapat tidak memerlukan konteks lain dalam sebuah halaman. Ini bisa berupa posting blog, artikel berita, atau konten lainnya.

6. `<section>`: Tag `<section>` digunakan untuk mengelompokkan konten berdasarkan tema atau topik yang sama. Ini membantu dalam mengatur konten.

7. `<svg>`: Tag `<svg>` digunakan untuk menampilkan grafik vektor dalam dokumen HTML. 

8. `<canvas>`: Tag `<canvas>` digunakan untuk menggambar grafik, animasi, atau visualisasi lainnya menggunakan JavaScript.

9. `<audio>`: Tag `<audio>` digunakan untuk menambahkan audio ke dalam halaman web. 

10. `<video>`: Tag `<video>` digunakan untuk menambahkan video ke dalam halaman web.

Sumber : https://www.tutorialrepublic.com/html-reference/html5-tags.php

## Perbedaan margin dan padding
1. Margin
Margin adalah ruang di luar batas elemen. Margin biasanya digunakan untuk mengatur jarak antar elemen tersebut dengan elemen - elemen lain. Margin itu sendiri transparan sehingga elemen tidak akan terpengaruh oleh margin.
Contoh :
```css
#margin {
    margin: 10px;
}
```
Elemen yang memiliki id margin tersebut akan memiliki margin sebesar 10 *pixel* yang mempengaruhi jarak elemen dengan sekitarnya (mengosongkan area di sekitar border).
2. Padding adalah ruang di dalam batas elemen. Padding biasanya digunakan untuk mengatur jarak antara isi elemen dan batasnya. Padding sendiri tidak memengaruhi elemen - elemen di luar elemen itu sendiri.
Contoh :
```css
#padding {
    padding: 10px;
}
```
Elemen yang memiliki id padding tersebut akan memiliki padding sebesar 10 *pixel* yang mengosongkan area di sekitar konten.
Untuk perbedaan antara margin dan lebih jelas, dapat dilihat gambar berikut:
![Margin dan Padding](https://github.com/Haramchu/Tugas-2/blob/main/Image/MarginPadding.png?raw=true)

## Perbedaan *framework* CSS Tailwind dan Bootstrap
**CSS Tailwind** adalah *framework* yang lebih fleksibel dan terdiri dari berbagai kelas utilitas. Hal ini memungkinkan kontrol lebih atas desain dan skalabilitas yang lebih besar
**Bootstrap** adalah *framework* yang lebih tidak fleksibel dan memiliki bawaan seperti, tombol, navigasi, dan komponen lainnya. Hal ini memungkinkan proses pengembangan yang lebih cepat, namun skalabilitas yang kurang dibandingkan dengan CSS Tailwind.
Berikut adalah tabel perbedaan CSS Tailwind dan Bootstrap
| Tailwind | Bootstrap |
| -------- | -------- |
| Membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah didefinisikan sebelumnya.   | Menggunakan gaya dan komponen yang telah didefinisikan, yang memiliki tampilan yang sudah jadi dan dapat digunakan secara langsung.   |
| Memiliki file CSS yang lebih kecil   | Memiliki file CSS yang lebih besar   |
| Fleksibilitas dan adaptabilitas tinggi terhadap proyek   | Menghasilkan tampilan yang lebih konsisten di seluruh proyek karena menggunakan komponen yang telah didefinisikan.   |
| Pembelajaran yang lebih curam karena memerlukan pemahaman terhadap kelas-kelas utilitas yang tersedia dan bagaimana menggabungkannya untuk mencapai tampilan yang diinginkan.   | Pembelajaran yang lebih cepat untuk pemula karena dapat mulai dengan komponen yang telah didefinisikan.   |

Penggunaan Bootstrap dan Tailwind CSS bergantung pada kebutuhan proyek atau web, cara mengatur, dan preferensi setiap orang. Berikut adalah beberapa pertimbangan dalam menggunakan Bootstrap atau Tailwind:
Tailwind:
1. Proyek membutuhkan tingkat kustomisasi yang tinggi.
2. Sudah memiliki pengalaman menggunakan Tailwind.
3. Saat ingin membuat proyek kecil, proyek dapat diatur setiap detailnya secara spesifik.
Bootstrap:
1. Lebih kompatibel pada beberapa tipe web tertentu (terutama web *browser* yang sudah tua)
2. Membutuhkan waktu yang relatif cepat dalam membuat proyek.
3. Belum memiliki banyak pengalaman mengenai CSS.

## Kustomisasi halaman *login, register,* dan *add product*
1. Halaman *login, register,* dan *add product* dikustomisasi melalui *internal style sheet* dengan `<style>`
2. Mengisi elemen `<style>` dengan format - format untuk tiap tag, id, class, dll. yang diinginkan.
Contoh *style* login.html:
```HTML
<style>
    body {
        background-image: url('link image');
        background-size: cover;
        background-position: center;
        height: 100vh;
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .login {
        background-color: rgba(255, 255, 255, 0.8); 
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }

    h1 {
        margin-bottom: 20px;
    }

    form {
        text-align: left;
    }

    table {
        margin: 0 auto;
    }

    td {
        padding: 10px;
    }

    input.form-control {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .login_btn {
        width: 100%;
        padding: 10px;
        background-color: #007BFF;
        color: #fff;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
</style>
```
Kode *style* CSS diatas akan menghasilkan semua elemen align center di tengah. Bagian body diatur untuk menampilkan latar belakang gambar dan diformat agar gambar sesuai. Bagian login dan elemen lainnya kemudian diberi *background* semi-transparan agar dapat dilihat dengna mudah oleh pengguna.

3. Menyesuaikan `register.html`, `login.html`, dan `create_product`dengan *style* CSS diatas agar format web konsisten.
4. Buka *virtual environment*, nyalakan server, dan buka http://localhost:8000 untuk melihat hasil *style* dan pengaturan lebih lanjut.

## Kustomisasi halaman main
1. Membuat navbar, seperti berikut:
```HTML
<nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container">
            <a class="navbar-brand" href="#">Store Page</a>
            <ul class="navbar-nav ml-auto">
                <li class="nav-item ml-auto">
                    <a class="nav-link" href="{% url 'main:logout' %}">
                        Logout
                    </a>
                </li>
            </ul>
        </div>
    </nav>
```
Navbar diatas akan menghasilkan tombol logout di kanan atas dan text Store Page di kiri atas. Logout kemudian di link agar pengguna bisa logout melalui kanan atas.
2. Membuat *internal style sheet* dengan `<style>` dan isi sesuai dengan keinginan.
*Style* `main.html`:
```css
<style>
    body {
        background-image: url('https://wallpaperaccess.com/full/2109.jpg');
        background-size: cover;
        color: white;
    }
    div {
        padding-left: 20px;
    }

    table {
        border-collapse: collapse;
        margin: 20px auto;
        width: 100%;
    }
    
    table tbody tr:last-child{
        background-color: rgb(76, 0, 0);
    }

    th {
        background-color: black; 
        color: white; 
        text-align: center;
        border: 1px solid #ddd; 
        padding: 8px; 
        font-size: 20px;
    }

    td {
        text-align: center;
        border: 1px solid #ddd; 
        padding: 8px; 
        font-size: 20px;
        color: white;
    }
    tr:nth-child(even) {
        background-color: #474747
    }
    tr:nth-child(odd) {
        background-color: rgb(39, 39, 39);
    }
    

    button {
        width: 80px; 
        height: 30px; 
        text-align: center;
        display: block;
        margin: 0 auto;
        margin-bottom: 10px;
    }
    #button_navbar{
        margin-left: 10%;
        margin: 0;
    }
    #text_navbar{
        margin-right: 10%;
        margin: 0;
    }
    #button_besar {
        width: 200px;
        height: 30px; 
        text-align: center;
        display: block;
        margin: 0 auto;
        margin-bottom: 10px;
    }
    #align_center{
        text-align: center;
    }
    #small_text{
        font-size: 16px;
    }
</style>
```
*Style* diaas berfungsi untuk mengatur ukuran, posisi, warna baik tabel, teks, gambar, dan lainnya.
Untuk beberapa *style* khusus seperti :
```css
tr:nth-child(even) {
    background-color: #474747
}
tr:nth-child(odd) {
    background-color: rgb(39, 39, 39);
}
```
berfungsi untuk mengatur tabel agar tiap barisan memiliki warna yang berbeda.

```css
table tbody tr:last-child{
    background-color: rgb(76, 0, 0);
}
```
berfungsi untuk mengatur warna akhir tabel agar berbeda dari yang lain.

```css
body {
    background-image: url('https://wallpaperaccess.com/full/2109.jpg');
    background-size: cover;
    color: white;
}
```
berfungsi untuk mengatur latar belakang web.

# Tugas 6
## Perbedaan *asynchronous programming* dan *synchronous programming*
### *Synchronous Programming*
- Operasi dijalankan secara berurutan, satu per satu.
- Setiap operasi menunggu operasi sebelumnya untuk selesai sebelum melanjutkan ke operasi berikutnya.
- Bertujuan untuk menjalankan operasi dalam urutan yang diinginkan.

### *Asynchronous Programming*
- Operasi dapat dijalankan secara bersamaan tanpa harus menunggu operasi sebelumnya selesai.
- Biasanya digunakan saat ada operasi yang membutuhkan waktu realtif lama.
- Dapat meningkatkan efisiensi program.


## *Event-driven programming*
Paradigma *event-driven programming* adalah pembuatan pemrograman dimana program merespons *event* yang terjadi, seperti interaksi pengguna, input, atau lainnya. Program tidak mengeksekusi operasi secara berurutan, tetapi program akan menunggu dan merespons *events* yang terjadi.
Sebuah program tidak harus seluruhnya *event-driven*, bisa hanya untuk beberapa fungsi atau operasi tertentu yang baru akan dijalankan saat suatu *event* terjadi.

Contoh operasi *event-driven* dalam program :
1. Pengguna menekan tombol Add Product by AJAX
2. Halaman web akan memunculkan pop up kriteria untuk menambahkan item.
3. Apabila detail item sudah diisi dan tombol *add product* ditekan, `XMLHttpRequest` objek akan dibuat oleh JavaScript
4. `XMLHttpRequest` objek mengirimkan *request* ke server
5. Server memproses *request* tersebut
6. Server mengembalikan *response* kembali kepada halaman web
7. *Response* dibaca oleh JavaScript
8. Halaman web kemudian diperbarui berdasarkan *respones* dan item baru yang didapatkan.

## *Asynchronous programming* pada AJAX
Asynchronous JavaScript and XML atau disingkat AJAX adalah bahasa pemrograman yang memadukan peramban web (untuk meminta data dari web server) dengan JavaScript dan HTML DOM (untuk menampilkan data). AJAX dapat menggunakan XML untuk mengirim data, tetapi AJAX juga dapat menggunakan teks ataupun JSON untuk mengirim data. AJAX memungkinkan halaman web untuk memperbarui data secara asinkronus dengan mengirimkan data di balik layar. Hal tersebut memungkinkan perubahan elemen data pada halaman tanpa harus *reload* halaman.
Contoh alur *asynchronous programming* pada AJAX:
1. Sebuah event terjadi pada halaman web (contohnya tombol submit data ditekan)
2. Sebuah `XMLHttpRequest` *object* dibuat oleh JavaScript
3. `XMLHttpRequest` *object* mengirimkan *request* ke server
4. Server memproses *request* tersebut
5. Server mengembalikan *response* kembali kepada halaman web
6. *Response* dibaca oleh JavaScript
7. Aksi berikutnya akan dipicu oleh JavaScript sesuai dengan langkah yang dibuat pada program

## Perbeedaan Fetch API dengan *library* jQuery
### Fetch API:
- Fetch API banyak digunakan web modern dan merupakan API resmi yang didukung oleh semua browser utama.
- Fetch API menggunakan *promise* yang memungkinkan penanganan *request* asinkron dengan cara yang yang relatif lebih mudah.
- Fetch API adalah API JavaScript murni dan lebih ringan daripada jQuery. Ini dapat mengurangi *source load* halaman dan mempercepat *load time*.

### jQuery:
- jQuery memiliki dukungan untuk browser lama dan baru. Ini memungkinkan pembuatan web yang *compatible* dengan berbagai jenis browser baik lama maupun baru.
- jQuery dianggap lebih mudah digunakan oleh pemula karena memiliki sintaks yang lebih sederhana dan mudah dibaca.
- jQuery memiliki jumlah plugin yang besar dan dapat membantu dalam membuat berbagai operasi atau fungsi.

### Pendapat
Berdasarkan penggunaan Fetch API yang digunakan oleh banyak browser utama, saya lebih condong ke penggunaan Fetch API. Walau terkadang membutuhkan waktu lebih untuk menyesuaikan kompatibilitas dengan semua browser, tujuan AJAX dalam memproses *request* asinkronus dapat lebih mudah diproses di dalam Fetch API. Maka dari itu, penggunaan Fetch API lebih disarankan dibandingkan jQuery.

## Implementasi AJAX GET
1. Buat fungsi baru di `views.py` dengan nama `get_product_json` seperti berikut:
```python
def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))
```
fungsi `get_product_json` akan mengambil data JSON berdasarkan *item* yang dimiliki user.
2. *Import* fungsi `get_product_json` di dalam `urls.py` pada *folder* `main` dan tambahkan *path url* fungsi `get_product_json`.
```python
...
path('get-product/', get_product_json, name='get_product_json'),
```
3. Buka `main.html` pada `main/templates` dan hapus bagian kode `table` yang sudah dibuat dan sesuaikan seperti kode berikut:
```python
<table id="product_table"></table>
```
4. Buat `<Script>` di bawah berkas dan buat fungsi baru di dalam `<Script>` dengan nama `getProducts()`
```html
<script>
    async function getProducts() {
        return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
    }
</script>
```
Fungsi `getProducts()` akan mengambil data melalui `fetch()` API ke data JSON secara *asynchronous* dan data akan diubah menjadi objek JavaScript.
5. Buat fungsi baru bernama `refreshProducts()` di dalam `<Script>` yang akan me-*refresh* data item secara *asynchronous*.
```html
<script>
    ...
    async function refreshProducts() {
        document.getElementById("product_table").innerHTML = ""
        const products = await getProducts()
        let htmlString = `<tr>
                <th>Name</th>
                <th>Amount</th>
                <th>Price</th>
                <th>Description</th>
                <th>Date Added</th>
                <th>Add/Sub</th>
                <th>Edit</th>
                <th>Delete</th>
            </tr>`
        products.forEach((item) => {
            htmlString += `\n<tr>
                <td>${item.fields.name}</td>
                <td>${item.fields.amount}</td>
                <td>${item.fields.price}</td>
                <td>${item.fields.description}</td>
                <td>${item.fields.date_added}</td>
                <td>
                    <a href="add_amount/${item.pk}">
                        <button>
                            Add
                        </button>
                    </a>
                    <a href="sub_amount/${item.pk}">
                        <button>
                            Sub
                        </button>
                    </a>
                </td>
                <td>
                    <a href="edit-product/${item.pk}">
                        <button>
                            Edit
                        </button>
                    </a>
                </td>
                <td>
                    <a href="delete/${item.pk}">
                        <button>
                            Delete
                        </button>
                    </a>
                </td>
            </tr>`
        })
        document.getElementById("product_table").innerHTML = htmlString
    }
</script>
```
Kode disesuaikan dengan button yang diinginkan dan isi tabel.
`document.getElementById("product_table")` berfungsi untuk mengambil elemen berdasarkan ID sehingga semua *item* akan masuk ke dalam tabel.

## Implementasi AJAX POST
### Membuat tombol yang membuka sebuah modal dengan form untuk menambahkan item ke dalam basis data dan menampilkan daftar item terbatu tanpa *reload* halaman.
1. Tambahkan kode berikut di atas kode untuk mengatur tampilan form untuk menambahkan item melalui AJAX.
```html
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
                        <label for="amount" class="col-form-label">Amount:</label>
                        <input type="text" class="form-control" id="amount" name="amount"></input>
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
```
Sesuaikan kode dengan *form* atau *model* data aplikasi.
2. Tambahkan kode berikut untuk menambahkan *button* pada halaman web.
```html
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Product by AJAX</button>
```
Sesuaikan letak *button* dengan keinginan.
3. Buat fungsi `addProduct()` di dalam `<Script>` seperti kode berikut:
```html
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
`new FormData(document.querySelector('#form'))` berfungsi untuk membuat FormData baru
`document.getElementById("form").reset()` berfungsi untuk mengosongkan isi *field* form setelah di-*submit*
4. Tambah fungsi `onclick` pada button "Add Product" untuk menjalankan fungsi `addProduct()` melalui kode berikut:
```html
<script>
...
document.getElementById("button_add").onclick = addProduct
</script>
```
### Menghubungkan fungsi `create-ajax` dengan fungsi *view* `add_product_ajax`
1. *Import* `from django.views.decorators.csrf import csrf_exempt` dan `HttpResponseNotFound` di dalam `views.py`.
2. Buat fungsi `add_product_ajax` di dalam `views.py` yang menerima `request` seperti berikut:
```python
@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        price = request.POST.get("price")
        description = request.POST.get("description")
        user = request.user

        new_product = Item(name=name, amount=amount, price=price, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```
Sesuaikan kode dengan *model* atau form data.
2. *Import* fungsi `add_product_ajax` di dalam `urls.py` pada *folder* `main` dan tambahkan *path url* fungsi `add_product_ajax`.
```python
...
path('create-ajax/', add_product_ajax, name='add_product_ajax')
```

## Melakukan perintah `collectstatic`
1. Jalankan *virtual environment* dengan `env\Scripts\activate.bat`.
2. Jalankan perintah `python manage.py collectstatic` untuk mengumpulkan *file static* dari setiap aplikasi ke dalam satu *folder*.