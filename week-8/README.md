## Nädal 8: Python APIs

### Minu roll
[Roll A+B]: [API Query + Data Processing]

### **Roll A - API Query** (Andmete pärimine)  
**ÜLESANNE**: Loo Python funktsioonid, mis pärivad UrbanStyle OÜ andmed
Supabase API-st: müügi-, kliendi- ja tooteandmed.

- Lõin Pythoni faili data_fetcher.py  
- Ühendasin programmi Supabase andmebaasiga .env faili abil  
- Lõin 3 funktsiooni:  
  - fetch_sales()
  - fetch_customers()
  - fetch_products() 
- Lisasin pagination'i ja veakäsitluse
- Tulemuseks on pandas DataFrame'id, mida saab kasutada edasiseks analüüsiks  
- Päringu tulemused:
  - 📊 Sales: 5137 rida
  - 👥 Customers: 3150 rida
  - 📦 Products: 362 rida  
    
### **Roll B - Data Processing** (Andmete töötlemine)  
**ÜLESANNE**: Kirjuta transformeerimisfunktsioonid: puhasta andmed,
arvuta nädalased koondnäitajad ja KPI-d, liida andmestikud.
Marko tahab nähtavaid numbreid — mitte toorandmeid.  

- Andmete puhastamine (duplikaadid, NULL-id, kuupäevad)
- Nädalaste koond näitajate arvutamine
- KPI-de arvutamine
- Müügi- ja kliendiandmete liitmine
- Päringu tulemused:  
  - 📊 Puhastatud andmestik: 3 müügikirjet (1 duplikaat eemaldati)
  - 💰 Kogukäive: 450 €
  - 👥 Unikaalseid kliente: 3
  - 🛒 Keskmine tellimuse väärtus: 150 €

### AI kasutamine
[1-2 lauset, kuidas AI aitas sel nädalal]
ChatGPT aitas teha vajalikud koodid, vajadusel leida erroritele põhjuseid ning teha kokkuvõtted

## Meeskonna töö
- [Link meeskonna Data Landscape slaidile] https://docs.google.com/presentation/d/1kJtM9jM5cdKQg91xikcIb1fakwzNAihSeg23QVzBWsg/edit?slide=id.g3ef495ecc6a_0_548#slide=id.g3ef495ecc6a_0_548
