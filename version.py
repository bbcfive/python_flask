# -*- encoding=utf-8 -*-


class Version:
    def __init__(self,):
        self.versionList = []

    def addVersion(self, strNo, strContent):
        self.versionList.append(dict(version=strNo, content=strContent))

    def getCurrentVersion(self):
        if len(self.versionList)>0:
            return self.versionList[-1].get('version')
        else:
            return '0.0.0'


softVersion = Version()
softVersion.addVersion("0.0.1", "诞生")
