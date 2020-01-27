from flask_seeder import Seeder, Faker, generator
from computer_model import ComputerModel
class ComputerSeeder(Seeder):
    def run(self):
        mock = Faker(
            cls = ComputerModel,
            init = {
                "com_id": generator.Sequence(),
                "name": generator.Name(),
                "price": generator.Integer(start=500, end=2000),
                "ram": generator.Integer(start=2, end=16),
                "disk": generator.Integer(start=120, end=500),
                "quantity": generator.Integer(start=1, end=50)
            }
        )
    
        for each_computer in mock.create(4):
            print("Adding computer: %s" % each_computer)
            self.db.session.add(each_computer)
            self.db.session.commit()
