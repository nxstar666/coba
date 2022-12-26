from django.shortcuts import render

# Create your views here.
def index (request):
    context = {
        'title':'PMB UMMI',
        'name':'Sri Tuning, S.Tr.Keb',
        'namee':'Ulfah Saraswati, S.Tr.Keb',
        'layanan':[
            ['lynmelahirkan.png','Melahirkan','Melahirkan','24Jam'],
            ['lynperiksahamil.png','Periksa Kehamilan','Periksa','Kehamilan'],
            ['lynimunisasi.png','Imunisasi','Suntik','Imunisasi'],
            ['lynkb.png','KB','Layanan','KB'],
            ['lynpascalahiran.png','Pasca Lahiran','Pasca','Melahirkan'],
            ['lynumum.png','Umum','Pemeriksaan','Umum']
        ],
        'teamsatu':[
            ['user.png','Tuning'],
            ['user.png','Ulfah']
        ],
        'teamdua':[
            ['adee.JPEG','Ade'],
            ['ani.JPG','Ani'],
            ['umii.jpg','Umi'],
            ['yeni.jpg','Yeni']
        ]
    }
    return render (request,'index.html',context)

def layanan (request):
    context = {
        'pelayanan':[
            ['lynmelahirkan.png','Melahirkan','Persalinan','24JAM','Tindakan persalinan 24 jam, tarif / biaya','tergantung obat & BKM'],
            ['lynperiksahamil.png','Periksa Kehamilan','Periksa Kehamilan','16.30 - 21.00','pemeriksaan biasa','(menggunakan doppler) / USG'],
            ['lynimunisasi.png','imunisasi','Imunisasi','Setiap Tanggal 15','Pendaftaran dibuka pada tanggal 13','(2 hari sebelum imunisasi)'],
            ['lynkb.png','KB','Layanan KB','08.00 - 21.00 WIB','Untuk suntikan dari jam 08.00,','dan implan / IUD dari jam 16.30'],
            ['lynpascalahiran.png','Pasca Melahirkan','Pasca Melahirkan','16.30 - 21 WIB','Kontrol setiap 5 - 7 hari sekali sebanyak','3X'],
            ['lynumum.png','Umum','Pemeriksaan Umum','16.30 - 21.00 WIB','Meliputi pemeriksaan anak dan','pemeriksaan dewasa']
        ]
    }
    return render (request,'layanan.html',context)

def pendaftaran (request):
    return render (request,'pendaftaran.html')

def artikel (request):
    context = {
        'artikel':[
            ['periksahamil.jpg','periksa hamil','Pemeriksaan Kehamilan','Salah satu solusi efektif dalam menurunkan Angka Kematian Ibu (AKI) dan Angka Kematian Bayi (AKB) adalah dengan cara meningkatkan pertolongan persalinan yang .....','periksahamil'],
            ['suntiktt.jpg','suntik tt','Suntik TT Ibu Hamil','Beberapa jenis imunisasi sangat dibutuhkan saat hamil untuk melindungi kesehatan Mommil dan janin. Imunisasi tersebut diberikan pada jangka waktu yang .....','suntiktt'],
            ['tandamelahirkan.jpg','tanda melahirkan','Tanda-Tanda Melahirkan','Memperhatikan munculnya tanda-tanda melahirkan adalah hal yang penting bagi para ibu hamil agar bisa mempersiapkan diri dan bersiaga dalam menghadapi persalinan .....','tandamelahirkan'],
            ['bahayabayi.jpg','bahaya bayi baru lahir','Bahaya Pada Bayi','Pasangan suami istri atau calon orangtua yang tengah mempersiapkan kelahiran buah hati penting untuk mengenal tanda-tanda bahaya pada bayi baru lahir. Dokter .....','bahayabayi'],
            ['kontrollahiran.jpg','kontrol melahirkan','Kontrol Pasca Melahirkan','Setelah melahirkan dan diperbolehkan dokter atau bidan untuk pulang ke rumah, para ibu lalu disibukan dengan aktivitas mengurus bayi. Hal ini kadang membuat .....','kontrollahiran'],
            ['kb.jpg','pemilihan KB','Pemilihan KB','Cara memilih alat kontrasepsi yang tepat penting untuk diketahui bila Anda dan pasangan ingin menunda kehamilan. Tak hanya untuk mencegah terjadinya kehamilan .....','kb'],
            ['imunisasi.jpg','imunisasi anak','Imunisasi Pada Anak','Berdasarkan data dari Ikatan Dokter Anak Indonesia (IDAI), imunisasi mampu mencegah 2 - 3 juta kematian anak setiap tahun. Pemberian imunisasi pada anak sangat .....','imunisasi'],
            ['gizi.jpg','gizi anak usia dini','Gizi Anak Usia Dini','Gizi seimbang untuk anak usia dini sangat diperlukan agar dapat mengoptimalkan tumbuh kembang anak dan menjaga kesehatan tubuh. Namun ternyata .....','gizi'],
            ['promil.jpg','program hamil','Persiapan Kehamilan','Apakah Anda dan pasangan sedang merencanakan kehamilan? Penting dicatat bahwa ada beberapa persiapan kehamilan yang perlu diketahui sebelum menjalani .....','promil']
        ]
    }
    return render (request,'artikel.html',context)

def periksahamil (request):
    context = {
        'title':'Periksa Hamil',
        'foto':'periksahamil.jpg',
        'alt':'periksa hamil',
        'judul':'pemeriksaan Kehamilan',
        'i':[
            ['Salah satu solusi efektif dalam menurunkan Angka Kematian Ibu (AKI) dan Angka Kematian Bayi (AKB) adalah dengan cara meningkatkan pertolongan persalinan yang dilakukan oleh tenaga medis terlatih yang disediakan oleh fasilitas pelayanan kesehatan. Di samping itu, dibutuhkan partisipasi serta kesadaran ibu terhadap pentingnya pemeriksaan kehamilan di fasilitas pelayanan kesehatan oleh tenaga kesehatan.','Apa Tujuan ANC (Antenatal Care) . ??','','','Pemeriksaan kehamilan dapat dilakukan di Puskesmas, klinik, atau rumah sakit. Pemeriksaan ANC pada ibu hamil dapat dilakukan oleh tenaga kesehatan, antara lain bidan, perawat, dokter umum, maupun dokter spesialis obstetri dan ginekologi (dokter kandungan).','',''],
            ['Pemeriksaan ANC (Antenatal Care) merupakan pemeriksaan kehamilan yang bertujuan untuk meningkatkan kesehatan fisik dan mental pada ibu hamil secara optimal, hingga mampu menghadapi masa persalinan, nifas, menghadapi persiapan pemberian ASI secara eksklusif, serta kembalinya kesehatan alat reproduksi dengan wajar','1. Memantau kemajuan proses kehamilan demi memastikan kesehatan pada ibu serta tumbuh kembang janin yang ada di dalamnya.','','','','',''],
            ['Pemeriksaan kehamilan dilakukan minimal 4 (empat) kali selama masa kehamilan, yaitu 1 kali pemeriksaan pada trimester pertama, 1 kali pemeriksaan pada trimester kedua, dan 2 kali pemeriksaan pada trimester ketiga.','2. Mengetahui adanya komplikasi kehamilan yang mungkin saja terjadi saat kehamilan sejak dini, termasuk adanya riwayat penyakitdan tindak pembedahan.','','','','',''],
            ['','3. Meningkatkan serta mempertahankan kesehatan ibu dan bayi.','','','','',''],
            ['','4. Mempersiapkan proses persalinan sehingga dapat melahirkan bayi dengan selamat serta meminimalkan trauma yang dimungkinkan terjadi pada masa persalinan.','','','','',''],
            ['','5. Menurunkan jumlah kematian dan angka kesakitan pada ibu.','','','','',''],
            ['','6. Mempersiapkan peran sang ibu dan keluarga untuk menerima kelahiran anak agar mengalami tumbuh kembang dengan normal.','','','','',''],
            ['','7. Mempersiapkan ibu untuk melewati masa nifas dengan baik serta dapat memberikan ASI eksklusif pada bayinya.','','','','',''],
        ],
        'redirect':'https://promkes.kemkes.go.id/pentingnya-pemeriksaan-kehamilan-anc-di-fasilitas-kesehatan',
        'artikellain':[
            ['gizi.jpg','gizi anak','gizi','Gizi Anak Usia Dini'],
            ['promil.jpg','promil','promil','Persiapan Kehamilan'],
            ['suntiktt.jpg','suntik tt','suntiktt','Suntik TT Ibu Hamil'],
            ['tandamelahirkan.jpg','tanda melahirkan','tandamelahirkan','Tanda-Tanda Melahirkan'],
            ['bahayabayi.jpg','bahaya bayi','bahayabayi','Bahaya Pada Bayi']
        ]
    }
    return render (request,'dummy.html',context)

def suntiktt (request):
    context = {
        'title':'suntik tt',
        'foto':'suntiktt.jpg',
        'alt':'suntik tt',
        'judul':'Suntik TT Ibu Hamil',
        'i':[
            ['Beberapa jenis imunisasi sangat dibutuhkan saat hamil untuk melindungi kesehatan Mommil dan janin. Imunisasi tersebut diberikan pada jangka waktu yang berbeda tiap jenisnya. Jenis imunisasi yang biasa diberikan pada ibu hamil yaitu imunisasi influenza dan imunisasi TT (Tetanus Toxoid)','','Tetanus yang menyerang bayi disebut tetanus neonatorum. Bayi yang terkena tetanus sebagian besar tidak dapat diselamatkan. Imunisasi TT pada ibu hamil pun dibutuhkan untuk mencegah terjadinya tetanus pada bayi yang dilahirkan.','','Pemberian imunisasi TT pada ibu hamil harus sedini mungkin. Usia kehamilan 27 hingga 36 minggu merupakan jadwal suntik TT untuk ibu hamil yang tepat. Imunisasi TT pada ibu hamil diberikan sebanyak dua kali. Masing-masing pemberian imunisasi TT pada ibu hamil memiliki jeda 4 minggu. Jadwal suntik TT untuk ibu hamil ini merupakan jadwal yang direkomendasikan WHO.','',''],
            ['Imunisasi TT pada ibu hamil diberikan untuk mencegah terjadinya penyakit tetanus. Tetanus disebabkan oleh bakteri yang masuk ke dalam tubuh melalui luka terbuka. Bakteri tetanus dapat menyebabkan peningkatan pengetatan otot, mengakibatkan kejang, kekakuan, dan lengkungan tulang belakang. Pada akhirnya, pernapasan akan menjadi lebih sulit dan kejang lebih sering terjadi.','','Imunisasi TT pada ibu hamil bermanfaat mencegah terjadinya tetanus pada bayi. Jika imunisasi TT pada ibu hamil dilakukan, maka akan menyelamatkan Mommil serta janin yang dikandung, karena antibodi yang didapatkan Mommil saat imunisasi TT ditransfer ke janin.','','Apakah terdapat Efek Samping dari Imunisasi TT pada Ibu Hamil . ?','',''],
            ['Orang dengan beragam usia memiliki kemungkinan terkena tetanus. Akan tetapi, penyakit ini sangat umum terjadi pada bayi yang baru lahir. Hal ini dapat terjadi karena proses persalinan dilakukan tanpa prosedur sterilisasi peralatan yang memadai.','','Kapan jadwal suntik TT untuk ibu hamil dilakukan . ?','','Secara umum, imunisasi yang diberikan baik untuk umum maupun untuk ibu hamil pastilah memiliki efek samping yang ringan dan berat. Efek suntik TT pada ibu hamil yang tergolong ringan yaitu demam, sakit kepala ringan, nyeri badan dan kemerahan pada area suntikan. Efek suntik TT pada ibu hamil yang berat biasanya seperti kesemutan pada tangan/kaki, masalah pendengaran, kesulitan menelan, kelemahan otot, kejang. Jika Mommil merasakan keluhan tersebut setelah imunisasi TT, Mommil harus segera memeriksakan diri ke dokter kandungan. Segera dapatkan bantuan medis jika Mommil merasa gejala reaksi alergi yang serius, termasuk ruam, gatal/bengkak (terutama pada wajah/lidah/tenggorokan), pusing parah dan kesulitan bernapas. Berbagai hal tersebut dapat membantu Mommil untuk mencegah terjangkitnya tetanus pada Mommil dan janin. Selain itu, pilihlah tempat bersalin yang terjamin kualitas dan kebersihannya agar Mom tenang saat melakukan persalinan.','',''],
        ],
        'redirect':'https://kehamilansehat.com/id/jadwal-imunisasi-tt-pada-ibu-hamil/#:~:text=Imunisasi%20TT%20pada%20ibu%20hamil%20diberikan%20untuk%20mencegah%20terjadinya%20penyakit,kekakuan%2C%20dan%20lengkungan%20tulang%20belakang.',
        'artikellain':[
            ['promil.jpg','promil','promil','Persiapan Kehamilan'],
            ['periksahamil.jpg','periksa hamil','periksahamil','Pemeriksaan Kehamilan'],
            ['tandamelahirkan.jpg','tanda lahiran','tandamelahirkan','Tanda-Tanda Melahirkan'],
            ['bahayabayi.jpg','bahaya bayi','bahayabayi','Bahaya Pada Bayi'],
            ['kontrollahiran.jpg','kontrol lahiran','kontrollahiran','Kontrol Pasca Melahirkan']
        ]

    }
    return render (request,'dummy.html',context)

def tandamelahirkan (request):
    context = {
        'title':'tanda lahiran',
        'foto':'tandamelahirkan.jpg',
        'alt':'tanda lahiran',
        'judul':'Tanda-Tanda Melahirkan',
        'i':[
            ['Memperhatikan munculnya tanda-tanda melahirkan adalah hal yang penting bagi para ibu hamil agar bisa mempersiapkan diri dan bersiaga dalam menghadapi persalinan. Oleh karena itu, mari kenali tanda-tanda melahirkan sudah dekat.','1. Sulit tidur','','','Hal yang Perlu Dipersiapkan Saat Mendekati Masa Persalinan','- Tas berisi pakaian dan peralatan mandi','Selain perlengkapan melahirkan, Bumil juga sudah harus memastikan siapa yang akan mendampingi Bumil selama persalinan. Bumil bisa memilih suami, orang tua, saudara, atau teman. Pastikan mereka siap menemani Bumil saat persalinan dimulai. Mengetahui tanda-tanda melahirkan sangat penting bagi para calon ibu, terutama yang berencana melahirkan secara normal, karena waktu melahirkan tidak dapat diatur dan tidak selalu sesuai dengan prediksi. Dengan begitu, Bumil bisa lebih siap dalam menghadapi persalinan. Namun, jika Bumil tidak merasakan tanda-tanda melahirkan meskipun sudah melewati tanggal prediksi, segera periksakan diri ke dokter agar dapat ditentukan apakah persalinan perlu segera dilakukan atau tidak.'],
            ['Kendati sudah memiliki hari perkiraan lahir (HPL), faktanya hanya sedikit ibu hamil yang bersalin tepat pada hari perkiraan lahirnya. Oleh sebab itu, Bumil perlu memperhatikan tanda-tanda melahirkan yang umumnya dapat mulai terasa dari 3 minggu sebelum hari perkiraan lahir hingga 2 minggu setelahnya.','Tidur malam yang terganggu dan perasaan gelisah bisa menjadi salah satu tanda melahirkan semakin dekat. Maka dari itu, sebisa mungkin, usahakan agar Bumil bisa tidur atau beristirahat di siang hari, karena Bumil pasti membutuhkan tenaga ketika persalinan berlangsung.','','Ini juga merupakan tanda-tanda melahirkan sudah dekat. Sebelum melahirkan, ibu hamil mungkin akan merasakan nyeri atau kram pada punggung, perut, atau kram layaknya nyeri yang dirasakan saat mendekati masa menstruasi, tetapi lebih sakit.','Ketika memasuki bulan ke-9 kehamilan, sebaiknya Bumil sudah menyiapkan segala perlengkapan yang dibutuhkan selama persalinan. Jadi, saat air ketuban pecah atau terjadi kontraksi, Bumil bisa langsung bergegas ke rumah sakit sambil membawa perlengkapan tersebut.','- Perlengkapan bayi',''],
            ['Tanda-Tanda Melahirkan yang Harus Diperhatikan','2. Lebih sering buang air kecil','','5. Kontraksi palsu','Perlengkapan yang perlu Bumil bawa meliputi:','- Makanan ringan',''],
            ['Tanda-tanda menjelang persalinan bisa saja berbeda pada setiap ibu hamil. Berikut adalah tanda-tanda melahirkan yang paling umum terjadi:','Beberapa pekan atau hari sebelum persalinan, bayi akan turun ke rongga panggul Bumil. Kondisi ini akan membuat rahim menekan kandung kemih, sehingga ibu hamil akan lebih sering buang air kecil dibandingkan biasanya.','','Kontraksi ini biasa disebut kontraksi Braxton-Hicks atau pengencangan perut yang datang dan pergi. Umumnya kontraksi ini berlangsung 30-120 detik, tidak terjadi dengan beraturan, dan dapat hilang ketika ibu hamil berpindah posisi atau rileks. Selain itu, kontraksi palsu biasanya hanya terasa di daerah perut atau panggul, sementara kontraksi sungguhan biasanya terasa di bagian bawah punggung kemudian berpindah ke bagian depan perut. Sebenarnya kontraksi Braxton-Hicks sudah bisa dirasakan sejak usia kehamilan 16 minggu, tapi kontraksi ini akan terasa lebih kuat dan lebih sering ketika mendekati masa melahirkan.','','- Bantal dan selimut yang nyaman',''],
            ['','3. Perubahan emosional','','6. Keluar lendir kental bercampur darah dari vagina','','- Buku, majalah, atau barang lain yang bisa menemani Bumil menunggu persalinan',''],
            ['','Biasanya ibu hamil akan merasakan perubahan dari segi emosional beberapa hari sebelum melahirkan, misalnya mudah marah atau moody, selayaknya masa-masa saat akan menstruasi.','','7. Air ketuban pecah','','- Kamera video dengan baterai yang telah terisi penuh beserta charger, jika Bumil ingin mengabadikan momen melahirkan',''],
            ['','4. Rasa sakit atau nyeri','','Tanda-tanda melahirkan yang diketahui oleh kebanyakan orang adalah pecahnya air ketuban. Kebanyakan ibu hamil akan lebih dulu merasakan kontraksi sebelum air ketuban pecah, tapi ada juga yang mengalami pecahnya ketuban terlebih dahulu. Ketika hal ini terjadi, biasanya persalinan akan segera menyusul.','','','']
        ],
        'redirect':'https://www.alodokter.com/tanda-tanda-melahirkan-sudah-dekat',
        'artikellain':[
            ['periksahamil.jpg','periksa hamil','periksahamil','Pemeriksaan Kehamilan'],
            ['suntiktt.jpg','suntik tt','suntiktt','Suntik TT Ibu Hamil'],
            ['bahayabayi.jpg','bahaya bayi','bahayabayi','Bahaya Pada Bayi'],
            ['kontrollahiran.jpg','kontrol lahiran','kontrollahiran','Kontrol Pasca Melahirkan'],
            ['kb.jpg','kb','kb','Pemilihan KB']
        ]
    }
    return render (request,'dummy.html',context)

def bahayabayi (request):
    context = {
        'title':'bahya bayi baru lahir',
        'foto':'bahayabayi.jpg',
        'alt':'bahaya pada bayi',
        'judul':'Bahaya Pada Bayi',
        'i':[
            ['Pasangan suami istri atau calon orangtua yang tengah mempersiapkan kelahiran buah hati penting untuk mengenal tanda-tanda bahaya pada bayi baru lahir.','1. Bayi tidak mau menyusu','','','','',''],
            ['Dokter spesialis kandungan dan kebidanan RSUD Bung Karno Surakarta, dr. Andy Wijaya, Sp.OG, M.Kes, menyampaikan tanda-tanda bahaya pada bayi baru lahir adalah suatu keadaan atau masalah yang dapat mengakibatkan kematian pada bayi.','dr. Andy menjelaskan bayi biasanya tidak mau menyusu ketika sudah dalam kondisi lemah dan mungkin dalam kondisi dehidrasi berat. Jika mendapati kondisi ini, para orangtua bisa mengupayakan agar sang buah hati tetap menempel ke payudara ibu dengan cara yang benar. Saat bayi membuka mulutnya, pastikan seluruh putting dan sebagian areola masuk ke dalam mulutnya. Apabila cara ini tak bisa membuat bayi minum ASI, para orangtua disarankan segera berkonsultasi dengan dokter atau tenaga medis mengenai langkah penanganan yang terbaik.','','','','',''],
            ['Oleh sebab itu, para orangtua diharapkan memahami tanda bahaya tersebut sekaligus tahu cara mengatasinya.','2. Kejang','','','','',''],
            ['Dia menyampaikan, sedikitnya ada 9 tanda bahaya pada bayi baru lahir yang perlu dikenali. Apa saja?','dr. Andy menyampaikan, kejang pada bayi baru lahir bisa saja terjadi. “Ketika mendapati kondisi ini, orangtua perlu mencari tahu pemicu kejang pada bayi,” jelas dia saat diwawancara Kompas.com, Senin (13/7/2020). Jika kejang bayi dipicu oleh demam, maka penting bagi para orangtua untuk memberikan obat penurun panas yang sesuai dengan dosis anjuran dokter. Sementara, jika bayi kejang tapi tidak dalam kondisi demam, para orangtua alangkah baiknya segera berkonsultasi dengan dokter untuk membicarakan kemungkinan penyebab lain. Sebelum itu, para orangtua bisa memperhatikan terlebih dahulu frekuensi dan lamanya kejang yang terjadi pada bayi untuk dilaporkan kepada dokter','','','','',''],
            ['','3. Bayi lemah','','','','',''],
            ['','dr. Andy mewanti-wanti, jika bayi terlihat tidak seaktif biasanya, maka waspadalah bagi para orangtua. “Jangan biarkan kondisi ini berlanjut,” jelas dia. Kondisi lemah pada bayi bisa dipicu oleh beragam penyebab, seperti diare, muntah yang berlebihan, ataupun infeksi berat. Untuk mengatasi masalah lemah pada bayi baru lahir ini, para orangtua perlu mengobati penyakit atau kondisi yang menjadi penyebab.','','','','',''],
            ['','4. Sesak nafas','','','','',''],
            ['','dr. Andy menerangkan, frekuensi napas pada bayi pada umumnya lebih cepat daripada orang dewasa, yakni sekitar 40-60 kali per menit. Jika bayi bernapas kurang dari 40 kali per menit atau lebih dari 60 kali per menit, maka para orangtua wajib waspada. “Lihat dinding dadanya, ada tarikan atau tidak. Jika ditemukan masalah, lebih baik segera berkonsultasi dengan dokter,” ujar dr. Andy.','','','','',''],
            ['','5. Merintih','','','','',''],
            ['','Bayi belum bisa mengungkapkan apa yang mereka rasakan. Maka dari itu, ketika mendapati bayi merintih terus-menerus meski sudah diberi ASI atau sudah ditimang-timang, para orangtua lebih baik segera menghubungi dokter. “Bisa jadi ada ketidaknyamanan lain yang dirasakan bayi,” kata dia.','','','','',''],
            ['','6. Pusar kemerahan','','','','',''],
            ['','Tali pusar yang berwarna kemerahan dapat menunjukkan adanya infeksi pada bayi. Saat merawat tali pusar yang harus orangtua perhatikan adaah jaga tali pusar tetap kering dan bersih.','','','','',''],
            ['','7. Demam','','','','',''],
            ['','dr. Andy berpendapat para orangtua cukup penting untuk menyimpan termometer di rumah. Alat ini tidak lain diperlukan untuk memastikan suhu badan sang buah hati sewaktu-waktu. Bayi dapat didiagnosis mengalami demam ketika suhu tubuhnya terpantau lebih dari 37,5 derajat Celsius. Jika mendapati bayi demam, para orangtua dianjurkan sesering mungkin untuk mencegah kekurangan cairan. Selain itu, pertolongan pertama pada bayi demam, bisa juga dilakukan dengan mengganti pakaian mereka dengan baju yang tipis agar panas cepat menguap. “Orangtua juga bisa memberikan kompres hangat di dahi dan ketiak,” kata dia. Sementara itu, jika suhu tubuh bayi tidak turun dan malah mencapai suhu 38 derajat Celsius, para orangtua sebaiknya meminta bantuan dokter.','','','','',''],
            ['','8. Mata bernanah','','','','',''],
            ['','Nanah pada mata bayi baru lahir bisa menjadi tanda adanya infeksi yang berasal dari proses persalinan. Untuk mengatasi masalah ini, para orangtua bisa melakukan tindakan berupa membersihkan mata bayi dengan kapas dan air hangat. Jika nanah yang keluar dalam jumlah berlebih atau sulit diatasi, para orangtua bisa berkonsultasi dengan dokter.','','','','',''],
            ['','9. Kulit bayi kuning','','','','',''],
            ['','dr. Andy menerangkan, kuning pada bayi pada umumnya terjadi karena bayi kurang minum ASI. Tapi, jika kuning pada bayi terjadi pada waktu kurang dari 24 jam setelah lahir atau lebih dari 14 hari setelah lahir dan menjalar hingga telapak tangan dan kaki, para orangtua patut cemas. Kondisi ini bisa menjadi gejala penyakit kuning. Para orangtua perlu berkonsultasi dengan dokter jika mendapati bayi mereka memiliki gejala penyakit kuning.','','','','','']
        ],
        'redirect':'https://health.kompas.com/read/2020/07/14/150000668/kenali-9-tanda-bahaya-pada-bayi-baru-lahir?page=all',
        'artikellain':[
            ['suntiktt.jpg','suntik tt','suntiktt','Suntik TT Ibu Hamil'],
            ['tandamelahirkan.jpg','tanda melahirkan','tandamelahirkan','Tanda-Tanda Melahirkan'],
            ['kontrollahiran.jpg','kontrol lahiran','kontrollahiran','Kontrol Pasca Melahirkan'],
            ['kb.jpg','pemilihan kb','kb','Pemilihan KB'],
            ['imunisasi.jpg','imunisasi','imunisasi','Imunisasi Pada Anak']
        ]
    }
    return render (request,'dummy.html',context)

def kontrollahiran (request):
    context={
        'title':'kontrol pasca melahirkan',
        'foto':'kontrollahiran.jpg',
        'alt':'kontrol lahiran',
        'judul':'Kontrol Pasca Melahirkan',
        'i':[
            ['Setelah melahirkan dan diperbolehkan dokter atau bidan untuk pulang ke rumah, para ibu lalu disibukan dengan aktivitas mengurus bayi. Hal ini kadang membuat mereka lupa untuk melakukan kontrol.','','Pemeriksaan, tiga hari hingga 1 minggu setelah persalinan adalah pemeriksaan yang sangat penting. Dokter akan memeriksa luka bekas persalinan, termasuk menganalisis keluhan yang dialami ibu dan bisa mendeteksi lebih cepat jika terjadi depresi pasca melahirkan," ujar Dane Shipp, seorang spesialis kandungan di Pacific Coast Womens Health.','','Hal yang tak kalah penting adalah pemeriksaan pasca persalinan bisa mendeteksi jika ibu mengalami depresi dan konsultasi yang diberikan bisa mengurangi risiko tersebut," ungkap dr. Shipp.','','Pemeriksaan juga dilakukan di area perut untuk memastikan apakah rahim telah kembali ke ukuran normal dan di area sayatan jika menjalani operasi caesar. Jadi, pastikan melakukan kontrol setelah persalinan.'],
            ['Merasa kondisi tubuh sudah pulih, terutama jika menjalani persalinan normal, pemeriksaan pasca persalinan kadang dianggap tak terlalu penting. Padahal pemeriksaan tersebut bukan hanya untuk mengetahui kondisi kesehatan fisik ibu tapi juga psikologis.','','Apabila terjadi keluhan yang sangat mengganggu seperti nyeri hebat di bagian perut, pendarahan yang berlebihan, payudara bengkak hingga demam, jangan menunda untuk segera memeriksakan diri ke dokter. Agar lebih efektif, jadwalkan pemeriksaan ibu sama dengan jadwal kunjungan bayi untuk vaksin pertama kali.','','Pemeriksaan pasca persalinan yang akan dilakukan dokter antara lain tekanan darah, lalu kelenjar tiroid jika ada pembengkakan yang mungkin tidak normal. Termasuk juga pemeriksaan payudara jika mungkin ada sumbatan dan memicu mastitis.','','']
        ],
        'redirect':'https://parenting.dream.co.id/diy/para-ibu-jangan-sepelekan-pemeriksaan-pasca-persalinan-180427j.html',
        'artikellain':[
            ['tandamelahirkan.jpg','tanda melahirkan','tandamelahirkan','Tanda-Tanda Melahirkan'],
            ['bahayabayi.jpg','bahaya bayi','bahayabayi','Bahaya Pada Bayi'],
            ['kb.jpg','pemilihan kb','kb','Pemilihan KB'],
            ['imunisasi.jpg','imunisasi','imunisasi','Imunisasi Pada Anak'],
            ['gizi.jpg','gizi','gizi','Gizi Anak Usia Dini']
        ]
    }
    return render (request,'dummy.html',context)

def kb (request):
    context = {
        'title':'KB',
        'foto':'kb.jpg',
        'alt':'pemilihan kb',
        'judul':'Pemilihan KB',
        'i':[
            ['Cara memilih alat kontrasepsi yang tepat penting untuk diketahui bila Anda dan pasangan ingin menunda kehamilan. Tak hanya untuk mencegah terjadinya kehamilan, jenis alat kontrasepsi tertentu juga dapat mencegah infeksi menular seksual.','','Mencegah Kehamilan dengan Cara Alami','1. Menghitung kalender masa subur','Bagi Anda dan pasangan yang sedang ingin menunda kehamilan, berbagai pilihan alat kontrasepsi di atas bisa dipilih sesuai kenyamanan dan kebutuhan masing-masing.','','Jika masih ada pertanyaan mengenai cara memilih alat kontrasepsi atau bingung memilih alat kontrasepsi yang tepat untuk Anda dan pasangan, cobalah untuk berkonsultasi ke dokter.'],
            ['Setiap pasangan perlu memilih jenis alat kontrasepsi mana yang cocok dan aman digunakan untuk menunda kehamilan. Hal ini dikarenakan setiap alat kontrasepsi memiliki kelebihan dan kekurangannya masing-masing.','','Selain beberapa alat kontrasepsi di atas, sebagian pasangan mungkin memilih cara alami untuk mencegah kehamilan. Berikut ini adalah beberapa metode yang tergolong sebagai KB alami:','Metode perhitungan kalender ini dilakukan dengan cara mencatat masa subur setiap bulan dan menghindari hubungan seks di masa tersebut. Wanita bisa menentukan masa subur atau ovulasinya dengan cara memeriksa suhu tubuh dan melihat perubahan cairan vagina.','','',''],
            ['Oleh karena itu, penting untuk mengetahui tingkat efektivitas setiap alat kontrasepsi agar sesuai dengan kebutuhan Anda dan pasangan.','','','Kelebihan: tidak memerlukan biaya, alat, maupun obat-obatan','','',''],
            ['Berbagai Jenis Alat Kontrasepsi Beserta Kelebihan dan Kekurangannya','','','- Harus membatasi hubungan seks selama beberapa hari','','',''],
            ['Untuk mencegah kehamilan, tidak sedikit pasangan yang lebih mengandalkan penggunaan alat kontrasepsi. Berbagai jenis alat kontrasepsi yang dapat digunakan meliputi:','','','- Sering terjadi kesalahan dalam perhitungan masa subur, sehingga peluang untuk hamil tetap ada','','',''],
            ['','1. Pil KB','','- Tidak cocok untuk wanita dengan siklus haid tidak teratur','','',''],
            ['','Pil KB merupakan alat kontrasepsi yang paling umum digunakan. Alat kontrasepsi ini mengandung hormon progestin dan estrogen untuk mencegah terjadinya ovulasi. Pil KB umumnya terdiri dari 21-35 tablet yang harus dikonsumsi dalam satu siklus atau secara berkelanjutan.','','2. Menarik penis keluar sebelum ejakulasi','','',''],
            ['','Kelebihan:','','Anda dan pasangan juga dapat mencegah kehamilan dengan menarik penis keluar sebelum ejakulasi saat melakukan penetrasi.','','',''],
            ['','- Tingkat efektivitas tinggi dengan persentase kegagalan hanya sekitar 8%','','Kelebihan: sangat efektif dengan tingkat kegagalan 4%','','',''],
            ['','- Haid menjadi lancar dan kram berkurang saat haid, tetapi ada pula jenis pil KB yang dapat menghentikan haid','','Kekurangan:','','',''],
            ['','Kekurangan:','','- Sulit dilakukan bila pasangan kerap mengalami ejakulasi dini','','',''],
            ['','- Tidak dapat mencegah penyakit menular seksual','','- Tidak memberikan perlindungan terhadap penyakit menular seksual','','',''],
            ['','- Dapat menimbulkan efek samping, seperti naiknya tekanan darah, pembekuan darah, keluarnya bercak darah, dan payudara mengeras','','','','',''],
            ['','- Tidak cocok untuk wanita dengan kondisi medis tertentu, seperti penyakit jantung, gangguan hati, kanker payudara dan kanker rahim, migrain, serta tekanan darah tinggi','','','','',''],
            ['','2. Kondom pria','','','','',''],
            ['','Tak hanya pil KB, kondom pria juga umum digunakan untuk mencegah kehamilan. Kondom biasanya terbuat dari bahan lateks dan bekerja dengan cara menghalangi sperma masuk ke vagina dan mencapai sel telur.','','','','',''],
            ['','Kelebihan:','','','','',''],
            ['','- Harga terjangkau','','','','',''],
            ['','- Praktis dan mudah digunakan','','','','',''],
            ['','- Dapat mencegah dari penyakit menular seksual','','','','',''],
            ['','- Mudah diperoleh di toko atau apotek','','','','',''],
            ['','Kekurangan:','','','','',''],
            ['','- Tingkat kegagalan mencapai 15%, terutama jika penggunaan kondom kurang tepat','','','','',''],
            ['','- Hanya bisa digunakan sekali dan harus diganti setelah ejakulasi','','','','',''],
            ['','3. Suntik KB','','','','',''],
            ['','Suntik KB merupakan alat kontrasepsi yang mengandung hormon progestin dan mampu menghentikan terjadinya ovulasi. Berdasarkan periode penggunaannya, ada dua jenis suntik KB, yaitu suntik KB 3 bulan dan 1 bulan.','','','','',''],
            ['','Kelebihan:','','','','',''],
            ['','- Lebih efektif dan praktis dari pil KB','','','','',''],
            ['','- Tingkat kegagalan pada suntik KB 1 bulan bisa kurang dari 1% jika digunakan dengan benar','','','','',''],
            ['','Kekurangan:','','','','',''],
            ['','- Harga relatif mahal','','','','',''],
            ['','- Perlu kunjungan secara rutin ke dokter atau bidan setiap bulannya','','','','',''],
            ['','- Tidak memberikan perlindungan terhadap penyakit menular seksual','','','','',''],
            ['','- Dapat menyebabkan efek samping, seperti keluarnya bercak darah','','','','',''],
            ['','- Siklus menstruasi menjadi tidak teratur','','','','',''],
            ['','- Tidak dianjurkan untuk digunakan pada wanita yang memiliki riwayat penyakit migrain, diabetes, sirosis hati, stroke, dan serangan jantung','','','','',''],
            ['','4. Implan','','','','',''],
            ['','KB implan atau susuk merupakan alat kontrasepsi berukuran kecil dan berbentuk seperti batang korek api. KB implan bekerja dengan cara mengeluarkan hormon progestin secara perlahan yang berfungsi mencegah kehamilan selama 3 tahun. Alat kontrasepsi ini digunakan dengan cara dimasukkan ke bagian bawah kulit, biasanya lengan bagian atas.','','','','',''],
            ['','Kelebihan:','','','','',''],
            ['','- Sangat efektif dengan tingkat kegagalan kurang dari 1%','','','','',''],
            ['','- Tahan lama hingga 3 tahun','','','','',''],
            ['','Kekurangan:','','','','',''],
            ['','- Biaya relatif mahal','','','','',''],
            ['','- Siklus menstruasi menjadi tidak teratur','','','','',''],
            ['','- Risiko memar dan bengkak pada kulit di awal pemasangan','','','','',''],
            ['','- Tidak memberikan perlindungan terhadap penyakit menular seksual','','','','',''],
            ['','5. IUD','','','','',''],
            ['','Intrauterine device (IUD) adalah alat kontrasepsi berbahan plastik dan berbentuk menyerupai huruf T yang diletakkan di dalam rahim. IUD atau KB spiral dapat mencegah kehamilan dengan cara menghalau sperma agar tidak membuahi sel telur. Ada dua jenis IUD yang umum digunakan, yaitu IUD yang terbuat dari tembaga dan dapat bertahan hingga 10 tahun serta IUD yang mengandung hormon yang perlu diganti setiap 5 tahun sekali.','','','','',''],
            ['','Kelebihan:','','','','',''],
            ['','- Tidak memerlukan perawatan yang rumit','','','','',''],
            ['','- Tahan lama','','','','',''],
            ['','Kekurangan:','','','','',''],
            ['','- IUD dari tembaga dapat menyebabkan haid tidak lancar','','','','',''],
            ['','- Risiko bergeser dan keluar dari tempatnya','','','','',''],
            ['','- Risiko efek samping, seperti munculnya bercak darah pada 3-6 bulan pertama pemakaian','','','','',''],
            ['','- Biaya mahal','','','','',''],
            ['','6. Kondom wanita','','','','',''],
            ['','Kondom wanita berbentuk plastik yang berfungsi untuk menyelubungi vagina. Terdapat cincin plastik di ujung kondom, sehingga posisinya mudah disesuaikan. Kondom wanita tidak dapat digunakan bersamaan dengan kondom pria.','','','','',''],
            ['','Kelebihan:','','','','',''],
            ['','- Memberikan perlindungan dari penyakit menular seksual','','','','',''],
            ['','- Menjaga suhu tubuh lebih baik daripada kondom pria','','','','',''],
            ['','Kekurangan:','','','','',''],
            ['','- Kurang efektif daripada kondom pria','','','','',''],
            ['','- Muncul bunyi yang mengganggu saat digunakan','','','','',''],
            ['','- Hanya sekali pakai','','','','',''],
            ['','- Tingkat kegagalan mencapai 21%','','','','',''],
            ['','7. Spermisida','','','','',''],
            ['','Spermisida adalah produk kontrasepsi yang digunakan di dalam vagina sebelum berhubungan seksual. Produk ini berbentuk jeli, krim, membran, atau busa yang mengandung bahan kimia untuk membunuh sperma.','','','','',''],
            ['','Kelebihan:','','','','',''],
            ['','- Harga terjangkau','','','','',''],
            ['','- Mudah digunakan','','','','',''],
            ['','Kekurangan:','','','','',''],
            ['','- Beberapa jenis spermisida perlu diaplikasikan 30 menit sebelum berhubungan seksual','','','','',''],
            ['','- Risiko terjadi iritasi pada organ intim bila terlalu sering digunakan','','','','',''],
            ['','- Penggunaannya perlu disertai dengan alat kontrasepsi lain, misalnya kondom','','','','',''],
            ['','- Tingkat kegagalan mencapai 29%','','','','',''],
            ['','8. Diafragma','','','','',''],
            ['','Diafragma merupakan alat kontrasepsi yang terbuat dari karet berbentuk kubah. Alat kontrasepsi ini ditempatkan di mulut rahim sebelum berhubungan seksual dan umumnya digunakan bersama dengan spermisida.','','','','',''],
            ['','Kelebihan: harganya terjangkau','','','','',''],
            ['','Kekurangan:','','','','',''],
            ['','- Tidak memberikan perlindungan terhadap penyakit menular seksual','','','','',''],
            ['','- Tingkat kegagalan mencapai 16%, terutama jika tidak dikenakan dengan tepat','','','','',''],
            ['','- Pemasangan harus dilakukan dokter','','','','',''],
            ['','- Harus dilepas saat haid','','','','',''],
            ['','9. Cervical cap','','','','',''],
            ['','Cervical cap berbentuk seperti diafragma, tetapi memiliki ukuran lebih kecil. Alat kontrasepsi ini umumnya digunakan bersama dengan spermisida dan berfungsi untuk menutup jalan sperma masuk ke rahim.','','','','',''],
            ['','Kelebihan:','','','','',''],
            ['','- Harga terjangkau','','','','',''],
            ['','- Bisa digunakan hingga 2X','','','','',''],
            ['','Kekurangan:','','','','',''],
            ['','- Tingkat kegagalan mencapai 30% pada wanita yang sudah memiliki anak dan 15 persen bagi yang belum memiliki anak','','','','',''],
            ['','- Pemasangan perlu dilakukan oleh dokter','','','','',''],
            ['','- Harus dilepas saat haid','','','','',''],
            ['','- Tidak memberikan perlindungan terhadap penyakit menular seksual','','','','',''],
            ['','10. Koyo ortho evra','','','','',''],
            ['','Koyo ortho evra digunakan dengan cara ditempelkan pada kulit dan diganti setiap seminggu sekali selama 3 minggu. Cara kerja koyo ini adalah dengan melepaskan hormon yang sama efektifnya dengan yang terdapat dalam pil KB.','','','','',''],
            ['','Kelebihan:','','','','',''],
            ['','- Tidak perlu repot mengingat untuk mengonsumsi pil','','','','',''],
            ['','- Haid menjadi lebih lancar dan mengurangi kram saat haid','','','','',''],
            ['','Kekurangan:','','','','',''],
            ['','- Harga relatif mahal','','','','',''],
            ['','- Tidak memberikan perlindungan terhadap penyakit menular seksual','','','','',''],
            ['','- Bisa menyebabkan efek samping yang serupa dengan efek samping pil KB','','','','',''],
            ['','11. Cincin vagina','','','','',''],
            ['','Cincin vagina atau NuvaRing merupakan cincin plastik yang ditempatkan di dalam vagina. NuvaRing bekerja dengan cara melepaskan hormon yang sama seperti pil KB.','','','','',''],
            ['','Kelebihan:','','','','',''],
            ['','- Hanya perlu diganti sebulan sekali','','','','',''],
            ['','- Siklus menstruasi menjadi lebih lancar','','','','',''],
            ['','Kekurangan:','','','','',''],
            ['','- Harga relatif mahal','','','','',''],
            ['','- Dapat menyebabkan iritasi dan efek samping yang mirip pil KB dan koyo','','','','',''],
            ['','- Tidak memberikan perlindungan terhadap penyakit menular seksual','','','','',''],
            ['','12. KB permanen','','','','',''],
            ['','Jika Anda dan pasangan sudah yakin untuk tidak ingin memiliki anak kembali, KB permanen atau KB steril bisa menjadi pilihan. Metode kontrasepsi ini memiliki efektivitas yang tinggi atau hampir 100 persen efektif untuk mencegahkehamilan. Jenis KB permanen untuk masing-masing orang berbeda, tergantung jenis kelaminnya. Pada pria, KB permanen dilakukan dengan vasektomi, sedangkan pada wanita bisa dengan tubektomi atau proses pengikatan tuba falopi.','','','','','']
        ],
        'redirect':'https://www.alodokter.com/memilih-alat-kontrasepsi',
        'artikellain':[
            ['bahayabayi.jpg','bahaya bayi','bahayabayi','Bahaya Pada Bayi'],
            ['kontrollahiran.jpg','kontrol lahiran','kontrollahiran','Kontrol Pasca Melahirkan'],
            ['imunisasi.jpg','imunisasi','imunisasi','Imunisasi Pada Anak'],
            ['gizi.jpg','gizi','gizi','Gizi Anak Usia Dini'],
            ['promil.jpg','promil','promil','Persiapan Kehamilan']
        ]
    }
    return render (request,'dummy.html',context)

def imunisasi (request):
    context = {
        'title':'imunisasi',
        'foto':'imunisasi.jpg',
        'alt':'imunisasi',
        'judul':'Imunisasi Pada Anak',
        'i':[
            ['Berdasarkan data dari Ikatan Dokter Anak Indonesia (IDAI), imunisasi mampu mencegah 2 - 3 juta kematian anak setiap tahun. Pemberian imunisasi pada anak sangat penting untuk kelangsungan hidupnya. Simak jadwal imunisasi bayi dan anak berdasarkan anjuran IDAI.','- Bayi baru lahir (usia kurang dari 24 jam): imunisasi hepatitis B (HB-1)','Mengutip dari Sari Pediatri, jadwal imunisasi dibuat sesuai dengan ketersediaan vaksin kombinasi, seperti:','- Hepatitis B','Jadwal imunisasi bayi usia 6 - 12 bulan','- Pneumokokus (PCV)','Agenda imunisasi anak usia 2 - 18 tahun. Pemberian imunisasi lanjutan pada anak usia dua tahun bersifat pengulangan atau booster. Berikut jadwal dan daftar imunisasi pada remaja.'],
            ['Jadwal imunisasi bayi dan anak menurut IDAI','- Usia 0 - 1 bulan: Polio 0 dan BCG','- DPT-HiB-HB (difteri, pertusis, haemofilus influenza, hepatitis)','Bila melihat dari tabel jadwal imunisasi bayi dari IDAI, anak mendapatkan imunisasi hepatitis B (HB) pertama yaitu monovalent saat bayi usia 1 bulan. Bayi menerima imunisasi Hepatitis B sebanyak 4 kali sebelum usia 6 bulan. Pemberian vaksin ini jaraknya satu bulan, yaitu ketika bayi baru lahir, bayi usia 2, 3, 4 bulan. Anda bisa memberikan imunisasi HB bersamaan dengan DPT.','Menginjak usia 6 bulan, rangkaian imunisasi untuk mencegah penyakit pada anak masih berlangsung. Berikut daftarnya.','Ini adalah vaksin untuk mencegah penyakit yang disebabkan oleh infeksi bakteri Streptococcus pneumoniae atau kuman pneumokokus. Penyakit yang disebabkan bakteri ini adalah radang paru (pneumonia), radang selaput otak (meningitis), dan infeksi darah (bakteremia). Jadwal imunisasi PCV dimulai sejak bayi usia 2 bulan dan diberikan 3 kali dengan interval 4 - 8 minggu (usia bayi 2, 4, 6 bulan). Berbeda dengan imunisasi lain yang menimbulkan efek samping ringan seperti demam, imunisasi PCV tidak menimbulkan efek samping pada bayi. Idealnya pemberian imunisasi pada si kecil ketika kondisi bayi dalam keadaan sehat dan tidak sedang sakit ringan (batuk, pilek, atau demam).','- Tifoid. Imunisasi ini bekerja untuk mencegah infeksi bakteri salmonella typhii yang menjadi penyebab penyakit tipes. Kapan anak mendapatkan vaksin tifoid? Pemberian ulang imunisasi tifoid setiap tiga tahun sekali pada anak 2 tahun. Hal yang perlu diperhatikan yaitu imunisasi tifoid mampu melindungi anak dari tipes hanya 50 - 80%. Inilah yang membuat orangtua tetap perlu memilih makanan yang sehat untuk anak agar terhindari dari penyakit tifus.'],
            ['Menurut Ikatan Dokter Anak Indonesia (IDAI) dalam situs resminya, vaksin adalah alat atau produk yang menghasilkan kekebalan terhadap penyakit tertentu. Pemberian imunisasi secara teratur dapat berdampak positif pada anak.','- Usia 2 bulan: DP-HiB 1, polio 1, hepatitis 2, rotavirus, PCV','- DPTa-HB-HiB-IPV (difteri, pertusisis, tetanus, hepatitis, haemofilus influenza, dan polio)','- Polio','- Rotavirus','Pemberian imunisasi rotavirus bertujuan untuk mencegah penyakit peradangan pada saluran pencernaan. Infeksi rotavirus menyebabkan diare pada bayi dan anak-anak dan bisa muncul setelah dua hari terpapar virus ini. Rotavirus bisa menyebabkan diare sampai membuat tubuh dehidrasi karena kekurangan cairan. Ada dua jenis imunisasi rotavirus dengan jadwal pemberian yang berbeda setiap usia bayi. Pertama imunisasi rotavirus monovalen yang diberikan 2 kali, saat bayi usia 6 - 14 minggu dan kedua diberikan dengan interval atau jeda minimal 4 minggu. Batas akhir pemberian imunisasi rotavirus yaitu saat bayi usia 24 minggu atau 6 bulan. Jenis imunisasi rotavirus kedua adalah pentavalen yang pemberiannya sebanyak 3 kali. Pertama saat bayi usia 6-14 minggu, sedangkan dosis kedua dan ketiga diberikan dengan jeda 4 - 10 minggu. Batas pemberian imunisasi rotavirus ketika bayi usia 32 minggu atau 8 bulan.','- Human papiloma virus (HPV). Infeksi virus HPV terjadi pria dan wanita pada sel kulit dan membran mukosa, salah satu yang paling sering area kelamin. Pada area kelamin, kanker bisa terjadi pada leher rahim, vulva, vagina, dan penis. Sementara untuk area non-kelamin, kanker bisa terjadi pada area mulut dan saluran pernapasan atas. Kapan waktu imunisasi HPV pada anak? Jadwal pemberian imunisasi HPV pada anak remaja usia 9-14 tahun, pemberiannya dua kali dengan jeda atau interval 6 - 12 bulan. Seseorang yang sudah aktif berhubungan seksual tidak bisa menerima imunisasi HPV. IDAI menjelaskan dalam situs resminya bahwa pemberian imunisasi HPV pada anak remaja usia 9 - 14 tahun terbukti membentuk antibodi untuk melawan infeksi ini. Pemberian imunisasi HPV belum tersedia di Puskesmas. Hal ini karena imunisasi HPV belum termasuk program imunisasi nasional. Namun, pemberian imunisasi HPV gratis pada anak perempuan kelas 5-6 sekolah dasar dan hanya berada pada beberapa sekolah.'],
            ['IDAI sudah memperbarui jadwal imunisasi pada 2020 lalu. Jadwal ini untuk memudahkan orangtua dan dokter untuk mengetahui waktu pemberian imunisasi yang tepat sesuai usia si kecil.','- Usia 3 bulan: DPT-HiB 2, polio 2, hepatitis 3','Untuk lebih jelasnya, berikut jadwal imunisasi bayi dan anak sesuai usianya mulai 0 - 18 tahun.','Masalah kesehatan yang satu ini merupakan penyakit menular yang menyerang sistem saraf pusat pada otak. Polio bisa menyebabkan lumpuh atau masyarakat mengenalnya dengan penyakit lumpuh layu. Pembagian vaksin dapat secara Oral Poliovirus Vaccine (OPV) dan suntikan Inactive Poliovirus Vaccine (IPV). Bayi mendapatkan imunisasi polio tipe OPV ketika ia baru lahir sampai usia 1 bulan. Kemudian pengulangan setiap bulan yaitu usia 2,3, dan 4 bulan. Pemberiannya bisa bersamaan dengan vaksin DPT yang tergabung dalam imunisasi pentabio. Setidaknya ada satu pemberian vaksin pada usia 2,3 dan 4 bulan melalui OPV yang dengan bersamaan OPV-3.','','- Campak, Mumps dan rubella (MMR)','- Dengue. Penyebab penyakit demam berdarah adalah gigitan nyamuk aedes aegypti yang bisa menyerang anak-anak dan orang dewasa. Imunisasi dengue berfungsi untuk cegah demam berdarah. Menurut IDAI, pemberian imunisasi dengue sesuai jadwal adalah saat ia berusia usia 9-16 tahun. Ini karena memberikan imunisasi saat usia anak lebih muda, justru meningkatkan risiko terkena infeksi dengue.'],
            ['Berdasarkan anjuran IDAI terbaru, berikut daftar imunisasi dasar lengkap bayi usia 0 - 9 bulan.','- Usia 4 bulan: DPT-HiB 3, Polio 3 (IPV atau polio suntik), hepatitis 4, dan rotavirus 2','Jadwal imunisasi bayi 0 - 6 bulan','- BCG','','Berdasarkan jadwal imunisasi terbaru dari IDAI, anak usia 9 bulan sudah bisa menerima vaksin MMR. Ini adalah vaksin untuk mencegah penyakit campak (measles), gondongan (mumps), dan rubella (campak jerman). Kemudian, saat anak usia 18 bulan, menerima imunisasi MMR ulang (booster) untuk meningkatkan efektivitas vaksin. Penyebab campak dan rubella adalah virus yang infeksi menular melalui saluran napas. Anak yang menerima imunisasi MMR tidak akan merasakan efek samping parah, seperti anak yang tidak mendapatkan vaksin.',''],
            ['','- Usia 6 bulan: PCV 3, influenza 1, rotavirus 3 (pentavalen)','Jadwal imunisasi untuk bayi usia 6 bulan termasuk ke dalam imunisasi wajib. Beberapa daftar imunisasi wajib untuk anak yaitu:','Imunisasi BCG berfungsi untuk mencegah penyakit tuberkulosis atau TBC. Penyakit ini sangat berbahaya dan menyerang saluran pernapasan, bahkan bisa menyebar ke bagian tubuh lain. Jadwal imunisasi BCG hanya satu kali, ketika bayi berusia 3 bulan, tetapi lebih efektif dan optimal bila bayi mendapatkannya saat usia 2 bulan.','','Jadwal imunisasi bayi usia 12 - 24 bulan. Anak Anda sudah masuk usia satu tahun? Anak tidak akan menerima imunisasi sebanyak sebelumnya. Namun, ada beberapa imunisasi yang tidak boleh anak lewatkan untuk mencegah penyakit, berikut daftar dan jadwalnya.',''],
            ['','- umur 9 bulan: Campak atau MR','','- Difteri, pertusis, dan tetanus (DPT)','','- Varisela',''],
            ['','','','Pemberian vaksinasi ini bertujuan untuk mencegah tiga penyakit sekaligus dalam satu suntikan, yaitu difteri, pertusis (batuk rejan), dan tetanus. Ketiganya merupakan penyakit yang sangat parah dan bisa menyebabkan kematian anak. Jadwal imunisasi DPT pertama kali diberikan pada bayi usia dua bulan dengan interval atau jeda satu bulan sehingga pemberiannya saat bayi usia 2, 3, 4 bulan. WHO mengembangkan imunisasi kombinasi yaitu pentavalen dan pentabio. Imunisasi pentavalen merupakan gabungan dari imunisasi DPT, HiB, (haemophilus influenza tipe B), dan hepatitis B (HB). Sementara itu untuk imunisasi bernama pentabio, gabungan dari imunisasi DPT, Hepatitis (HB), dan polio.','','Cacar air bisa dicegah dengan imunisasi varisela yang diberikan sesuai jadwal, yaitu satu kali setelah anak usia 1 tahun. Namun, akan lebih optimal bila si kecil menerima imunisasi varisela sebelum masuk sekolah dasar. Orang dewasa yang belum pernah kena cacar juga harus menerima imunisasi varisela. Hanya saja, pemberian imunisasi varisela hanya bisa menurunkan tingkat keparahan gejala penyakit cacar air. Alasannya, bila si kecil tidak mendapat imunisasi sama sekali, risiko terkena komplikasi cacar air akan lebih tinggi.',''],
            ['','','','- Influenza','','- Japanese encephalitis (JE)',''],
            ['','','','Pemberian imunisasi influenza bisa dimulai ketika bayi berusia 6 bulan dan bisa diberikan kapan saja, tidak perlu sesuai jadwal. Sebaiknya anak menerima imunisasi influenza setiap satu tahun sekali. Imunisasi influenza tidak termasuk dalam kelompok imunisasi wajib, tetapi anak tetap permu mendapatkannya untuk mengurangi tingkat keparahan penyakit flu.','','Nyamuk menularkan penyakit infeksi virus Japanese Encepalitis (JE). Penyakit ini awalnya ditemukan di Jepang pada 1871 dengan sebutan summer encephalitis. Gejalanya tidak spesifik dan menyerupai flu dan biasanya muncul setelah 4 - 14 hari dari gigitan nyamuk. Mengutip dari IDAI, Japanese encephalitis (JE) bisa menyebabkan kematian. Kasus JE setiap tahunnya mencapai 67 ribu kasus dengan angka kematian 20 - 30%. Tidak hanya itu, 30 - 50% kasusnya mengakibatkan gejala gangguan saraf. Anak-anak berusia kurang dari 10 tahun sering mengalami hal ini. Oleh karenanya, pemberian imunisasi JE yang sesuai jadwal sangat penting pada bayi dan anak. Jadwal imunisasi japanese encephalitis (JE) yaitu dimulai saat anak mulai usia 12 bulan dan diulang atau booster 1-2 tahun berikutnya. Imunisasi Japanese encephalitis (JE) biasanya diberikan pada daerah endemis atau turis yang akan berpergian ke daerah tersebut. Ada pula negaranya yaitu Jepang, China, Taiwan, Korea, dan Thailand. Program imunisasi JE di negara tersebut efektif mencegah dan menurunkan angka pengidap penyakit ini.',''],
            ['','','','','','- Hepatitis A',''],
            ['','','','','','Imunisasi hepatitis A diberikan untuk mencegah infeksi virus dengan nama yang sama, melalui makanan dan feses penderita. Pemberiannya pada anak 2 tahun disebabkan karena mereka rentan terserang penyakit tersebut. Anak menerima imunisasi hepatitis A sebanyak dua kali dengan interval atau jeda 6 - 12 bulan setelah suntikan pertama. Sementara untuk orang dewasa, perlu melakukan pengulangan imunisasi hepatitis A setiap 10 tahun sekali. Daya tahan imunisasi ini akan bekerja 15 hari setelah penyuntikan dan bertahan selama 20 - 50 tahun.',''],
            ['','','','','','- Rangkaian imunisasi booster',''],
            ['','','','','','Saat anak Anda masuk usia 12 bulan, selama satu tahun sampai ia berusia 24 bulan (2 tahun) akan mendapatkan imunisasi ulangan atau booster. Ini untuk meningkatkan efektivitas dan kinerja imunisasi karena anak sudah mendapatkan vaksin sebelumnya. Jadwal imunisasi PCV booster diberikan saat anak berusia 12-15 bulan. Sementara itu, imunisasi HiB booster didapatkan anak ketika berusia 15 - 18 bulan. Pada usia 18 bulan, anak Anda akan mendapatkan imunisasi DPT dan polio booster.','']
        ],
        'redirect':'https://hellosehat.com/parenting/kesehatan-anak/imunisasi/jadwal-imunisasi-bayi-anak/',
        'artikellain':[
            ['kontrollahiran.jpg','kontrol lahiran','kontrollahiran','Kontrol Pasca Melahirkan'],
            ['kb.jpg','pemilihan kb','kb','Pemilihan KB'],
            ['gizi.jpg','gizi','gizi','Gizi Anak Usia Dini'],
            ['promil.jpg','promil','promil','Persiapan Kehamilan'],
            ['periksahamil.jpg','periksa hamil','periksahamil','Pemeriksaan Kehamilan']
        ]
    }
    return render (request,'dummy.html',context)

def gizi (request):
    context = {
        'title':'gizi anak',
        'foto':'gizi.jpg',
        'alt':'gizi anak',
        'judul':'Gizi Anak',
        'i':[
            ['Gizi seimbang untuk anak usia dini sangat diperlukan agar dapat mengoptimalkan tumbuh kembang anak dan menjaga kesehatan tubuh. Namun ternyata gizi seimbang bukan hanya dari makanan saja, tetapi juga dari pola hidup sehat lainnya, seperti rajin berolahraga dan membiasakan berperilaku bersih.','1. Mengonsumsi Makanan Sehat','Pengaruh Gizi Seimbang Terhadap Kecerdasan Anak','','','',''],
            ['4 Prinsip Pilar Gizi Seimbang untuk Anak Usia Dini','Berikan makanan yang bergizi pada anak setiap harinya untuk memenuhi nutrisi tubuh. Setiap harinya makanan dan minuman yang dikonsumsi oleh anak harus mempunyai gizi yang seimbang. Gizi seimbang dalam makanan yaitu terdiri dari karbohidrat, lemak, vitamin, mineral, serat, dan sebagainya. Setiap makan, dalam piring si Kecil disarankan tersedia makanan pokok sumber karbohidrat (nasi atau kentang), lauk-pauk untuk sumber protein (ikan, daging ayam, tahu, tempe, kacang-kacangan), sayur-mayur untuk sumber mineral dan serat (bayam, wortel, kol, brokoli, dsb.), dan buah-buahan untuk sumber vitamin (jeruk, apel, pisang, dll.).','Dalam sebuah penelitian yang dilakukan di Amerika Serikat, asupan gizi seimbang untuk anak usia dini dapat membantu meningkatkan volume otak, mendukung kemampuan berpikir, dan meningkatkan potensi akademik ketika di sekolah. Dengan begitu, proses tumbuh kembang anak akan berjalan secara optimal.','','','',''],
            ['Melansir dari akun Instagram Kemendikbud, ada 4 prinsip pilar gizi seimbang untuk anak usia dini yang harus diterapkan oleh orang tua. Prinsip pilar gizi seimbang ini harus dibiasakan dalam kehidupan sehari-hari terutama saat musim banyak penyakit. Berikut ini keempat prinsip pilar gizi seimbang tersebut.','2. Perilaku Hidup Bersih dan Sehat (PHBS)','Selain kecerdasan otak, gizi seimbang pun akan berpengaruh baik terhadap perkembangan emosional anak. Contohnya jika anak kekurangan vitamin B dan D, zat besi, zink, magnesium, dan omega 3 bisa membuat suasana hati kurang bahagia.','','','',''],
            ['','Anak-anak harus diajarkan sejak dini untuk berperilaku hidup bersih dan sehat dalam kehidupan sehari-hari. Contoh PHBS yaitu menutup mulut dan hidung saat bersin dan batuk, mencuci tangan dengan sabun dan air bersih, membersihkan tempat tinggal, tidak makan makanan yang sudah jatuh, dan sebagainya. Selain itu, pakaikan alas kaki ketika anak akan bermain di luar rumah untuk mencegah dari penyakit cacingan. Dengan perilaku hidup bersih dan sehat akan membuat anak lebih kecil kemungkinan untuk terserang penyakit yang disebabkan kumat dan bakteri.','Sedangkan, jika kelebihan nutrisi misalnya karbohidrat dapat membuat kadar gula darah dalam tubuh naik turun sehingga membuat anak mudah lelah dan kurang semangat untuk belajar. Emosional anak yang terganggu dapat berpengaruh juga terhadap proses tumbuh kembangnya.','','','',''],
            ['','3. Melakukan Aktivitas Fisik','Gizi seimbang untuk anak usia dini mempunyai banyak manfaat untuk kecerdasan, kesehatan, dan emosional anak. Oleh karena itu, orang tua harus memenuhi asupan nutrisinya dengan seimbang dan mengajak anak untuk melakukan kegiatan prinsip gizi seimbang lainnya.','','','',''],
            ['','Saat ini, banyak anak usia dini yang jarang melakukan aktivitas fisik karena hanya berdiam diri menonton hiburan yang ada di gadget/hp. Padahal, aktivitas fisik sangat penting dalam menyempurnakan gizi seimbang untuk anak usia dini. Aktivitas fisik akan membuat tubuh sehat dan menjadi kesempatan untuk anak melakukan eksplorasi. Aktivitas fisik yang bisa dilakukan oleh anak usia dini yaitu olahraga ringan, bermain, dan belajar melakukan pekerjaan rumah, seperti menyapu, menyiram tanaman, dan sebagainya. Aktivitas fisik ini bisa dilakukan bersama-sama dengan orang tua agar hubungan orang tua dan anak semakin erat.','','','','',''],
            ['','4. Menimbang Berat Badan','','','','',''],
            ['','Memiliki berat badan ideal sangat dianjurkan untuk semua kalangan, termasuk anak-anak. Setelah rutin memberikan makanan yang bernutrisi, melakukan aktivitas fisik dan berperilaku sehat, maka selanjutnya untuk rutin menimbang berat badan anak. Berat badan yang gemuk berpotensi menimbulkan berbagai penyakit, sedangkan berat badan yang terlalu ringan pada anak bisa karena cacingan atau penyakit lainnya. Jika rutin menimbang berat badan dan pada saat tertentu anak mengalami perubahan berat badan yang drastis, maka kemungkinan ada yang salah pada tubuhnya. Berat badan yang ideal adalah berat badan yang serasi dengan tinggi badan. Terdapat rumus khusus untuk menghitung berat badan ideal seseorang berdasarkan tinggi badannya, lalu rumus untuk mengetahui apakah berat badan saat ini termasuk obesitas, ideal, atau kekurangan gizi.','','','','',''],
        ],
        'redirect':'http://yd.blog.um.ac.id/apa-saja-gizi-seimbang-untuk-anak-usia-dini/',
        'artikellain':[
            ['kb.jpg','pemilihan kb','kb','Pemilihan KB'],
            ['imunisasi.jpg','imunisasi','imunisasi','Imunisasi Pada Anak'],
            ['promil.jpg','promil','promil','Persiapan Kehamilan'],
            ['periksahamil.jpg','periksa hamil','periksahamil','Pemeriksaan Kehamilan'],
            ['suntiktt.jpg','suntik tt','suntiktt','Suntik TT Ibu Hamil']
        ]
    }
    return render (request,'dummy.html',context)

def promil (request):
    context = {
        'title':'promil',
        'foto':'promil.jpg',
        'alt':'promil',
        'judul':'Persiapan Kehamilan',
        'i':[
            ['Apakah Anda dan pasangan sedang merencanakan kehamilan? Penting dicatat bahwa ada beberapa persiapan kehamilan yang perlu diketahui sebelum menjalani promil atau program hamil. Berikut penjelasan lengkap mengenai persiapan kehamilan yang perlu diperhatikan!','1. Apakah Anda benar-benar sudah siap memiliki anak?','Kapan sebaiknya merencanakan kehamilan?','1. Hentikan penggunaan kontrasepsi','Hal yang dihindari saat persiapan kehamilan','1. Menghindari asap rokok',''],
            ['Mengapa perlu melakukan persiapan kehamilan?','Tanyakan hal ini kepada Anda dan pasangan dari hati nurani yang paling dalam. Bukan karena tuntutan orang tua atau tren di lingkungan pertemanan Anda. Ini bukan hanya keputusan sesaat yang bisa Anda batalkan keesokan hari. Namun, keputusan seumur hidup tentang sebuah jiwa yang akan bergantung kepada Anda. Mungkin sulit untuk mengukur kesiapan ini. Namun paling tidak, Anda dan pasangan sudah satu suara untuk memiliki anak diiringi dengan kesiapan mental serta finansial.','Dibutuhkan periode prakonsepsi (sebelum proses kehamilan) atau tiga bulan untuk melakukan persiapan. Namun idealnya, rencana kehamilan dibuat 6 bulan sebelum Anda hamil. Baik itu kelahiran bayi pertama, kedua, ketiga, atau lebih. Pasalnya mempersiapkan tubuh adalah prioritas agar Anda memiliki kehamilan yang sehat. Akan tetapi, apabila Anda sudah mencoba untuk hamil tetapi belum juga berhasil setelah satu tahun pernikahan, periksakan diri Anda dan pasangan ke dokter.','Apapun metode kontrasepsi yang digunakan, Anda harus menghentikannya sebagai salah satu persiapan kehamilan atau perencanaan kehamilan. Bagi sebagian besar wanita, kesuburan mungkin langsung kembali setelah berhenti menggunakan alat kontrasepsi. Namun, untuk alat KB yang mengandung hormon, tubuh membutuhkan waktu lebih lama untuk bisa hamil kembali. Oleh karena itu, sebaiknya lepas alat kontrasepsi Anda satu tahun sebelumnya agar tubuh memiliki waktu untuk membersihkan diri dari pengaruh hormon alat kontrasepsi.','Tidak hanya masalah kesuburan, ada beberapa faktor lainnya yang bisa membuat keberhasilan promil jadi tertunda. Berikut beberapa hal yang sebaiknya dihindari ketika Anda melakukan persiapan kehamilan atau cara membuat anak, yaitu:','Apabila Anda atau pasangan merokok, sebaiknya berhenti dan jauhi orang terdekat yang merokok. Merokok atau menghirup asap rokok sebelum hamil dapat mengganggu proses persiapan kehamilan. Hal ini karena kandungan di dalam rokok dapat memengaruhi kesehatan rahim. Selain itu, asap rokok yang menempel pada tubuh juga bisa memengaruhi produksi sperma di dalam tubuh. Setidaknya, Anda memerlukan waktu hingga 3 bulan untuk mendetoksifikasi racun akibat rokok di dalam tubuh. Merokok saat hamil juga berisiko untuk mengalami kehamilan ektopik, keguguran, bayi lahir prematur, dan memiliki bayi dengan berat rendah.',''],
            ['Sebagian besar pasangan yang sudah menikah pasti mendambakan adanya buah hati dan mempertanyakan bagaimana cara membuat anak yang tepat. Apalagi, memang tidak semua orang bisa mengalami datangnya kehamilan dengan cepat. Maka dari itu, penting untuk merencanakan kehamilan terlebih dahulu agar kehamilan terjadi sesuai yang diharapkan. Dikutip dari Pregnancy Birth & Baby, persiapan kehamilan tidak bisa dilakukan sembarangan. Apabila direncanakan dengan baik, kehamilan Anda bisa terhindar dari masalah yang mungkin muncul termasuk risiko cacat lahir. Maka dari itu, Anda perlu berkonsultasi mengenai perencanaan kehamilan dengan orang yang tepat seperti dokter kandungan. Bagaimana dengan bidan? Kedua tenaga kesehatan ini memiliki kompetensi dan keahlian yang cukup berbeda. Wewenang dan kompetensi bidan yang tidak sama dengan dokter kandungan untuk merencanakan kehamilan. Biasanya, bidan hanya mampu melakukan sebatas konsultasi maupun pemeriksaan dasar di awal saja. Namun, untuk pemeriksaan kesehatan yang lebih mendalam dilakukan oleh dokter spesialis kandungan. Hal ini seperti pemberian obat, pemeriksaan USG, maupun tindakan lanjutan lainnya.','2. Ingin menjadi orang tua seperti apa?','Persiapan program hamil yang bisa dilakukan','2. Mengetahui masa subur','','2. Menghindari alkohol',''],
            ['Hal lain yang dipertimbangkan dalam persiapan kehamilan','Apakah Anda akan menjadi orangtua yang keras untuk menggapai keberhasilan? Atau Anda ingin menjadi orangtua yang santai? Ini hal yang harus dipertimbangkan sebelum persiapan dan perencanaan kehamilan. Bicarakan peran apa yang ingin Anda pilih saat menjadi orangtua dan buat beberapa perjanjian dengan pasangan.','Seperti yang telah disebutkan sebelumnya, dalam persiapan kehamilan, sebaiknya konsultasi terlebih dahulu ke dokter kandungan. Nantinya, hasil diskusi tersebut akan menjadi panduan promil atau cara membuat anak yang tepat karena kondisi setiap orang berbeda-beda. Diskusikan pula mengenai berbagai kondisi yang pernah atau sedang Anda alami dalam merencakan kehamilan dengan bantuan dokter. Berikut beberapa perencanaan kehamilan yang mungkin akan direkomendasikan dokter sebagai cara agar cepat hamil, seperti:','Masa subur merupakan proses ketika sel telur sudah siap untuk dibuahi setiap bulannya. Maka dari itu, Anda perlu mengetahui cara menghitung masa subur yang tepat untuk memperbesar kesempatan terjadinya pembuahan. Namun, apabila dalam jangka waktu tertentu belum ada pembuahan, Anda dan pasangan sebaiknya melakukan tes kesuburan. Apabila Anda mempunyai masalah dengan kesuburan, dibutuhkan perawatan khusus agar mempersiapkan kehamilan berhasil.','','Selain rokok, Anda juga harus menjauhi minuman yang mengandung alkohol. Minum alkohol saat persiapan dan perencanaan kehamilan juga dapat membuat Anda lebih sulit untuk hamil. Tidak ada yang tahu batasan konsumsi alkohol yang aman saat kehamilan. Namun, minuman beralkohol dapat meningkatkan risiko Anda untuk mengalami keguguran.',''],
            ['Sebelum melakukan promil serta mengetahui lebih banyak cara agar cepat hamil, Anda dan pasangan harus siap dengan tanggung jawab yang lebih besar. Memiliki anak tidak hanya memikirkan nutrisi atau perawatannya saja. Jangan lupa bahwa Anda juga bertanggung jawab untuk mendidiknya. Berikut hal yang harus dipertimbangkan dalam merencanakan kehamilan:','3. Apakah siap secara finansial?','','3. Melakukan tes medis ','','3. Hindari stres',''],
            ['','Siap secara finansial adalah hal lain yang harus dipertimbangkan sebelum mempersiapkan kehamilan. Perlu diketahui bahwa membesarkan anak membutuhkan biaya yang tidak sedikit. Pasalnya, beberapa aspek penting yang sebaiknya dipikirkan yaitu perihal kesehatan hingga pendidikan. Oleh karena itu, matang secara finansial juga menjadi aspek yang sebaiknya menjadi pertimbangan dalam merencanakan kehamilan.','','Beberapa penelitian menunjukkan bahwa perawatan pra-kehamilan dapat meningkatkan peluang program hamil dan menurunkan peluang keguguran atau komplikasi persalinan. Dokter akan menjalankan beberapa tes yang bertujuan untuk memastikan apakah Anda dan pasangan tidak memiliki penyakit tersembunyi yang belum diketahui. Berikut beberapa tes yang mungkin akan disarankan dokter, seperti:','','Selama mempersiapkan kehamilan, Anda harus memastikan bahwa tidak ada hal yang mengganggu pikiran. Bahkan, hal ini juga harus Anda terapkan saat hamil maupun setelahnya. Pasalnya, jika selama persiapan kehamilan Anda membiarkan berbagai hal menghantui pikiran, hal ini dapat berujung pada stres. Stres saat sedang persiapan membuat anak dapat menjadi salah satu penyebab Anda sulit hamil. Tak hanya itu, stres yang dirasakan selama kehamilan juga dapat mengganggu kesehatan. Maka dari itu, saat merencanakan kehamilan, lakukan hal-hal yang dapat membuat Anda senang dan tenang. Sebaiknya hindari stres yang bisa Anda dapatkan dari lingkungan keluarga, pertemanan, atau tempat kerja.',''],
            ['','','','- Tes darah untuk melihat apakah ada penyakit keturunan.','','4. Berat badan kurang atau terlalu kurus',''],
            ['','','','- Melakukan tes penyakit menular seksual.','','Ternyata, jumlah lemak tubuh memengaruhi kesuburan Anda. Lemak dibutuhkan dalam produksi hormon estrogen sehingga terjadinya menstruasi. Jika terlalu sedikit hormon estrogen dalam tubuh, maka siklus menstruasi dan ovulasi dapat berkurang sehingga lebih sulit hamil. Saat akan melakukan persiapan kehamilan, Anda memerlukan lemak tubuh minimal sebesar 22%. Hal ini dapat membantu berovulasi dan memiliki siklus menstruasi yang normal. Jika berat badan kurang dan memiliki siklus menstruasi yang tidak teratur sebaiknya periksakan ke dokter agar masalah dapat segera diatasi. Namun, apabila hanya butuh menambah berat badan beberapa kilogram, sebaiknya lakukan secara bertahap dengan cara makan makanan yang bergizi seimbang.',''],
            ['','','','- Pemeriksaan pap smear untuk area serviks.','','',''],
            ['','','','- Melakukan tes untuk menilai kualitas sperma sehat atau tidak.','','',''],
            ['','','','4. Mengonsumi vitamin kesuburan','','',''],
            ['','','','Mengonsumsi vitamin untuk promil juga bisa membantu Anda dalam persiapan kehamilan. Hal ini dibutuhkan saat Anda tidak dapat memenuhi kebutuhan zat gizi tertentu. Asupan vitamin B atau asam folat sebelum hamil penting diperhatikan dalam merencanakan kehamilan. Tidak hanya obat penyubur kandungan yang diresepkan oleh dokter, ada pula obat tradisional atau obat herbal untuk kesuburan. Namun, konsultasikan terlebih dahulu dengan dokter untuk memastikan asupan suplemen atau vitamin yang dikonsumsi aman dan sesuai dengan kebutuhan Anda.','','',''],
            ['','','','5. Berhubungan intim di waktu yang tepat','','',''],
            ['','','','Salah satu cara program hamil yang satu ini juga dapat memperbesar peluang kehamilan. Hal yang perlu dilakukan oleh Anda dan pasangan adalah berhubungan intim secara teratur. Cobalah untuk berhubungan intim 2 sampai 3 kali selama masa subur.','','',''],
            ['','','','6. Menjaga berat badan ideal','','',''],
            ['','','','Memiliki berat badan normal dalam masa program hamil dapat menambah peluang keberhasilan hamil. Pasalnya, kelebihan berat badan dapat menurunkan tingkat kesuburan sehingga akan lebih sulit untuk hamil. Selain itu, hal ini juga menurunkan risiko komplikasi saat hamil seperti tekanan darah tinggi dan diabetes gestasional. Jika berat badan Anda kurang saat masih dalam masa persiapan kehamilan, yang harus dilakukan adalah menaikkan berat badan.','','',''],
            ['','','','7. Memerhatikan nutrisi saat program hamil','','',''],
            ['','','','Dalam persiapan kehamilan, salah satu hal yang harus menjadi perhatian Anda adalah nutrisi sebelum hamil. Sebaiknya, perbaiki pola makan Anda saat sedang merencanakan kehamilan. Cobalah dimulai dengan mengonsumsi makanan untuk penyubur kandungan yang sehat dan seimbang. Hal ini dilakukan demi memenuhi kebutuhan gizi selama program hamil.','','',''],
            ['','','','8. Berolahraga atau aktivitas fisik','','',''],
            ['','','','Tidak hanya mampu menjaga berat badan tetap ideal, berolahraga atau melakukan aktivitas fisik juga dapat menambah kekuatan Anda. Hal ini membuat Anda lebih siap menjalani promil, kehamilan, sampai proses persalinan nanti. Maka dari itu, tidak ada salahnya untuk rutin berolahraga selama program hamil. Biasakan dengan olahraga ringan seperti berjalan, berenang, yoga untuk program hamil, dan lain-lain.','','',''],
            ['','','','9. Melengkapi vaksin','','',''],
            ['','','','Saat merencanakan kehamilan, tidak ada salahnya untuk segera melengkapi vaksin yang diperlukan sebelum hamil. Hal ini dianjurkan untuk melindungi Anda dan calon bayi dari berbagai penyakit. Berbagai penyakit menular bisa saja mengenai Anda selama kehamilan, sehingga Anda perlu meningkatkan kekebalan tubuh.','','',''],
        ],
        'redirect':'https://hellosehat.com/kehamilan/kesuburan/program-hamil/posisi-seks-terbaik-peluang-hamil/',
        'artikellain':[
            ['imunisasi.jpg','imunisasi','imunisasi','Imunisasi Pada Anak'],
            ['gizi.jpg','gizi','gizi','Gizi Anak Usia Dini'],
            ['periksahamil.jpg','periksa hamil','periksahamil','Pemeriksaan Kehamilan'],
            ['suntiktt.jpg','suntik tt','suntiktt','Suntik TT Ibu Hamil'],
            ['tandamelahirkan.jpg','tanda lahiran','tandamelahirkan','Tanda-Tanda Melahirkan']
        ]
    }
    return render (request,'dummy.html',context)