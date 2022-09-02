import random
import sys
from faker import Faker
from ups_track import Track
from utils.db import db


def create_fake_tracks(n):
    """Generate fake users."""
    faker = Faker()
    for i in range(n):
        user = Track(name=faker.name(),
                    age=random.randint(20, 70),
                    address=faker.address().replace('\n', ', '),
                    phone=faker.phone_number(),
                    email=faker.email(),
                    tracking_number = faker.pystr())
        db.session.add(user)
    db.session.commit()
    print(f'Added {n} fake users to the database.')


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Pass the number of users you want to create as an argument.')
        sys.exit(1)
    create_fake_tracks(int(sys.argv[1]))
