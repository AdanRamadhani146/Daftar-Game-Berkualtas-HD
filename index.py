print("|================================================|")
print("|========== Daftar Game Berkualtas HD  ==========|")
print("|================================================|")

game= ["God Of War 4","Grand Theft Auto V","Devil May Cry 4","Devil May Cry 5","Assassins Creed Odesey","REsident Evil 2 Remake","Just Cause 4","Final Fantasy XV","Lego Marvel Super Heroes","Dynasty Warriors 9"]
tanggal= ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
bulan= ["januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"] 
tahun= ["2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]
gamemode= ["(Singel Player)","(Multi Player)","(Multi Player Online)"]
console= ["(Playstation 3)","(Playstation 4)","(Microsoft Windows (PC))","(XBOX One)","(XBOX 360)"]
ranting= ["R13+","D17+","SU"]

import time;
localtime=time.localtime(time.time())

kesempatan=3
while kesempatan >=0:
    print("SIlahkan diisi PIN")
    pin=int(input("Masukan PIN : "))
    
# Waktu Pagi   
    if localtime[3] >= 0 and localtime[3] <= 10: 
        print("selamat pagi")
        if pin==2811:
            print("1. God Of War 4")
            print("2. Grand Theft Auto V")
            print("3. Devil May Cry 4")
            print("4. Devil May Cry 5")
            print("5. Assassins Creed Odesey")
            print("6. Resident Evil 2 Remake")
            print("7. Just Cause 4")
            print("8. Final Fantasy XV")
            print("9. Lego Marvel Super Heroes")
            print("10. Dynasty Warriors 9")
            
            pilihan=int(input("Pilih Game : "))
            if pilihan == 1:
                print("=======================================================")
                print(" Game : ", (game[0]))
                print(" Tanggal Rilis : ", (tanggal[19]), (bulan[3]), (tahun[10]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]))
                print(" Ranting : ", (ranting[1]))
                print("=======================================================")
                break
            
            elif pilihan == 2:
                print("=======================================================")
                print(" Game : ", (game[1]))
                print(" Tanggal Rilis : ", (tanggal[16]), (bulan[8]), (tahun[5]))
                print(" Game Mode : ", (gamemode[0]), (gamemode[2]))
                print(" Console : ", (console[0]), (console[1]), (console[2]), (console[3]), (console[4]))
                print(" Ranting : ", (ranting[1]))
                print("=======================================================")
                break
                
            elif pilihan == 3:
                print("=======================================================")
                print(" Game : ", (game[2]))
                print(" Tanggal Rilis : ", (tanggal[30]), (bulan[0]), (tahun[0]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[0]), (console[2]), (console[3]), (console[4]))
                print(" Ranting : ", (ranting[0]))
                print("=======================================================")
                break
                
            elif pilihan == 4:
                print("=======================================================")
                print(" Game : ", (game[3]))
                print(" Tanggal Rilis : ", (tanggal[7]), (bulan[2]), (tahun[11]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]), (ranting[1]))
                print("=======================================================")
                break
            
            elif pilihan == 5:
                print("=======================================================")
                print(" Game : ", (game[4]))
                print(" Tanggal Rilis : ", (tanggal[1]), (bulan[9]), (tahun[10]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[1]))
                print("=======================================================")
                
            elif pilihan == 6:
                print("=======================================================")
                print(" Game : ", (game[5]))
                print(" Tanggal Rilis : ", (tanggal[24]), (bulan[0]), (tahun[11]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]), (ranting[1]))
                print("=======================================================")
                break
            
            elif pilihan == 7:
                print("=======================================================")
                print(" Game : ", (game[6]))
                print(" Tanggal Rilis : ", (tanggal[2]), (bulan[11]), (tahun[10]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]))
                print("=======================================================")
                break
            
            elif pilihan == 8:
                print("=======================================================")
                print(" Game : ", (game[7]))
                print(" Tanggal Rilis : ", (tanggal[30]), (bulan[10]), (tahun[8]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]))
                print("=======================================================")
                break
            
            elif pilihan == 9:
                print("=======================================================")
                print(" Game : ", (game[8]))
                print(" Tanggal Rilis : ", (tanggal[21]), (bulan[9]), (tahun[5]))
                print(" Game Mode : ", (gamemode[0]), (gamemode[1]))
                print(" Console : ", (console[0]), (console[1]), (console[2]), (console[3]), (console[4]))
                print(" Ranting : ", (ranting[2]))
                print("=======================================================")
                break
            
            elif pilihan == 10:
                print("=======================================================")
                print(" Game : ", (game[9]))
                print(" Tanggal Rilis : ", (tanggal[12]), (bulan[1]), (tahun[10]))
                print(" Game Mode : ", (gamemode[0]), (gamemode[1]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]))
                print("=======================================================")
                break
            
        elif kesempatan != 0:
            print('pin anda salah\n')
            print('masukkan pin anda dengan benar')
            kesempatan-=1
        if kesempatan== 0:
            print('akun anda terblokir silahkan datangi kasir')
            break
            
# Waktu Siang  
    if localtime[3] >= 11 and localtime[3] <= 15: 
        print("Selamat Siang")
        if pin==2811:
            print("1.  God Of War 4")
            print("2.  Grand Theft Auto V")
            print("3.  Devil May Cry 4")
            print("4.  Devil May Cry 5")
            print("5.  Assassins Creed Odesey")
            print("6.  Resident Evil 2 Remake")
            print("7.  Just Cause 4")
            print("8.  Final Fantasy XV")
            print("9.  Lego Marvel Super Heroes")
            print("10. Dynasty Warriors 9")
            
            pilihan=int(input("Pilih Game : "))
            if pilihan == 1:
                print("=======================================================")
                print(" Game : ", (game[0]))
                print(" Tanggal Rilis : ", (tanggal[19]), (bulan[3]), (tahun[10]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]))
                print(" Ranting : ", (ranting[1]))
                print("=======================================================")
                break
            
            elif pilihan == 2:
                print("=======================================================")
                print(" Game : ", (game[1]))
                print(" Tanggal Rilis : ", (tanggal[16]), (bulan[8]), (tahun[5]))
                print(" Game Mode : ", (gamemode[0]), (gamemode[2]))
                print(" Console : ", (console[0]), (console[1]), (console[2]), (console[3]), (console[4]))
                print(" Ranting : ", (ranting[1]))
                print("=======================================================")
                break
                
            elif pilihan == 3:
                print("=======================================================")
                print(" Game : ", (game[2]))
                print(" Tanggal Rilis : ", (tanggal[30]), (bulan[0]), (tahun[0]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[0]), (console[2]), (console[3]), (console[4]))
                print(" Ranting : ", (ranting[0]))
                print("=======================================================")
                break
                
            elif pilihan == 4:
                print("=======================================================")
                print(" Game : ", (game[3]))
                print(" Tanggal Rilis : ", (tanggal[7]), (bulan[2]), (tahun[11]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]))
                print("=======================================================")
                break
            
            elif pilihan == 5:
                print("=======================================================")
                print(" Game : ", (game[4]))
                print(" Tanggal Rilis : ", (tanggal[1]), (bulan[9]), (tahun[10]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[1]))
                print("=======================================================")
                break
                
            elif pilihan == 6:
                print("=======================================================")
                print(" Game : ", (game[5]))
                print(" Tanggal Rilis : ", (tanggal[24]), (bulan[0]), (tahun[11]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]), (ranting[1]))
                print("=======================================================")
                break
            
            elif pilihan == 7:
                print("=======================================================")
                print(" Game : ", (game[6]))
                print(" Tanggal Rilis : ", (tanggal[2]), (bulan[11]), (tahun[10]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]))
                print("=======================================================")
                break
            
            elif pilihan == 8:
                print("=======================================================")
                print(" Game : ", (game[7]))
                print(" Tanggal Rilis : ", (tanggal[28]), (bulan[10]), (tahun[8]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]))
                print("=======================================================")
                break
            
            elif pilihan == 9:
                print("=======================================================")
                print(" Game : ", (game[8]))
                print(" Tanggal Rilis : ", (tanggal[21]), (bulan[9]), (tahun[5]))
                print(" Game Mode : ", (gamemode[0]), (gamemode[1]))
                print(" Console : ", (console[0]), (console[1]), (console[2]), (console[3]), (console[4]))
                print(" Ranting : ", (ranting[2]))
                print("=======================================================")
                break
            
            elif pilihan == 10:
                print("=======================================================")
                print(" Game : ", (game[9]))
                print(" Tanggal Rilis : ", (tanggal[12]), (bulan[1]), (tahun[10]))
                print(" Game Mode : ", (gamemode[0]), (gamemode[1]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]))
                print("=======================================================")
                break
            
        elif kesempatan != 0:
            print('pin anda salah\n')
            print('masukkan pin anda dengan benar')
            kesempatan-=1
        if kesempatan== 0:
            print('akun anda terblokir silahkan datangi kasir')
            break
            
# Waktu Sore  
    if localtime[3] >= 16 and localtime[3] <= 18: 
        print("selamat Sore")
        if pin==2811:
            print("1. God Of War 4")
            print("2. Grand Theft Auto V")
            print("3. Devil May Cry 4")
            print("4. Devil May Cry 5")
            print("5. Assassins Creed Odesey")
            print("6. Resident Evil 2 Remake")
            print("7. Just Cause 4")
            print("8. Final Fantasy XV")
            print("9. Lego Marvel Super Heroes")
            print("10. Dynasty Warriors 9")
            
            pilihan=int(input("Pilih Game : "))
            if pilihan == 1:
                print("=======================================================")
                print(" Game : ", (game[0]))
                print(" Tanggal Rilis : ", (tanggal[19]), (bulan[3]), (tahun[10]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]))
                print(" Ranting : ", (ranting[1]))
                print("=======================================================")
                break
            
            elif pilihan == 2:
                print("=======================================================")
                print(" Game : ", (game[1]))
                print(" Tanggal Rilis : ", (tanggal[16]), (bulan[8]), (tahun[5]))
                print(" Game Mode : ", (gamemode[0]), (gamemode[2]))
                print(" Console : ", (console[0]), (console[1]), (console[2]), (console[3]), (console[4]))
                print(" Ranting : ", (ranting[1]))
                print("=======================================================")
                break
                
            elif pilihan == 3:
                print("=======================================================")
                print(" Game : ", (game[2]))
                print(" Tanggal Rilis : ", (tanggal[30]), (bulan[0]), (tahun[0]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[0]), (console[2]), (console[3]), (console[4]))
                print(" Ranting : ", (ranting[0]))
                print("=======================================================")
                break
                
            elif pilihan == 4:
                print("=======================================================")
                print(" Game : ", (game[3]))
                print(" Tanggal Rilis : ", (tanggal[7]), (bulan[2]), (tahun[11]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]), (ranting[1]))
                print("=======================================================")
                break
            
            elif pilihan == 5:
                print("=======================================================")
                print(" Game : ", (game[4]))
                print(" Tanggal Rilis : ", (tanggal[1]), (bulan[9]), (tahun[10]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[1]))
                print("=======================================================")
                
            elif pilihan == 6:
                print("=======================================================")
                print(" Game : ", (game[5]))
                print(" Tanggal Rilis : ", (tanggal[24]), (bulan[0]), (tahun[11]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]), (ranting[1]))
                print("=======================================================")
                break
            
            elif pilihan == 7:
                print("=======================================================")
                print(" Game : ", (game[6]))
                print(" Tanggal Rilis : ", (tanggal[2]), (bulan[11]), (tahun[10]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]))
                print("=======================================================")
                break
            
            elif pilihan == 8:
                print("=======================================================")
                print(" Game : ", (game[7]))
                print(" Tanggal Rilis : ", (tanggal[30]), (bulan[10]), (tahun[8]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]))
                print("=======================================================")
                break
            
            elif pilihan == 9:
                print("=======================================================")
                print(" Game : ", (game[8]))
                print(" Tanggal Rilis : ", (tanggal[21]), (bulan[9]), (tahun[5]))
                print(" Game Mode : ", (gamemode[0]), (gamemode[1]))
                print(" Console : ", (console[0]), (console[1]), (console[2]), (console[3]), (console[4]))
                print(" Ranting : ", (ranting[2]))
                print("=======================================================")
                break
            
            elif pilihan == 10:
                print("=======================================================")
                print(" Game : ", (game[9]))
                print(" Tanggal Rilis : ", (tanggal[12]), (bulan[1]), (tahun[10]))
                print(" Game Mode : ", (gamemode[0]), (gamemode[1]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]))
                print("=======================================================")
                break
            
        elif kesempatan != 0:
            print('pin anda salah\n')
            print('masukkan pin anda dengan benar')
            kesempatan-=1
        if kesempatan== 0:
            print('akun anda terblokir silahkan datangi kasir')
            break 
          
# Waktu Malam   
    if localtime[3] >= 19 and localtime[3] <= 23: 
        print("selamat Malam")
        if pin==2811:
            print("1. God Of War 4")
            print("2. Grand Theft Auto V")
            print("3. Devil May Cry 4")
            print("4. Devil May Cry 5")
            print("5. Assassins Creed Odesey")
            print("6. Resident Evil 2 Remake")
            print("7. Just Cause 4")
            print("8. Final Fantasy XV")
            print("9. Lego Marvel Super Heroes")
            print("10. Dynasty Warriors 9")
            
            pilihan=int(input("Pilih Game : "))
            if pilihan == 1:
                print("=======================================================")
                print(" Game : ", (game[0]))
                print(" Tanggal Rilis : ", (tanggal[19]), (bulan[3]), (tahun[10]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]))
                print(" Ranting : ", (ranting[1]))
                print("=======================================================")
                break
            
            elif pilihan == 2:
                print("=======================================================")
                print(" Game : ", (game[1]))
                print(" Tanggal Rilis : ", (tanggal[16]), (bulan[8]), (tahun[5]))
                print(" Game Mode : ", (gamemode[0]), (gamemode[2]))
                print(" Console : ", (console[0]), (console[1]), (console[2]), (console[3]), (console[4]))
                print(" Ranting : ", (ranting[1]))
                print("=======================================================")
                break
                
            elif pilihan == 3:
                print("=======================================================")
                print(" Game : ", (game[2]))
                print(" Tanggal Rilis : ", (tanggal[30]), (bulan[0]), (tahun[0]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[0]), (console[2]), (console[3]), (console[4]))
                print(" Ranting : ", (ranting[0]))
                print("=======================================================")
                break
                
            elif pilihan == 4:
                print("=======================================================")
                print(" Game : ", (game[3]))
                print(" Tanggal Rilis : ", (tanggal[7]), (bulan[2]), (tahun[11]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]), (ranting[1]))
                print("=======================================================")
                break
            
            elif pilihan == 5:
                print("=======================================================")
                print(" Game : ", (game[4]))
                print(" Tanggal Rilis : ", (tanggal[1]), (bulan[9]), (tahun[10]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[1]))
                print("=======================================================")
                
            elif pilihan == 6:
                print("=======================================================")
                print(" Game : ", (game[5]))
                print(" Tanggal Rilis : ", (tanggal[24]), (bulan[0]), (tahun[11]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]), (ranting[1]))
                print("=======================================================")
                break
            
            elif pilihan == 7:
                print("=======================================================")
                print(" Game : ", (game[6]))
                print(" Tanggal Rilis : ", (tanggal[2]), (bulan[11]), (tahun[10]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]))
                print("=======================================================")
                break
            
            elif pilihan == 8:
                print("=======================================================")
                print(" Game : ", (game[7]))
                print(" Tanggal Rilis : ", (tanggal[30]), (bulan[10]), (tahun[8]))
                print(" Game Mode : ", (gamemode[0]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]))
                print("=======================================================")
                break
            
            elif pilihan == 9:
                print("=======================================================")
                print(" Game : ", (game[8]))
                print(" Tanggal Rilis : ", (tanggal[21]), (bulan[9]), (tahun[5]))
                print(" Game Mode : ", (gamemode[0]), (gamemode[1]))
                print(" Console : ", (console[0]), (console[1]), (console[2]), (console[3]), (console[4]))
                print(" Ranting : ", (ranting[2]))
                print("=======================================================")
                break
            
            elif pilihan == 10:
                print("=======================================================")
                print(" Game : ", (game[9]))
                print(" Tanggal Rilis : ", (tanggal[12]), (bulan[1]), (tahun[10]))
                print(" Game Mode : ", (gamemode[0]), (gamemode[1]))
                print(" Console : ", (console[1]), (console[2]), (console[3]))
                print(" Ranting : ", (ranting[0]))
                print("=======================================================")
                break
            
        elif kesempatan != 0:
            print('pin anda salah\n')
            print('masukkan pin anda dengan benar')
            kesempatan-=1
        if kesempatan== 0:
            print('akun anda terblokir silahkan Hubungi Kontak Yang bersangkutan')
            break