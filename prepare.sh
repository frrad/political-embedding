echo 'Fetching info from server...'
./fetch.sh

echo 'Formatting downloaded data...'
./preprocess.py > data.txt

echo 'Producing data summary...'
./aggregate.py > data_info.txt

