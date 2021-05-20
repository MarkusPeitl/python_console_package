#!/usr/bin/env python3

"""Simple Launcher useful when running application locally from this directory (not used in install)"""

import sys
import yourpackage.entrypoint

if __name__ == '__main__':
    sys.exit(yourpackage.entrypoint.main())