import networktables
import code
import io
import time
from contextlib import redirect_stdout, redirect_stderr

class RemoteREPL:

    def __init__(self, robot, **kwargs):

        self.table = networktables.NetworkTables.getTable('RemoteREPL')
        self.interpreter = code.InteractiveInterpreter(locals={"robot": robot, "r": robot})
        self.table.putString("stdin", "")
        self.table.putString("stdout", "")

        def ep(entry, *args, **kwargs):
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                stderr = io.StringIO()
                with redirect_stderr(stderr):
                    self.interpreter.runsource(entry.value.getRaw()[:-22])

            out = stdout.getvalue()

            if not out.strip():
                out = "\n"

            out += stderr.getvalue()

            out += f" T{time.time_ns():<20}"

            self.table.putString("stdout", out)

        self.table.getEntry("stdin").addListener(ep, networktables.NetworkTablesInstance.NotifyFlags.UPDATE | networktables.NetworkTablesInstance.NotifyFlags.NEW)
