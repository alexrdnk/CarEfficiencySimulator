# Ekonomiczna Ocena Efektywności Utrzymania Floty Carsharingowej

Projekt ten wykorzystuje symulacje w Pythonie do generowania zestawów danych dotyczących różnych predefiniowanych strategii konserwacji pojazdów floty. Wygenerowane zbiory danych, obejmujące symulacje o różnych okresach trwania, są zapisywane w formacie CSV. Następnie dane te są analizowane i wizualizowane przy użyciu bibliotek takich jak matplotlib i pandas, co umożliwia szczegółową ocenę efektywności strategii konserwacyjnych.

---

## Funkcje

- **Dostosowywalne Strategie Konserwacji:**
  - Symulacja różnych podejść do konserwacji (reaktywna, prewencyjna lub mieszana).
  - Ocena wpływu strategii konserwacyjnych na ogólną wydajność floty.
  
- **Śledzenie i Rejestrowanie Danych:**
  - Śledzi czas użytkowania pojazdów, okresy konserwacji, koszty napraw oraz wymianę pojazdów.
  - Rejestruje czas przestoju operacyjnego i wskaźniki dostępności usług.
  
- **Metryki Wydajności:**
  - Oblicza dostępność floty.
  - Ocenia efektywność ekonomiczną i niezawodność komponentów w czasie.

- **Analiza Symulacji:**
  - Generuje pliki CSV z szczegółowymi danymi z każdej symulacji.
  - Zapewnia szczegółowy podział kosztów i efektywności floty.

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
   NONE
    ```

---

## Użytkowanie

### 1. Konfiguracja Symulacji
- **Wybór Strategii:** Wybierz między konserwacją reaktywną, prewencyjną lub mieszaną.
- **Parametry Pojazdu:** Ustaw czas użytkowania pojazdu, interwały konserwacji oraz modele starzenia komponentów.

### 2. Uruchom Symulację
Po konfiguracji, uruchom symulację. Wygenerowany zostanie plik CSV z metrykami wydajności i podziałem kosztów dla wybranej strategii konserwacji.

### 3. Analizuj Wyniki
Użyj wygenerowanych plików CSV do analizy skuteczności każdej strategii. Analizę można przeprowadzić za pomocą bibliotek takich jak **pandas** do manipulacji danymi oraz **matplotlib** do wizualizacji.

---

## Obsługa Danych

- **Dane wejściowe:**
  - Zdefiniowane przez konfiguracje użytkownika, w tym czas użytkowania pojazdu, czas naprawy oraz interwały konserwacji.
  
- **Generowane dane:**
  - Pliki CSV zawierające okresy działania pojazdu, koszty konserwacji oraz wskaźniki dostępności floty.
  
- **Wizualizacja:**
  - Skorzystaj z dołączonych skryptów do generowania wykresów z danych symulacyjnych, pokazujących ekonomiczny wpływ różnych strategii konserwacyjnych.

---

## Autorzy

- **Oleksandr Radionenko**
- **Bohdan Stepanenko**
- **Mykhailo Dek**


