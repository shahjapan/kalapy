import pickle

try:
    import threading
except ImportError:
    import dummy_threading as threading

from werkzeug.contrib.sessions import SessionStore


class Store(SessionStore):

    def __init__(self, session_class=None):
        super(Store, self).__init__(session_class)
        self.store = {}
        self.lock = threading.RLock()

    def save(self, session):
        self.lock.acquire()
        try:
            self.store[session.sid] = pickle.dumps(dict(session))
        except pickle.PickleError:
            #raise TypeError('Invalid session data')
            pass
        finally:
            self.lock.release()

    def delete(self, session):
        self.lock.acquire()
        try:
            del self.store[session.id]
        finally:
            self.lock.release()

    def get(self, sid):
        if not self.is_valid_key(sid):
            return self.session_class.new()
        try:
            data = pickle.loads(self.store[sid])
        except KeyError:
            data = {}
        return self.session_class(data, sid, False)

    def list(self):
        return self.store.keys()

