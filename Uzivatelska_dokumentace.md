# Uživatelská dokumentace

<p>Do rukou se Vám dostává program zpracovávající data o jízdních řádech ve formátu gtfs. Tento formát sestává z textových souborů popisujících jednotlivé části 
  vstupních dat. Stěžejní pro běh této aplikace jsou soubory stop.txt, routes.txt, trips.txt a stop_times.txt, držící postupně: informace o zastávkách, informace o linkách,
  informace o úsekách spojů mezi 2 zastávkami a o návaznosti zastávek na lince a o časech příjezdu a odjezdu spoje ze zastávky.
  V případě, že program nenalezne některý z těchto souborů ve složce gtfs uložené ve stejném adresáři, ze kterého je spouštěn tento program, tuto chbu Vám oznámí. Stejně tak Vás informuje,
  je-li některý soubor nepřístupný.
  
  Program při svém běhu zpracuje získaná data a na výstupu v příkazové řádce vypíše 5 nejvytíženějších mezizastávkových úseků a informaci o tom, 
  kolik spojů tímto úsekem projede.
  
  Program v aktuální verzi nepracuje s datem, a tak je počet vypsaných spojů většinou nadsazen oproti realitě. Pro zjištění absolutních čísel tedy tento program není vhodný.
  Spíše nalezne využití pro porovnání jednotlivých úseků.
  

  
