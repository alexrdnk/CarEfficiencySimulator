# Temat projektu

## Railway System Maintenance Simulator

Projekt ten służy do symulacji różnych strategii konserwacji systemu kolejowego, w celu oceny ich wpływu na dostępność, koszty i czas przestojów. Symulacje bazują na modelu Weibulla dla przewidywania czasów awarii, a wyniki zawierają metryki takie jak średni czas do awarii (MTBF), średni czas naprawy (MTTR), oraz koszty utrzymania.

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

## Instalacja i Konfiguracja

1. Sklonuj repozytorium:
    ```bash
    git clone https://github.com/alexrdnk/CarEfficiencySimulator.git
    ```

2. Zainstaluj wymagane biblioteki Pythona:
    ```bash
    pip install -r requirements.txt
    ```

3. Uruchom skrypt symulacyjny:
    ```bash
    python main.py
    ```

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



