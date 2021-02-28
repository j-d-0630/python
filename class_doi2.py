class student():
    def __init__(self, name, math, japanese, science):
        self.name = name
        self.math = math
        self.japanese = japanese
        self.science = science
    
    def getTotalScore(self):
        return self.math + self.japanese + self.science


class rankingSystem():
    def __init__(self, members):
        self.members = members
        self.members_ranked = []
    
    def ranking(self):
        self.members_ranked = self.members.copy()

        for i in range(0, len(self.members)):
            for j in range(len(self.members)-1, i, -1):
                if self.members_ranked[j].getTotalScore() > self.members_ranked[j-1].getTotalScore():
                    tmp = self.members_ranked[j-1]
                    self.members_ranked[j-1] = self.members_ranked[j]
                    self.members_ranked[j] = tmp
    
    def annouce(self):
        for i in self.members_ranked:
            score = i.getTotalScore()
            print(i.name + str(score))


if __name__ == "__main__":
    a = student("aさん", 10, 10, 10)
    b = student("bさん", 20, 20, 20)
    c = student("cさん", 30, 30, 30)
    d = student("dさん", 40, 40, 40)
    e = student("eさん", 50, 50, 50)

    rankingSystem = rankingSystem([a, b, c, d, e])
    rankingSystem.ranking()
    rankingSystem.annouce()