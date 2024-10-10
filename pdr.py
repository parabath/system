def extractp(row:str)->str:
    elements = row.split(",")
    recorde = elements[1]
    return recorde

file_path="C:\\Users\\wppsk\\Desktop\\karuna\\spd.txt"
spd_file=open(file_path,'r')

for row in spd_file:
    recorde = extractp(row)
    print(recorde)

