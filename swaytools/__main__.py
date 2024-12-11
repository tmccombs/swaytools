import sys


def cli():
    cmd = None
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
    if cmd == "info":
        from .info import main
    elif cmd == "focus":
        from .winfocus import main
    elif cmd == "floatnext":
        from .floatnext import main
    else:
        if cmd:
            print("Unrecognized command: {cmd}", file=sys.stderr)
        else:
            print("USAGE: swayt COMMAND", file=sys.stderr)
        sys.exit(2)

    main()


if __name__ == "__main__":
    cli()
