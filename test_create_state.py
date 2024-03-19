import unittest
import os
import mysql.connector

class TestCreateState(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Connect to the MySQL database using environment variables
        cls.conn = mysql.connector.connect(
            host=os.getenv("HBNB_MYSQL_HOST"),
            user=os.getenv("HBNB_MYSQL_USER"),
            password=os.getenv("HBNB_MYSQL_PWD"),
            database=os.getenv("HBNB_MYSQL_DB")
        )
        cls.cursor = cls.conn.cursor()

    @classmethod
    def tearDownClass(cls):
        # Clean up
        cls.cursor.close()
        cls.conn.close()

    def setUp(self):
        # Get initial record count
        self.cursor.execute("SELECT COUNT(*) FROM states")
        self.initial_count = self.cursor.fetchone()[0]

    def test_create_state(self):
        # Execute the console command (e.g., insert a record)
        self.cursor.execute("INSERT INTO states (name) VALUES ('California')")
        self.conn.commit()

        # Get the number of records again
        self.cursor.execute("SELECT COUNT(*) FROM states")
        final_count = self.cursor.fetchone()[0]

        # Check if the difference is +1
        self.assertEqual(final_count - self.initial_count, 1)

if __name__ == '__main__':
    unittest.main()

