import pandas as pd

if __name__ == "__main__":
    print("search microservice is running.....")
    while True:
        # keep checking the content in the txt file
        file = open('basic_search.txt', 'r')
        item = file.readline()
        file.close()

        # check if the line is empty, if not---> continue to search this item in csv
        if len(item) != 0:
            # Clear file
            heading = "Name,Brand,Category,Color,Location,Width,Depth,Height,Price,Link\n"
            with open("basic_result.csv", "w") as f:
                f.write(heading)

            df = pd.read_csv('home_inventory.csv')
            res = df[(df["Name"] == item) | (df["Brand"] == item)]
            print(res.to_string() + "\n")
            if res.shape[0] > 0:
                # write the res row into basic_result.csv
                res.to_csv('basic_result.csv', mode='a', index=False, header=False)
                # open search_item.txt and delete contents (so that the text file will be empty and this program will
                # not keep writing results to csv)
                with open('basic_search.txt', 'r+') as f:
                    f.truncate()
            # if not found, return not found
            else:
                pd.DataFrame([{"item": 'Not Found'}]).to_csv('basic_result.csv', mode='a', index=False, header=False)
                with open('basic_search.txt', 'r+') as f:
                    f.truncate()
