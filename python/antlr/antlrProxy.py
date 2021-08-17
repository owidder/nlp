from py4j.java_gateway import JavaGateway
import subprocess
import time
import sys

from python.get_args import get_str_env_var, PATH_TO_JAR

class AntlrProxy:
    def __init__(self):
        self.sub = None
        self.counter = 0
        self.gateway = JavaGateway()
        self.restartJvm()

    def restartJvm(self):
        print("------------- restarting JVM -----------------")
        if self.sub:
            self.sub.kill()

        self.sub = subprocess.Popen(["java", "-jar",  get_str_env_var(PATH_TO_JAR, "")])
        print("------------- JVM restarted -----------------")

    def _startListener(self, file_path: str, ctr: int) -> str:
        try:
            words = self.gateway.entry_point.startListener(file_path)
            print(words)
            return words
        except:
            print(sys.exc_info()[0])
            if ctr > 20:
                sys.exit(-1)
            time.sleep(.5)
            return self._startListener(file_path, ctr+1)

    def startListener(self, file_path) -> str:
        self.counter += 1
        if self.counter > 10:
            self.restartJvm()
            self.counter = 0
        return self._startListener(file_path, 0)