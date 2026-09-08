# Performance Test
## Vecka 36
<br>

### Status uppgifter

| Uppgift                         | Status | 🟠🟡🟢 |
|---------------------------------|--------|--------|
| 0 Projektstruktur               | 100%   | 🟢     |
| 1 Diskutera tillsammans         | 100%   | 🟢     |
| 2 Prestandatest: insertion sort | 100%   | 🟢     |
| 3 Prestandatest: merge sort     | 100%   | 🟢     |

<br>

> **_1 Diskutera tillsammans:_**
> 1. Vad är en regression? När inträffar de oftast under ett projekts livstid? <br>
Regression är en försämring. En regression inträffar när ny funktionalitet som laddats upp förstör befintlig funktionalitet. <br><br>
> 2. Vad är skillnaden mellan enhetstest och regressionstest? <br>
Ett enhetstest gör man egentligen bara när en ny funktion har byggts för att testa funktionaliteten. <br> Ett regressionstest innebär att man testar funktionaliteten på befintliga funktioner för att se till att de inte slutar fungera efter att ny kod introducerats. <br><br>
> 3. Vilka krav på git-kunskap kräver det av utvecklare att jobba med CI? <br>
Grundläggande förståelse för versionshantering. Fetch, pull, merge, rebase. Lösa merge-konflikter. <br> Kunna återställa egna misstag på ett enkelt sätt med git revert. <br> Hur CI-konfigurationen i repot fungerar.
Man ska kunna hålla sin branch ren. Kunna använda CI-logger för att rätta problem. <br><br>
>4. Vad är en feature? Hur förhåller det sig till kraven? <br>
En feature är en funktion. <br><br>
>5. Vilka fördelar får en kund av att utvecklarna jobbar med CD? <br>
Efterfrågade funktioner kommer snabbare ut i produktion. En stor kund kan även påverka vad som ska prioriteras. <br><br>
>6. Vilka fördelar får utvecklare av att jobba med CD? <br>
Continious Delivery innebär att man har en relativt tät frekvens på utrullningar och det i sin tur gör att det blir mindre kod att rulla ut vid varje release. <br> Det blir mindre att förbereda och det är enklare att hålla koll på koden. Smidig rollback ifall fel uppstår. <br><br>
>7. Varför kan man inte veta exakt hur lång tid det kommer ta att köra kod? <br>
Hastigheten påverkas av bakomliggande hårdvara och processer. <br><br>
>8. Varför skriver man till exempel O(n) men inte O(2*n + 10)? <br>
Det är meningslöst att skriva O(2*n +10) eftersom 2*n kommer växa linjärt liksom n. Konstanten 10 kommer inte visa någon nyttig information när n blir stor. <br> Det viktigaste är att vissa formen på tillväxten - inte den exakta tiden.




> **_2.4 - Diagram:_**<br>
> För att rita diagrammet. Kör prestandatest.main.

>**_3.1 - Vad har funktionerna för tidskomplexitet?:_** <br>
Insertion sort O(N^2) (Kvadratisk) - Dåligt för stora datamängder <br>
Merge sort O(N) (Linjär) - Bättre för stora datamängder


>**_Visualisering:_**<br>
> 
<img width="791" height="476" alt="Image" src="https://github.com/user-attachments/assets/2ffacd8b-e3db-4482-be4b-b58498fbf265" />