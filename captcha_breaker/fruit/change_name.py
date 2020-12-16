import os

Source_Path = "C:/Users/ASUS/Downloads/training/New folder"
Destination = "C:/Users/ASUS/Downloads/training/mango"

for i, filename in enumerate(os.listdir(Source_Path)):
	# đưa tên file cần đổi tên vô đây
	dst = "{}.png".format(str(i+99).zfill(6))


	os.rename(os.path.join(Source_Path, filename),  os.path.join(Destination, dst))
