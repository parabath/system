emd="<html><head></head><body><div><a href='https://drive.google.com/drive/folders/1ofMTr1DwS9a0YZmiyukTBABwCldrQRxH?usp=drive_link'>files</a></div></body></html>"
f = open("C:\\Users\\wppsk\\Desktop\\karuna\\kindexo.html", "a")
f.write(emd)
f.close()

#open and read the file after the appending:
f = open("C:\\Users\\wppsk\\Desktop\\karuna\\kindexo.html", "r")
print(f.read())
