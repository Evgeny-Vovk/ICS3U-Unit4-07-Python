# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: November 2022
# ICS3U-Unit4-07.py File, learning while and if statements in python.


def main():

    # input and variables
    counter = 1000

    # process and output
    print("")
    while counter <= 2000:
        print("{0} ".format(counter), end="")
        counter += 1
        if counter % 5 == 0:
            print("")
    print("\n\nDone.")


if __name__ == "__main__":
    main()
