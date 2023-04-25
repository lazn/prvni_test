# laznicek, 2023_04_25
# pokus 04 - namaluji ctverecek i sestiuhelnik
# tento soubor vyzaduje daleko podrobnejsi komentare

# prazdna zkusebni funkce
for _ in range (10):
    pass

import turtle

# kresleni ctverce pomoci modulu turtle
for _ in range (4):
    turtle.forward(100)
    turtle.left(90)

# kresleni sestiuhelniku pomoci modulu turtle
for _ in range (6):
    turtle.forward(100)
    turtle.left(60)

# okno s obrazkem se zavre po klepnuti mysi
turtle.exitonclick()    