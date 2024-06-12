import pandas as pd
from faker import Faker

fake = Faker()

# Column names
columns = [
    'n_TradeNumber', 'n_TradeStatus', 's_InstrumentType', 's_Symbol', 'd_ExpiryDate',
    'n_StrikePrice', 's_OptionType', 's_SecurityName', 's_BookType', 's_BookTypeName',
    's_MarketType', 'n_UserId', 's_BrankNumber', 'n_BuySellIndicator', 'n_TradeQuantity',
    'n_Price', 'n_ProClient', 's_AccountNumber', 's_ParticipantCode', 's_OpenCloseIndicator',
    's_CoverUncoverIndicator', 'd_ActivityTime', 'd_LastModifiedTime', 'n_OrderNumber',
    's_OppBrokerId', 'd_OrderEntryDateTime', 's_CTCLId', 'n_ExNo', 'n_SchemaId'
]

# Date columns
date_columns = ['d_ExpiryDate', 'd_ActivityTime', 'd_LastModifiedTime', 'd_OrderEntryDateTime']


def generate_csv(num_rows, file_name):
    data = []

    for _ in range(num_rows):
        n_TradeNumber = fake.unique.random_int(min=1000, max=999999)  # Ensure unique TradeNumber
        n_TradeStatus = fake.random_element(elements=('Completed', 'Pending', 'Cancelled'))
        s_InstrumentType = fake.random_element(elements=('OPTSTK', 'OPTIDX', 'FUTSTK', 'FUTIDX'))
        s_Symbol = fake.random_element(elements=('AAPL', 'GOOGL', 'TSLA', 'AMZN', 'MSFT'))
        d_ExpiryDate = fake.date_between(start_date='-1y', end_date='+1y')
        n_StrikePrice = round(fake.random_number(digits=5, fix_len=True) / 100, 2)
        s_OptionType = fake.random_element(elements=('CE', 'PE'))
        s_SecurityName = fake.company()
        s_BookType = fake.random_element(elements=('Alpha', 'Beta', 'Gamma', 'Delta'))
        s_BookTypeName = fake.bs()
        s_MarketType = fake.random_element(elements=('Primary', 'Secondary'))
        n_UserId = fake.random_int(min=1, max=1000)
        s_BrankNumber = fake.bban()
        n_BuySellIndicator = fake.random_element(elements=(1, 2))
        n_TradeQuantity = fake.random_int(min=1, max=10000)
        n_Price = round(fake.random_number(digits=5, fix_len=True) / 100, 2)
        n_ProClient = fake.random_element(elements=(1, 2))
        s_AccountNumber = fake.bban()
        s_ParticipantCode = fake.bban()
        s_OpenCloseIndicator = fake.random_element(elements=('Open', 'Close'))
        s_CoverUncoverIndicator = fake.random_element(elements=('Cover', 'Uncover'))
        d_ActivityTime = fake.date_time_this_year()
        d_LastModifiedTime = fake.date_time_this_year()
        n_OrderNumber = fake.random_int(min=1000000, max=9999999)
        s_OppBrokerId = fake.random_element(elements=('BKR1', 'BKR2', 'BKR3', 'BKR4'))
        d_OrderEntryDateTime = fake.date_time_this_year()
        s_CTCLId = fake.random_element(elements=('CTCL1', 'CTCL2', 'CTCL3'))
        n_ExNo = fake.random_int(min=1, max=10)
        n_SchemaId = fake.random_int(min=1, max=5)

        data.append([
            n_TradeNumber, n_TradeStatus, s_InstrumentType, s_Symbol, d_ExpiryDate,
            n_StrikePrice, s_OptionType, s_SecurityName, s_BookType, s_BookTypeName,
            s_MarketType, n_UserId, s_BrankNumber, n_BuySellIndicator, n_TradeQuantity,
            n_Price, n_ProClient, s_AccountNumber, s_ParticipantCode, s_OpenCloseIndicator,
            s_CoverUncoverIndicator, d_ActivityTime, d_LastModifiedTime, n_OrderNumber,
            s_OppBrokerId, d_OrderEntryDateTime, s_CTCLId, n_ExNo, n_SchemaId
        ])

    df = pd.DataFrame(data, columns=columns)
    for col in date_columns:
        df[col] = df[col].astype(str)

    return df
