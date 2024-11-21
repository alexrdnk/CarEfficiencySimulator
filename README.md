# Temat projektu

## Railway System Maintenance Simulator

Ten kod projektu to platforma symulacyjna do analizy niezawodności i opłacalności różnych polityk utrzymania ruchu w systemie kolejowym. Oblicza kluczowe wskaźniki, takie jak dostępność, przestoje, koszty utrzymania i miary niezawodności (MTBF, MTTR), symulując proces awarii i napraw przy użyciu rozkładu Weibulla. Po uruchomieniu symulacji, kod zapisuje wyniki do pliku CSV i generuje wizualne porównania między politykami.

## Funkcje

- **Dostosowywalne Strategie Konserwacji:**
  Symulator obsługuje różne strategie konserwacji, takie jak konserwacja prewencyjna, reaktywna i predykcyjna, które można łatwo konfigurować i testować.
  
- **Śledzenie i Rejestrowanie Danych:**
  Podczas symulacji zbierane są szczegółowe dane dotyczące awarii, kosztów utrzymania, czasów przestojów i innych metryk, które mogą być zapisane do pliku CSV.

- **Metryki Wydajności:**
  Po każdej symulacji generowane są metryki takie jak MTBF, MTTR, dostępność systemu oraz koszty konserwacji, które są analizowane i przedstawiane w formie wykresów.

- **Analiza Symulacji:**
  Symulator umożliwia uruchamianie wielu symulacji, agregowanie wyników oraz wizualizację danych w postaci wykresów porównujących efektywność różnych polityk konserwacji.

---

## Użytkowanie

Po uruchomieniu programu, symulator przeprowadzi serię symulacji na podstawie zdefiniowanych strategii konserwacji. Wyniki zostaną zapisane do pliku CSV, a także wygenerowane wykresy, które pozwolą na wizualną analizę wyników. 

Plik konfiguracyjny `maintenance_policies.json` zawiera wszystkie ustawienia dotyczące polityk konserwacji, czasów awarii, kosztów napraw oraz innych parametrów, które można łatwo dostosować.

---

## Obsługa Danych

- **Dane wejściowe:**
  - Plik konfiguracyjny JSON zawierający definicje polityk konserwacji, czasów użytkowania, kosztów, oraz innych parametrów.
  - Wartości wejściowe do symulacji, takie jak czas symulacji, liczba symulacji, oraz cele SLA.

- **Generowane dane:**
  - Symulator generuje dane dotyczące awarii, kosztów konserwacji, oraz czasów przestojów.
  - Wyniki symulacji zawierają metryki, takie jak średni czas do awarii (MTBF), średni czas naprawy (MTTR), średni czas przestoju, oraz dostępność systemu.

- **Wizualizacja:**
  - Generowane są wykresy porównujące różne polityki konserwacji pod względem dostępności, kosztów konserwacji, czasu przestoju, oraz liczby wymian komponentów.
  - Wykresy są zapisywane w pliku `maintenance_policy_comparison.png`.

---

## Autorzy

- **Oleksandr Radionenko**
- **Bohdan Stepanenko**
- **Mykhailo Dek**



