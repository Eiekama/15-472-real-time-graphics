#!/bin/bash
# for i in {1,2,5,10,20,50,100,200,500,1000,2000,5000}; do
#     ./bin/viewer --scene ../a3-submission/report/s72-files/lights-performance-test/sun_$i.s72 --timer ../a3-submission/report/timings/sun-lights/sun_$i.txt --headless < _temp.txt 
# done
# for i in {1,2,5,10,20,50,100,200,500,1000,2000,5000}; do
#     ./bin/viewer --scene ../a3-submission/report/s72-files/lights-performance-test/sphere_$i.s72 --timer ../a3-submission/report/timings/sphere-lights/sphere_$i.txt --headless < _temp.txt
# done
# for i in {1,2,5,10,20,50,100,200,500,1000,2000,5000}; do
#     ./bin/viewer --scene ../a3-submission/report/s72-files/lights-performance-test/spot_$i.s72 --timer ../a3-submission/report/timings/spot-lights/spot_$i.txt --headless < _temp.txt 
# done

python ../python_helpers/analyze.py ../a3-submission/report/timings/sun-lights/
python ../python_helpers/analyze.py ../a3-submission/report/timings/sphere-lights/
python ../python_helpers/analyze.py ../a3-submission/report/timings/spot-lights/