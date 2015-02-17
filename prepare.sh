echo 'Fetching info from server...'
rsync -avz --delete --delete-excluded --exclude **/text-versions/ govtrack.us::govtrackdata/congress/113/votes .

echo 'Formatting downloaded data...'
./preprocess.py > data.txt

echo 'Producing data summary...'
./aggregate.py > data_info.txt


