"""
Write a function named setAlarm/set_alarm/set-alarm/setalarm (depending on language)
which receives two parameters. The first parameter, employed, is true whenever you are
employed and the second parameter, vacation is true whenever you are on vacation.

The function should return true if you are employed and not on vacation
(because these are the circumstances under which you need to set an alarm).
It should return false otherwise.
"""


def set_alarm(employed, vacation):
    return employed and not vacation
