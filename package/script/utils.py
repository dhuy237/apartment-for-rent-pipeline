from sqlalchemy import create_engine
import io
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
    '''
    Clean the raw data. Convert the data type to match the schema.
    '''
    convert_dict = {
        'id': object,
        'category': object,
        'title': object,
        'body': object,
        'amenities': object,
        'bathrooms': float,
        'bedrooms': float,
        'currency': object,
        'fee': object,
        'has_photo': object,
        'pets_allowed': object,
        'price': int,
        'price_display': object,
        'price_type': object,
        'square_feet': int,
        'address': object,
        'cityname': object,
        'state': object,
        'latitude': float,
        'longitude': float,
        'source': object,
        'time': int
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