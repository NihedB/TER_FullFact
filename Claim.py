import sys
if sys.version_info[0] >= 3:
    unicode = str
class Claim:

	def __init__(self):
		self.source=""
		self.claim=unicode("")
		self.body=unicode("")
		self.conclusion=unicode("")
		self.refered_links=""
		self.title=unicode("")
		self.date=""
		self.url=""
		self.tags=""
		self.verdictTompo=""
		self.html=False


	def setSource(self, str_):
		self.source = str_
		return self

	def setClaim(self, str_):
		self.claim = unicode(str_)
		return self

	def setBody(self, str_):
		self.body = unicode(str_)
		return self

	def setConclusion(self, str_):
		self.conclusion = unicode(str_)
		return self

	def setRefered_links(self, str_):
		self.refered_links = str_
		return self

	def setTitle(self, str_):
		self.title = unicode(str_)
		return self

	def setVerdictTompo(self, str_):
		self.verdictTompo= unicode(str_)
		return self

	def setDate(self, str_):
		self.date = str_
		return self

	def setUrl(self, str_):
		self.url = unicode(str_)
		return self

	def setTags(self, str_):
		self.tags = str_

	def setHtml(self, str_):
		self.html = str_

	

	def getDict(self):
		dict_={}
		dict_['source']=self.source
		dict_['claim']=self.claim
		dict_['body']=self.body.replace("\n","")
		dict_['conclusion']=self.conclusion
		dict_['refered_links']=self.refered_links
		dict_['title']=self.title
		dict_['date']=self.date
		dict_['url']=self.url
		dict_['tags']=self.tags
		dict_['verdictTompo']=self.verdictTompo
		if (self.html):
			dict_['html']=self.html
		return dict_

