from subprocess import check_output
from python.get_args import get_str_env_var, PATH_TO_JAR

def callAntlr(file_path) -> str:
    bytes = check_output(["java", "-jar", get_str_env_var(PATH_TO_JAR, ""), file_path])
    return bytes.decode("utf-8")
