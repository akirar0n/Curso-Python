#
# ** Quando usar closures?
#
# - Para manter estados simples sem usar classes
# - Para criar fábricas (factories) de funções
# - Para encapsular o código e esconder nomes importantes de escopos amplos
# - Para usar funções de callback (onde algo é feito por etapas)
# - Para decoradores de função em Python
# - Para programação funcional e algoritmos em geral
#


################################################################################

from utils import Logger

def make_logger(name: str, color: str, icon: str = "…") -> Logger:
    def logger(log: str) -> None:
        log_name = f"{color}[{name.upper(): <7}] "
        print(f"{log_name} {icon} {log}\033[0m")

    return logger


debug = make_logger("debug", "\033[032m", icon="…")
info = make_logger("info", "\033[034m", icon="✔")
warning = make_logger("warning", "\033[033m", icon="⚠")
error = make_logger("error", "\033[031m", icon="✘")

print()
debug("Esse é um log de DEBUG")
info("Aconteceu alguma coisa no código")
warning("OPA!!! PRESTENÇÃO MINNINUUUUU...")
error("Te falei que ia dar ruim...")
debug("Esse é um log de DEBUG")
print()