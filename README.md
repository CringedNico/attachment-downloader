# Cedolino (PDF) Downloader
## Informazioni
Questo script mi permette di scaricare mensilmente i cedolini che mi vengono inviati tramite mail come allegati.

Con l'utilizzo di crontab sul mio server ho schedulato il download in una directory presente nel mio share Samba in modo tale che possa consultarli facilmente da ogni dispositivo. 

Una volta scaricati, vengono rinominati in base all'anno e al mese di riferimento (YYYYMM_cedolino.pdf), in seguito tramite la libreria pikepdf vengono aperti e viene rimossa la password affinché sia più veloce l'apertura e la consultazione.
