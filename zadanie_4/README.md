# Zadanie 2

## GET (metoda)

### /get_v_card/\<name\>

Endpoint zwraca plik vCard dla wybranej firmy. 

#### Parametry:
<b>name</b>: nazwa firmy, dla której pobieramy vCard, <i>typ: tekst</i>

<b>Przykładowa odpowiedź</b>: 

Plik w formacie .vcf, format nazwy: \<nazwa_firmy\>.vcf, przykład: AdamKołotaUdrażnianierur.vcf

##### Przykład:

```
    http://localhost/get_v_card/AdamKołotaUdrażnianierur
```

Odpowiedź:

Plik: AdamKołotaUdrażnianierur.vcf, zawartość:

```
    BEGIN:VCARD
    VERSION:4.0
    ORG:Adam Kołota Udrażnianie rur
    TEL;TYPE=work;VALUE=uri:tel:+48 781 266 854
    EMAIL:joanna-kolota@wp.pl
    ADR;TYPE=WORK;LABEL="ul. Zaciszna 30A, 05-230 Kobyłka"
    URL:http://www.udraznianierurkobylka.pl
    END:VCARD
```

## POST (metoda)

### /search

Endpoint pozwala na wyszukiwanie firm, wykorzystwana przez stronę. Zwraca wyrenderowany plik index.html, wypełniony danymi

<b>Dane</b>: 
Nazwa formularza pobierana jest z formularza, szukany klucz: searching_key.