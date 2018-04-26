#!/usr/bin/env python3

"""
Application Runner
"""

try:
    import coloredlogs
    coloredlogs.install()
except ImportError:
    print("Use Python coloredlogs module for colored output")


class Runner:
    """Setup, set status, and tear down your application"""
    def __init__(self):
        self.state = "OK"

    def status(self):
        """
        Perform your checks at some point, storing your sanity in self.state
        """
        return self.state

    def shutdown(self):
        """Use this function for any necessary cleanup"""
        pass


if __name__ == "__main__":
    runner = Runner()
    print(f"Status: {runner.status()}")
    runner.shutdown()
