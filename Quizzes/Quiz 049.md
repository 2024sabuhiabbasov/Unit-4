# Quiz 049

![image](https://user-images.githubusercontent.com/111758436/221758659-5c1aeddd-0890-4496-b056-9ba22d5a31d5.png)

## My codes
### Python
```.py
# Program for Quiz 049

from secure_password import check_password
import sqlite3

class database_worker:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()

db = database_worker("bitcoin_exchange.db")
query = "SELECT * from ledger"
result = db.search(query)
db.close()

total = 0

for row in result:
    (id, sender_id, receiver_id, amount, hash) = row
    string_hash = f"id {id},sender_id {sender_id},receiver_id {receiver_id},amount {amount}"
    checker = check_password(hashed_password=hash, user_password=string_hash)

    if checker:
        total += amount
    else:
        pass

print(f"The total amount of bitcoins transferred by valid transactions{total}")
```
### Proof
![image](https://user-images.githubusercontent.com/111758436/221759199-08de0d3b-24ed-4890-bb72-10c9098854fd.png)
