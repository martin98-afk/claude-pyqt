# -*- coding: utf-8 -*-
import argparse
import sys

from PyQt5.QtWidgets import QApplication

from standalone_app import StandaloneMainWindow


def main():
    parser = argparse.ArgumentParser(description="GUI ClaudeCode standalone app")
    parser.add_argument(
        "--workspace",
        default=None,
        help="Workspace directory for file tools and shell execution",
    )
    args, qt_args = parser.parse_known_args()

    app = QApplication([sys.argv[0], *qt_args])
    window = StandaloneMainWindow(workspace=args.workspace)
    window.show()
    return app.exec_()


if __name__ == "__main__":
    raise SystemExit(main())
