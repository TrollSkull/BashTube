#!/usr/bin/env python3

# Name: BashTube
# GitHub: https://github.com/TrollSkull/BashTube
# Version: v2.0

try:
    from lib.main import Main, main
    from lib.core.exceptions import BashTubeExceptions
except Exception as err:
    import sys

    print(err, file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main()
