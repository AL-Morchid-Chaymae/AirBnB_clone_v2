import unittest
import MySQLdb

class TestAddState(unittest.TestCase):

    def test_add_state(self):
        # Connexion à la base de données de test
        conn = MySQLdb.connect(host='localhost', user='hbnb_test', passwd='hbnb_test_pwd', db='hbnb_test_db')
        cursor = conn.cursor()

        # Compter le nombre d'états avant l'ajout
        cursor.execute("SELECT COUNT(*) FROM states")
        count_before = cursor.fetchone()[0]

        # Exécuter la commande pour ajouter un état (simulant une action de l'utilisateur)
        # (par exemple, vous pouvez appeler une fonction de votre application ici)
        # Commande hypothétique: add_state("California")

        # Compter le nombre d'états après l'ajout
        cursor.execute("SELECT COUNT(*) FROM states")
        count_after = cursor.fetchone()[0]

        # Vérifier si le nombre d'états a augmenté de 1
        self.assertEqual(count_after, count_before + 1)

        # Fermer la connexion
        cursor.close()
        conn.close()

if __name__ == '__main__':
    unittest.main()
