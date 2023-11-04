from sqlalchemy import create_engine
import psycopg2 
import io
import pandas as pd
import config as C


def run_statistics(df):
    '''
    Generate summary statistics for some key variables.
    '''
    print("Generate descriptive statistics:")
    print(df.describe())

    print("Generate State column statistics:")
    print(df['state'].value_counts()[:5])

    print("Generate Bedrooms column statistics:")
    print(df['bedrooms'].value_counts())
    
    print("Generate Category column statistics:")
    print(df['category'].value_counts())


def clean_data(df):
    convert_dict = {
        'id': object
    }

    df = df.astype(convert_dict)

    return df


def save_csv_to_db(df):
    conn_string = "postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}".format(
        username=C.username,
        password=C.password,
        host=C.host,
        port=C.port,
        database=C.database
    )
    engine = create_engine(conn_string)

    # Drop existing table and create new empty table
    # df.head(0).to_sql(C.table_name, engine, if_exists='replace', index=False)

    conn = engine.raw_connection()
    cur = conn.cursor()
    output = io.StringIO()

    df.to_csv(output, sep='\t', header=False, index=False)

    output.seek(0)
    cur.copy_from(output, C.table_name, null="")
    conn.commit()

    cur.close()
    conn.close()


def main(path_to_raw_csv):

    df = pd.read_csv(path_to_raw_csv, encoding='cp1252', sep=';')

    print("-------- Clean data --------")
    df = clean_data(df)

    print("-------- Generate statistics --------")
    run_statistics(df)

    print("-------- Save raw data to PostgreSQL --------")
    save_csv_to_db(df)


main(C.path_to_raw_csv)
