# user_management

# Tutorial: System Zarządzania Użytkownikami - `user_management.py`

## Struktura plików i branchy

- **`feature/password_validation`**: Gałąź do implementacji funkcji walidacji haseł.

## Nazwy funkcji:
- `add_user(user_data)`: Dodaje nowego użytkownika.
- `remove_user(user_id)`: Usuwa istniejącego użytkownika.
- `edit_user(user_id, updated_data)`: Edytuje dane użytkownika.
- `validate_nip(nip)`: Waliduje numer NIP.
- `validate_pesel(pesel)`: Waliduje numer PESEL.
- `validate_regon(regon)`: Waliduje numer REGON.
- `generate_password()`: Generuje silne hasło.
- `validate_password(password)`: Waliduje siłę hasła.

## Sprint 2: Walidacja i Bezpieczeństwo

### Milestone 2: Generowanie i walidacja haseł

#### Funkcja `validate_password(password)`
- Implementuj funkcję walidującą siłę hasła, sprawdzając, czy spełnia minimalne wymagania (długość, złożoność, brak popularnych wzorców).

---

## Sprint 3: Testowanie i Dokumentacja

### Milestone 1: Testowanie funkcjonalności
#### Testowanie dodawania i edycji użytkowników
- Sprawdź scenariusze, takie jak brak pliku `users.json`, usuwanie nieistniejącego użytkownika itp.

### Milestone 3: Dokumentacja
#### Przygotuj dokumentację
- Utwórz plik `README.md`, opisując kroki instalacji oraz używania programu.
- Dodaj instrukcje dotyczące dodawania, edycji, usuwania użytkowników oraz wymagania dotyczące walidacji.
- Wymień najlepsze praktyki dotyczące zarządzania danymi użytkowników, w tym bezpieczeństwo haseł oraz przechowywanie danych osobowych.