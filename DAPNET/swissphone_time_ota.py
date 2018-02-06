# adapted from https://github.com/DL7FL/DAPNET/blob/master/DAPNET/senden.py

import os
import dapnet
import logging # -> Logging vom Fehlermeldungen
import sys
import ntplib
import time

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s;%(levelname)s;%(message)s")
logger = logging.getLogger(sys.argv[0])


###############################################################################
#  Zeit/Datum u. NTP / OTA String fuer Swissphone mit Startzeichen X erstellen
###############################################################################


c = ntplib.NTPClient()
response = c.request('pool.ntp.org')
ts = response.tx_time
date = time.strftime('%H%M%d%m%y',time.localtime(ts))

string_to_send  = ("XTIME=%s" %date)
string_to_send += ("XTIME=%s" %date)

###############################################################################
#  Daten in Variablen Speichern
###############################################################################

# Konstante

login = 'dapnet_passwort' #  DAPNET Benutzername
passwd = 'dapnet_passwort'  #  DAPNET Passwort


url = 'http://www.hampager.de:8080/calls'  #  versenden uebers Internet Variable

text = string_to_send  		#  Nachrichtentext bis 80 Zeichen  eingeben
callsign_list = ["subscriber_to_send"]  	#  zB. ["dl1xx","dl2xx","dl3xx"] ein oder mehrere Empfaenger
txgroup = "all"			#  Sendergruppe zB. dl-all fuer alle Sender in Deutschland

##############################################################################
# Hauptprogramm
##############################################################################


dapnet.send(text, callsign_list, login, passwd, url, txgroup)
