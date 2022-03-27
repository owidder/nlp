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
export EXCLUDE_FOLDERS=static,lib,jquery
nohup python3 -m python.create_vectors --outpath /root/dev/nlp/dict/_all/$1 --docpath /root/dev/erp_doc/$1 2>&1 > $1.out &

