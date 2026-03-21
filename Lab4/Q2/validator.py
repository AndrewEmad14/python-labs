import constants
import re

def isAlpha(input):
  """
  Checks if all characters in the input string are alphabets.
  
  Parameters
  ----------
  input : str
    The string to be checked.
  
  Returns
  -------
  bool
    True if all characters in the string are alphabets, False otherwise.
  """
  return input.isalpha


def isAlnum(input):
  """
  Checks if all characters in the input string are alphanumeric.
  
  Parameters
  ----------
  input : str
    The string to be checked.
  
  Returns
  -------
  bool
    True if all characters in the string are alphanumeric, False otherwise.
  """
  return input.isalnum


def isNumber(input):
  """
  Checks if all characters in the input string are numbers.
  
  Parameters
  ----------
  input : str
    The string to be checked.
  
  Returns
  -------
  bool
    True if all characters in the string are numbers, False otherwise.
  """
  return input.isdigit


def isMood(input):

  """
  Checks if the input string matches any of the predefined mood constants.
  
  Parameters
  ----------
  input : str
    The string to be checked.
  
  Returns
  -------
  bool
    True if the input string matches any of the predefined mood constants, False otherwise.
  """
  input = input.upper()
  for i in constants.Mood:

    if input == i.name:
      return True
  return False


def isFloat(input):
    """
    Checks if the input string can be converted to a float.
    
    Parameters
    ----------
    input : str
        The string to be checked.
    
    Returns
    -------
    bool
        True if the input string can be converted to a float, False otherwise.
    """
    try:
        float(input)
        return True
    except ValueError:
        return False
    

def isIntanceOf(input, type):
    """
    Checks if the input string is an instance of the specified type.
    
    Parameters
    ----------
    input : str
        The string to be checked.
    type : type
        The type to check against.
    
    Returns
    -------
    bool
        True if the input string is an instance of the specified type, False otherwise.
    """
    return isinstance(input, type)


def isEmail(input):
    """
    Checks if the input string is a valid email address.
    
    Parameters
    ----------
    input : str
        The string to be checked.
    
    Returns
    -------
    bool
        True if the input string is a valid email address, False otherwise.
    """
    return re.match(constants.EMAIL_REGEX, input)

def isPostive(input):
    """
    Checks if the input string is a positive number.
    
    Parameters
    ----------
    input : str
        The string to be checked.
    
    Returns
    -------
    bool
        True if the input string is a positive number, False otherwise.
    """
    input = float(input)
    return input > 0

def isValidRange(input,start,end):
    """
    Checks if the input string is within the specified range.
    
    Parameters
    ----------
    input : str
        The string to be checked.
    start : int
        The start of the range.
    end : int
        The end of the range.
    
    Returns
    -------
    bool
        True if the input string is within the specified range, False otherwise.
    """
    input = float(input)
    return input >= start and input <= end