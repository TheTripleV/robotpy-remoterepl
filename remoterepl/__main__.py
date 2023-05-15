import time
import socket
import ntcore
# import readline # just importing this modifies behavior
import uuid
import sys


def start():

    ip_address = sys.argv[1] if len(sys.argv) > 1 else None

    if ip_address is None:
        print("No IP address provided in Command Line Argument.")
        print("Usage is 'python -m remoterepl IPADDRESS'")
        print("Defaulting to 127.0.0.1 for simulator.")
        ip_address = "127.0.0.1"

    inst = ntcore.NetworkTableInstance.getDefault()
    inst.startClient4("Remote Shell DS" + str(uuid.uuid1()))
    inst.setServer(ip_address)

    while not inst.isConnected():
        pass

    print("---------------------------")
    print("---------------------------")
    if ip_address == '127.0.0.1':
        print("Connected to SIMULATOR")
    else:
        print("Connected to ROBOT")
    print("---------------------------")
    print("You are now in a pseudo python shell within the robot.")
    print("Your robot is located at 'robot' or at 'r'.")
    print("Ex. 'robot.oi' is the OI object of your robot.")
    print("---------------------------")
    print("---------------------------")

    table = inst.getTable("Remote Shell")
    stdout_sub = table.getStringTopic("stdout")

    def r():
        user_input = input(">>> ")
        if user_input == "exit()":
            exit()
        user_input += f" T{time.time_ns():<20}"
        table.putString("stdin", user_input)
        # print("sent ->", user_input)

    def pr(event: ntcore.Event):
        print(event.data.value.getString()[:-22]) # type: ignore
        r()

    inst.addListener(stdout_sub, ntcore.EventFlags.kValueAll, pr)

    # r()

    while True: pass


if __name__ == "__main__":
    start()
