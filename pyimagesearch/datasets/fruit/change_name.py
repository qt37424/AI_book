import os

Source_Path = "D:/PyCharm/AI_book/pyimagesearch/datasets/fruit/star_fruit"
Destination = "D:/PyCharm/AI_book/captcha_breaker/fruit/star_fruit"

for i, filename in enumerate(os.listdir(Source_Path)):
	# đưa tên file cần đổi tên vô đây
	dst = "{}.png".format(str(i).zfill(6))


	os.rename(os.path.join(Source_Path, filename),  os.path.join(Destination, dst))
