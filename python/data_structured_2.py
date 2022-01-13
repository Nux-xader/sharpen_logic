# fungsi untuk mengubah teks ke bentuk struktur data dictionary
def parsing_text(text):
	# memisahkan teks per baris dan di ubah ke dalam bentuk data list
	data = [x for x in text.split("\n") if len(x)>7]

	# inisialisasi var clean_data untuk menyimpan data yang telah di bersihkan dari spasi ganda "  "
	clean_data = []
	for x in data:
		while x.count("  ") > 0:
			x = x.replace("  ", " ")
		# menambahkan data ke dalam var clean_data
		clean_data.append(x)

	# inisialisasi var result
	result_total_buku = dict()
	result_total_pinjam = dict()

	# memproses data agar menjadi data dictionary dengan memisahkan data berdasarkan spasi
	for x in clean_data:
		x = x.split(" ")

		# mendefinisikan data sesuai format dan urutan
		key = x[0]
		total = int(x[1])
		total_pinjam = sum([int(y) for y in x[2:]])

		# menyimpan data dalam bentuk dictionary
		result_total_buku[key] = total
		result_total_pinjam[key] = total_pinjam

	# kembalikan data yang telah selesai di proses
	return result_total_buku, result_total_pinjam


# fungsi untuk mencari buku dengan total pinjam terbanyak menggunakan function max()
def favorit(data_buku):
	dipinjam_terbanyak = max(list(data_buku.values()))
	nama_buku = [k for k, v in data_buku.items() if v == dipinjam_terbanyak]
	return nama_buku, dipinjam_terbanyak


# fungsi untuk mendapatkn data laporan stok buku
def laporan_stok(data_total, data_buku):
	# inisialisasi var result yang di gunakan untuk menyimpan hasil
	result = ""

	# melooping semua nama buku untuk di cari sisa buku yang masih belum di pinjam
	for book in list(data_total.keys()):
		sisa = data_total[book]-data_buku[book]
		if sisa < 1:
			sisa = "Telah habis"
		else:
			sisa = f"Tersisa {sisa} buku"

		result+=f"Buku dengan ISBN {book} {sisa}\n"

	# mengembalikan result.
	return result

# main program yang memanggil seluruh fungsi
def main():
	# inisialisasi nama file yang akan di baca
	file_path = "teks.txt"
	# membaca sekaligus mengubah teks ke dalam bentuk dictionary menggunakan fungsi parsing_text
	data_total, data_buku = parsing_text(str(open(file_path, "r").read()))
	

	# menampilkan buku yang paling banyak di pinjam dalam seminggu
	fav_books, total = favorit(data_buku)
	print("Buku yang paling banyak di pinjam dalam seminggu :")
	for fav_book in fav_books:
		print(f"Buku dengan ISBN {fav_book} di pinjam sebanyak {total} buku")


	# menampilkan laporan stok buku yang masih tersisa
	print("\nLaporan stok buku : ")
	print(laporan_stok(data_total, data_buku))


if __name__ == '__main__':
	main()