from dotenv import load_dotenv
import boto3
import os

TABLE_NAME = "ue_kat_db_test"
AWS_ACCESS_KEY = os.environ["AWS_ACCESS_KEY"]
AWS_SECRET_KEY = os.environ["AWS_SECRET_KEY"]
REGION = os.environ["REGION"]

# Tworzenie obiektu sesji
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION
)

# Tworzenie obiektu klienta DynamoDB
dynamodb = session.resource('dynamodb')

# Tworzenie tabeli
table = dynamodb.create_table(
    TableName='ue_dynamodb_warsztaty',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'  # Klucz partycji
        },
        {
            'AttributeName': 'sort_key',
            'KeyType': 'RANGE'  # Klucz sortowania
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'N'  # Typ atrybutu dla klucza partycji (liczba)
        },
        {
            'AttributeName': 'sort_key',
            'AttributeType': 'S'  # Typ atrybutu dla klucza sortowania (tekst)
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Oczekiwanie na utworzenie tabeli
table.meta.client.get_waiter('table_exists').wait(TableName='ue_dynamodb_warsztaty')

# Dodawanie rekordów do tabeli
items = [
    {
        'id': 1,
        'sort_key': 'A',
        'imię': 'Jan',
        'wiek': 25,
        'miasto': 'Warszawa'
    },
    {
        'id': 2,
        'sort_key': 'B',
        'imię': 'Alicja',
        'wiek': 30,
        'kraj': 'Polska'
    },
    {
        'id': 3,
        'sort_key': 'C',
        'imię': 'Paweł',
        'wiek': 35,
        'zawód': 'Inżynier'
    },
    {
        'id': 4,
        'sort_key': 'D',
        'imię': 'Ewa',
        'wiek': 28,
        'adres': {
            'ulica': 'ul. Główna 123',
            'miasto': 'Kraków',
            'województwo': 'Małopolskie'
        }
    },
    {
        'id': 5,
        'sort_key': 'E',
        'imię': 'Michał',
        'wiek': 40,
        'zainteresowania': ['sport', 'muzyka', 'czytanie']
    },
    {
        'id': 6,
        'sort_key': 'F',
        'imię': 'Anna',
        'wiek': 32,
        'stanowisko': 'Menadżer',
        'dział': 'Sprzedaż'
    },
    {
        'id': 7,
        'sort_key': 'G',
        'imię': 'Piotr',
        'wiek': 45,
        'kraj': 'Polska',
        'hobby': ['wędrówki', 'gotowanie']
    },
    {
        'id': 8,
        'sort_key': 'H',
        'imię': 'Olga',
        'wiek': 27,
        'płeć': 'kobieta',
        'email': 'olga@example.com'
    },
    {
        'id': 9,
        'sort_key': 'I',
        'imię': 'Adam',
        'wiek': 33,
        'telefon': '+48123456789',
        'języki': ['polski', 'angielski']
    },
    {
        'id': 10,
        'sort_key': 'J',
        'imię': 'Zofia',
        'wiek': 29,
        'kraj': 'Niemcy',
        'adres': {
            'ulica': 'Niemiecka 456',
            'miasto': 'Berlin'
        }
    },
    {
        'id': 11,
        'sort_key': 'K',
        'imię': 'Kamil',
        'wiek': 38,
        'zawód': 'Nauczyciel',
        'przedmioty': ['Matematyka', 'Fizyka']
    },
    {
        'id': 12,
        'sort_key': 'L',
        'imię': 'Emilia',
        'wiek': 31,
        'miasto': 'Łódź',
        'zainteresowania': ['podróże', 'fotografia']
    },
    {
        'id': 13,
        'sort_key': 'M',
        'imię': 'Jakub',
        'wiek': 36,
        'kraj': 'Australia',
        'email': 'jakub@example.com'
    },
    {
        'id': 14,
        'sort_key': 'N',
        'imię': 'Liliana',
        'wiek': 26,
        'hobby': ['malarstwo', 'ogrodnictwo'],
        'edukacja': {
            'stopień': 'Licencjat',
            'kierunek': 'Sztuki Piękne'
        }
    },
    {
        'id': 15,
        'sort_key': 'O',
        'imię': 'Mateusz',
        'wiek': 34,
        'zawód': 'Inżynier oprogramowania',
        'umiejętności': ['Python', 'Java', 'SQL']
    }
]

with table.batch_writer() as batch:
    for item in items:
        batch.put_item(Item=item)

print("Dodano rekordy do tabeli 'PrzykladowaTabela'.")