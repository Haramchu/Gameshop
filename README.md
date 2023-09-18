Nama        : Clement Samuel Marly

NPM         : 2206082114

Kelas       : PBP C

[Tugas 2](#tugas-2)

[Tugas 3](#tugas-3)

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
![DJango Framework](https://github.com/Haramchu/Tugas-2/blob/main/PBP-Tugas%202.png)
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
Mendukung pengiriman daa berupa angka, objek, string, array Boolean.

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
