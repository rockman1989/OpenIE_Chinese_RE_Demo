#   coding=utf-8

from stanfordcorenlp import StanfordCoreNLP
import json
try:
	nlp = StanfordCoreNLP(r'./stanford-corenlp-4.0.0', lang="zh")

	ss = '我爱北京'
	props={'annotators': 'openie','pipelineLanguage':'zh','outputFormat':'json'}
	res = json.loads(nlp.annotate(ss,properties=props))
	triples = []
	for sentence in res["sentences"]:
		for triple in sentence['openie']:
			triples.append({
			'subject': triple['subject'],
			'relation': triple['relation'],
			'object': triple['object']
			})
	print(triples)
finally:
	nlp.close()
	print("NLP_close")
