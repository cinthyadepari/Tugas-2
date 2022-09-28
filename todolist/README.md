link heroku : https://katalogpbp.herokuapp.com/todolist/

1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

-- dari sumber-sumber yang telah saya baca, {% csrf_token %} merupakan sebuah perlindungan dari serangan pemalsuan permintaan lintas situs (CSRF) yang dapat membuat penyerang tidak akan memungkinkan untuk melakukan permintaan HTTP yang secara sepenuhnya valid yang cocok untuk diumpankan ke pengguna korban. Seperti penjelasan yang telah saya paparkan dari berbagai sumber, apabila tidak memakai csrf_token tentu akan mendapatkan serangan dari CSRF yang tidak dapat dipastikan nilai dari token CSRF pengguna yang nantinya menyebabkan tidak dapat membuat permintaan dengan semua parameter yang diperlukan oleh aplikasi untuk memenuhi permintaan tersebut.

2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

-- dari yang telah saya baca berbagai sumber, pembuatan elemen <form> memungkinkan apabila ingin dibuat secara manual. Namun jika membuat elemennya secara manual akan memiliki cara yang cukup rumit, karena itu django sudah mempersiapkan atau memudahkan kita dalam menggunakan elemen dari <form>. Gambaran besarnya adalah dengan menggunakan POST dalam code applikasi yang akan dibuat dan tidak lupa untuk menggunakan {% csrf_token %}. Kita juga dapat menggunakan elemen lainnya seperti <input> serta elemen lain yang telah disediakan.

3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

-- pertama user diminta untuk menginput data diri yang terdiri dari username serta password(jika belum ada maka dapat masuk ke menu daftar akun), setelahnya kita dapat mengecek apakah form telah disubmisi atau belum. Lalu menyimpan data tersebut dengan code yang telah dibuat seperti berikut. Apabila datanya telah kita dapatkan, kita dapat menyimpannya ke dalam data base dengan menggunakan method save(). Setelah semua proses telah terjadi, maka kita dapat merender data tersebut ke HTML dan mengiterasinya ke dalam HTML.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

 -- cara saya mengimplementasikan semua checklist diatas adalah dengan mengaktifkan terlebih dahulu aplikasi yang ingin dibuat dan mendaftarkan aplikasi tersebut dengan menambahkan path dari aplikasi tersebut. Lalu saya mulai dengan membuat models aplikasinya bagaimana di dalam file models.py yang didalamnya terdapat user yang gunanya untuk menghubungkan task dengan pengguna yang membuat task tersebut, date untuk mendeskripasikan tanggal dari pembuatan task, title yang nantinya kan mendeskripsikan judul dari task tersebut, dan description yang gunanya untuk mendeskripsikan deskripsi task. Kemudian meneruskannya dengan views.py, pada file ini saya juga mengimplementsikan form registrasi, login, dan logout. Saya juga membuat file baru untuk form yang akan membantu berjalannya app ini dengan baik.