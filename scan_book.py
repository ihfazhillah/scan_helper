# Enter Directory Name
directory = raw_input("Dirname: ")
# x as horizontal, and y vertical, in mm
try:
    x = raw_input("tentukan ukuran x(mendatar) dalam mm: ")
    int(x)
except ValueError:
    x = raw_input("tentukan ukuran x(mendatar) dalam mm [harus angka]: ")
try:
    y = raw_input("tentukan ukuran y(meninggi) dalam mm: ")
    int(x)
except ValueError:
    y= raw_input("tentukan ukuran y(meninggi) dalam mm [harus angka]: ")
# decide the format (tiff/pnm)
format_pilihan = None
while format_pilihan is None:
    format_pilihan = raw_input("pnm/tiff: ")
    while format_pilihan not in ["pnm", "tiff"]:
        format_pilihan = raw_input("pnm/tiff (format yang anda pilih salah):")
x = int(x)
y = int(y)

# loop 

import os
count = 1
os.mkdir(directory)
while True:
    try:
        
        os.system(" ".join([
                   "sudo",
                   "scanimage",
                   "-d brother4",
                   "-x %d" %x,
                   "-y %d" %y,
                   "--format=%s" %format_pilihan,
                   ">",
                   directory+"/scanned"+str(count)]))
        raw_input("enter to continue and ctrl c to exit")
        count += 1
    except KeyboardInterrupt:
        import os
        print "\nPekerjaan selesai"
        exit()
