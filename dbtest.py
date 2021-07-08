import mysql.connector
from mysql.connector import Error
from time import sleep
import datetime
from gpiozero import LED
import RPi.GPIO as GPIO


def startDetectionLoop():
    previous_value = None
    hash = False
    while True:
        current_value = getDatabaseState()
        if GPIO.input(15) == GPIO.HIGH and hash == False:
            print("" + str(datetime.datetime.now().timestamp()) + " BTNPress detected!")
            target_value = None
            if current_value == 1:
                target_value = 0
            else:
                target_value = 1
            setDatabaseState(target_value)
            hash = True
        elif GPIO.input(15) == GPIO.LOW and hash == True:
            hash = False
        if previous_value is None:
            previous_value = current_value
        elif previous_value != current_value:
            previous_value = current_value
            print("" + str(datetime.datetime.now().timestamp()) + " Change detected!")
            moveGarageDoor(current_value)
        sleep(1)


def simulateBtnPress():
    print("Button pressed!")
    relay = LED(4)

    relay.on()
    sleep(0.5)
    relay.close()


def moveGarageDoor(currentState):
    setDatabaseMovingState(1)
    if currentState == 0:
        simulateBtnPress()
        sleep(getDatabaseTime())
        setDatabaseMovingState(0)
        simulateBtnPress()
    else:
        simulateBtnPress()
        sleep(getDatabaseTime())
        setDatabaseMovingState(0)

def setDatabaseState(state):
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='178.18.246.147',
                                       database='smart_home',
                                       user='root',
                                       password='Milli_2013!')
        cursor = conn.cursor()
        print("UPDATE simple_components SET state=" + str(state) + " WHERE id=1")
        cursor.execute("UPDATE simple_components SET state=" + str(state) + " WHERE id=1")
        conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()

def setDatabaseMovingState(state):
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='178.18.246.147',
                                       database='smart_home',
                                       user='root',
                                       password='Milli_2013!')
        cursor = conn.cursor()
        print("UPDATE simple_components SET moving=" + str(state) + " WHERE id=1")
        cursor.execute("UPDATE simple_components SET moving=" + str(state) + " WHERE id=1")
        conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


def getDatabaseState():
        conn = None
        try:
            conn = mysql.connector.connect(host='178.18.246.147',
                                           database='smart_home',
                                           user='root',
                                           password='Milli_2013!')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM simple_components WHERE id=1")

            row = cursor.fetchone()

            while row is not None:
                return row[3]

        except Error as e:
            print(e)

        finally:
            if conn is not None and conn.is_connected():
                conn.close()


def getDatabaseTime():
    conn = None
    try:
        conn = mysql.connector.connect(host='178.18.246.147',
                                       database='smart_home',
                                       user='root',
                                       password='Milli_2013!')
        cursor = conn.cursor()
        cursor.execute("SELECT closing_time FROM simple_components WHERE id=1")

        row = cursor.fetchone()

        while row is not None:
            return row[0]

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    startDetectionLoop()
