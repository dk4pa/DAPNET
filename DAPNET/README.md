Zeit/Datum über OAP an Swissphone Meldeempfänger im DAPNET


In dem Script werden Datum und Uhrzeit (UTC) über NTP geholt und in den für Swissphone benötigten String geformt.


Als Startzeichen wurde X gewählt.

Der Befehl zum Setzen von Datum und Uhrzeit ist wie folgt aufgebaut:

XTIME=%H%M%d%m%yXTIME=%H%M%d%m%y

Im Meldeempfänger muss hierzu das Startzeichen und eine OAP RIC konfiguriert sein.





