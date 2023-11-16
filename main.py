class Elev:
    def __init__ (self, name, clasa, list = []):
        self.name = name
        self.clasa = clasa
        self.materii = list
    def __repr__(self):
        return self.name + " " + str(self.clasa)

class Materie:
    def __init__(self, nume_materie, nume_profesor, tip_evaluare, sala_curs, lista_elevi_participanti = []):
        self.nume_materie = nume_materie
        self.nume_profesor = nume_profesor
        self.tip_evaluare = tip_evaluare
        self.sala_curs = sala_curs
        self.lista_elevi_participanti = lista_elevi_participanti

class Evaluare:
    def __init__(self, elevul, materia, nota_obtinuta):
        self.elevul = elevul
        self.materia = materia
        self.nota_obtinuta = nota_obtinuta
        self.admitere = None
    
        
    # daca vrem sa oprim: x = True -> schimbam apoi in False cand utilizam una din optinui
x = Elev("Mirel Radoi", 12)
elevi = {}
while True:
    
    print("1) Add a new student. ")       
    print("2) Add a new subject. ")       
    print("3) Add a student to the list of a subject. ")        
    print("4) Print students that attend a specific subject. ")
    print("5) Add a grade for a student at a subject. ")
    print("6) Print student with highest grades. ")
    print("7) Print CORINGET students. ")
    print("8) EXIT")

    x = True
    while x:

        alegere_client = input("\nAlege dintre variantele de mai sus pentru a folosi catalogul electronic: ")
        # alegere_client = alegere_client.strip()
        if alegere_client.isdigit() and 1 <= float(alegere_client) <= 8:
            break  # Break out of the inner loop if a valid choice is entered
        else:
            print(" ")
            print("Invalid choice. Please chose a number between 1 and 8.")
            print(" ")

    match alegere_client:
        case "1":
            elev = Elev(input("\nIntroduceti numele: "),int(input("\nIntroduceti varsta: ")))
            print("Elevul introdus: {}".format(elev))
        case "2":
            print(" ")
            print(2)
            print(" ")
        case "3":
            print(" ")
            print(3)
            print(" ")
        case "4":
            print(" ")
            print(4)
            print(" ")
        case "5":
            print(" ")
            print(5)
            print(" ")
        case "6":
            print(" ")
            print(6)
            print(" ")
        case "7":
            print(" ")
            print(7)
            print(" ")
        case "8":
            print("Exit...")
            break

            


    
    

    