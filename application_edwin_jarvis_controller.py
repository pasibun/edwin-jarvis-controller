from Service.ej_controller import EJController

if __name__ == "__main__":
    print("Init Edwin jarvis controlboard")
    try:
        edwin = EJController()
    except:
        print("Something went knijter wrong.. Exit() application.")
