class Notifications:

    def __init__(self):

        self.__notifications = []


    def add(self, notification : str):

        self.__notifications.append(notification)

    def clear(self):

        self.__notifications.clear()

    def load(self) -> str:

        out = ""
        for node in self.__notifications:

            out += f"{node}\n"

        return out



