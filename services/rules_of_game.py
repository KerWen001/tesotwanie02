class RulesOfGame:

    """
        Metoda zwraca true, tylko gdy przejscie z polozenia source na destination w jednym ruchu jest zgodne
        z zasadami gry w szachy.
    """
    def is_correct_move(self, source, destination):
        raise NotImplementedError("Subclasses must implement this method")

class Bishop(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        return abs(source_col - dest_col) == abs(source_row - dest_row) and source != destination

class Knight(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination
        moved_col = abs(source_col - dest_col)
        moved_row = abs(source_row - dest_row)

        return (moved_col, moved_row) in [(1, 2), (2, 1)] and source != destination

class Rook(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination
        moved_col = abs(source_col - dest_col)
        moved_row = abs(source_row - dest_row)

        return abs(source_row == dest_row) or abs(source_col == dest_row) and source != destination

class King(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        return abs(source_col - dest_col) <= 1 and abs(source_row - dest_row) <= 1 and source != destination

class Pawn(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        if source_col == dest_col:
            if source_row == 2 and dest_row == 4:
                return True
            return abs(source_row - dest_row) == 1

        return False

class Queen(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination


        return (abs(source_col - dest_col) == abs(source_row - dest_row) or source_col == dest_col or source_row == dest_row) and source != destination


# TODO: Prosze dokonczyc implementacje kolejnych figur szachowych: Knight, King, Queen, Rook, Pawn
# TODO: Klasy powinny dziedziczyc RulesOfGame