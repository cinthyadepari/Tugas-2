link heroku : https://katalogpbp.herokuapp.com/mywatchlist/

Jelaskan perbedaan antara JSON, XML, dan HTML!
-- JSON adalah singkatan dari JavaScript Object Notation. JSON didesain menjadi self-describing, sehingga JSON sangat mudah untuk dimengerti. JSON digunakan pada banyak aplikasi web maupun mobile, yaitu untuk menyimpan dan mengirimkan data. Sintaks JSON merupakan turunan dari Object JavaScript. Akan tetapi format JSON berbentuk text, sehingga kode untuk membaca dan membuat JSON banyak terdapat dibanyak bahasa pemrograman.
-- XML adalah singkatan dari eXtensible Markup Language. XML didesain menjadi self-descriptive, jadi dengan membaca XML tersebut kita bisa mengerti informasi apa yang ingin disampaikan dari data yang tertulis. XML digunakan pada banyak aplikasi web maupun mobile, yaitu untuk menyimpan dan mengirimkan data. XML hanyalah informasi yang dibungkus di dalam tag. Kita perlu menulis program untuk mengirim, menerima, menyimpan, atau menampilkan informasi tersebut.
-- HTML merupakan singkatan dari HyperText Markup Language, yaitu bahasa markup standar untuk membuat serta menyusun halaman dan aplikasi web. HTML digunakan untuk mendeskripsikan struktur dan layout pada web. HTML tidak dianggap sebagai bahasa pemrograman karena tak bisa memberikan fungsi yang dinamis. Umumnya, fungsi HTML adalah untuk mengelola serangkaian data serta informasi sehingga suatu dokumen dapat diakses dan ditampilkan di web.

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
--Format untuk pertukaran data, pengiriman data, atau request response bisa dalam bentuk JSON, XML, maupun HTML, yang mana format-format data tersebut merupakan data delivery, yang digunakan untuk menyimpan dan mengirimkan data, serta komunikasi antar program, guna pengimplementasian sebuah platform.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
-- pertama membuat serta menjalankan virtual environment, menginstall dependencies, dan melakukan runserver terlebih dahulu. lalu saya membuat app dengan nama mywatchlist. Dan kemudian saya mulai membuat code di views, models, serta url. Saya juga membuat folder fixtures yang berisi data-data yang akan ditampilkan dalam bentuk file .json. Pada folder templates saya membuat 3 file yaitu base.html, create.html, dan juga read.html. Setelah semua code saya selesai, saya langsung melakukan test dan semua berjalan.

![html](https://user-images.githubusercontent.com/112605451/191650108-6514b595-d677-40c4-97e6-8a04dcf3da5d.png)
![json](https://user-images.githubusercontent.com/112605451/191650115-ac672a8a-b7be-4fb3-8837-76a8d1796013.png)
![xml (1)](https://user-images.githubusercontent.com/112605451/191650140-ffa4470c-b49c-48fc-95db-310890c28f09.png)
![xml (2)](https://user-images.githubusercontent.com/112605451/191650146-8c0a056b-cfbd-4462-84c3-7ae2368236c1.png)