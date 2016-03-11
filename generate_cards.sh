python generate_cards.py

cd cards
for filename in *.svg
do
    echo ${filename/.svg/.png}
    inkscape -z -e ${filename/.svg/.png} $filename -d 400
done
cd ..
