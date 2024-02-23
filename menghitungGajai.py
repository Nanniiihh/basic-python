gaji_pokok = int(input("gaji daniel adalah"))
perhari = int(input("berapa hari kerja"))

total_transport = 100000 * perhari
total_makan = 50000 * perhari

jam_lembur = int(input("berapa jam lembur"))

if jam_lembur <= 2:
    upah_lembur = jam_lembur *perhari
else:
    upah_lembur = 200000 + (jam_lembur - 2) *150000
    
honor = gaji_pokok+total_transport+ total_makan+upah_lembur

print("honor yang diterima adalah", honor , "rupiah")
    