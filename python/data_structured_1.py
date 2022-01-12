def get_index_house(database, sample):
	for num, i in enumerate(list(database.items())):
		if sample in i:
			return num


def get_dict(data, num_me, total_house):
	information = [x.split(" ") for x in data]
	rumah_ganjil, rumah_genap = dict(), dict()
	result_ganjil, result_genap = dict(), dict()
	me = ""

	for i in range(1, total_house+1):
		if i%2 == 0:
			rumah_genap[i] = ""
			if num_me == i: rumah_genap[i] = "me"
			me = "genap"
		else:
			rumah_ganjil[i] = ""
			if num_me == i: rumah_ganjil[i] = "me"
			me = "ganjil"


	item_ganjil, item_genap = [list(i) for i in list(rumah_ganjil.items())], [list(i) for i in list(rumah_genap.items())]
	index_me = get_index_house(rumah_ganjil if me == "ganjil" else rumah_genap, "me")

	for data in information:
		if data[2] == "seberang":
			if me == "genap":
				if data[3] == "kiri":
					item_ganjil[index_me-int(data[0])][1] = data[-1]
					index_me = index_me-int(data[0])
				else:
					item_ganjil[index_me+int(data[0])][1] = data[-1]
					index_me = index_me+int(data[0])
				me = "ganjil"

			else:
				if data[3] == "kiri":
					item_genap[index_me-int(data[0])][1] = data[-1]
					index_me = index_me-int(data[0])
				else:
					item_genap[index_me+int(data[0])][1] = data[-1]
					index_me = index_me+int(data[0])
				me = "genap"

		else:
			if me == "genap":
				if data[3] == "kiri":
					item_genap[index_me-int(data[0])][1] = data[-1]
					index_me = index_me-int(data[0])
				else:
					item_genap[index_me+int(data[0])][1] = data[-1]
					index_me = index_me+int(data[0])
				me = "genap"

			else:
				if data[3] == "kiri":
					item_ganjil[index_me-int(data[0])][1] = data[-1]
					index_me = index_me-int(data[0])
				else:
					item_ganjil[index_me+int(data[0])][1] = data[-1]
					index_me = index_me+int(data[0])
				me = "ganjil"

	for x in item_genap:
		if x[1] == "": x[1] = "tidak tahu"
		result_genap[x[0]] = x[1]

	for x in item_ganjil:
		if x[1] == "": x[1] = "tidak tahu"
		result_ganjil[x[0]] = x[1]

	return result_ganjil, result_genap


def nomor_rumah(data, name):
	for x in data:
		result = [k for k, v in x.items() if v == name]
		if len(result) > 0: break

	if len(result) == 0:
		return "tidak tahu"
	else:
		return f"Nomor rummah : {result[0]}"


def penghuni_rumah(data, num):
	result = "tidak tahu"
	for x in data:
		try:
			result = f"Nama keluarga penghuni rumah : {x[num]}"
		except:
			pass

	return result


def view_table(data):
	for x in data:
		dash = ""
		num = ""
		for y in list(x.keys()):
			dash+="-------"
			num+=f"| {y} | "
		print(dash[:-1])
		print(num[:-1])
		print(dash[:-1])


def main():
	text = """
13 27
2 rumah seberang kiri rumah anda dihuni oleh keluarga Joni
1 rumah seberang kiri rumah Joni dihuni oleh keluarga Kylie
3 rumah sebelah kanan rumah Kylie dihuni oleh keluarga Herry
"""
	data = [x for x in text.split("\n") if len(x) > 3]
	num_me, total_house = [int(x) for x in data[0].split(" ")]
	rumah_ganjil, rumah_genap = get_dict(data[1:], num_me, total_house)

	# view_table([rumah_genap, rumah_ganjil])  enable it if you want

	print("""Menu :
1. Temukan nama penghuni rumah
2. Temukan nomor rumah
0. Keluar
""")

	while True:
		choice = str(input("Pilih Menu : "))

		if choice in "1":
			while True:
				num = str(input("Masukkan nomor rumah : "))
				try:
					num = int(num)
					break
				except:
					print("Mohon inputkan angka!")

			print(penghuni_rumah([rumah_ganjil, rumah_genap], num))
			break

		elif choice == "2":
			name = str(input("Masukkan nama keluarga penghuni rumah : "))
			print(nomor_rumah([rumah_ganjil, rumah_genap], name))
			break

		elif choice == "0":
			break

		else:
			print("Mohon pilih sesuai yang tersedia pada menu!")

if __name__ == '__main__':
	main()