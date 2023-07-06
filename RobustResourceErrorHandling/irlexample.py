class Conntection:
    def __init__(self):
        self.xid = 0
    
    def _start_transcation(self):
        print('starting transcation,' self.xid)
        rslt = self.xid
        self.xid = self.xid + 1
        return rslt
    
    
    def _commit_transcation(self, xid):
        print('commiting trans', xid)
        
    def _rollback_transaction(self, xid):
        print('rolling back trans', xid)
    
    
class Transcation:
    def __init__(self, conn):
        self.conn = conn
        self.xid - conn._start_transcation()
    
    def commit(self):
        self.conn._commit_transcation(self.xid)
        
    def rollback(self):
        self.conn_rollback_transation(self.xid)
        
        
        