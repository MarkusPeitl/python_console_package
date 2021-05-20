#!/usr/bin/env python3

"""Simple Launcher useful when running application locally from this directory (not used in install)"""

import sys
import python_console_package.entrypoint

if __name__ == '__main__':
    sys.exit(python_console_package.entrypoint.main())