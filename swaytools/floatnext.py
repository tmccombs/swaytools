from .ipc import Event, I3Ipc, Request


def _next_new_window(ipc):
    "Wait for an event for the next new window"
    while True:
        typ, event = ipc.recv()
        if typ == Event.WINDOW and event["change"] == "new":
            return event["container"]


def _set_floating(ipc, con_id):
    "Set 'floating enable' on the given container id"
    cmd = f"[con_id={con_id}] floating enable".encode("utf-8")
    ipc.send(Request.RUN_COMMAND, cmd)
    # there is a bug in sway where we never get the response to the command
    # so for now, just assume that it succeeds.
    #
    # if that bug is fixed, then we should probably read messages until we get the response,
    # ignoring any other events
    #
    # See https://github.com/swaywm/sway/issues/8210


def main():
    with I3Ipc() as ipc:
        ipc.subscribe("window")
        win = _next_new_window(ipc)
        _set_floating(ipc, win["id"])
