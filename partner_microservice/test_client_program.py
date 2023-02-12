import time

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

                # overwrite prng-service.txt value with "run"
                f = open("pipeline.txt", "w")
                f.write("run")
                f.close()
                time.sleep(5)

                # read the generated number from prng-service.txt,
                f = open("pipeline.txt", "r")
                line = f.readline()

            elif user_input == 2:
                # quit program if input is 2
                print("Quiting...")
                break

            else:
                print("An error has occurred... Please enter '1' or '2'\n")
