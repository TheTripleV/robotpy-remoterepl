import time
import socket
from networktables import NetworkTables
# import readline # just importing this modifies behavior
import networktables

def start():
    local_ips = [i[4][0] for i in socket.getaddrinfo(socket.gethostname(), None)]

    local_ipv4s = {i for i in local_ips if "." in i}

    potential_robot_ips = {
        ".".join(i.split(".")[:-1]) + ".2" for i in local_ipv4s
    }

    potential_robot_ips.add("127.0.0.1")

    NetworkTables.startClient(list(potential_robot_ips))

    while not NetworkTables.isConnected():
        pass

    server_ip = NetworkTables.getRemoteAddress()

    print("---------------------------")
    print("---------------------------")
    if server_ip == '127.0.0.1':
        print("Connected to SIMULATOR")
    else:
        print("Connected to ROBOT")
    print("---------------------------")
    print("You are now in a pseudo python shell within the robot.")
    print("Your robot is located at 'robot' or at 'r'.")
    print("Ex. 'robot.oi' is the OI object of your robot.")
    print("---------------------------")
    print("---------------------------")

    table = NetworkTables.getTable("RemoteREPL")

    def r():
        user_input = input(">>> ")
        if user_input == "exit()":
            exit()
        user_input += f" T{time.time_ns():<20}"
        table.putString("stdin", user_input)

    def pr(entry, *args, **kwargs):
        print(entry.value.getRaw()[:-22])
        r()

    table.getEntry("stdout").addListener(pr, networktables.NetworkTablesInstance.NotifyFlags.UPDATE)

    r()

    while True: pass


if __name__ == "__main__":
    start()
