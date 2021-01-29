from Service.display_service import show_msg
from Service.ej_controller_service import EJControllerService

if __name__ == "__main__":
    print("Init Edwin jarvis controlboard")
    try:
        edwin = EJControllerService()
    except:
        show_msg("Something went knijter wrong.. Exit() application.")
