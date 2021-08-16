from py4j.java_gateway import JavaGateway
import subprocess

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

    def startListener(self, file_path) -> str:
        self.counter += 1
        if self.counter > 1000:
            self.restartJvm()
            self.counter = 0

        words = self.gateway.entry_point.startListener(file_path)
        print(words)
        return words
