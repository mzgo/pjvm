import zipfile

f = zipfile.ZipFile("zipfilePath",'r')
for file in f.namelist():
f.extract(file,"temp/")