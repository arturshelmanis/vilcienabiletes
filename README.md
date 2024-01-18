# Vilciena biļešu apstrāde
### Projekta uzdevums
Uzdevums ir izveidot pilnvērtīgu programmatūru, kas varētu automatizēt vienu no izmaksu komponenšu uzskaitēm - transporta izdevumus. Projekta autors ikdienā pārvietojas ar vilcienu, pērkot biļetes Mobilly aplikācijā, taču izmaksu uzskaiti ir grūti veikt, jo vispirms finanšu līdzekļi ir jāpārskaita uz Mobilly aplikāciju un tikai tad var tikt veikta biļešu pirkšana. Mobilly nopirktās biļetes sūta uz e-pastu, kā PDF failu. Šis PDF fails satur informāciju par veikto braucienu (Maršruts, Laiks, Cena). Lai sasniegtu projekta darba mērķi, ir jāatrod veids, kā automatizēti var lejupielādēt biļetes no e-pasta, veikt PDF failu lasīšanu un informācijas saglabāšanu Excel (.xlsx) datnē, vienkāršotai izmaksu pārskatīšanai.Projekts krietni atvieglos darbu finanšu līdzekļu uzskaitē.
### Izmantotās Python bibliotēkas
* imaplib - tiek izmantots, lai varētu savienoties ar e-pastu, izmantojot IMAP protokolu
* email - tiek izmantots, lai varētu apstrādāt e-pasta vēstules
* os - tiek izmantots, lai varētu izveidot mapi un norādīt, kurā mapē nepieciešams saglabāt PDF failus
* datetime - tiek izmantots, lai varētu pārvērst lietotāja ievadītu datumu par imaplib un pandas bibliotēkai saprotamu datu formātu
* pandas - tiek izmantots, lai izveidotu sarakstu, kurā ietilpst katrs mēnesis, no lietotāja ievadītajam sākuma datumam līdz beigu datumam
* PyPDF2 - tiek izmantots, lai varētu lasīt PDF failā esošo tekstu
* pathlib - tiek izmantots, lai varētu norādīt, kurā mapē ir saglabāti PDF faili, lai pēc tam varētu šos failus nolasīt ar PyPDF2
* openpyxl - tiek izmantots, lai varētu izveidot EXCEL (.xlsx) datni un rakstīt tajā
### Programmatūras izmantošanas metodes
Pirms sākat izmantot programmu ir nepieciešams veikt sekojošas darbības:
* Veikt izmaiņas failā **user_login**, mainīgā my_email vertībai piešķirt e-pasta adresi, no kuras nepieciešams lejupielādēt failus, mainīga password_key vērtībai piešķirt IMAP paroli
* Lai uzinstalētu vajadzīgās Python bibilotēkas, termināli nepieciešams iekopēt **pip install -r requirements.txt**. Ja nu gadījumā Jūs izmantojat vecāku python versiju, kādu bibliotēku var nākties instalēt atsevišķi terminālī ierakstot **pip install "bilbiotēkas nosaukums"**

Šo programmatūru var izmantot, lai apstrādātu vilciena biļetes, kas pirktas tieši Mobilly aplikācijā un tādā veidā atvieglotu finanšu līdzekļu uzskaiti. Manuāla darba vietā var palaist šo python skriptu, kas šo darbu spēj izdarīt vien pāris sekundēs.

Palaižot skriptu vispirms tiek paprasīts perioda sākuma un beigu datums konkrētā formātā, par kuru vēlaties iegūt datus. Tad mapē Vilciena_Biletes tiek lejupielādēti pielikumi, kas sūtīti no e-pasta adreses **info@mobilly.lv** ievadītajā laika periodā. Pēc tam tiek veikta informācijas nolasīšana no PDF faila, tiek nolasīta cena un datums, kurā konkrētais reiss ir veikts. Pēdējais posms ir informācijas ierakstīšana EXCEL datnē, uzskatāmā veidā. Reisi tiek sadalīti pa mēnešiem un par katru reisu tiek pievienota informācija, cik šis reiss ir izmaksājis. Tiek arī veikti aprēķini par braucienu skaitu mēnesī, kopējo summu, kas konkrētajā mēnesī ir samaksāta un vidējo cenu par braucienu. Visa informācija tiek saglabāta EXCEL failā **vilcienaizmaksas.xlsx**.

Programmatūru ir iespējams izmantot arī, lai nolasītu informāciju par jau ierīcē lejupielādētām vilciena biļetēm. Šajā gadījumā ir nepieciešams izkomentēt ārā daļu, kas ir paredzēta biļešu lejupielādēšanai no e-pasta un visas biļetes jāievieto mapē **Vilciena_Biletes**.
