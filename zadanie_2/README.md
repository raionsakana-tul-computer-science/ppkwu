# Zadanie 2

## GET (metoda)

### /all-characters/\<text\>

Endpoint zwraca informację o ilości wystąpięń wszystkich obłsugiwanych znaków, liczbie ciągów takich znaków i listę zwierającej ilość znaków w ciągach.

<b>Przykładowa odpowiedź<b>:
```json
{
  "big-letters": {
    "count": 0,
    "number-of-strings": 0,
    "number-of-characters-in-string": [0]
  },
  "small-letters": {
    "count": 0,
    "number-of-strings": 0,
    "number-of-characters-in-string": [0]
  },
  "numbers": {
    "count": 0,
    "number-of-strings": 0,
    "number-of-characters-in-string": [0]
  },
  "special-characters": {
    "count": 0,
    "number-of-strings": 0,
    "number-of-characters-in-string": [0]
  }
}
```

### /big-letters/\<text\>

Endpoint zwraca informację o ilości wystąpięń wielkich liter, liczbie ciągów takich znaków i listę zwierającej ilość znaków w ciągach.

<b>Przykładowa odpowiedź<b>:
```json
{
  "count": 0,
  "number-of-strings": 0,
  "number-of-characters-in-string": [0]
}
```

### /small-letters/\<text\>

Endpoint zwraca informację o ilości wystąpięń małych liter, liczbie ciągów takich znaków i listę zwierającej ilość znaków w ciągach.

<b>Przykładowa odpowiedź<b>:
```json
{
  "count": 0,
  "number-of-strings": 0,
  "number-of-characters-in-string": [0]
}
```

### /numbers/\<text\>

Endpoint zwraca informację o ilości wystąpięń liczb w ciągu znaków, liczbie ciągów takich znaków i listę zwierającej ilość znaków w ciągach.

<b>Przykładowa odpowiedź<b>:
```json
{
  "count": 0,
  "number-of-strings": 0,
  "number-of-characters-in-string": [0]
}
```

### /special-characters/\<text\>

Endpoint zwraca informację o ilości wystąpięń znaków specjalnych w ciągu znaków, liczbie ciągów takich znaków i listę zwierającej ilość znaków w ciągach.

<b>Przykładowa odpowiedź<b>:
```json
{
  "count": 0,
  "number-of-strings": 0,
  "number-of-characters-in-string": [0]
}
```

## NOT SUPPORTED ENDPOINT

API zwraca kod błędu <b><i>415</i></b>.