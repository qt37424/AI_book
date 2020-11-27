from tkinter import Frame, Tk, BOTH, Label
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
        self.parent.title("File Dialog")
        self.pack(fill = BOTH, expand = 1)
        error = Button(self, text="Ảnh Mới", command=self.onOpen) #nghiên cứu đặt update text
        error.grid(padx=220, pady=5)

    def onOpen(self):
        ftypes = [("Image Files", "*.jpg *.png"), ('All files', '*')] #lưu ý tên file đường dẫn không được có dấu
        dlg = Open(self, filetypes = ftypes)
        fl = dlg.show()
        # check = fl.split(".")
        if fl != '':
            img = self.openImage(fl)

    def readFile(self, filename):
        f = open(filename, 'r')
        text = f.read()
        return text #nó chỉ trả về một giá trị text không được xuất ra

    def openImage (self, filename):
        bard = Image.open(filename)
        bard = bard.resize((256,256))
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image = bardejov)
        label1.image = bardejov
        label1.place(x=122, y=30)
        self.predict(filename)

    def predict(self, filename):
        model = tensorflow.keras.models.load_model('model/model.h5')
        id_to_label = {0: 'banana', 1: 'orange', 2: 'star_fruit'}

        origin = cv2.imread('test_photo.jpg')

        check = cv2.resize(origin, (64, 64))
        check = cv2.cvtColor(check, cv2.COLOR_BGR2RGB)
        check = np.array(check)
        check = check[np.newaxis, :, :, :]
        prediction = model.predict(check)

        # run the inference
        prediction = model.predict(check)
        print(prediction)
        print(np.argmax(prediction))
        print("{}".format(id_to_label[np.argmax(prediction)]))

root = Tk()
ex = Example(root)
root.geometry('500x500+50+50')
root.mainloop()
