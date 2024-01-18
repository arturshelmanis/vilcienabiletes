# Projekta darbs
### Projekta uzdevums
Uzdevums ir izveidot pilnvērtīgu programmatūru, kas varētu automatizēt vienu no izmaksu komponenšu uzskaitēm - transporta izdevumus. Projekta autors ikdienā pārvietojas ar vilcienu, pērkot biļetes Mobilly aplikācijā, taču izmaksu uzskaiti ir grūti veikt, jo vispirms finanšu līdzekļi ir jāpārskaita uz Mobilly aplikāciju un tikai tad var tikt veikta biļešu pirkšana. Mobilly nopirktās biļetes sūta uz e-pastu, kā PDF failu. Šis PDF fails satur informāciju par veikto braucienu (Maršruts, Laiks, Cena). Lai sasniegtu projekta darba mērķi, ir jāatrod veids, kā automatizēti var lejupielādēt biļetes no e-pasta, veikt PDF failu lasīšanu un informācijas saglabāšanu Excel (.xlsx) datnē, vienkāršotai izmaksu pārskatīšanai.
### Izmantotās Python bibliotēkas
* imaplib - tiek izmantots, lai varētu savienoties ar e-pastu, izmantojot IMAP protokolu
* email - tiek izmantots, lai varētu apstrādāt e-pasta vēstules
* os - tiek izmantots, lai varētu izveidot mapi un norādīt, kurā mapē nepieciešams saglabāt PDF failus
* datetime - tiek izmantots, lai varētu pārvēst lietotāja ievadītu datumu par imaplib un pandas bibliotēkai saprotamu datu formātu
* pandas - tiek izmantots, lai izveidotu sarakstu, kurā ietilpst katrs mēnesis, no lietotāja ievadītajam sākuma datumam līdz beigu datumam
* PyPDF2 - tiek izmantots, lai varētu lasīt PDF failā esošo tekstu
* pathlib - tiek izmantots, lai varētu norādīt, kurā mapē ir saglabāti PDF faili, lai pēc tam varētu šos failus nolasīt ar PyPDF2
* openpyxl - tiek izmantots, lai varētu izveidot EXCEL (.xlsx) datni un rakstīt tajā
### Progrmammatūras izmantošanas metodes
