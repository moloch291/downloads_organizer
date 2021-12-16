import sys

import Organizer as org
import variable_storage.string_factory as str_f

if __name__ == '__main__':
    organizer = org.Organizer()
    if len(sys.argv) > 1 and sys.argv[1] == str_f.REDEFINE_PATHS:
        organizer.wants_to_redefine_paths()
    organizer.distribute_files()
