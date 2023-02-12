import pandas as pd
import random
import time

if __name__ == "__main__":
    while True:
        # retrieve the value in the first line of the file
        print("microservice.py is running...")
        time.sleep(5)
        f = open("pipeline.txt", "r")
        line = f.readline()
        f.close()

        # if line in file is "run", rewrite line with a random card
        if line == "run":
            # open database.csv and get a random row from the file
            df = pd.read_csv("database.csv")
            row_count = len(df)-1
            rand_num = random.randint(0, row_count)
            result = f"{df.iloc[rand_num, 0]},{df.iloc[rand_num, 1]}\n"

            # overwrite new result to result.txt
            with open("result.txt", "w") as r_file:
                r_file.write(result)

            # append new result to inventory.csv
            with open("inventory.csv", "a") as i_file:
                i_file.write(result)

            # overwrite pipeline.txt to blank line
            f = open("pipeline.txt", "w")
            f.write("")
            f.close()


