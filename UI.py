from tkinter import Frame, Tk, BOTH, Label, Canvas , W, Text, END
from tkinter.filedialog import Open
from tkinter.ttk import Frame, Button
from PIL import Image, ImageTk
import tensorflow.keras
# from PIL import Image, ImageOps
import cv2
import numpy as np

class Example(Frame): 
	def __init__(self, parent): 
		Frame.__init__(self, parent)
		self.parent = parent
		self.initUI()

	def initUI(self): 
		self.parent.title('BTL của nhóm')
		self.pack(fill=BOTH, expand=1)
		openFile = Button(self, text = "Ảnh Mới", command=self.onOpen)
		openFile.place(x=210, y=5)

		predict0 = Button(self, text='Our model', command=self.onOurPredict) 
		predict0.place(x=150, y=300)

		predict1 = Button(self, text='Other model', command=self.onOtherPredict1) 
		predict1.place(x=250, y=300)

	def onOpen(self): 
		my_text.delete('1.0', 'end')
		ftypes = [("Image Files", "*.jpg *.png"), ('All files', '*')]
		dlg = Open(self, filetypes = ftypes)
		fl = dlg.show()
		try: 
			if fl != '':
				self.origin = cv2.imread(fl)
				cv2.imshow('test', self.origin)
				img = self.openImage(fl)
			print(fl)
		except Exception as e:
			print(e) 

	def openImage (self, filename):
		bard = Image.open(filename)
		bard = bard.resize((256, 256))
		bardejov = ImageTk.PhotoImage(bard)
		label1 = Label(self, image = bardejov)
		label1.image = bardejov
		label1.place(x=122, y=30)

	def onOurPredict(self):
		my_text.delete('1.0', 'end')
		try: 
			if self.origin != "":
				model=tensorflow.keras.models.load_model('model/modeltest.h5')
				id_to_label = {0: 'banana', 1: 'mango', 2: 'orange', 3: 'plum'}

				check = cv2.resize(self.origin, (64, 64))
				check = cv2.cvtColor (check, cv2.COLOR_BGR2RGB)
				check = np.array(check)
				check = check[np.newaxis,:,:,:]

				prediction = model.predict(check) 
				i = "{}".format(id_to_label[np.argmax(prediction)])
				print(i)
				my_text.insert(END, i)
				
		except Exception as e:
			print('Chưa có ảnh')

	def onOtherPredict1(self):
		my_text.delete('1.0', 'end')
		try: 
			if self.origin != "":
				model=tensorflow.keras.models.load_model('kaggle/model.h5')
				id_to_label = {0: 'Apple Braeburn', 1: 'Apple Crimson Snow', 2: 'Apple Golden 1', 3: 'Apple Golden 2', 4: 'Apple Golden 3', 5: 'Apple Granny Smith', 6: 'Apple Pink Lady', 7: 'Apple Red 1', 8: 'Apple Red 2', 9: 'Apple Red 3', 10: 'Apple Red Delicious', 11: 'Apple Red Yellow 1', 12: 'Apple Red Yellow 2', 13: 'Apricot', 14: 'Avocado', 15: 'Avocado ripe', 16: 'Banana', 17: 'Banana Lady Finger', 18: 'Banana Red', 19: 'Beetroot', 20: 'Blueberry', 21: 'Cactus fruit', 22: 'Cantaloupe 1', 23: 'Cantaloupe 2', 24: 'Carambula', 25: 'Cauliflower', 26: 'Cherry 1', 27: 'Cherry 2', 28: 'Cherry Rainier', 29: 'Cherry Wax Black', 30: 'Cherry Wax Red', 31: 'Cherry Wax Yellow', 32: 'Chestnut', 33: 'Clementine', 34: 'Cocos', 35: 'Corn', 36: 'Corn Husk', 37: 'Cucumber Ripe', 38: 'Cucumber Ripe 2', 39: 'Dates', 40: 'Eggplant', 41: 'Fig', 42: 'Ginger Root', 43: 'Granadilla', 44: 'Grape Blue', 45: 'Grape Pink', 46: 'Grape White', 47: 'Grape White 2', 48: 'Grape White 3', 49: 'Grape White 4', 50: 'Grapefruit Pink', 51: 'Grapefruit White', 52: 'Guava', 53: 'Hazelnut', 54: 'Huckleberry', 55: 'Kaki', 56: 'Kiwi', 57: 'Kohlrabi', 58: 'Kumquats', 59: 'Lemon', 60: 'Lemon Meyer', 61: 'Limes', 62: 'Lychee', 63: 'Mandarine', 64: 'Mango', 65: 'Mango Red', 66: 'Mangostan', 67: 'Maracuja', 68: 'Melon Piel de Sapo', 69: 'Mulberry', 70: 'Nectarine', 71: 'Nectarine Flat', 72: 'Nut Forest', 73: 'Nut Pecan', 74: 'Onion Red', 75: 'Onion Red Peeled', 76: 'Onion White', 77: 'Orange', 78: 'Papaya', 79: 'Passion Fruit', 80: 'Peach', 81: 'Peach 2', 82: 'Peach Flat', 83: 'Pear', 84: 'Pear 2', 85: 'Pear Abate', 86: 'Pear Forelle', 87: 'Pear Kaiser', 88: 'Pear Monster', 89: 'Pear Red', 90: 'Pear Stone', 91: 'Pear Williams', 92: 'Pepino', 93: 'Pepper Green', 94: 'Pepper Orange', 95: 'Pepper Red', 96: 'Pepper Yellow', 97: 'Physalis', 98: 'Physalis with Husk', 99: 'Pineapple', 100: 'Pineapple Mini', 101: 'Pitahaya Red', 102: 'Plum', 103: 'Plum 2', 104: 'Plum 3', 105: 'Pomegranate', 106: 'Pomelo Sweetie', 107: 'Potato Red', 108: 'Potato Red Washed', 109: 'Potato Sweet', 110: 'Potato White', 111: 'Quince', 112: 'Rambutan', 113: 'Raspberry', 114: 'Redcurrant', 115: 'Salak', 116: 'Strawberry', 117: 'Strawberry Wedge', 118: 'Tamarillo', 119: 'Tangelo', 120: 'Tomato 1', 121: 'Tomato 2', 122: 'Tomato 3', 123: 'Tomato 4', 124: 'Tomato Cherry Red', 125: 'Tomato Heart', 126: 'Tomato Maroon', 127: 'Tomato Yellow', 128: 'Tomato not Ripened', 129: 'Walnut', 130: 'Watermelon'
				}

				check = cv2.resize(self.origin, (64, 64))
				check = cv2.cvtColor (check, cv2.COLOR_BGR2RGB)
				check = np.array(check)
				check = check[np.newaxis,:,:,:]

				prediction = model.predict(check) 
				i = "{}".format(id_to_label[np.argmax(prediction)])
				print(i)
				my_text.insert(END, i)
		except Exception as e:
			print(e)


root = Tk()



ex = Example(root)

my_text = Text(root, width=15, height=1, font=('Helvetica', 16))
my_text.place(x=150, y=340)

root.geometry('500x450')

root.mainloop()