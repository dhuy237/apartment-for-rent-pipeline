import pandas as pd
import config as C
import utils as U


def main(path_to_raw_csv):

    df = pd.read_csv(path_to_raw_csv, encoding='cp1252', sep=';')

    print("-------- Clean data --------")
    df = U.clean_data(df)

    print("-------- Generate statistics --------")
    U.run_statistics(df)

    print("-------- Save raw data to PostgreSQL --------")
    U.save_csv_to_db(df)


main(C.path_to_raw_csv)
