import itertools
import re

from lark import Transformer

from yaag_mme.yaag_parser import Command, Parameter


class YaagTransformer(Transformer):
    @staticmethod
    def command(command):
        return Command(command[0].value, command[1], command[2])

    @staticmethod
    def special_parameter(special_parameter):
        return [parameter.value for parameter in special_parameter]

    @staticmethod
    def parameter_list(parameter_list):
        return parameter_list

    @staticmethod
    def parameter(parameter):
        value = re.sub(
            r"{{((?:\\n)+)}}",
            lambda x: x.group().count(r"\n") * "\n",
            parameter[0].value.strip()
        )

        indent = (len(parameter[0].value) - len(
            parameter[0].value.lstrip())) // 4
        return Parameter(value, indent)
