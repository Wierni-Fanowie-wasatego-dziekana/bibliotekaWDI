**Cele**
Biblioteka została stworzona aby ułatwić pisanie zadań z przedmiotu Wstęp do Informatyki i ograniczyć
monotonne przepisywanie podstawowych funkcji

**UWAGA**
Zalecamy nie używać tej biblioteki przed pierwszym kolokwium

**Instalacja**
Linuksiarze(do wora i do jeziora)
**pip3 install -U garus.py**
Windows:
**pip install -U garus.py**

**Komendy**

*nwd(int a, int b)* - (treść oczywista)

*nww(int a, int b)* - (treść oczywista)

*is_prime(int a)* - (treść oczywista)

*rebase(int liczba, int baza_docelowa)* - funkcja konwertującą liczbę w system liczbowy o dowolnej podstawie (2-16)
(UWAGA dla systemów większych od 10 funkcja zwraca typ string!)

*number_count(int number, int base, int counted_digit)* - funkcja zliczająca wystąpienia podanej cyfry w podanej liczbie zapisanej w podanym systemie (2-10)

*reverse_number(int a)* - odwraca kolejność cyfr w liczbie

*class Node* - Podstawowa klasa przeznaczona głównie do zadań z list odsyłaczowych posiadająca następujące metody:

    *add(int a)* - dodaje liczbę do końca listy

    *add_list(int T)* - dodaje liczby z tablicy zaczynając od końca listy

    *remove(int a)* - usuwa pierwsze wystąpienie liczby z listy

    *reverse_list()* - metoda zwraca odwróconą listę (UWAGA, lista na której wywołuje się metodę zostaje bez zmian)

    *is_present(int a)* - sprawdza czy dana liczba występuje w liście

    *print_list()* - wypisuje całą listę w terminalu


**PRZYKŁADY UŻYCIA**
nwd(8,4) # wypisze 4
nww(8,4) # wypisze 8
is_prime(77) # zwróci False
rebase(101, 2) # zwróci 1100101
number_count(213769420, 10, 2) # zwróci 2
reverse_number(21) # zwróci 12

lista = Node(2) # stworzy węzeł z value = 2
lista.add(3) # do wyżej stworzonego węzła dołączy węzeł z value = 3
lista.add_list([1,2,3,4,5]) # do wyżej stworzonego węzła dołączy tabelę w formię listy połączonej
lista.remove(3) # usunie pierwszy napotkany węzeł z value = 3, w tym przypadku drugi
lista=lista.reverse_list() # odwróci kolejność wyżej utworzonej listy połączonej
lista.is_present(3) # zwróci True, ponieważ mimo usuniętej pierwszego węzła z value = 3, występuje później jeszcze drugi
lista.print_list() # wypisze całą zawartość value listy, każdą w nowej linijce