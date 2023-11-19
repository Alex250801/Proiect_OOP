class Elev:
    def __init__(self, name, clasa, lista_materii_studenti=None):
        self.name = name
        self.clasa = clasa
        self.materii = lista_materii_studenti if lista_materii_studenti is not None else []

    def add_student_to_subject(self, materie):
        self.materii.append(materie)

    def __repr__(self):
        return self.name + " " + str(self.clasa)

class Materie:
    def __init__(self, nume_materie, nume_profesor, tip_evaluare, sala_curs, lista_elevi_participanti=None):
        self.nume_materie = nume_materie
        self.nume_profesor = nume_profesor
        self.tip_evaluare = tip_evaluare
        self.sala_curs = sala_curs
        self.lista_elevi_participanti = lista_elevi_participanti if lista_elevi_participanti is not None else []

    def add_subject_to_student(self, elev):
        self.lista_elevi_participanti.append(elev)

    def __repr__(self):
        return self.nume_materie

class Evaluare:
    def __init__(self, elevul, materia, nota_obtinuta):
        self.elevul = elevul
        self.materia = materia
        self.nota_obtinuta = nota_obtinuta
        self.admitere = None

studenti = []
materii = []
studenti_dic= {}  

while True:
    print("1) Add a new student.")
    print("2) Add a new subject.")
    print("3) Add a student to the list of a subject.")
    print("4) Print students that attend a specific subject.")
    print("5) Add a grade for a student at a subject.")
    print("6) Print student with the highest grades.")
    print("7) Print CORINGET students.")
    print("8) EXIT")

    x = True
    while x:
        alegere_client = input("\nAlege dintre variantele de mai sus pentru a folosi catalogul electronic: ")

        if alegere_client.isdigit() and 1 <= float(alegere_client) <= 8:
            break
        else:
            print(" ")
            print("Invalid choice. Please choose a number between 1 and 8.")
            print(" ")

    match alegere_client:
        case "1":
            nume = input("\nIntroduceti numele elevului: ")
            clasa = input("\nIntroduceti clasa elevului: ")
            elev_nou = Elev(nume, clasa)
            studenti.append(elev_nou.name)
            studenti_dic[elev_nou.name] = elev_nou 
            print("\nElevul introdus: {}, clasa {}".format(elev_nou.name, elev_nou.clasa))
            print("\nLista cu studentii: {}".format(studenti))
            print(studenti_dic)
            print(" ")

        case "2":
            nume_materie = input("\nIntroduceti numele materiei: ")
            profesor = input("\nIntroduceti numele profesorului: ")
            tip_evaluare = input("\nIntroduceti tipul de evaluare: ")
            sala_curs = input("\nIntroduceti sala de curs: ")
            materie_noua = Materie(nume_materie, profesor, tip_evaluare, sala_curs)
            materii.append(materie_noua)
            print("\nMateria introdusa: {}".format(materie_noua))
            print("\nLista cu materii: {}".format(materii))
            print(" ")

        case "3":
            print("\nLista elevilor:")
            for i, elev in enumerate(studenti):
                print("{}. {}".format(i, elev))

            elev_index = int(input("\nIntroduceti indexul elevului: "))
            
            print("\nLista materiilor:")
            for i, materie in enumerate(materii):
                print("{}. {}".format(i, materie))

            materie_index = int(input("\nIntroduceti indexul materiei: "))

            elev_name = studenti[elev_index]
            materie = materii[materie_index]

            studenti_dic[elev_name].add_student_to_subject(materie)
            materie.add_subject_to_student(studenti_dic[elev_name])

            print("\nStudentul {} a fost adaugat la materia {}.".format(elev_name, materie.nume_materie))
            print("\nMateria {} a fost adaugata elevului {}.".format(materie.nume_materie, elev_name))
            print(" ")

        case "4":
            print("\nLista materiilor:")
            for i, materie in enumerate(materii):
                print(f"{i}. {materie}")

            materie_index = int(input("\nIntroduceti indexul materiei pentru a afisa elevii: "))

            materie = materii[materie_index]

            elevi_participanti = [student_name for student_name in studenti if materie in studenti_dic[student_name].materii]

            if elevi_participanti:
                print("\nElevii care participa la materia {}:".format(materie.nume_materie))
                for student_name in elevi_participanti:
                    print(student_name)
            else:
                print("\nNiciun elev nu participa la materia {}".format(materie.nume_materie))
            print(" ")

        case "5":
            # adaugare nota materie
            pass

        case "6":
            # elevul cu cele mai mari note(media notelor max)
            pass

        case "7":
            # corigent
            pass

        case "8":
            print("Exit...")
            break
