Zeit/Datum �ber OAP an Swissphone Meldeempf�nger im DAPNET


In dem Script werden Datum und Uhrzeit (UTC) �ber NTP geholt und in den f�r Swissphone ben�tigten String geformt.


Als Startzeichen wurde X gew�hlt.

Der Befehl zum Setzen von Datum und Uhrzeit ist wie folgt aufgebaut:

XTIME=%H%M%d%m%yXTIME=%H%M%d%m%y

Im Meldeempf�nger muss hierzu das Startzeichen und eine OAP RIC konfiguriert sein.





