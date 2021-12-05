export PYTHONUNBUFFERED=1
export PYTHONPATH=/root/dev/nlp/python
export DO_REMOVE_NON_CHARS=True
export DO_SPLIT_CAMEL_CASE=True
export DO_REMOVE_STOP_WORDS=True
export DO_FILTER_NON_EN_DE_WORDS=True
export MIN_WORD_SIZE=1
export WITH_STEMMING=True
export NUM_TOPICS=2000
export MAX_WORDS=0
export OUT_SUB_FOLDER=antlr
export MIN_TFIDF=0
export PATH_TO_JAR=/root/dev/antlr/build/libs/antlr-1.0-SNAPSHOT.jar
export USE_ANTLR=True
#python3 -m python.create_vectors --outpath /root/dev/nlp/dict/erpnext --docpath /root/dev/erp_doc/erpnext
#python3 -m python.create_vectors --outpath /root/dev/nlp/dict/adempiere --docpath /root/dev/erp_doc/adempiere
#python3 -m python.create_vectors --outpath /root/dev/nlp/dict/axelor-open-suite --docpath /root/dev/erp_doc/axelor-open-suite
#python3 -m python.create_vectors --outpath /root/dev/nlp/dict/dolibarr --docpath /root/dev/erp_doc/dolibarr
#python3 -m python.create_vectors --outpath /root/dev/nlp/dict/metafresh --docpath /root/dev/erp_doc/metafresh
python3 -m python.create_vectors --outpath /root/dev/nlp/dict/_all --docpath /root/dev/erp_doc
