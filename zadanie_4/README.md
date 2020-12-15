# Zadanie 2

## GET (metoda)

### /calendar/\<year\>/\<month\>

Endpoint zwraca plik iCalendar dla podanego miesiąca oraz roku. 

#### Parametry:
<b>year</b>: rok, dla któego pobieramy kalendarz, <i>typ: liczba całkowita</i>
<b>month</b>: miesiąc, dla któego pobieramy kalendarz, <i>typ: liczba całkowita, zakres: \<1-12\></i>

<b>Przykładowa odpowiedź</b>: 

Plik w formacie .ics, format nazwy: weeia_\<year\>_\<month\>.ics, przykład: weeia_2020_10.ics

##### Przykład:

```
    http://localhost/calendar/2020/10
```

Odpowiedź:

Plik: weeia_2020_10.ics, zawartość:

```
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//WEEIA calendar 10-2020//mxm.dk//
BEGIN:VEVENT
SUMMARY:Akcja Integracja Online
DTSTART;TZID=Europe/Warsaw;VALUE=DATE-TIME:20201001T000000
DTEND;TZID=Europe/Warsaw;VALUE=DATE-TIME:20201001T235900
DTSTAMP;VALUE=DATE-TIME:20201201T144911Z
UID:2020-10-01_00:00:00_CEST+0200@mxm.dk
END:VEVENT
BEGIN:VEVENT
SUMMARY:Wielka Integracja WIP
DTSTART;TZID=Europe/Warsaw;VALUE=DATE-TIME:20201008T000000
DTEND;TZID=Europe/Warsaw;VALUE=DATE-TIME:20201008T235900
DTSTAMP;VALUE=DATE-TIME:20201201T144911Z
UID:2020-10-08_00:00:00_CEST+0200@mxm.dk
END:VEVENT
BEGIN:VEVENT
SUMMARY:Wielka Integracja WIP
DTSTART;TZID=Europe/Warsaw;VALUE=DATE-TIME:20201009T000000
DTEND;TZID=Europe/Warsaw;VALUE=DATE-TIME:20201009T235900
DTSTAMP;VALUE=DATE-TIME:20201201T144911Z
UID:2020-10-09_00:00:00_CEST+0200@mxm.dk
END:VEVENT
BEGIN:VEVENT
SUMMARY:Wielka Integracja WIP
DTSTART;TZID=Europe/Warsaw;VALUE=DATE-TIME:20201010T000000
DTEND;TZID=Europe/Warsaw;VALUE=DATE-TIME:20201010T235900
DTSTAMP;VALUE=DATE-TIME:20201201T144911Z
UID:2020-10-10_00:00:00_CEST+0200@mxm.dk
END:VEVENT
END:VCALENDAR
```

### /calendar

Endpoint zwraca plik iCalendar dla aktualnego miesiąca oraz roku. 

<b>Przykładowa odpowiedź</b>: 

Plik w formacie .ics, format nazwy: weeia_\<year\>_\<month\>.ics, przykład: weeia_2020_10.ics

##### Przykład:

```
    http://localhost/calendar
```

Odpowiedź:

Plik: weeia_2020_12.ics, zawartość:

```
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//WEEIA calendar 12-2020//mxm.dk//
END:VCALENDAR
```

## NOT SUPPORTED ENDPOINT

API zwraca kod błędu <b><i>415</i></b>.

## VALIDATION ERROR

API zwraca kod błędu <b><i>404</i></b> i `ERROR, given year or month is not correct data, please, check out and try again.`.