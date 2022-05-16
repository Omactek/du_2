# Vývojářská dokumentace

<p>Program busiest_stop.py zpracovává informace o jízdních řádech ve formátu gtfs.
  Vytvořeny jsou třídy Stop, Route, Trip, StopTime, StopSegment.
  
  ###### Třída Stop
  Objekty v této třídě jsou vytvářeny při importu z csv souboru stops.txt pomocí DictReader.
  Objekt třídy Stop má atributy stop_id a stop_name.
  
  ###### Třída Route
  Objekty v této třídě jsou vytvářeny při importu z csv souboru routes.txt pomocí DictReader.
  Objekt třídy Route má atributy route_id, short_name a long_name.
  
  ###### Třída Trip
  Objekty v této třídě jsou vytvářeny při importu z csv souboru trip.txt pomocí DictReader.
  Objekt třídy Route má atributy route_id, short_name a long_name.
  
  ###### Třída StopTime
  Objekty v této třídě jsou vytvářeny při importu z csv souboru stop_times.txt pomocí DictReader.
  Objekt třídy Route má atributy stop, trip a stop_sequence.
  
  ###### Třída StopSegment
  Objekty třídy StopSegment drží informace o dvou stanicích a o počtu průjezdů mezi nimi (označeno jako occurrences).
  
  Tyto objekty jsou vytvářeny metodou create_segments, která načítá zastávky ze slovníku stop_times.
  Zde jsou uloženy jednotlivé StopTime stříděné dle Tripů. Metoda si "vytáhne" dvojice zastávek tak, že první pokud je stop_sequence = 1, je tato zastávka brána 
  jako první, pokud je stop_sequence = 2, je zastávka brána jako druhá. Při vyšších stop_sequence je brána jako první zastávka předchozí načtená a jako druhá 
  současná.
  Tato dvojice tvoří segment_key. Tento segment_key je přidán do slovníku stopsegments_dict v případě, že v něm ještě není. Pokud v něm již takový segment je, je mu
  zvednut atribut occurences o 1.
  
  Nakonec je slovník vytříděn dle hodnoty occurences a výsledné nejvytíženější mezizastávkové úseku spolu s počtem spojů vypsány.
  
 
  
  
