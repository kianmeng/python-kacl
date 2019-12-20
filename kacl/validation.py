class KACLValidationError():
    def __init__(self, line="", line_number=0, start_character_pos=None, end_character_pos=None, error_message=""):
        self.__line_number = line_number
        self.__start_character_pos = start_character_pos
        self.__end_character_pos = end_character_pos
        self.__error_message = error_message
        self.__line = line

    def line_number(self):
        return self.__line_number

    def position(self):
        return self.__start_character_pos, self.__end_character_pos

    def line(self):
        return self.__line

    def error_message(self):
        return self.__error_message


class KACLValidation():
    def __init__(self):
        self.__validation_errors = []

    def is_valid(self):
        return (len(self.__validation_errors) == 0)

    def errors(self):
        return self.__validation_errors

    def add_error(self, line, line_number, error_message, start_character_pos=None, end_character_pos=None):
        self.__validation_errors.append(KACLValidationError(line=line,
                                                            line_number=line_number,
                                                            start_character_pos=start_character_pos,
                                                            end_character_pos=end_character_pos,
                                                            error_message=error_message))
