import configparser
import os
# config = configparser.RawConfigParser()
# config.read(".\\Configurations\\config.ini")
config = configparser.RawConfigParser()
thisfolder = os.path.dirname(os.path.abspath(__file__))
#initfile = os.path.join(thisfolder, 'C:\\Users\\CHANDNI\\PycharmProjects\\hypd\\Configurations\\config.ini')
initfile = os.path.join(thisfolder, 'C:\\Users\\CHANDNI\\PycharmProjects\\testkru\\Configurations\\config.ini')
res = config.read(initfile)
print(initfile)
config.read(initfile)
class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    # @staticmethod
    # def getUsername():
    #     username = config.get('common info', 'username')
    #     return username
    #
    # @staticmethod
    # def getPassword():
    #     password = config.get('common info', 'password')
    #     return password
