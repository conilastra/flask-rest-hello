from flask_sqlalchemy import SQLAlchemy
from twilio.rest import Client

db = SQLAlchemy()

account_sid = 'AC283c1fbabe575473f86738d54fa75c9a'
auth_token = '25dc1579063bc40790cf93361f623150'
client = Client(account_sid, auth_token)



# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<Person %r>' % self.username

#     def serialize(self):
#         return {
#             "username": self.username,
#             "email": self.email
#         }

class Queue:

    def __init__(self):
        self._queue = []
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = 'FIFO'

    def enqueue(self, item):
        size = self.size()
        content = item['name'] + ' hay ' + str(size) + ' personas antes que tú en la fila'
        message = client.messages \
            .create(
                body= content,
                from_='+12563673043',
                status_callback='http://postb.in/1234abcd',
                to=item['phone']
            )

        return self._queue.append(item)

    def dequeue(self):
        name = self._queue[0]['name']
        recipient = self._queue[0]['phone']
        content = name + ', es tu turno! :)'
        message = client.messages \
            .create(
                body= content,
                from_='+12563673043',
                status_callback='http://postb.in/1234abcd',
                to=recipient
            )

        return self._queue.pop(0)


    def get_queue(self):
        return self._queue

    def size(self):
        return len(self._queue)