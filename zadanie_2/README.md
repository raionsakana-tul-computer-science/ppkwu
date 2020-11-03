# Zadanie 2

## GET (metoda)

### /all-characters/\<text\>

Endpoint zwraca informację o ilości wystąpięń wszystkich obłsugiwanych znaków.

<b>Przykładowa odpowiedź<b>:
```json
{
  "big-letters": 0,
  "small-letters": 0,
  "numbers": 0,
  "special-characters": 0
}
```

### /big-letters/\<text\>

Endpoint zwraca informację o ilości wystąpięń wielkich liter.

<b>Przykładowa odpowiedź<b>:
```json
{
  "big-letters": 0
}
```

### /small-letters/\<text\>

Endpoint zwraca informację o ilości wystąpięń małych liter.

<b>Przykładowa odpowiedź<b>:
```json
{
  "small-letters": 0
}
```

### /numbers/\<text\>

Endpoint zwraca informację o ilości wystąpięń liczb w ciągu znaków.

<b>Przykładowa odpowiedź<b>:
```json
{
  "numbers": 0
}
```

### /special-characters/\<text\>

Endpoint zwraca informację o ilości wystąpięń znaków specjalnych w ciągu znaków.

<b>Przykładowa odpowiedź<b>:
```json
{
  "special-characters": 0
}
```

## NOT SUPPORTED ENDPOINT

API zwraca kod błędu <b><i>415</i></b>.