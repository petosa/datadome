import random
from clusters import Clusters
import numpy as np

class Gather:
    def __init__(self):
        self.caller = Clusters()
        self.caller.ingest()
        print(self.caller.guess)
        print(self.caller.cluster(8))

    def gen_company(self):
        return {
          "name": "Company",
          "size": random.randint(1, 10),
          "prediction": random.random()
        }

    def get_json(self, clusters):
        fresh = self.caller.unsupervised[1:,1:]
        fresh_guesses = np.concatenate((fresh,self.caller.guess.reshape(-1,1)),axis=1)
        clustguess = np.concatenate((fresh_guesses,self.caller.cluster(clusters).reshape(-1,1)),axis=1)
        frame = {
            "name": "FINRA",
            "children": []
        }
        clustmap = {}
        count = 0
        for row in clustguess:
            ind = row[-1]
            inforow = self.caller.info[count]
            if not ind in clustmap:
                clustmap[ind] = []

            clustmap[ind].append({
                "name": self.caller.keys[count],
                "prediction": row[-2],
                "busNm": inforow[0],
                "city": inforow[2],
                "state": inforow[3],
                "SECNb": inforow[1],
                "courtCases": inforow[4],
                "size": 1
            })
            count += 1

        for clusternum in clustmap:
            cluster = {
                "name": "Cluster " + str(clusternum),
                "children": clustmap[clusternum],
                "size": len(clustmap[clusternum])
            }
            print(len(clustmap[clusternum]))
            frame["children"].append(cluster)
        return frame