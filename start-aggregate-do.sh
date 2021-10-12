export PYTHONUNBUFFERED=1
export PYTHONPATH=/root/dev/nlp/python
export OUT_SUB_FOLDER=antlr
python3 -m python.aggregate --outpath /root/dev/nlp/dict/erpnext
python3 -m python.aggregate --outpath /root/dev/nlp/dict/adempiere
python3 -m python.aggregate --outpath /root/dev/nlp/dict/axelor-open-suite
python3 -m python.aggregate --outpath /root/dev/nlp/dict/dolibarr
python3 -m python.aggregate --outpath /root/dev/nlp/dict/metafresh
