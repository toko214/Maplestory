import time
from database import DatabaseConnection
from constants import ServerConstants
from handling.world import World


class Start:
    def __init__(self):
        self.startTime = time.time()
        self.properties = {}
        self.cursor = None

    def run(self):
        print "starting server...."
        self.properties['wzpath'] = ['wz','WZ','Wz','wZ']
        connection = DatabaseConnection.getConnection()
        cursor = connection.cursor()
        DatabaseConnection.execute(cursor,"UPDATE accounts SET loggedin = 0")
        print "Loading " + ServerConstants.SERVERNAME
        World.init()


def main():

    instance = Start()
    instance.run()

if __name__ == '__main__':
    main()