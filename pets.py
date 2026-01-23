from pylab import *

# tekst som skal stå under stolpene i diagrammet
label = ["0 søsken", "1 søsken", "2 søsken", "3 søsken"]

antall_venner = [2, 4, 3, 1]              # tall som skal plottes

#bar(label, antall_venner)                 # tegner stolpediagram
#plot(label, antall_venner)
pie(antall_venner, labels = label, startangle = 90)

#xlabel("Antall søsken", fontsize = 12)    # tekst på x-aksen
#ylabel("Frekvens", fontsize = 12)         # tekst på y-aksen
#xticks(label, fontsize = 7)               # tekst under stolpene
axis("equal")                               # gjør at sektordiagrammet blir rundt

# diagramtittel
title("Hvor mange søsken har du?", fontsize = 20)

show()
