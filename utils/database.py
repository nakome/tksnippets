from sqlite3 import *
import os
import uuid
import random
import string

def uid(long=16):
    # Generates a unique ID consisting of letters and numbers
    charts = string.ascii_letters + string.digits
    unique_id = ''.join(random.choice(charts) for _ in range(long))
    return unique_id

class database:

    def __init__(self):
        # Initialize the connection to the SQLite database
        self.conn = connect("./storage/data.db")

    def get_all(self):
        """
        Retrieves all records from the 'snippets' table in the database.

        Returns:
            A list of tuples, where each tuple represents a record in the 'snippets' table.
            Each tuple contains the following fields:
                - uid (str): The unique identifier of the snippet.
                - title (str): The title of the snippet.
                - description (str): The description of the snippet.
                - content (str): The content of the snippet.
                - created (datetime): The timestamp when the snippet was created.
                - category (str): The category of the snippet.

        Raises:
            OperationalError: If there is an error executing the SQL statement.
        """
        # SQL statement to select all fields from the 'snippets' table
        sql = "SELECT uid, title, description, content, created, category FROM snippets"
        try:
            # Execute the SQL statement
            results = self.conn.execute(sql)
            # Return all results as a list of tuples
            return results.fetchall()
        except OperationalError as e:
            # Handle any operational error and re-raise it
            raise e

    def get_by_uid(self, uid):
        """
        Retrieves a single record from the 'snippets' table in the database based on the provided uid.

        Args:
            uid (str): The unique identifier of the snippet.

        Returns:
            A tuple representing a single record in the 'snippets' table. The tuple contains the following fields:
                - uid (str): The unique identifier of the snippet.
                - title (str): The title of the snippet.
                - description (str): The description of the snippet.
                - content (str): The content of the snippet.
                - created (datetime): The timestamp when the snippet was created.
                - category (str): The category of the snippet.

        Raises:
            OperationalError: If there is an error executing the SQL statement.
        """
        # SQL statement to select fields from the 'snippets' table where uid matches the provided uid
        sql = 'SELECT uid, title, description, content, created, category FROM snippets WHERE uid = ?'
        try:
            # Execute the query with the provided uid as a parameter
            results = self.conn.execute(sql, (uid,))
            # Return a single record (first match)
            return results.fetchone()
        except OperationalError as e:
            # Handle any operational error and re-raise it
            raise e

    def find_by_title(self, txt):
        """
        Finds snippets in the 'snippets' table that have titles or categories matching the provided text.

        Parameters:
            txt (str): The text to search for in the titles or categories.

        Returns:
            list: A list of tuples representing the matching records in the 'snippets' table. Each tuple contains the following fields:
                - uid (str): The unique identifier of the snippet.
                - title (str): The title of the snippet.
                - description (str): The description of the snippet.
                - content (str): The content of the snippet.
                - updated (datetime): The timestamp when the snippet was last updated.
                - category (str): The category of the snippet.

        Raises:
            OperationalError: If there is an error executing the SQL statement.
        """
        # SQL statement to find snippets with titles or categories matching the provided text
        sql = 'SELECT uid, title, description, content, updated, category FROM snippets WHERE title LIKE ? OR category LIKE ?'
        try:
            # Execute the query with wildcard search for text matching the title or category
            results = self.conn.execute(sql, ('%' + txt + '%', '%' + txt + '%'))
            # Return all matching records as a list of tuples
            return results.fetchall()
        except OperationalError:
            # Handle any operational error and re-raise it
            raise

    def set(self, *args):
        """
        Inserts a new snippet into the 'snippets' table.

        Parameters:
            *args (tuple): The arguments to be inserted into the table. The order of the arguments should be as follows:
                - uid (str): The unique identifier of the snippet.
                - created (datetime): The timestamp when the snippet was created.
                - stars (int): The number of stars the snippet has.
                - title (str): The title of the snippet.
                - description (str): The description of the snippet.
                - content (str): The content of the snippet.
                - thumbnail (str): The URL of the thumbnail image for the snippet.
                - author (str): The author of the snippet.
                - author_info (str): Additional information about the author.
                - uuid (str): The UUID of the snippet.

        Returns:
            None

        Raises:
            OperationalError: If there is an error executing the SQL statement.
        """
        # SQL statement to insert a new snippet into the 'snippets' table
        sql = """ INSERT INTO snippets
                  VALUES (null, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?, ?, ?,?)"""
        try:
            # Execute the SQL statement with provided arguments
            self.conn.execute(sql, (str(uid(16)), args[3], 0, args[0], args[1], args[2], "https://picsum.photos/80", "Me", "My info", str(uuid.uuid4())))
        except OperationalError as e:
            # Handle any operational error and re-raise it
            raise e
        else:
            # Commit the transaction to save changes
            self.conn.commit()

    def update(self, *args):
        """
        Updates a snippet in the 'snippets' table based on the provided uid.

        Args:
            *args: Variable-length argument list. The arguments should be in the following order:
                - uid (str): The unique identifier of the snippet to be updated.
                - title (str): The new title of the snippet.
                - description (str): The new description of the snippet.
                - content (str): The new content of the snippet.
                - category (str): The new category of the snippet.

        Raises:
            OperationalError: If there is an error executing the SQL statement.

        Returns:
            None
        """
        # SQL statement to update a snippet in the 'snippets' table based on the provided uid
        sql = """ UPDATE snippets
                  SET title = ?,
                      description = ?,
                      content = ?,
                      category = ?,
                      updated = CURRENT_TIMESTAMP
                  WHERE uid = ?"""
        try:
            # Execute the SQL statement with provided arguments
            self.conn.execute(sql, (args[1], args[2], args[3], args[4], args[0]))
        except OperationalError as e:
            # Handle any operational error and re-raise it
            raise e
        else:
            # Commit the transaction to save changes
            self.conn.commit()

    def delete_uid(self, uid):
        """
        A function to delete a snippet from the 'snippets' table based on the provided uid.

        Args:
            - uid (str): The unique identifier of the snippet to be deleted.
        
        Raises:
            Exception: If there is an error during deletion.
        
        Returns:
            bool: True to indicate successful deletion.
        """
        # SQL statement to delete a snippet from the 'snippets' table based on the provided uid
        sql = 'DELETE FROM snippets WHERE uid = ?'
        try:
            # Execute the SQL statement with the provided uid as a parameter
            self.conn.execute(sql, (uid,))
            # Commit the transaction to confirm the deletion
            self.conn.commit()
            # Return True to indicate the deletion was successful
            return True
        except Exception as e:
            # Handle any exception and re-raise it
            raise e
