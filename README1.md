# UrbanStyle Müügianalüüs ja RFM-Kliendisegmentatsioon

## Äriprobleem
UrbanStyle juhtkond vajas sisendit eeloleva aasta turunduseelarve planeerimiseks ja lojaalsusprogrammi muutmiseks, et lõpetada ebaefektiivsed pime-kampaaniad.

## Peamised järeldused ("So what?")
* Meie analüüs tuvastas, et kõigest 15% UrbanStyle'i püsiklientidest genereerib üle poole ettevõtte 1,09 miljoni eurosest kogukäibest.
* Q4 kampaania saavutas küll 35% müügikasvu, kuid stabiilse tulu tagamiseks tuleb turunduseelarve suunata otse kõige profitabiliimale kliendisegmendile (VIP-kliendid).

## Lähenemine ja tehniline pinurida
* **Andmebaas & valideerimine:** SQL (Supabase) ristikontrolliks ja päringuteks.
* **Andmete puhastamine:** Python (`pandas`) dublikaatide eemaldamiseks ja NULL-väärtuste korrastamiseks.
* **Analüüs & visuaal:** Power BI kvartiilipõhine RFM-mudel (Recency, Frequency, Monetary).

## Projektivisuaal
![UrbanStyle Dashboard](images/dashboard.png)

## Kuidas käivitada
1. Klooni repositoorium: `git clone <sinu-repo-link>`
2. Paigalda vajalikud teegid: `pip install -r requirements.txt`
3. Jooksuta andmetorustik: `python main.py`

## AI Kasutamine
Kasutasin Claude'i SQL päringu debugimiseks ja README teksti viimistlemiseks. Analüütiline loogika ja ärijäreldused on minu omad.
