from clusters import Clusters

c = Clusters()
c.ingest()
print(c.guess)
print(c.cluster(8))
