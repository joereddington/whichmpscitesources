cd /home/joereddington/joereddington.com/mps_always
python tweet_dumper.py
mv *.csv full/
python process_stores.py > list.txt
#tar -zcvf "$(date '+%y-%m-%d').tar.gz" full/
