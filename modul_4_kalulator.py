import logging
logging.basicConfig(level=logging.DEBUG)
print("Program kalkulator, posługując się odpowiednią liczbą wybierz : 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie, Aby zakończyć program wpisz 10")

while(True):
    what_user_want_to_do = input("Tutaj wpisz co chcesz zrobić : ")
    if what_user_want_to_do == "1":
        logging.debug("Wybrałeś dodawanie wypisz liczby które chcesz dodać może być ich wiecej niż 2 \nWypisz je po spacji np. 1 2 3 4")
        what_the_user_wants_to_add = input()
        int_list_of_numbers_ready_to_be_added = []
        x = list(map(int, what_the_user_wants_to_add.split()))
        for i in x:
            int_list_of_numbers_ready_to_be_added.append(i)
        logging.debug("Kalkulator dodaje teraz %s" % int_list_of_numbers_ready_to_be_added +"\n")
        print("Wynik dodawania to %s" % sum(int_list_of_numbers_ready_to_be_added))
    elif what_user_want_to_do == "2":
        value_1 = int(input("Tutaj podaj 1 liczbę do obliczeń : "))
        value_2 = int(input("Tutaj podaj 2 liczbę do obliczeń : "))
        subtraction_sum = value_1-value_2
        logging.debug("Kalkulator odejmuje teraz %s" % value_1 + " - %s" % value_2 + "\n")
        print("Wynik odejmowania to: %s " % subtraction_sum)        
    elif what_user_want_to_do == "3":
        logging.debug("Wybrałeś mnożenie wypisz liczby które chcesz pomnożyć może być ich wiecej niż 2 \nWypisz je po spacji np. 1 2 3 4")
        what_the_user_wants_to_add = input()
        int_list_of_numbers_ready_to_be_multiply = []
        x = list(map(int, what_the_user_wants_to_add.split()))
        for i in x:
            int_list_of_numbers_ready_to_be_multiply.append(i)
            result = 1
            for i in int_list_of_numbers_ready_to_be_multiply:
                result = result * i 
        logging.debug("Kalkulator mnoży teraz %s" % int_list_of_numbers_ready_to_be_multiply +"\n")
        print("Wynik dodawania to %s" % result )
    elif what_user_want_to_do == "4":
        value_1 = int(input("Tutaj podaj 1 liczbę do obliczeń : "))
        value_2 = int(input("Tutaj podaj 2 liczbę do obliczeń : "))
        if value_1 == 0:
            logging.debug("Nie dzielimy przez zero")
        else:
            division_sum = value_1/value_2
        logging.debug("Kalkulator dzieli teraz %s" % value_1 + " / %s" % value_2 + "\n")
        print("Wynik dzielenia to: %s " % subtraction_sum)  
    elif what_user_want_to_do == "10":
        print("Dziekuje do zobaczenia\n")
        break   
    else:
        logging.debug("podales cos z poza zakresu\n")
        print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie\nAby zakończyć program pisz 10")


