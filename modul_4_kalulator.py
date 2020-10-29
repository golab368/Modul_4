
print("Program kalkulator, posługując się odpowiednią liczbą wybierz : 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie, Aby zakończyć program wpisz 10")
external_def_list = []
def values_1_2():
    value_1 = int(input("Tutaj podaj 1 liczbę do obliczeń : "))
    value_2 = int(input("Tutaj podaj 2 liczbę do obliczeń : "))
    external_def_list.append(value_1)
    external_def_list.append(value_2)

int_list_of_numbers_ready_to_be_added_or_multiply = []
def what_the_user_wants_to_for_addition_multiplication():
    print("Wypisz liczby, może być ich wiecej niż 2 \nWypisz je po spacji np. 1 2 3")
    what_the_user_wants_to_add_or_multiply = input()
    x = list(map(int, what_the_user_wants_to_add_or_multiply.split()))
    for i in x:
        int_list_of_numbers_ready_to_be_added_or_multiply.append(i)

while(True):
    what_user_want_to_do = input("Tutaj wpisz co chcesz zrobić : ")
    if what_user_want_to_do == "1":
        what_the_user_wants_to_for_addition_multiplication()
        print("Wynik dodawania to %s" % sum(int_list_of_numbers_ready_to_be_added_or_multiply))
    elif what_user_want_to_do == "2":
        values_1_2()
        subtraction_sum = external_def_list[0]-external_def_list[1]
        print("Wynik odejmowania to: %s " % subtraction_sum)        
    elif what_user_want_to_do == "3":
        what_the_user_wants_to_for_addition_multiplication()
        result = 1
        for i in int_list_of_numbers_ready_to_be_added_or_multiply:
            result = result * i 
        print("Wynik mnożenia to %s" % result )
    elif what_user_want_to_do == "4":
        values_1_2()
        if external_def_list[0] == 0:
            print("Nie dzielimy przez zero")
        else:
            division_sum = external_def_list[0]/external_def_list[1]
            print("Wynik dzielenia to: %s " % division_sum)  
    elif what_user_want_to_do == "10":
        print("Dziekuje do zobaczenia\n")
        break   
    else:
        print("podales cos z poza zakresu\nPodaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie, Koniec 10")
        





