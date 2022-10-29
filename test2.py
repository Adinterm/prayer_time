from tkinter import*                            #GUI
from tkinter import ttk                         #Tkinter Theme
from tkinter.font import Font                   #Tkinter Font
from tkinter.filedialog import asksaveasfile    #tool to save file
from tkinter import scrolledtext, Scrollbar     #scrolled bar
from tkcalendar import Calendar, DateEntry      #Display Calandar
from bidi.algorithm import get_display          #Unicode Arabic
from datetime import date                       #import date now
from time import strftime                       #jam
import calendar, datetime                       #kalender
import arabic_reshaper                          #Arabic reshaper
import pandas as pd                             #Read dataset
import numpy as np                              #List jadwal
import math                                     #Math
import sys                                      #to get path file
import os                                       #to get path file

waktu_a = u"مواقيت الصلاة"
tanggal_a = u"التاريخ"
subuh_a = u"الصبح"
terbit_a = u"الشروق"
dzuhur_a = u"الظهر "
ashar_a = u"العصر"
maghrib_a = u"المغرب"
isya_a = u"العشاء "

class Frames:

	def __init__(self, main):
		'''Initialization window'''
		self.main = main
		self.init_Frames()
		
	def init_Frames(self):
		'''Combine all methods in single window'''
		self.tabControl = ttk.Notebook(self.main)
		self.fontstyle = Font(family='Times New Roman', size=12)
		self.fontstyle2 = Font(family='Times New Roman', size=11)
		self.fontstyle2nd = ('Times New Roman', 11, 'bold')
		self.fontstyle3th = ('Times New Roman', 12, 'bold')
		self.fontstyle3 = ('Times New Roman', 14, 'bold')
		self.fontstyle4 = ('Times New Roman', 25, 'bold')
		self.color0 = 'white'
		self.color1 = '#fffff'
		self.color2 = '#dbdbdb'
		self.color3 = '#adadad'
		self.color4 = 'black'
		self.waktu = get_display(arabic_reshaper.reshape(waktu_a))
		self.tanggal = get_display(arabic_reshaper.reshape(tanggal_a))
		self.subuh = get_display(arabic_reshaper.reshape(subuh_a))
		self.terbit = get_display(arabic_reshaper.reshape(terbit_a))
		self.dzuhur = get_display(arabic_reshaper.reshape(dzuhur_a))
		self.ashar = get_display(arabic_reshaper.reshape(ashar_a))
		self.maghrib = get_display(arabic_reshaper.reshape(maghrib_a))
		self.isya = get_display(arabic_reshaper.reshape(isya_a))
		self.sizex = 895
		self.sizey = 535
		self.tab1 = ttk.Frame(self.tabControl)
		self.tab2 = ttk.Frame(self.tabControl)
		self.tabControl.pack(expand=1,fill="both")
		self.make_frame()
		self.frame_1()
		self.frame_2()
		self.frame_3()
		self.convert_button()
		self.convert_button2()
		self.convert_button3()
		self.save_as()

		'''Membuat properties frame'''
	def make_frame(self):
		'''Membuat Tabs'''
		self.tabControl.add(self.tab1, text="Set Location")
		self.tabControl.add(self.tab2, text="Monthly Prayer Time")
		'''Membuat Frames'''
		self.frame1 = Frame(self.tab1, height=self.sizey, width=self.sizex*2/3, bg=self.color2, borderwidth=1, relief=GROOVE)
		self.frame2 = Frame(self.tab1, height=self.sizey, width=self.sizex*1/3, bg=self.color2, borderwidth=1, relief=GROOVE)
		self.frame3 = Frame(self.tab2, height=self.sizey, width=self.sizex-8, bg=self.color0, borderwidth=1, relief=GROOVE)
		'''Show Background Image'''
		bg0 = PhotoImage(file = os.path.dirname(os.getcwd())+'/Prayer_time/Data/frame2.png')
		self.bg0 = bg0
		bg1 = PhotoImage(file = os.path.dirname(os.getcwd())+'/Prayer_time/Data/Untitled.png')
		self.bg = bg1
		self.frame1.place(x=5, y=10)
		self.frame2.place(x=590, y=10)
		self.frame3.place(x=5, y=10)

	def dataset(self):
		'''Memuat dataset untuk waktu sholat'''
		dataset = pd.read_csv(os.path.dirname(os.getcwd())+'/Prayer_time/Data/dataset.csv', sep=';')
		negara = dataset.Country
		'''duplicate rows removed'''
		negara = negara.drop_duplicates()
		return negara, dataset

	def frame_1(self): 
		'''Frame - 1'''
		'''Kalender'''
		self.kalender = Calendar(self.frame1,background="#3f3f3f", disabledbackground="#3f3f3f", bordercolor="#3f3f3f", headersbackground="#3f3f3f", normalbackground="#3f3f3f", foreground='white', normalforeground='white', headersforeground='white', font=self.fontstyle2, selectmode='day', cursor='hand1')
		self.kalender.place(x=340, y=10)
		self.kalender.config(background = "#3f3f3f")
		selected_date=None
		'''Properties input'''
		title = Label(self.frame1, text="Input Location and Date", font=(self.fontstyle), fg='black', bg=self.color2)
		title.place(x=65, y=5)
		'''style'''
		style = ttk.Style()
		style.theme_use('default')

		lbl_negara = Label(self.frame1, text='Country 	    : ', font=self.fontstyle, bg='white')
		tanggal = Label(self.frame1, text='Date 	    : ', font=self.fontstyle, bg='white')
		lbl_kota = Label(self.frame1, text='City    	    :', font=self.fontstyle, bg='white')
		self.lbl_tanggalVar = StringVar()
		self.lbl_tanggal = Label(self.frame1, text=self.kalender.selection_get(), font=self.fontstyle, width=25, justify='center')

		input_hijr = Label(self.frame1, text='Input Date : ', font=self.fontstyle)
		input_hijr.place(x=5, y=250)

		input_JD = Label(self.frame1, text='Input JD    : ', font=self.fontstyle)
		input_JD.place(x=5, y=330)

		'''Entry input from Hijri'''
		self.from_Hijr = ttk.Entry(self.frame1, width=20)
		self.from_Hijr.place(x=110, y=250)

		'''Entry input from JD'''
		self.from_JD = ttk.Entry(self.frame1, width=20)
		self.from_JD.place(x=110, y=330)

		#Combobox Negara dan Kota
		style.map('TCombobox', fieldbackground=[('readonly', 'white')])
		style.map('TCombobox', background=[('readonly', 'white')])
		style.map('TCombobox', foreground=[('readonly', 'black')])
		cmb_negaraVar = StringVar()
		self.cmb_negara = ttk.Combobox(self.frame1, textvariable='cmb_negaraVar', font=self.fontstyle, width=25, justify='center')	
		cmb_kotaVar = StringVar()
		self.cmb_kota = ttk.Combobox(self.frame1, textvariable='cmb_kotaVar', font=self.fontstyle, width=25, justify='center')
		
		negara, dataset = self.dataset()
		value_negara = ['Select Country']
		for country in negara:
			value_negara.append(country)
		
		self.cmb_negara['values'] = value_negara
		self.cmb_negara['state'] = 'readonly'
		self.cmb_negara.current(0)

		#Place
		lbl_negara.place(x=5, y=32)
		tanggal.place(x=5, y=100)
		self.cmb_negara.place(x=100, y=32)
		self.lbl_tanggal.place(x=100, y=100)
		lbl_kota.place(x=5, y=68)
		self.cmb_kota.place(x=100, y=65)

	def frame_2(self):
		'''Frame - 2'''
		label1 = Label(self.frame2, image = self.bg0)
		label1.place(x = 0, y = 0)
		#Mengammbil tanggal hari ini
		hari_ini = datetime.datetime.now()
		hari = hari_ini.weekday()
		nama_hari = calendar.day_name[hari]

		harii = '{}, {} {} {}'.format(nama_hari, hari_ini.day, hari_ini.strftime('%B'), hari_ini.year)

		def time():
			'''Konfigurasi lbl_jam denga format H:M:S'''
			string = strftime('%H:%M:%S')
			lbl_jam.config(text = string)
			lbl_jam.after(1000, time)

		lbl_jadwal = Label(self.frame2, text=self.waktu, font=self.fontstyle4, bg='#3f3f3f', fg='white')
		lbl_jadwal.place(x=58, y=25)

		x_size2 = 210
		y_size2 = 140


		index = [self.subuh, self.terbit, self.dzuhur, self.ashar, self.maghrib, self.isya  ]
		for i in range(0, len(index)):
			lbl_label = Label(self.frame2, text=index[i], font=self.fontstyle3, bg=self.color0, fg='black')
			lbl_label.place(x=x_size2, y=y_size2)
			y_size2 = y_size2+40


	def take_city_value(self):
		'''Mengambil value dari Combobox berupa negara dan kota'''

		negara, dataset = self.dataset()
		negara_pilih = self.cmb_negara.current()

		def callback(eventObject):
			'''Event handling, jika terjadi event pada combobox Negara, akan menambilkan
				daftar kota paa combobox Kota'''

			pilihan_negara = eventObject.widget.get()
			print(eventObject.widget.get()) #Negara yang dipilih User
			negara_mask = dataset["Country"].values == pilihan_negara
			kota = dataset["City"].loc[negara_mask]

			self.value_kota = []
			for city in kota:
				self.value_kota.append(city)

			self.cmb_kota['values'] = self.value_kota
			self.cmb_kota['state'] = 'readonly'
			self.cmb_kota.current(0)
		
		#Bind callback ke combobox
		self.cmb_negara.bind("<<ComboboxSelected>>", callback)

		kota_cmb = self.cmb_kota.get()
		negara_cmb = self.cmb_negara.get()
		print(kota_cmb) #Kota yang dipilih User
		nama_kota = dataset.loc[dataset['City'] == kota_cmb]
		
		return nama_kota, kota_cmb, negara_cmb

	def hitung_waktu_shalat(self):
		'''Menghitung waktu sholat dengan menggunakan module Waktu Sholat'''
		
		nama_kota, kota_cmb, negara_cmb = self.take_city_value()
		
		#Untuk pertama kali, nilai lintang dll harus ada nilainya,
		#sehingga perlu diinisialisasi
		try:
			lintang = float(nama_kota.Latitude.values[0])
			bujur = float(nama_kota.Longitude.values[0])
			ketinggian = nama_kota.Elevation.values[0]
			zona_waktu = nama_kota.Time_zone.values[0]
		except IndexError:	
			lintang =  0
			bujur = 0
			ketinggian = 50
			zona_waktu = 0

		''' input tahun, bulan, tanggal '''	

		tahun = self.kalender.selection_get().year
		bulan = self.kalender.selection_get().month
		tanggal = self.kalender.selection_get().day

		#Menambahkan tanda + pada zona waktu tertentu
		if int(zona_waktu) > 0:
			get_time_zone = '+'+str(zona_waktu)
		else:
			get_time_zone = str(zona_waktu)

		nama_bulanDict = {1:'Jan.', 2:'Feb.', 3:'Mar.', 4:'Apr.', 5:'May.', 6:'Jun.', 7:'Jul.', 8:'Aug.', 9:'Sep.', 10:'Oct.', 11:'Nov.', 12:'Dec.'}
		no_bulan = list(nama_bulanDict.keys())
		nama_bulan = list(nama_bulanDict.values())
		jumlah_hari = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

		sign_lat = 'N'
		if lintang < 0:
			sign_lat = 'S'

		sign_lng = 'E'
		if bujur < 0:
			sign_lng = 'W'
#keterangan
		lbl_desc0 = Label(self.frame2, text='Description :', font=('Times New Roman', 11, 'bold'), bg=self.color2, fg='black')
		lbl_desc1 = Label(self.frame2, text=("{}, {}").format(kota_cmb,negara_cmb), font=('Times New Roman', 11), bg=self.color2, fg='black')
		lbl_desc2 = Label(self.frame2, text=("Longitude :{}\N{DEGREE SIGN} {}  - Latitude : {}\N{DEGREE SIGN} {}").format(abs(lintang), sign_lat, abs(bujur), sign_lng), font=('Times New Roman', 11), bg=self.color2, fg='black')
		lbl_desc3 = Label(self.frame2, text=("Time Zone : GMT {}").format(get_time_zone), font=('Times New Roman', 11, 'bold'), bg=self.color2, fg='black')
		lbl_desc0.place(x=15, y=420)
		lbl_desc1.place(x=15, y=453)
		lbl_desc2.place(x=15, y=473)
		lbl_desc3.place(x=15, y=493)

		#Jika user menyimpan file
		self.file_to_save1 = "\t\t\t\t\t\tJADWAL SHALAT BULANAN {}, {} - BULAN {} TAHUN {}\n".format(kota_cmb, negara_cmb, bulan, tahun)
		self.file_to_save2 = "\t\t\t\t\t\t\tLintang : {}\N{DEGREE SIGN} {}, Bujur : {}\N{DEGREE SIGN} {}, GMT : {}\n\n\n".format(abs(lintang), sign_lat, abs(bujur), sign_lng, get_time_zone)

		def isLeap(tahun):
			'''Menentukan apakah tahun kabisat atau tidak'''

			kabisat = 28
			if tahun % 4 == 0:
				if tahun % 100 == 0:
					if tahun % 400 == 0:
						kabisat = 29
					else:
						kabisat = 28
				else:
					kabisat = 29
			else:
				kabisat = 28
			return kabisat

		if bulan == 2:
			jumlah_hari[1] = isLeap(tahun)

		month = []
		date = 0
		for i in range(0, len(no_bulan)+1):
			if bulan == no_bulan[i-1]:
				month.append(nama_bulan[i-1])
			if i == bulan:
				date = (jumlah_hari[i-1])
		
		#List kosong jadwal sholat	
		subuh_list = []
		terbit_list = []
		zuhur_list = []
		ashar_list = []
		maghrib_list = []
		isya_list = []

		for day in range(1, int(date)+1):


			try:
				jadwal_shalat = WaktuSholat(tahun, bulan, day, lintang, bujur, zona_waktu, ketinggian)
				subuh, terbit, zuhur, ashar, maghrib, isya = jadwal_shalat.show_result()
				subuh_list.append(subuh)
				terbit_list.append(terbit)
				zuhur_list.append(zuhur)
				ashar_list.append(ashar)
				maghrib_list.append(maghrib)
				isya_list.append(isya)

			except ValueError:
				try:
					jadwal_shalat = Lintang(tahun, bulan, day, lintang, bujur, zona_waktu, ketinggian)
					subuh, terbit, zuhur, ashar, maghrib, isya = jadwal_shalat.result()
					subuh_list.append(subuh)
					terbit_list.append(terbit)
					zuhur_list.append(zuhur)
					ashar_list.append(ashar)
					maghrib_list.append(maghrib)
					isya_list.append(isya)
				except IndexError:
					continue
				continue

		self.lbl_date = Label(self.frame2, text='{} {} {}'.format(tanggal, month[0], tahun), width=10, font=self.fontstyle3, bg=self.color2, justify="center", fg='black')
		self.lbl_date.place(x=370, y=35)

		return date, month, subuh_list, terbit_list, zuhur_list, ashar_list, maghrib_list, isya_list

	def convert_button(self):
		'''Membuat button / tombol konversi'''

		style = ttk.Style()
		style.configure('TButton', font=self.fontstyle2, bg=self.color2, width=10)
		btn_convert = ttk.Button(self.frame1, text='Calc Prayer Time', style='TButton', width=20, command=self.take_value)
		btn_convert.place(x=60, y=160)

	def convert_button2(self):
		style = ttk.Style()
		style.configure('TButton', font=self.fontstyle2, bg=self.color2, width=10)
		btn_convert = ttk.Button(self.frame1, text='Calc from Hijriyah', style='TButton', width=20, command=self.take_value)
		btn_convert.place(x=360, y=250)

	def convert_button3(self):

		style = ttk.Style()
		style.configure('TButton', font=self.fontstyle2, bg=self.color2, width=10)
		btn_convert = ttk.Button(self.frame1, text='Calc from JD', style='TButton', width=20) #,command=self.take_value3)
		btn_convert.place(x=360, y=330)


	def take_value(self):

		date = self.kalender.selection_get()
		self.lbl_tanggal.configure(text=date)

		'''Perintah mengambil nilai'''

		date, month, subuh, terbit, zuhur, ashar, maghrib, isya = self.hitung_waktu_shalat()
		tanggal = self.kalender.selection_get().day

		self.scr_jadwal.delete(1.0, END)
		x_tanggal = 3
		x_subuh = x_tanggal+135
		x_terbit = x_subuh+135
		x_zuhur = x_subuh+135
		x_ashar = x_zuhur+135
		x_maghrib = x_ashar+135
		x_isya = x_maghrib+135
		y_size = 30

		for i in range(0, date):
#			if i >= 2:
			if i+1 < 10:
				self.scr_jadwal.state = NORMAL
				self.scr_jadwal.insert(END, '  0{} {}           \t{}         \t{}           \t{}          \t {}           \t  {}        \t  {}\n'.format(i+1, str(month[0]), subuh[i], terbit[i], zuhur[i], ashar[i], maghrib[i], isya[i]))
				self.scr_jadwal.state = DISABLED

			else:
				self.scr_jadwal.state = NORMAL
				self.scr_jadwal.insert(END, '  {} {}           \t{}         \t{}           \t{}          \t {}           \t  {}        \t  {}\n'.format(i+1, str(month[0]), subuh[i], terbit[i], zuhur[i], ashar[i], maghrib[i], isya[i]))
				self.scr_jadwal.state = DISABLED


			if tanggal == i+1:
				lbl_subuh = Label(self.frame2, text=subuh[i], font=self.fontstyle3, bg=self.color0, fg='black')
				lbl_terbit = Label(self.frame2, text=terbit[i], font=self.fontstyle3, bg=self.color0, fg='black')
				lbl_zuhur = Label(self.frame2, text=zuhur[i], font=self.fontstyle3, bg=self.color0, fg='black')
				lbl_ashar = Label(self.frame2, text=ashar[i], font=self.fontstyle3, bg=self.color0, fg='black')
				lbl_maghrib = Label(self.frame2, text=maghrib[i], font=self.fontstyle3, bg=self.color0, fg='black')
				lbl_isya = Label(self.frame2, text=isya[i], font=self.fontstyle3, bg=self.color0, fg='black')
				xp = 35
				
				lbl_subuh.place(x=xp, y=140)
				lbl_terbit.place(x=xp, y=180)
				lbl_zuhur.place(x=xp, y=220)
				lbl_ashar.place(x=xp, y=260)
				lbl_maghrib.place(x=xp, y=300)
				lbl_isya.place(x=xp, y=340)


	def frame_3(self):
		'''Frame - 3'''
		label1 = Label(self.frame3, image = self.bg)
		label1.place(x = 0, y = 0)
		
		tahun = self.kalender.selection_get().year
		bulan = self.kalender.selection_get().month
		tanggal = self.kalender.selection_get().day

		date, month, subuh, terbit, zuhur, ashar, maghrib, isya = self.hitung_waktu_shalat()
	

		indexx = [self.tanggal, self.subuh, self.terbit, self.dzuhur, self.ashar, self.maghrib,self.isya]
		x_size = 20
		y_size = 3
		
		for i in range(0, len(indexx)):
			lbl_tanggal = Label(self.frame3, text=indexx[i], font=self.fontstyle3th, bg='#ffffff')
			lbl_tanggal.place(x=x_size, y=y_size)
			x_size = x_size + 105

		self.scr_jadwal = scrolledtext.ScrolledText(self.frame3, width=90, height=24, bg=self.color2, font=self.fontstyle3th)

		self.scr_jadwal.place(x=10, y=30)


	def save_as(self):
		menu = Button(self.frame3, text="Save as '.txt'",command=self.save_file)
		menu.place(x=750,y=500)


	def save_file(self):
		'''Command untuk menyimpan file dalam format .txt'''

		files = [('Text Document', '*.txt')]
		file = asksaveasfile(mode='w', filetypes=files, defaultextension=files)

		if file is None:  #Jika user menekan cancel
			return

		file_to_save3 = "  TANGGAL           \tSUBUH         \t\tTERBIT          \tDZUHUR        \t\t ASHAR           \t  MAGHRIB        \t  ISYA'\n"
		file_to_save4 = "------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
		file.write(self.file_to_save1)
		file.write(self.file_to_save2)
		file.write(file_to_save4)
		file.write(file_to_save3)
		file.write(file_to_save4)
		file.write(self.scr_jadwal.get("1.0", 'end'))
		file.close()


#################################################################################################################
###############################################  Borderline  ####################################################
#################################################################################################################

class WaktuSholat:
	'''
	ketinggian = ketinggian tempat (default: 25 meter)
	jam = jam (default : 12 UT) 
	'''

	def __init__(self, tahun, bulan, tanggal, lintang, bujur, zona_waktu, ketinggian = 25, jam = 12):
		self.tahun = tahun
		self.bulan = bulan 
		self.tanggal = tanggal
		self.lintang = lintang
		self.bujur = bujur
		self.zona_waktu = zona_waktu
		self.jam = jam
		self.ketinggian = ketinggian

	def sudut_tanggal(self):
		'''Menghitung Nilai T'''

		julian_day = Masehi_Ke_JD(self.tahun, self.bulan, self.tanggal)
		JD = (julian_day.konversi_ke_JD() + self.jam/24) - self.zona_waktu/24
		T = 2*np.pi*(JD - 2451545)/365.25
		return T, JD

	def deklinasi_matahari(self):
		'''Menghitung deklinasi mataharu (delta)'''

		T, JD = self.sudut_tanggal()
		delta = (0.37877 + 23.264*np.sin(np.deg2rad(57.297*T - 79.547)) + 
				 0.3812*np.sin(np.deg2rad(2*57.297*T - 82.682)) + 
				 0.17132 * np.sin(np.deg2rad(3*57.927 * T - 59.722)))
		return delta

	def equation_of_time(self):
		'''Menghitung Equation of Time (ET)'''
		
		T, JD = self.sudut_tanggal()
		U = (JD - 2451545)/36525
		L0 = 280.46607 + 36000.7698*U
		ET = (-(1789+237*U)*np.sin(np.deg2rad(L0)) - 
			 (7146-62*U)*np.cos(np.deg2rad(L0)) + 
			 (9934-14*U)*np.sin(np.deg2rad(2*L0)) - 
			 (29+5*U)*np.cos(np.deg2rad(2*L0)) + 
			 (74+10*U)*np.sin(np.deg2rad(3*L0)) + 
			 (320 - 4*U)*np.cos(np.deg2rad(3*L0)) - 
			 212*np.sin(np.deg2rad(4*L0)))/1000
		return ET

	def waktu_transit(self):
		'''Menghitung waktu transit matahari'''
		
		ET = self.equation_of_time()
		transit = 12 + self.zona_waktu - self.bujur/15 - ET/60
		return transit

	def hour_angle(self, altitude, delta):
		'''Menentukan Hour Angle (HA)'''
		
		hour_angle = (np.sin(np.deg2rad(altitude)) - 
					 np.sin(np.deg2rad(self.lintang)) * 
					 np.sin(np.deg2rad(delta))) / (np.cos(np.deg2rad(self.lintang)) *
					 np.cos(np.deg2rad(delta)))

		HA = np.arccos(hour_angle)
		# print(hour_angle)
		# if hour_angle < -1:
		# 	hour_angle = -1
		# elif hour_angle > 1:
		# 	hour_angle = 1
		# HA = np.arccos(hour_angle)
		return np.degrees(HA)

	def zuhur(self):
		'''Menentukan waktu shalat Zuhur'''
		
		transit = self.waktu_transit()
		zuhur = transit + 2/60
		return zuhur

	def ashar(self):
		'''Menentukan waktu shalat Azhar'''
		
		transit = self.waktu_transit()
		delta = self.deklinasi_matahari()
		KA = 1
		altitude_1 = np.tan(np.deg2rad(np.abs(delta - self.lintang)))
		altitude = np.arctan(1/(KA + altitude_1 ))
		HA = self.hour_angle(np.degrees(altitude), delta)
		ashar = transit + HA/15
		return ashar

	def maghrib(self):
		'''Menentukan waktu shalat Maghrib'''
		
		transit = self.waktu_transit()
		delta = self.deklinasi_matahari()
		altitude = -0.8333 - 0.0347*np.sqrt(self.ketinggian)
		HA = self.hour_angle(altitude, delta)
		maghrib = transit + HA/15
		return maghrib

	def isya(self):
		'''Menentukan waktu shalat Isya'''
		
		transit = self.waktu_transit()
		delta = self.deklinasi_matahari()
		altitude = -18
		HA = self.hour_angle(altitude, delta)
		isya = transit + HA/15
		return isya

	def subuh(self):
		'''Menentukan waktu shalat Subuh'''
		
		transit = self.waktu_transit()
		delta = self.deklinasi_matahari()
		altitude = -20
		HA = self.hour_angle(altitude, delta)
		subuh = transit - HA/15
		return subuh

	def terbit(self):
		'''Menentukan waktu terbit matahari'''
		
		transit = self.waktu_transit()
		delta = self.deklinasi_matahari()
		altitude = -0.8333 - 0.0347*np.sqrt(self.ketinggian)
		HA = self.hour_angle(altitude, delta)
		terbit = transit - HA/15
		return terbit

	def ubah_ke_jam(self, waktu):
		'''Mengubah jam ke dalam format pukul:menit:detik'''
		
		pukul = int(waktu)
		menit = int((waktu - pukul)*60)
		detik = int((((waktu - pukul)*60) - menit )*60)

		if pukul<10:
			pukul = '0'+str(abs(pukul))
		if menit<10:
			menit = '0'+str(abs(menit))
		if detik<10:
			detik = '0'+str(abs(detik))
		hasil = '{}:{}:{}'.format(pukul, menit, detik)
		return hasil

	def show_result(self):
		'''Menampilkan hasil perhitungan berupa waktu sholat'''
		
		subuh = self.ubah_ke_jam(self.subuh())
		terbit = self.ubah_ke_jam(self.terbit())
		zuhur = self.ubah_ke_jam(self.zuhur())
		ashar = self.ubah_ke_jam(self.ashar())
		maghrib = self.ubah_ke_jam(self.maghrib())
		isya = self.ubah_ke_jam(self.isya())

		return subuh, terbit, zuhur, ashar, maghrib, isya

#################################################################################################################
###############################################  Borderline  ####################################################
#################################################################################################################


class Lintang:  

	def __init__(self, tahun, bulan, tanggal, lintang, bujur, zona_waktu, ketinggian=100):
		self.tahun = tahun
		self.bulan = bulan
		self.tanggal = tanggal
		self.lintang = lintang
		self.bujur = bujur 
		self.zona_waktu = zona_waktu
		self.ketinggian = ketinggian

		self.tahun0 = tahun
		self.bulan0 = bulan
		self.tanggal0 = tanggal

		self.tahun1 = tahun
		self.bulan1 = bulan
		self.tanggal1 = tanggal
		
	def isLeap(self):
		'''Apakah tahun kabisat???'''
		kabisat = False
		if self.tahun % 4 == 0:
			if self.tahun % 100 == 0:
				if self.tahun % 400 == 0:
					kabisat = True
				else:
					kabisat = False
			else:
				kabisat = True
		else:
			kabisat = False

		return kabisat


	def prev_available(self):
		'''Mencari waktu sholat yang ada sebelum tanggal X'''

		no_bulan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

		if self.isLeap() == True:
			jumlah_hari = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		else:
			jumlah_hari = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

		prev_available_date = []
		prev_available_month = []
		prev_available_year = []

		for i in range(1, len(no_bulan)+1):
			if self.bulan0 == i:
				banyak_hari = jumlah_hari[self.bulan0-1]
		
				if self.tanggal0 < banyak_hari:
					while self.tanggal0 > 0:
						self.tanggal0 = self.tanggal0 - 1
						# print(tanggal)
						if self.tanggal0 < 1:
							self.bulan0 = self.bulan0-1
							self.tanggal0 = jumlah_hari[self.bulan0-1]
						if self.bulan0 < 1:
							self.tahun0 = self.tahun0 - 1
							self.bulan0 = 12
						try:
							jadwal_shalat = WaktuSholat(self.tahun0, self.bulan0,self.tanggal0, self.lintang, self.bujur, self.zona_waktu, self.ketinggian)
							subuh, terbit, zuhur, ashar, maghrib, isya = jadwal_shalat.show_result()

							prev_available_date.append(self.tanggal0)
							prev_available_month.append(self.bulan0)
							prev_available_year.append(self.tahun0)
							break
						except:
							continue

		return (prev_available_year, prev_available_month, prev_available_date)


	def next_available(self):
		'''Mencari waktu sholat yang ada setelah tanggal X'''

		no_bulan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

		if self.isLeap() == True:
			jumlah_hari = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		else:
			jumlah_hari = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

		next_available_date = []
		next_available_month = []
		next_available_year = []

		for i in range(1, len(no_bulan)+1):
			if self.bulan1 == i:
				banyak_hari = jumlah_hari[self.bulan1-1]
				
				if self.tanggal1 < banyak_hari:
					
					while self.tanggal1 > 0:
						self.tanggal1 = self.tanggal1 + 1
						
						if self.tanggal1 > jumlah_hari[self.bulan1-1]:
							self.bulan1 = self.bulan1 + 1
							self.tanggal1 = jumlah_hari[self.bulan1-1]
						if self.bulan1 > 12:
							self.tahun1 = self.tahun1 + 1
							self.bulan1 = 1
						try:
							jadwal_shalat = WaktuSholat(self.tahun1, self.bulan1, self.tanggal1, self.lintang, self.bujur, self.zona_waktu, self.ketinggian)
							subuh, terbit, zuhur, ashar, maghrib, isya = jadwal_shalat.show_result()
							
							next_available_date.append(self.tanggal1)
							next_available_month.append(self.bulan1)
							next_available_year.append(self.tahun1)
							break
						except:
							continue

		return (next_available_year, next_available_month, next_available_date)

	def take_date(self, prev_tahun, prev_bulan, prev_tanggal, next_tahun, next_bulan, next_tanggal):
		'''Mengambil tanggal sebelum dan sesudah tanggal X'''

		date1 = date(prev_tahun[0], prev_bulan[0], prev_tanggal[0])
		date2 = date(next_tahun[0], next_bulan[0], next_tanggal[0])
		date_now = date(self.tahun, self.bulan, self.tanggal)
		I = date2 - date1
		C = date_now - date1

		return date1, date2, date_now, I, C

	def calculate_date(self, waktuA, waktuB):
		'''Mengecek waktu sholat tanggal A dan B dan return dalam format jam desimal'''

		def split_time(time):
			'''Mengambil jam, menit dan detik'''
			hour = int(time[0:2])
			minute = int(time[3:5])
			second = int(time[6:8])

			return hour, minute, second

		def convert_to_decimal(jam, menit, detik):
			'''Konversi jam, menit, detik ke desimal'''

			detik_des = detik/3600
			menit_des = menit/60
			jam_des = jam+menit_des+detik_des
			return jam_des

		#cari waktu sholat 
		jamB, menitB, detikB = split_time(waktuB)
		jamA, menitA, detikA = split_time(waktuA)

		jam_desB = convert_to_decimal(jamB, menitB, detikB)
		jam_desA = convert_to_decimal(jamA, menitA, detikA)

		return jam_desB, jam_desA


	def calculate_interpolate(self, A, B, I, C):
		'''Interpolasi nilai pada tanggal X'''

		time = A - (A-B)*C/I

		pukul = int(time)
		menit = int((time - pukul)*60)
		detik = int((((time - pukul)*60) - menit )*60)

		if pukul<10:
			pukul = '0'+str(pukul)
		if menit<10:
			menit = '0'+str(menit)
		if detik<10:
			detik = '0'+str(detik)
		hasil = '{}:{}:{}'.format(pukul, menit, detik)
		return hasil

	def count_time(self):
		'''Menghitung waktu sholat subuh sampai isya'''

		prev_tahun, prev_bulan, prev_tanggal = self.prev_available()
		next_tahun, next_bulan, next_tanggal = self.next_available()
		dateA, dateB, dateC, I, C = self.take_date(prev_tahun, prev_bulan, prev_tanggal, next_tahun, next_bulan, next_tanggal)

		jadwal_shalatA = WaktuSholat(dateA.year, dateA.month, dateA.day, self.lintang, self.bujur, self.zona_waktu)
		subuhA, terbitA, zuhurA, asharA, maghribA,isyaA = jadwal_shalatA.show_result()

		jadwal_shalatB = WaktuSholat(dateB.year, dateB.month, dateB.day, self.lintang, self.bujur, self.zona_waktu)
		subuhB, terbitB, zuhurB, asharB, maghribB,isyaB = jadwal_shalatB.show_result()

		timeA = [subuhA, terbitA, zuhurA, asharA, maghribA, isyaA]
		timeB = [subuhB, terbitB, zuhurB, asharB, maghribB, isyaB]
		jadwal = []

		for i in range(0, len(timeA)):
			A, B = self.calculate_date(timeA[i], timeB[i])
			hasil = self.calculate_interpolate(A, B, I, C)
			jadwal.append(hasil)

		return jadwal

	#getter
	def result(self):
		'''Menampilkan hasil interpolasi'''
		jadwal = self.count_time()
		subuh = jadwal[0]
		terbit = jadwal[1]
		zuhur = jadwal[2]
		ashar = jadwal[3]
		maghrib = jadwal[4]
		isya = jadwal[5]

		return subuh, terbit, zuhur, ashar, maghrib, isya


#################################################################################################################
###############################################  Borderline  ####################################################
#################################################################################################################


'''Gregorian,Hijriyah'''

    #format untuk nilai desimal dalam perhitungan
def Desimal(ds):  
    if ds < -0.0000001: return math.ceil(ds - 0.0000001)
    return math.floor(ds + 0.0000001)

def Gregorian_ke_Hijriyah(tahun, bulan, tanggal):
        #awal penerapan tahun gregorian di tahun 15 oktober 1582
    if ((tahun > 1582) or ((tahun == 1582) and (bulan > 10)) or ((tahun == 1582) and (bulan == 10) and (tanggal > 14))):
        jd1 = Desimal((1461 * (tahun + 4800 + Desimal((bulan - 14) / 12.0))) / 4)
        jd2 = Desimal((367 * (bulan - 2 - 12 * (Desimal((bulan - 14) / 12.0)))) / 12)
        jd3 = Desimal((3 * (Desimal((tahun + 4900 + Desimal((bulan - 14) / 12.0)) / 100))) / 4)
        jd = jd1 + jd2 - jd3 + tanggal - 32075
    else:
        jd1 = Desimal((7 * (tahun + 5001 + Desimal((bulan - 9) / 7.0))) / 4)
        jd2 = Desimal((275 * bulan) / 9.0)
        jd = 367 * tahun - jd1 + jd2 + tanggal + 1729777

    l = jd - 1948440 + 10632 
    n = Desimal((l - 1) /10631.0)
    l = l - 10631 * n + 354
    j1 = (Desimal((10985 - l) / 5316.0)) * (Desimal((50 * l) / 17719.0))
    j2 = (Desimal(l / 5670.0)) * (Desimal((43 * l) / 15238.0))
    j = j1 + j2
    l1 = (Desimal((30 - j) / 15.0)) * (Desimal((17719 * j) / 50.0))
    l2 = (Desimal(j / 16.0)) * (Desimal((15238 * j) / 43.0))
    l = l - l1 - l2 + 29
    m = Desimal((24 * l) / 709.0)
    d = l - Desimal((709 * m) / 24.0)  #jam 6 sore sudah masuk besok jika di hijriyah
    y = 30 * n + j - 30

    nama_bulan = ["Muharram","Safar","Rabiul Awal","Rabiul Akhir","Jumadil Awal","Jumadil Akhir","Rajab","Syaban","Ramadhan","Syawal","Dzulqa'dah","dzulhijah"]
    a = nama_bulan
    nb = str(a[m-1])
    return y,m,d,nb
        #print("Tanggal {}, Bulan ke {} / {}, Tahun {} Hijriyah".format(d,m,nb,y))
        #return y, m, d

def Hijriyah_ke_Gregorian( tahun, bulan, tanggal):
    jd1 = Desimal((11 * tahun + 3) / 30.0)
    jd2 = Desimal((bulan - 1) / 2.0)
    jd = jd1 + 354 * tahun + 30 * bulan - jd2 + tanggal + 1948440 - 385

    if jd > 2299160:   #5 Oktober 1582 M = JD 2299160
        l = jd + 68569
        n = Desimal((4 * l) / 146097.0)
        l = l - Desimal((146097 * n + 3) / 4.0)
        i = Desimal((4000 * (l + 1)) / 1461001.0)
        l = l - Desimal((1461 * i) / 4.0) + 31
        j = Desimal((80 * l) / 2447.0)
        d = l - Desimal((2447 * j) / 80.0)
        l = Desimal(j / 11.0)
        m = j + 2 - 12 * l
        y = 100 * (n - 49) + i + l
    else:
        j = jd + 1402
        k = Desimal((j - 1) / 1461.0)
        l = j - 1461 * k
        n = Desimal((l - 1) / 365.0) - Desimal(l / 1461.0)
        i = l - 365 * n + 30
        j = Desimal((80 * i) / 2447.0)
        d = i - Desimal((2447 * j) / 80.0)
        i = Desimal(j / 11.0)
        m = j + 2 - 12 * i
        y = 4 * k + n + i - 4716
    nama_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    a = nama_bulan
    nb = str(a[m-1])

    return y,m,d  

""" Note : waktu Hijriyah dimulai pada jam 6 sore, sehingga jika siang hari sama-sama tanggal 1, maka mulai jam 6 sore sudah tanggal 2 Hijriyah """


#Gregorian,JD

class JD_ke_Masehi:

	def __init__(self, JD):
		self.JD = JD
		self.tahun = 0
		self.bulan = 0
		self.tanggal = 0

	def hitung_variabel(self):
		JD1 = self.JD + 0.5
		Z = int(JD1)
		F = JD1 - Z

		if Z == 229916:
			A = Z
		else:
			AA = int((Z - 1867216.25)/36524.25)
			A = Z + 1 + AA - int(AA/4)

		B = A + 1524
		C = int((B - 122.1)/365.25)
		D = int(365.25*C)
		E = int((B-D)/30.6001)

		return B, C, D, E, F

	def hitung_waktu(self, waktu):
		'''Menghitung waktu berupa jam, menit dan detik'''
		jam = int(waktu*24)
		menit = int(((waktu*24) - jam)*60)
		detik = int(((((waktu*24) - jam)*60)-menit)*60)

		return int(jam), int(menit), int(detik)

	def konversi_ke_masehi(self):
		'''Mengkonversi JD ke Masehi'''


		B, C, D, E, F = self.hitung_variabel()

		self.tanggal = B - D - int(30.6001*E)

		if E == 14 or E == 15:
			self.bulan = E - 13

		elif E < 14:
			self.bulan = E - 1

		if self.bulan == 1 or self.bulan == 2:
			self.tahun = C - 4715
		elif self.bulan > 2:
			self.tahun = C-4716

		jam, menit, detik = self.hitung_waktu(F)

		hasil = self.tahun, self.bulan, self.tanggal

		return hasil


class Masehi_Ke_JD:
	'''
	KONSVERSI MASEHI KE JULIAN DAY
	Parameter:
	tahun = tahun yang ingin dikonversi
	bulan = bulan yang ingin dikonversi
	tanggal = tanggal yang ingin dikonversi
	Keluaran :
		julian_day = julian day
	'''

	def __init__(self, tahun, bulan, tanggal):
		self.tahun = tahun
		self.bulan = bulan
		self.tanggal = tanggal
		self.Gregorian = True

	def isGregorian(self):
		''' 
		Menentukan apakah tanggal yang diinput merupakan kalender Gregorian
		atau bukan (kalender Julian)
		'''

		if self.tanggal < 15:
			if self.bulan < 10:
				if self.tahun <= 1582:
					self.Gregorian == False
				else:
					self.Gregorian == True

		return self.Gregorian

	def hitung_JD(self, Y, M, D):
		'''Menghitung Julian day'''

		if self.isGregorian() == True:
			A = int(Y/100)
			B = 2 + int(A/4) - A

		elif self.isGregorian() == False:
			B = 0

		JD = 1720994.5 + int(365.25*Y) + int(30.6001*(M+1) + B + D)
		return JD

	def isLeap(self):
		kabisat = False
		if self.tahun % 4 == 0:
			if self.tahun % 100 == 0:
				if self.tahun % 400 == 0:
					kabisat = True
				else:
					kabisat = False
			else:
				kabisat = True
		else:
			kabisat = False

		return kabisat 

	def hari_dalam_bulan(self):
		tanggal = []
		if self.bulan in [4, 6, 9, 11]:
			tanggal = np.arange(1,31)
		elif self.bulan == 1:
			tanggal = np.arange(1,32)
		elif self.bulan == 2:
			if self.isLeap():
				tanggal = np.arange(1,30)
			else:
				tanggal = np.arange(1,29)
		elif self.bulan in [3, 5, 7, 8, 10, 12]:
			tanggal = np.arange(1,32)
		else:
			tanggal = [0]

		return tanggal

	def konversi_ke_JD(self):
		'''Mengkonversikan masehi ke Julian Day'''

		if self.tahun >= -4712:

			julian_day = 0

			if self.tahun == 1582 and self.bulan == 10:
				if self.tanggal in np.arange(5,15):
					julian_day = 'Tanggal tidak tersedia'
				else:
					julian_day = self.hitung_JD(self.tahun, self.bulan, self.tanggal)

			elif self.bulan <= 2:
				hari = self.hari_dalam_bulan()
				if self.tanggal in hari:
					self.bulan = self.bulan + 12
					self.tahun = self.tahun -1
					julian_day = self.hitung_JD(self.tahun, self.bulan, self.tanggal)
				else:
					julian_day = 'Tanggal tidak tersedia'

			elif self.bulan > 12:
				julian_day = 'Bulan tidak teredia'

			else:
				self.bulan = self.bulan
				self.tahun = self.tahun

				hari = self.hari_dalam_bulan()
				if self.tanggal in hari:
					julian_day = self.hitung_JD(self.tahun, self.bulan, self.tanggal)
				else:
					julian_day = 'Tanggal tidak tersedia'

		else:
			julian_day = 'Tahun tidak tersedia'

		return julian_day


#################################################################################################################
###############################################  Borderline  ####################################################
#################################################################################################################



root = Tk()
root.title(waktu_a)
Frames(root)
root.geometry('900x580')
#bg1 = PhotoImage(file = "Untitled.png")

#root.configure(bg='white')
root.resizable(0,0)
icon_photo = PhotoImage(file=os.path.dirname(os.getcwd())+'/GUI_Jadwal_Shalat/Data/icon.png')
root.iconphoto(False, icon_photo)
root.mainloop()
