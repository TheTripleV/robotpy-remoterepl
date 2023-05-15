# robotpy-remoterepl
Access a REPL that runs within your robot code

# Usage

## Robot Code

In robot.py:
```py
from remoterepl import RemoteREPL

def robotInit(self):
    self.remote_repl = RemoteREPL(self)
```

## Client Side

```
python -m remoterepl 10.40.96.2
```

### Example Interface

```shell
Connected to SIMULATOR
---------------------------
You are now in a pseudo python shell within the robot.
Your robot is located at 'robot' or at 'r'.
Ex. 'robot.oi' is the OI object of your robot.
---------------------------
---------------------------
>>> robot
<__main__.Robot object at 0x109af1c20>

>>> robot.shooter.motor_bottom.config_kP(0, 0.1)
<ErrorCode.OK: 0>

>>> robot.shooter.motor_bottom.set(0)


>>> robot.intake.down()


>>> robot.drivetrain.getPose2d()
Pose2d(Translation2d(x=0.000000, y=0.000000), Rotation2d(0.000000))

>>> 
```