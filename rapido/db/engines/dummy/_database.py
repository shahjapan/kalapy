from rapido.db._interface import IDatabase

__all__ = ('DatabaseError', 'IntegrityError', 'Database')


class DatabaseError(Exception):
    pass

class IntegrityError(DatabaseError):
    pass

class Database(IDatabase):
    pass

