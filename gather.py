import random

class Gather:
    def __init__(self):
        pass

    def gen_company(self):
        return {
          "name": "Company",
          "size": random.randint(1, 10),
          "prediction": random.random()
        }

    def get_json(self, clusters, sizeper):
        children = []

        for i in range(0, clusters):
            temp = []
            for i in range(0, sizeper):
                temp.append(self.gen_company())
            wrapper = {
              "name": "thing" + str(i),
              "children": temp
            }
            children.append(wrapper)

        return {
          "name": "FINRA",
          "children": children
        }