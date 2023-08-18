#!/usr/bin/python3

import os
import time

class UnifiedProgram:
    def __init__(self):
        self.clear_screen()
        self.data_dict = {"A": "You", "B": "Are", "C": "The", "D": "Best"}

    def clear_screen(self):
        os.system('clear')

    def print_with_delay(self, text, delay=0.01):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def sum_list(self, my_list):
        result = 0
        for x in my_list:
            result += x
        return result

    def sum_tuple(self, *args):
        result = 0
        for x in args:
            result += x
        return result

    def make_sentence(self, **piplo):
        result = ""
        for x in piplo:
            result += piplo[x]
        return result

    def add_variable(self, variable, value):
        self.data_dict[variable] = value

    def print_variables(self):
        variables = ' '.join(self.data_dict.keys())
        print(variables)

    def print_values(self):
        values = ' '.join(self.data_dict.values())
        print(values)

    def print_dictionary(self):
        entries = ', '.join([f'{key}=\'{value}\'' for key, value in self.data_dict.items()])
        print(f'({entries})')

    def main(self):
        intro_lines = [
            "\033[1;34m╔══════════════════════════════════════════╗",
            "║     *ARGS        AND        **KWARGS     ║",
            "║                                          ║",
            "║   1 - use arg                            ║",
            "║   2 - use kwargs                         ║",
            "║                                          ║",
            "╚══════════════════════════════════════════╝\033[0m"
        ]

        for line in intro_lines:
            self.print_with_delay(line, delay=0.01)

        for x in range(15):
            print("\n")

        num = int(input("\x1b[91m=> Choose a number : \x1b[93m"))
        self.clear_screen()

        if num == 1:
            list_intro = [
                "\033[1;35m╔══════════════════════════════════════════╗",
                "║       => Here are the choices <=         ║",
                "║                                          ║",
                "║   1 - use list                           ║",
                "║   2 - use tuple                          ║",
                "╚══════════════════════════════════════════╝",
                "                                            "
            ]

            for line in list_intro:
                self.print_with_delay(line, delay=0.01)

            for x in range(15):
                print("\n")

            num_2 = int(input("\x1b[91m=> Choose a number : \x1b[93m"))
            self.clear_screen()

            if num_2 == 1:            # 1 - use list 
                list_code = [
                    "\033[1;36m╔═════════════════════════════════════════════╗",
                    "║  #!/usr/bin/python3                         ║",
                    "║  def sum_list(my_list):                     ║",
                    "║      result = 0                             ║",
                    "║      for x in my_list:                      ║",
                    "║          result += x                        ║",
                    "║      return result                          ║",
                    "║  print(sum_list([1,2, 3, 4, 5]))            ║",
                    "╚═════════════════════════════════════════════╝\033[0m",
                    " \033[1;36m 1- sum_list                 2 - modify list  \033[0m"
                    "                                               ",
                    "                                               "
                ]

                for line in list_code:
                    self.print_with_delay(line, delay=0.01)
                for x in range(13):
                    print("\n")

                num_3 = int(input("\x1b[91m=> Choose a number : \x1b[93m"))

                if num_3 == 1:
                    print(f"\033[1;32mSum of the list: {self.sum_list([1, 2, 3, 4, 5])}\033[0m")
                if num_3 == 2:
                    num_2 = int(input("\x1b[90m=> Try changing the first variable in this string : sum_list([0]) = \x1b[37;1m"))
                    modified_code = f"""
\033[1;33m╔════════════════════════════════════════════════╗
║  #!/usr/bin/python3                            ║
║  def sum_list(my_list):                        ║    
║      result = 0                                ║
║      for x in my_list:                         ║   
║          result += x                           ║
║      return result                             ║ 
║                                                ║
║  print(sum_list([{num_2}, 2, 3, 4, 5]))             ║                    
╚════════════════════════════════════════════════╝\033[0m
"""
                    self.print_with_delay("\x1b[32mModified Code:\x1b[0m")
                    self.print_with_delay(modified_code)

                    calculate = input("\x1b[90m=> Do you want to calculate the sum of this modified list? (yes or no): \x1b[37;1m")
                    if calculate.lower() == "yes":
                        modified_list = [num_2, 2, 3, 4, 5]
                        self.print_with_delay(f"\033[1;32mSum of the modified list: {self.sum_list(modified_list)}\033[0m")

            
            if num_2 == 2:
                tuple_intro = [
                    "\033[1;35m╔═════════════════════════════════════════════╗",
                    "║  #!/usr/bin/python3                         ║",
                    "║  def sum_tuple(*args):                      ║",
                    "║      result = 0                             ║",
                    "║      for x in args:                         ║",
                    "║          result += x                        ║",
                    "║      return result                          ║",
                    "║  print(sum_tuple(1,2, 3, 4, 5))             ║",
                    "╚═════════════════════════════════════════════╝\033[0m",
                    " \033[1;35m1 - sum_tuple                 2 - modify tuple\033[0m",
                    "                                               "
                ]

                for line in tuple_intro:
                    self.print_with_delay(line, delay=0.01)

                for x in range(13):
                    print("\n")

                num_3 = int(input("\x1b[91m=> Choose a number : \x1b[93m"))

                if num_3 == 1:
                    print(f"\033[1;32mSum of the tuple: {self.sum_tuple(1, 2, 3, 4, 5)}\033[0m")

                if num_3 == 2:
                    num_2 = int(input("\x1b[90m=> Try changing the first variable in this tuple : sum_tuple[0] = \x1b[37;1m"))
                    modified_code = f"""
\033[1;31;14mTraceback (most recent call last):
  File "/home/oualid/Desktop/project_alx/TEST_PR/./project.py", line ..., in <module>
    sum_tuple[0] =  {num_2}    
TypeError: 'tuple' object does not support item assignment\033[0m
"""
                    self.print_with_delay(modified_code)
            
        if num == 2:
            kwargs_intro = [
                "\033[1;35m╔════════════════════════════════════════════════════════════╗",
                "║                => Here are the choices <=                  ║",
                "║                                                            ║",
                "║   1 -  def my_sum(a, b, *args, option=True ):              ║",
                "║   2 -  def my_sum(a, b, *args, option=False ):             ║",
                "║   3 -  def make_sentence(**piplo):                         ║",
                "║   4 -  def human_details(**kwargs):                        ║",
                "║   5 -  def print_args(x, y, *args, option=True, **kwargs): ║",
                "║                                                            ║",
                "╚════════════════════════════════════════════════════════════╝",
                "                                                              "
            ]

            for line in kwargs_intro:
                self.print_with_delay(line, delay=0.01)

            for x in range(13):
                print("\n")

            num_3 = int(input("\x1b[91m=> Choose a number : \x1b[93m"))
            self.clear_screen()
    
            if num_3 == 1:
                    my_sum_1_intro = [
                        "\033[1;36m╔════════════════════════════════════════╗",
                        "║ def my_sum(a, b, *args, option=True ): ║",
                        "║    result =                            ║",
                        "║    if option:                          ║",
                        "║        for x in args:                  ║",
                        "║            result += x                 ║",
                        "║        return a + b + result           ║",
                        "║    else:                               ║",
                        "║        return result                   ║",
                        "║                                        ║",
                        "║ print(my_sum(1, 2, 3, 4, 5))           ║",
                        "╚════════════════════════════════════════╝\033[0m"
                    ]

                    for line in my_sum_1_intro:
                        self.print_with_delay(line, delay=0.01)

                    input("\x1b[90mPress enter to display the result...\x1b[37;1m")
                    self.print_with_delay("\033[1;32m\nSum of the code: 15\033[0m")

            if num_3 == 2:
                my_sum_2_intro = [

                    "\033[1;36m╔══════════════════════════════════════════════╗",
                    "║ def my_sum(a, b, *args, option=True ):       ║",
                    "║   result = 0                                 ║",
                    "║   if option:                                 ║",
                    "║     for x in args:                           ║",
                    "║       result += x                            ║",
                    "║     return a + b + result                    ║",
                    "║     else:                                    ║",
                    "║         return result                        ║",
                    "║ print(my_sum(1, 2, 3, 4, 5, option=False))   ║",
                    "╚══════════════════════════════════════════════╝\033[0m"
                ]
                for line in my_sum_2_intro:
                    self.print_with_delay(line, delay=0.01)
                input("\x1b[90mPress enter to display the result...\x1b[37;1m")
                self.print_with_delay("\033[1;32m\nSum of the code: 0 \033[0m")

            if num_3 == 3:
                data_dict_intro = [
                    "\033[1;36m╔═════════════════════════════════════════════════════════╗",
                    "║ def human_details(**kwargs):                            ║",
                    "║   for key, value in kwargs.items():                     ║",
                    "║     print(f\"{key} : {value}\")                           ║",
                    "║                                                         ║",
                    "║ human_details(name=\"asmaa\", job=\"developer\", age=\"23\")  ║",
                    "║ print(\"------------------------------\")                 ║",
                    "║ human_details(name=\"oualid\", job=\"hacking\")             ║",
                    "╚═════════════════════════════════════════════════════════╝\033[0m"
                ]
                for line in data_dict_intro:
                    self.print_with_delay(line, delay=0.01)

                input("\x1b[90mPress enter to display the result...\x1b[37;1m")
                print_all = """
name : asmaa
job : developer
age : 23
------------------------------
name : oualid
job : hacking
"""
                self.print_with_delay(print_all)

            if num_3 == 4:
                print_args_intro = [
                    "\033[1;36m╔══════════════════════════════════════════════════════════════════════════╗",
                    "║ def print_args(x, y, *args, option=True, **kwargs):                      ║",
                    "║   print(x, y)                                                            ║",
                    "║   print(args)                                                            ║",
                    "║   print(option)                                                          ║",
                    "║   print(kwargs)                                                          ║",
                    "║                                                                          ║",
                    "║ print_args(1, 2, \"MY NAME\", \"IS OUALID ELHADIM\",MY_AGE=\"IS ...\")         ║",
                    "╚══════════════════════════════════════════════════════════════════════════╝\033[0m"
                ]
                for line in print_args_intro:
                    self.print_with_delay(line, delay=0.01)
                
                input("\x1b[90mPress enter to display the result...\x1b[37;1m")
                print_all = """
1 2
('MY NAME', 'IS OUALID ELHADIM')
True
{'MY_AGE': 'IS ...'}
"""
                self.print_with_delay(print_all)


            if num_3 == 5:
                make_sentence_intro = [
                    "\033[1;35m╔═════════════════════════════════════════════════════════════════════╗",
                    "║ def make_sentence(**piplo):                                         ║",
                    "║    result = ''                                                      ║",
                    "║    for x in piplo:                                                  ║",
                    "║      result += piplo[x]                                             ║",
                    "║    return result                                                    ║",
                    "║                                                                     ║",
                    "║ print(make_sentence(A=\"You\", B=\"Are\", C=\"The\", D=\"Best\"))           ║",
                    "══════════════════════════════════════════════════════════════════════╝\033[0m",
                    "                                                                              "
                ]
                for line in make_sentence_intro:
                    unified_instance.print_with_delay(line, delay=0.01)
                    
                print(" \033[1;35m1 - Add key_and_value   2 - Display keys   3 - Display values  4 - exit \033[0m")
                for x in range(13):
                    print("\n")
                while True:
                    choice = input("\x1b[91mEnter your choice: \x1b[93m")
                    if choice == '1':
                        variable = input("\x1b[32mEnter the variable:\x1b[0m ")
                        value = input("\x1b[32mEnter the value:\x1b[0m ")
                        unified_instance.add_variable(variable, value)
                        print("\033[1;36mUpdated dictionary:\033[0m")
                        unified_instance.print_dictionary()
                    elif choice == '2':
                        print("\033[1;36mthese are keys:\033[0m", end=" ")
                        unified_instance.print_variables()
                    elif choice == '3':
                        print("\033[1;36mthese are values:\033[0m", end=" ")
                        unified_instance.print_values()
                    elif choice == '4':
                        break
                    else:
                        print("\033[1;31;14mInvalid choice, please choose again.\033[0m")

if __name__ == "__main__":
    unified_instance = UnifiedProgram()
    unified_instance.main()
