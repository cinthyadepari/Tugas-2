 link heroku : https://katalogpbp.herokuapp.com/todolist/
 
 Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

 -- Synchronous programming adalah paradigma programming untuk sebuah aplikasi atau sistem yang tidak bisa diotak-atik di tengah jalan. Hal ini dikarenakan metode pemanggilan function atau request yang hanya bisa dilakukan satu-satu (synchronous). Contohnya, web yang synchronous ketika pagenya dibuka oleh user maka dia harus refresh untuk melihat perubahan yang baru.

-- Asynchronous programming adalah paradigma untuk sebuah sistem yang bisa update atau berubah tanpa harus dijalankan ulang. Hal ini dikarenakan sistem bisa multitasking dan menjalankan banyak hal sekaligus (sambil jalan sambil update). Contohnya, web yang asynchronous bisa mengubah tampilan sambil dibuka oleh user.

 Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

 -- Event-driven programming adalah paradigma dimana program bergantung pada 'event' yang terjadi pada sistem atau aplikasi. Event yang dimaksud dapat berupa perubahan waktu, button click, button hover, key press, dll. Contohnya, pada tugas 6 kita membuat modal (yang sudah ada di html) yang hanya akan muncul jika tombol New Task dipencet.

 Jelaskan penerapan asynchronous programming pada AJAX.

 --AJAX (Asynchronous JavaScript And XML) memiliki kemampuan untuk mengubah isi html / tampilan page tanpa harus mengubah file/data yang tentunya membutuhkan refresh. AJAX juga mampu membuat HTTP POST dan GET request sendirinya.

 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
 -- saya hanya menambahkan script pada todolis.html agar dapat berjalan sesuai yang diinginkan. Saya juag membuat beberapa code tambahan untuk mengambil datanya, menghapus, dan menampilkannya utk ajax juga code untuk json. Saya tidak banyak menambahkan code pada tugas kali ini.