SELECT * FROM sales LIMIT 10;


SELECT sale_id, customer_id, total_price
FROM sales
ORDER BY total_price DESC
LIMIT 10;


SELECT COUNT(*) AS ridu_kokku
FROM sales;


--Mõnikord on veergude nimed pikad või ebaselged. AS loob ajutise nime (alias) ehk nt 'customer_id' muudeti väljund tabelis 'klient'.
SELECT
    customer_id AS klient,
    total_price AS summa,
    sale_date AS kuupäev
FROM sales;


--ORDER BY sorteerib tulemused veeru järgi
-- Väiksemast suuremani (vaikimisi)
SELECT customer_id, total_price
FROM sales
ORDER BY total_price;


-- Suuremast väiksemani
SELECT customer_id, total_price
FROM sales
ORDER BY total_price DESC;


-- 5 väikseimat müüki: kõige väiksem summa -1405,32
SELECT sale_id, total_price AS summa
FROM sales
ORDER BY total_price
LIMIT 5;


--Ülesanne: Toomas tahab näha tellimuste loetelu koos kliendi ID, kuupäeva ja summaga — sorteerituna kuupäeva järgi (uuemad enne). Kirjuta see päring ise. Kasuta LIMIT 20, et mitte kogu tabelit väljastada.
SELECT customer_id, sale_date, total_price
FROM sales
ORDER BY sale_date
LIMIT 20;