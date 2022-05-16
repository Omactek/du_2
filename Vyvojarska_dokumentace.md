# Vývojářská dokumentace

<p>Program busiest_stop.py zpracovává informace o jízdních řádech ve formátu gtfs.
  Vytvořeny jsou třídy Stop, Route, Trip, StopTime, StopSegment.
  
  Třída Stop
  Objekty v této třídě jsou vytvářeny při importu z csv souboru stops.txt pomocí DictReader.
  Objekt třídy Stop má atributy stop_id a stop_name.
  
  Třída Route
  Objekty v této třídě jsou vytvářeny při importu z csv souboru routes.txt pomocí DictReader.
  Objekt třídy Route má atributy route_id, short_name a long_name.
  
  Třída Trip
  Objekty v této třídě jsou vytvářeny při importu z csv souboru trip.txt pomocí DictReader.
  Objekt třídy Route má atributy route_id, short_name a long_name.
  
  Třída StopTime
  Objekty v této třídě jsou vytvářeny při importu z csv souboru stop_times.txt pomocí DictReader.
  Objekt třídy Route má atributy stop, trip a stop_sequence.
  
  Třída StopSegment
  Objekty třídy StopSegment
 
  
  
