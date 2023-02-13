import time
import pandas as pd

if __name__ == "__main__":
    while True:
        try:
            user_input = int(
                input("Enter '1' to get a random card or '2' to quit: "))
        except ValueError:
            # throw an exception if input is not numerical
            print("An error has occurred... Please enter a valid number\n")
            continue
        else:
            if user_input == 1:
                # generate an image if input is 1
                print("Generating card...")

                # overwrite pipeline.txt value with "run"
                f = open("pipeline.txt", "w")
                f.write("run")
                f.close()
                time.sleep(3)

                # read and print the generated card in result.txt
                with open("result.txt", "r") as r_file:
                    result = r_file.readline()
                print(f"Content in result.txt:\n"
                      f"{result}")

                # read and print the generated card in inventory.csv
                df = pd.read_csv("inventory.csv")
                print(f"Content in inventory.csv:\n"
                      f"{df}")

            elif user_input == 2:
                # quit program if input is 2
                print("Quiting...")
                break

            else:
                print("An error has occurred... Please enter '1' or '2'\n")
