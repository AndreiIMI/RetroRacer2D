# RetroRacer2D
Jocul se bazează pe controlul unei mașinuțe pe diferite circuite. Există trei circuite: Grassy Greens, Sandy Plains și Nightly Stroll, cu niveluri de dificultate variate (Grassy Greens: Ușor, Sandy Plains: Mediu, Nightly Stroll: Greu).

Am utilizat biblioteca Pygame pentru implementarea jocului și câteva trucuri specifice jocurilor de tipul Retro Racer (precum Out Run!). Acestea implică manipularea texturilor pentru a crea iluzia de 3D. Deși jocul și toate texturile din el sunt complet 2D, l-am putea descrie ca având un aspect pseudo 3D.

Mașina a fost implementată folosind trei texturi ale unei mașini pixelate. Aceasta poate accelera/decelera, se poate deplasa la stânga și la dreapta, și poate frâna. În cazul curbelor, mașina este "împinsă" spre exteriorul curbei pentru a simula o curba reală.

Instrucțiuni de rulare:

* Jocul poate fi rulat direct folosind "python3 meniu.py".
* De asemenea, jocul poate fi rulat folosind Makefile cu comenzile "make" sau "make start".

Controale: Folosiți săgețile pentru a controla mașina (și cam atât).

Contribuția fiecărui membru al echipei:

* Ignat Andrei: Meniu + Interfață utilizator.
* Ilie Nicolai și Iacob Andrei: Implementare sectiuni de circuit (drept, curba, deal/vale).
* Imireanu Andrei: Implementare mașină + texturi pentru circuit.
  
Dificultăți:

* Cea mai dificilă parte a fost implementarea sectiunilor de circuit și modul în care acestea interacționează cu mașina, necesitând multe încercări și erori până am obținut efectul dorit.

  
