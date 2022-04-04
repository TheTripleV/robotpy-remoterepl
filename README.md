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
python -m remoterepl
```

