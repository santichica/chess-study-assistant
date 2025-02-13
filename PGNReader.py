import chess
import chess.pgn
import zipfile
import io

class PGNReader:
    def __init__(self, zip_filepath, pgn_filename, encoding='utf-8'):
        self.zip_filepath = zip_filepath
        self.pgn_filename = pgn_filename
        self.encoding = encoding
        self.game = self._load_game()

    def _load_game(self):
        """Loads the PGN from the zip file."""
        try:
            with zipfile.ZipFile(self.zip_filepath, 'r') as zip_ref:
                with zip_ref.open(self.pgn_filename) as pgn_file:
                    pgn_text = io.TextIOWrapper(pgn_file, encoding=self.encoding)
                    game = chess.pgn.read_game(pgn_text)
                    return game
        except FileNotFoundError:
            print(f"Error: Zip file '{self.zip_filepath}' or PGN file '{self.pgn_filename}' not found.")
            return None
        except zipfile.BadZipFile:
            print(f"Error: Invalid zip file: '{self.zip_filepath}'.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_game(self):
        return self.game


if __name__ == "__main__":
    zip_file = "poc-data.zip"
    pgn_file = "twic1579.pgn"
 
    # Example of how to access the game object:
    pgn_reader = PGNReader(zip_file, pgn_file)
    game = pgn_reader.get_game()
    if game:
        print(game.headers)