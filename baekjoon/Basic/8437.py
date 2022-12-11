'''
==============================================================================================
@ Title: Julka
@ URL: https://www.acmicpc.net/problem/8437
@ Author: jopemachine
@ Created Date: 12/10/2022, 8:01:25 PM
@ Tags: arbitrary_precision arithmetic math
@ Level: Bronze 5
@ Description:
Julka zaskoczyła wczoraj w przedszkolu swoją wychowawczynię rozwiązując
następującą zagadkę: Klaudia i Natalia mają razem 10 jabłek, ale Klaudia ma
o 2 jabłka więcej niż Natalia. Ile jabłek ma każda z dziewczynek? Julka
odpowiedziała bez namysłu: Klaudia ma sześć jabłek, natomiast Natalia ma
cztery jabłka. Wychowywaczyni postanowiła sprawdzić, czy odpowiedź Julki
nie była przypadkowa i powtarzała zagadkę, za każdym razem zwiększając
liczby jabłek w zadaniu. Julka zawsze odpowiadała prawidłowo. Zaskoczona
wychowawczyni chciała kontynuować ,,badanie'' Julki, ale przy bardzo dużych
liczbach sama nie potrafiła szybko rozwiązać zagadki. Pomóż pani
przedszkolance i napisz program, który będzie podpowiadał jej rozwiązania.
Napisz program, który: wczyta (ze standardowego wejścia) liczbę jabłek,
które mają razem obie dziewczynki oraz o ile więcej jabłek ma Klaudia,
obliczy, ile jabłek ma Klaudia i ile jabłek ma Natalia, wypisze wynik (na
standardowe wyjście).
@ Input: Wejście składa się z dwóch wierszy. Pierwszy wiersz zawiera liczbę
wszystkich jabłek posiadanych przez dziewczynki, natomiast drugi - liczbę
mówiącą, o ile więcej jabłek ma Klaudia. Obie liczby są całkowite i
dodatnie. Wiadomo, że dziewczynki mają razem nie więcej niż 10100 (jedynka
i sto zer) jabłek. Jak widać, jabłka mogą być bardzo malutkie.
@ Output: Twój program powinien wypisać (na standardowe wyjście) w dwóch kolejnych
wierszach dwie liczby całkowite, po jednej w wierszu. Pierwszy wiersz
powinien zawierać liczbę jabłek Klaudii, natomiast drugi - liczbę jabłek
Natalii. Wiadomo, że dziewczynki zawsze mają całe jabłka.
==============================================================================================
'''

N = int(input())
K = int(input())

# A + B = N
# B + K = A

# B = A - K
# A = N - B = N - (A - K) = N - A + K
# A = (N + K) // 2
A = (N + K) // 2
B = A - K

print(A)
print(B)