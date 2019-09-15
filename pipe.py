import pandas as pd

import os

# https://www.partow.net/miscellaneous/airportdatabase/

def pipe(): 
    EXCEL_FILENAME = 'Exported_FlightLegs_From_2017-07-24_To_2017-07-301.xlsx'
    EXCEL_PATH = 'input/'
    CSV_IATA = 'GlobalAirportDatabase.txt'

    iata_columns = ["ICAO Code", "IATA Code", "Airport Name", "City/Town", "Country", 
                    "Latitude Degrees", "Latitude Minutes", "Latitude Seconds", "Latitude Direction", 
                    "Longitude Degrees", "Longitude Minutes", "Longitude Seconds", "Longitude Direction", 
                    "Altitude", "Latitude Decimal Degrees", "Longitude Decimal Degrees"]

    # df = pd.read_excel(EXCEL_PATH + EXCEL_FILENAME)
    df = pd.read_excel(os.path.join(EXCEL_PATH, EXCEL_FILENAME))
    iata = pd.read_csv(os.path.join(EXCEL_PATH, CSV_IATA), sep=":",names=iata_columns)

    iata_short = iata[['IATA Code', 'Country', 'Latitude Decimal Degrees', 'Longitude Decimal Degrees']]

    df1 = df.merge(iata_short, how="inner", left_on='DEP', right_on='IATA Code')
    df2 = df1.merge(iata_short, how="inner", left_on='ARR', right_on='IATA Code', suffixes=('_DEP', '_ARR'))

    return df2
# print(df2.shape)