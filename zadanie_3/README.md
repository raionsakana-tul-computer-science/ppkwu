# Zadanie 2

## GET (metoda)

### /calendar/\<year\>/\<month\>

Endpoint zwraca plik iCalendar dla podanego miesiąca oraz roku. 

#### Parametry:
<b>year</b>: rok, dla któego pobieramy kalendarz, <i>typ: liczba całkowita</i>
<b>month</b>: miesiąc, dla któego pobieramy kalendarz, <i>typ: liczba całkowita, zakres: \<1-12\></i>

<b>Przykładowa odpowiedź</b>: 

Plik w formacie .ics, format nazwy: weeia_\<year\>_\<month\>.ics, przykład: weeia_2020_10.ics

### /calendar

Endpoint zwraca plik iCalendar dla aktualnego miesiąca oraz roku. 

<b>Przykładowa odpowiedź</b>: 

Plik w formacie .ics, format nazwy: weeia_\<year\>_\<month\>.ics, przykład: weeia_2020_10.ics



## NOT SUPPORTED ENDPOINT

API zwraca kod błędu <b><i>415</i></b>.