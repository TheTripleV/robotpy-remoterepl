import wpilib
from remoterepl import RemoteREPL

class MyRobot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        self.remote_repl = RemoteREPL(self)

if __name__ == "__main__":
    wpilib.run(MyRobot)