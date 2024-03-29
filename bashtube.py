#!/usr/bin/env python3

"""
App name: BashTube
Author: TrollSkull
Github: https://github.com/TrollSkull
Version: 3.0
"""

try:
    from lib.main import Main, main
    from lib.core.exceptions import BashTubeExceptions

except ImportError as err:
    import sys

    print(err, file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main()
