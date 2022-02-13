from notification import toast
from fetch import get_status
from checks import load
from time import sleep
from config import wait, terminalMessages

status = str(get_status("synapse"))

notUpdated = []
if __name__ == "__main__":
    try:
        for i in load:
            if get_status(i) == False:
                print(i + " is currently not updated. You will be notified when it is updated.")
                notUpdated.append(i)
            elif get_status(i) == True:
                print(i + " is currently updated.")
            

        print("-----------\n\nRunning...")

        while True:
            if notUpdated == []:
                print("All selected exploits are updated.")
                break
            else:
                for i in notUpdated:
                    if get_status(i) == True:
                        print(i + " is now updated!")
                        toast("whatexploitsare.online", i + " is now updated!")
                        notUpdated.remove(i)
                    elif get_status(i) == False:
                        if terminalMessages == True:
                            print(i + " is still not updated.")
            sleep(wait)
    except:
        print("Error : something went wrong.")