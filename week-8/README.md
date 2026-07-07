## 📌 Nädal 8: Python APIs

---

### 👤 Minu roll

**Roll A + B – API Query & Data Processing**

---

### 🌐 Roll A – API Query (Andmete pärimine)

**Eesmärk:** Luua Pythoni funktsioonid UrbanStyle OÜ müügi-, kliendi- ja tooteandmete pärimiseks Supabase API kaudu.

#### Minu panus

- Lõin faili **`data_fetcher.py`**
- Ühendasin rakenduse **Supabase** andmebaasiga kasutades **`.env`** faili
- Arendasin kolm andmete pärimise funktsiooni:
  - `fetch_sales()`
  - `fetch_customers()`
  - `fetch_products()`
- Lisasin **pagination'i** suurte andmemahtude laadimiseks
- Rakendasin **veakäsitluse**
- Tagastasin andmed **pandas DataFrame'idena** edasiseks analüüsiks

#### Tulemused

| Andmestik | Kirjete arv |
|-----------|------------:|
| 📊 Sales | **5 137** |
| 👥 Customers | **3 150** |
| 📦 Products | **362** |

---

### ⚙️ Roll B – Data Processing (Andmete töötlemine)

**Eesmärk:** Puhastada andmed, arvutada KPI-d ning valmistada andmestik ette analüüsiks ja visualiseerimiseks.

#### Minu panus

- Andmete puhastamine (duplikaadid, NULL-väärtused, kuupäevade teisendamine)
- Nädalaste koondnäitajate arvutamine
- KPI-de arvutamine
- Müügi- ja kliendiandmete ühendamine
- Analüüsiks valmis andmestiku loomine

#### Tulemused

| KPI | Tulemus |
|-----|---------:|
| 📊 Puhastatud müügikirjed | **3** *(1 duplikaat eemaldati)* |
| 💰 Kogukäive | **450 €** |
| 👥 Unikaalsed kliendid | **3** |
| 🛒 Keskmine tellimuse väärtus | **150 €** |

---

### 🤖 AI kasutamine

Kasutasin ChatGPT-d, et:

- aidata kirjutada Pythoni koodi;
- leida ja parandada vigasid (debugging);
- täiustada funktsioonide ülesehitust;
- koostada projekti kokkuvõtteid ja dokumentatsiooni.

---

### 🛠 Omandatud oskused

- REST API päringud Pythonis
- Supabase API kasutamine
- `.env` failide ja keskkonnamuutujate kasutamine
- pandas DataFrame'ide töötlemine
- ETL-andmepipeline'i alused
- Andmete puhastamine ja KPI-de arvutamine
- Veakäsitlus ja pagination

---

### 📁 Failid

- [`data fetcher`](data_fetcher.py)
- [`pipeline`](pipeline.py)
- [`transform`](transform.py)

---

## 👥 Meeskonnatöö

📊 **Meeskonna töö:** [`dokument`](https://docs.google.com/presentation/d/1kJtM9jM5cdKQg91xikcIb1fakwzNAihSeg23QVzBWsg/edit?slide=id.g3ef495ecc6a_0_548#slide=id.g3ef495ecc6a_0_548)

---
