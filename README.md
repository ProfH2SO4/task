# task

#TODO

vytvor script, který bude automaticky spouštěn jako linuxový cron job.
K němu připojte README s popisem projektu a příkladem použití a testy.

každých 30 dní vezme soubory ve 
složce /var/log a zkomprimujeme 
je do gzip souborů.

#Co implementacia dokaze <br>
1.Ak by cesta /var/log (po pripade ina cesta) 
neexistovala skonci proces a vypise uzivatelovi
2.zkomprimuje subory len s koncovkou .log, s ostatnymi subormi neurobi nic
3. Ak uzivatel zada prepinac -d, tak ten povodny vymaze 
1.log => 1.log.gz ###t.j nenastane pripad 1.log => 1.log, 1.log.gz

   
#Pozor
prava do /var/log ma su(super user) alebo uzivatelia, 
ktory dostali tieto prava od su

#Run
V pripade ak nebol crontab pouzivany
pip install python-crontab
ak root tak (sudo pip install python-crontab)
Ak nebol upgradnuty
pip install python-crontab --upgrade
ak root tak (sudo pip install python-crontab --upgrade)

Run:
service cron status
ak by bol neaktivny tak
service cron start

###############################
Moznost 1 ################
###############################
        
Pre spustenie vsetkeho(cron job + gzip) staci spustit: sudo python3 ./run.py
ak by som chcel aj deletovat tak sudo python3 ./run.py -d

Po pripade ak by spustenie vyhodilo 
TypeError: __init__() takes exactly 2 arguments alebo 
ValueError: improper number of cron entries specified; got 1 need 5 to 7
tak treba nainstelovat python-crontab a nie crontab


###############################
Moznost 2 ################
###############################

sudo crontab -e a na spodok dopisat
pozn. @monthly nie je standard,  ak standard tak  0 0 1 * *
@monthly /usr/bin/python3 path/compress.py
alebo s prepinacom 
@monthly /usr/bin/python3 path/compress.py -d

Po zadani prikazu sudo crontab -l by malo vidiet ze bezi job 
Pre vypnutie cron jobu staci zakomentovat
#########################################

Pre spustenie testov: python3 ./tests.py