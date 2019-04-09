# Bundescrawler
Collection of crawlers for german Verkündungen (EU, Bund, Länder)

## Getting started
1. Install scrapy via ```pip install scrapy```
2. run spider via ```scrapy run spiders/GblBremen.py```

## Results overview
|Spider|	Last Run |	Outcome|	Items|	Requests|
| ------ | ------ |------ |------ |------ |
|GesetzblattBremen|	2019-04-08 10:56:37 UTC|	finished|	845|	1|
|GesetzblattBrandenburg|	2019-04-08 10:55:49 UTC|	closespider_timeout|	1760|	19|
|EUVerordnungen|	2019-04-08 10:54:18 UTC|	closespider_timeout|	190|	20|
|MinisterialblattBayern|	2019-04-08 10:47:32 UTC|	closespider_timeout|	1221|	157|
|GesetzblattBayern|	2019-04-01 09:12:32 UTC|	closespider_timeout|	1125|	107|


## Sample output
|Datum|ID|Link|Seiten|Titel|_type|
|-----|--|----|------|-----|-----|
|08.04.2019|Gesetzblatt 2019 Nr. 39|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_04_08_GBl_Nr_0039_signed.pdf|S. 171| Verordnung zur Aufhebung bauordnungsrechtlicher Vorschriften|dict|
|08.04.2019|Gesetzblatt 2019 Nr. 38|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_04_08_GBl_Nr_0038_signed.pdf|S. 169 - 170| Gesetz zur Änderung des Bremischen Verfassungsschutzgesetzes und des Bremischen Polizeigesetzes|dict|
|08.04.2019|Gesetzblatt 2019 Nr. 37|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_04_08_GBl_Nr_0037_signed.pdf|S. 167 - 168| Gesetz zur Änderung des Gesetzes über die Rechtsverhältnisse der Mitglieder der Bremischen Bürgerschaft (Bremisches Abgeordnetengesetz)|dict|
|08.04.2019|Gesetzblatt 2019 Nr. 36|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_04_08_GBl_Nr_0036_signed.pdf|S. 164 - 166| Gesetz zur Änderung des Gesetzes über die Deputationen|dict|
|05.04.2019|Gesetzblatt 2019 Nr. 35|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_04_05_GBl_Nr_0035_signed.pdf|S. 162 - 163| Gesetz zur fortlaufenden Untersuchung der Kriminalitätslage und ergänzenden Auswertung der polizeilichen Kriminalitätsstatistik im Land Bremen (Bremisches Kriminalitätsstatistikgesetz – BremKStatG)|dict|
|05.04.2019|Gesetzblatt 2019 Nr. 34|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_04_05_GBl_Nr_0034_signed.pdf|S. 159 - 161| Gesetz zur Änderung des Bremischen Verwaltungsvollstreckungsgesetzes|dict|
|05.04.2019|Gesetzblatt 2019 Nr. 33|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_04_05_GBl_Nr_0033_signed.pdf|S. 152 - 158| Bremisches Landes-Carsharinggesetz (BremLCsgG)|dict|
|05.04.2019|Gesetzblatt 2019 Nr. 32|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_04_05_GBl_Nr_0032_signed.pdf|S. 147 - 151| Gesetz über Finanzzuweisungen an die Gemeinden Bremen und Bremerhaven (Finanzzuweisungsgesetz)|dict|
|04.04.2019|Gesetzblatt 2019 Nr. 31|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_04_04_GBl_Nr_0031_signed.pdf|S. 141 - 146| Gesetz zum Staatsvertrag zwischen der Freien und Hansestadt Hamburg |dict|
|04.04.2019|Gesetzblatt 2019 Nr. 30|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_04_04_GBl_Nr_0030_signed.pdf|S. 133 - 140| Gesetz zur Änderung des Bremischen Archivgesetzes|dict|
|04.04.2019|Gesetzblatt 2019 Nr. 29|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_04_04_GBl_Nr_0029_signed.pdf|S. 131 - 132| Gesetz zur Änderung des Gesetzes zur Ausführung des Betreuungsgesetzes |dict|
|03.04.2019|Gesetzblatt 2019 Nr. 28|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_04_03_GBl_Nr_0028_signed.pdf|S. 130| Sechste Verordnung zur Änderung der Kostenverordnung der Umweltverwaltung|dict|
|28.03.2019|Gesetzblatt 2019 Nr. 27|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_03_28_GBl_Nr_0027_signed.pdf|S. 128 - 129| Vierte Verordnung zur Änderung der Verordnung über Beförderungsentgelte im Taxenverkehr der Stadtgemeinde Bremerhaven (Taxentarifverordnung) in der Fassung der Bekanntmachung vom 20. November 2002|dict|
|27.03.2019|Gesetzblatt 2019 Nr. 26|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_03_27_GBl_Nr_0026_signed.pdf|S. 127| Verordnung zur Änderung der Bremischen Gaststättenverordnung|dict|
|26.03.2019|Gesetzblatt 2019 Nr. 25|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_03_26_GBl_Nr_0025_signed.pdf|S. 119 - 125| Verordnung zur Errichtung der Schiedsstelle nach dem Pflegeberufegesetz|dict|
|25.03.2019|Gesetzblatt 2019 Nr. 24|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_03_25_GBl_Nr_0024_signed.pdf|S. 108 - 118| Verordnung zur Anerkennung und Förderung von Angeboten zur Unterstützung im Alltag nach § 45a, der Weiterentwicklung der Versorgungsstrukturen und des Ehrenamtes nach § 45c sowie der Selbsthilfe nach § 45d des Elften Buches Sozialgesetzbuch für das Land Bremen|dict|
|22.03.2019|Gesetzblatt 2019 Nr. 23|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_03_22_GBl_Nr_0023_signed.pdf|S. 106 - 107| Verordnung zur Änderung der Bremischen Hafengebührenordnung|dict|
|18.03.2019|Gesetzblatt 2019 Nr. 22|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_03_18_GBl_Nr_0022_signed.pdf|S. 105| Bekanntmachung einer Entscheidung des Staatsgerichtshofs der Freien Hansestadt Bremen|dict|
|14.03.2019|Gesetzblatt 2019 Nr. 21|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_03_14_GBl_Nr_0021_signed.pdf|S. 103 - 104| Verordnung über abweichende Öffnungszeiten von Verkaufsstellen an Sonntagen in der Stadtgemeinde Bremen für das Jahr 2019|dict|
|14.03.2019|Gesetzblatt 2019 Nr. 20|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_03_14_GBl_Nr_0020_signed.pdf|S. 86 - 102| Verordnung über die Zweijährige Höhere Handelsschule|dict|
|14.03.2019|Gesetzblatt 2019 Nr. 19|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_03_14_GBl_Nr_0019_signed.pdf|S. 84 - 85| Viertes Gesetz zur Änderung des Gesetzes zur Errichtung einer Stiftung des öffentlichen Rechts „Alfred-Wegener-Institut für Polar- und Meeresforschung“ |dict|
|14.03.2019|Gesetzblatt 2019 Nr. 18|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_03_14_GBl_Nr_0018_signed.pdf|S. 80 - 83| Gesetz zu dem Staatsvertrag zur Änderung des Staatsvertrags zwischen dem Land Niedersachsen und der Freien Hansestadt Bremen über die Zusammenarbeit bei Überwachungs- und Untersuchungsaufgaben im Verbraucherschutz- und Tiergesundheitsbereich|dict|
|13.03.2019|Gesetzblatt 2019 Nr. 17|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_03_13_GBl_Nr_0017_signed.pdf|S. 76 - 79| Gesetz zur Änderung des Bremischen Tageseinrichtungs- und Kindertagespflegegesetzes|dict|
|13.03.2019|Gesetzblatt 2019 Nr. 16|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_03_13_GBl_Nr_0016_signed.pdf|S. 71 - 75| Fünftes Hochschulreformgesetz|dict|
|13.03.2019|Gesetzblatt 2019 Nr. 15|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_03_13_GBl_Nr_0015_signed.pdf|S. 57 - 70| Gesetz zum Zweiundzwanzigsten Rundfunkänderungsstaatsvertrag|dict|
|13.03.2019|Gesetzblatt 2019 Nr. 14|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_03_13_GBl_Nr_0014_signed.pdf|S. 55 - 56| Drittes Gesetz zur Änderung des Bremer Informationsfreiheitsgesetzes |dict|
|12.03.2019|Gesetzblatt 2019 Nr. 13|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_03_13_GBl_Nr_0013_signed.pdf|S. 52 - 54| Gesetz zur Änderung des Bremischen Ausbildungsgesetzes für Lehrämter |dict|
|12.03.2019|Gesetzblatt 2019 Nr. 12|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_03_12_GBl_Nr_0012_signed.pdf|S. 45 - 51| Gesetz zur Umsetzung des Bundesteilhabegesetzes|dict|
|11.03.2019|Gesetzblatt 2019 Nr. 11|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_03_11_GBl_Nr_0011_signed.pdf|S. 43 - 44| Ortsgesetz zur Änderung des Ortsgesetzes über Beiräte und Ortsämter|dict|
|01.03.2019|Gesetzblatt 2019 Nr. 10|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_03_01_GBl_Nr_0010_signed.pdf|S. 36 - 42| Verordnung über Landschaftsschutzgebietsverordnungen im Ortsteil Lüssum-Bockhorn der Stadtgemeinde Bremen|dict|
|21.02.2019|Gesetzblatt 2019 Nr. 9|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_02_21_GBl_Nr_0009_signed.pdf|S. 31 - 39| Verordnung über die Festlegung der Zulassungszahlen zum Vorbereitungsdienst für die Lehrämter an öffentlichen Schulen im Lande Bremen|dict|
|19.02.2019|Gesetzblatt 2019 Nr. 8|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_02_19_GBl_Nr_0008_signed.pdf|S. 29 - 30| Verordnung zur Änderung der Verordnung über die Ausbildung und Prüfung |dict|
|15.02.2019|Gesetzblatt 2019 Nr. 7|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_02_15_GBl_Nr_0007_signed.pdf|S. 25 - 28| Gesetz zur Änderung gesundheitsrechtlicher Gesetze|dict|
|15.02.2019|Gesetzblatt 2019 Nr. 6|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_02_15_GBl_Nr_0006_signed.pdf|S. 24| Gesetz für den Übergangszeitraum nach dem Austritt des Vereinigten Königreichs Großbritannien und Nordirland aus der Europäischen Union|dict|
|15.02.2019|Gesetzblatt 2019 Nr. 5|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_02_15_GBl_Nr_0005_signed.pdf|S. 21 - 23| Ortsgesetz zur Anpassung von Vorschriften aus dem Bereich Kultur an die europäische Datenschutz-Grundverordnung |dict|
|13.02.2019|Gesetzblatt 2019 Nr. 4|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_02_13_GBl_Nr_0004_signed.pdf|S. 15 - 20| Verordnung zur Änderung dienstrechtlicher Vorschriften|dict|
|05.02.2019|Gesetzblatt 2019 Nr. 3|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_02_05_GBl_Nr_0003_signed.pdf|S. 7 - 14| Verordnung über die Vergütung der Gerichtsvollzieherinnen und Gerichtsvollzieher sowie weiterer im Vollstreckungsdienst eingesetzter Beamtinnen und Beamten (Bremische Vollstreckungsvergütungsverordnung - BremVollstrVergV)|dict|
|15.01.2019|Gesetzblatt 2019 Nr. 2|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_01_15_GBl_Nr_0002_signed.pdf|S. 5-6| Verordnung zur Änderung der Lehrverpflichtungs- und Lehrnachweisverordnung|dict|
|04.01.2019|Gesetzblatt 2019 Nr. 1|https://www.gesetzblatt.bremen.de/fastmedia/832/2019_01_04_GBl_Nr_0001_signed.pdf|S. 1 - 4| Verordnung über Zuständigkeiten von Amtsgerichten|dict|