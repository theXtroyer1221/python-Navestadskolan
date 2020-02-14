[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/theXtroyer1221/python-Navestadskolan) 

`Projekten programerades i Gitpod`
# Matte digital - Programmering

Olika uppgifter för programmering med språket python.

## Svar på uppgifter

### Uppgift 2.2

1. **a)** 26 cm **b)** 644 cm **c)** 26 dm 
 
```python
b = x
h = y
o = b+b+h+h
print(o)
```
c) uppgiften:
```python
b = 1 * 10
h = 3
o = b+b+h+h
print(o)
```

2. **a)** 15 **b)** -20

3. 
a)
```python
tal_1 = 25
tal_2 = 60
print("Produkten av", tal_1, "och", tal_2, "är", tal_1*tal_2)
```
```bash
Produkten av 25 och 60 är 1500
```
b)
```python
tal_1 = 97
tal_2 = 30
print("Kvoten av", tal_1, "och", tal_2, "är", tal_1/tal_2)
```
```bash
Kvoten av 97 och 30 är 3.2333333333333334
```
4.
```python
x = 10
y = 5
differens = x - y
print(differens)
```

5.
```python
sidan = 5
print(f"En kvadrat med sidan {sidan} centimeter har arean {sidan * sidan} kvadratcentimeter ")
```

6.
```python
b = 5
h = 10 
print(f"En triangel med basen {b} centimeter och höjden {h} har arean {b * h / 2}")
```

7. **svar:** Peter har sätt värded 3 och4 för variablerna bas och höjd. men han försökte använda de variabler i print() med stor bokstav. Python är skiftlägeskänslig (Case sensitive) det betyder att X är inte samma sak som x. Han måste skriva samma namn på alla variabler. 

8. **a)** 140km **b)** 275km **c)** 67.5km
```python
class app:
  def number(self, v, t):
    #En function som tar hastigheten och tiden och räknar ut sträckan
    s = float(v) * float(t)
    print(f"sträckan är {s} km")

print("Genom att ta tiden och hastigheten kan vi få fram sträckan, prova att sätta in nformationen för programmet")
hastighet = input("hastighet(km/h): ")
tiden = input("tiden(timme): ")
#tar upp inputen och skickar till functionen för att räckna ut
app.number(app, hastighet,tiden)
```
När programmet körs ser det ut så här.
```bash
linux bash python main.py
Genom att ta tiden och hastigheten kan vi få fram sträckan, prova att sätta in nformationen för programmet
hastighet(km/h): 70
tiden(timme): 2
sträckan är 140.0 km
```

9. 
```python
class app:
  def convert_cm_meter(self, number):
    #Detta function tar in "number" och multiplicerar med 100 
    mulnumber = float(number) / 100 
    print(f"{number}cm är {mulnumber}m")

print("Genom att dela med hundra får vi cm till m")
#input från användaren
cmmeter = input("hur mycket cm?: ")
app.convert_cm_meter(app, cmmeter)
```
```bash
Genom att dela med hundra får vi cm till m
hur mycket cm?: 100
100cm är 1.0m
```
---
## bidraganded
Pull requests är välkomna. För större ändringar, öppna en fråga först för att diskutera vad du vill ändra.

## License
[MIT](https://choosealicense.com/licenses/mit/)

> Jad Alnabki