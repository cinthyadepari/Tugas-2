link heroku : https://katalogpbp.herokuapp.com/katalog/

![Bagan PBP](https://user-images.githubusercontent.com/112605451/190192035-15f540df-858b-408b-89de-1d3651bc7df4.jpg)

Alasan menggunakan virtual environment karena virtual environment memudahkan kita dalam melakukan pemisahan pengaturan dan package yang diinstal pada setiap proyek Django yang menyebabkan apabila terdapat perubahan yang dilakukan, maka tidak akan berpengaruh atau menyinggung proyek lainnya.
Lalu jika tidak menggunakan virtual environment, berdasarkan berbagai sumber yang telah saya baca dan mengenai alasan yang telah saya paparkan, maka singkatnya suatu proyek ataupun aplikasi pasti akan mempengaruhi proyek lainnya.

Cara saya mengimplementasikan poin 1 sampai 4 adalah sebenarnya tidak jauh berbeda dengan tutorial 1 yang telah saya kerjakan minggu lalu. Pertama saya membuat repositori yang baru untuk menampung tugas minggu ini kemudian saya melakukan clone repositori tersebut, membuat serta menjalankan virtual environment, menginstall dependencies, dan melakukan runserver terlebih dahulu.
Selanjutnya saya mulai membuat code untuk aplikasi django dan konfigurasi dari model untuk katalog saya. Pada file models.py saya membuat satu fungsi yang berisi elemen-elemen yang akan terdapat pada katalog saya. Kemudian saya melakukan makemigration untuk migrasi sketsa model ke database django lokal, lalu migrate untuk menerapkan skema model ke dalam database django lokal, karena telah terdapat file initial_catalog_data.json, maka saya langsung menjalankan perintah loaddata untuk memasukkan data ke django lokal.
Selanjutnya saya melakukan implementasi views dasar dengan langkah awal membuat sebuah fungsi untuk menerima parameter request dan mengembalikan render pada file views.py yang berada pada folder katalog, lalu pada file katalog.html saya mengganti Fill me! menjadi nama serta NPM saya. pada file urls.py yang berada pada folder project_django, saya mendaftarkan aplikasi katalog saya, dan langkah akhir saya menjalankan runserver dan mencoba membuka link untuk melihat katalog saya.

![html](https://user-images.githubusercontent.com/112605451/191650108-6514b595-d677-40c4-97e6-8a04dcf3da5d.png)
![json](https://user-images.githubusercontent.com/112605451/191650115-ac672a8a-b7be-4fb3-8837-76a8d1796013.png)
![xml (1)](https://user-images.githubusercontent.com/112605451/191650140-ffa4470c-b49c-48fc-95db-310890c28f09.png)
![xml (2)](https://user-images.githubusercontent.com/112605451/191650146-8c0a056b-cfbd-4462-84c3-7ae2368236c1.png)