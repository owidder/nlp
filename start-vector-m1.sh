export PYTHONUNBUFFERED=1
export PYTHONPATH=/Users/oliverwidder/Documents/github/nlp/python
export DO_REMOVE_NON_CHARS=True
export DO_SPLIT_CAMEL_CASE=True
export DO_REMOVE_STOP_WORDS=True
export DO_FILTER_NON_EN_DE_WORDS=True
export MIN_WORD_SIZE=4
export WITH_STEMMING=True
export NUM_TOPICS=2000
export MAX_WORDS=0
export OUT_SUB_FOLDER=antlr
export MIN_TFIDF=0.18
export PATH_TO_JAR=/Users/oliverwidder/Documents/github/antlr/build/libs/antlr-1.0-SNAPSHOT.jar
export USE_ANTLR=True
echo PYTHONPATH=$PYTHONPATH
/Users/oliverwidder/Documents/github/nlp/venv/bin/python -m python.create_vectors --outpath /Users/oliverwidder/Documents/github/nlp/dict/_all --docpath /Users/oliverwidder/Documents/dev/erp_doc/erpnext
