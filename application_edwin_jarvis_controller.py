from Service.display_service import DisplayService
from Service.ej_controller_service import EJControllerService

dp = DisplayService()
if __name__ == "__main__":
    print("Init Edwin jarvis controlboard")
    try:
        edwin = EJControllerService()
    except:
        dp.show_msg("Something went knijter wrong.. Exit() application.")
