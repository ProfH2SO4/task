# task

<h2>#TODO</h2><br>

vytvor script, který bude automaticky spouštěn jako linuxový cron job.
K němu připojte README s popisem projektu a příkladem použití a testy.

každých 30 dní vezme soubory ve 
složce /var/log a zkomprimujeme 
je do gzip souborů.

<h3>#Co implementacia dokaze </h3><br>
1.Ak by cesta /var/log (po pripade ina cesta) <br>
neexistovala skonci proces a vypise uzivatelovi <br>
2.zkomprimuje subory len s koncovkou .log, s ostatnymi subormi neurobi nic <br>
3. Ak uzivatel zada prepinac -d, tak ten povodny vymaze  <br>
1.log => 1.log.gz ###t.j nenastane pripad 1.log => 1.log, 1.log.gz <br>

   
<h3>#Pozor</h3><br>
prava do /var/log ma su(super user) alebo uzivatelia, 
ktory dostali tieto prava od su

<h3>#Run </h3> <br>
V pripade ak nebol crontab pouzivany <br>
pip install python-crontab <br>
ak root tak (sudo pip install python-crontab) <br>
Ak nebol upgradnuty <br>
pip install python-crontab --upgrade <br>
ak root tak (sudo pip install python-crontab --upgrade) <br>

Run: <br>
service cron status <br>
ak by bol neaktivny tak <br>
service cron start <br>

############################### <br>
Moznost 1 ################ <br>
############################### <br>
        
Pre spustenie vsetkeho(cron job + gzip) staci spustit: <br>
sudo python3 ./run.py
ak  aj deletovat tak  <br>
sudo python3 ./run.py -d

Po pripade ak by spustenie vyhodilo 
TypeError: __init__() takes exactly 2 arguments alebo <br> 
ValueError: improper number of cron entries specified; got 1 need 5 to 7
tak treba nainstelovat python-crontab a nie crontab


############################### <br>
Moznost 2 ################ <br>
############################### <br>

sudo crontab -e a na spodok dopisat <br>
pozn. kazdych 30 dni 0 5 */30 * * <br>
<u>0 5 */30 * * /usr/bin/python3 path/compress.py </u> <br>
alebo s prepinacom  <br>
<u>0 5 */30 * * /usr/bin/python3 path/compress.py -d </u>

Po zadani prikazu sudo crontab -l by malo vidiet ze bezi job 
Pre vypnutie cron jobu staci zakomentovat
######################################### <br>

Pre spustenie testov: python3 ./tests.py