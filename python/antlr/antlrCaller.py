from subprocess import check_output
import os

def callAntlr(file_path) -> str:
    bytes = check_output(["java", "-jar", os.environ["PATH_TO_JAR"], file_path])
    return bytes.decode("utf-8")
