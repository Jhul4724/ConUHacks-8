import sqlite3
from typing import Tuple

from config.loader import load_config, load_db

def connect(config_path: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    '''
    Connect to a SQLite database using the configuration provided.

    Parameters:
    - config_path (str): The path to the configuration file.

    Returns:
    Tuple[sqlite3.Connection, sqlite3.Cursor]: A tuple containing the SQLite connection
    and cursor objects.
    '''
    # Get project config
    config = load_config(config_path)
    dbname, _, _, _, _ = load_db(config)

    # Establish a connection to the database
    connection = sqlite3.connect(dbname)

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()
    
    # Return connection and cursor
    return connection, cursor


def disconnect(connection: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
    cursor.close()
    connection.close()