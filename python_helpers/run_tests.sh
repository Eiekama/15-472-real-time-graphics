#!/bin/bash

# source /Users/chenjingxuan/VulkanSDK/1.4.335.1/setup-env.sh  

# ./bin/viewer --scene ../f-submission/report/scenes/cloud.s72 --headless --timer ../f-submission/report/timings/step_size/adj250.txt < _temp.txt
# ./bin/viewer --scene ../f-submission/report/scenes/cloud_big.s72 --headless --timer ../f-submission/report/timings/cloud_big_no_adastep.txt < _temp.txt
# ./bin/viewer --scene ../f-submission/report/scenes/cloud_16.s72 --headless --timer ../f-submission/report/timings/cloud_16.txt < _temp.txt
# ./bin/viewer --scene ../f-submission/report/scenes/cloud_32.s72 --headless --timer ../f-submission/report/timings/cloud_32.txt < _temp.txt
# ./bin/viewer --scene ../f-submission/report/scenes/cloud_64.s72 --headless --timer ../f-submission/report/timings/cloud_64.txt < _temp.txt


# python ../python_helpers/analyze.py ../f-submission/report/timings/screen_space/cloud_small.txt -r
# python ../python_helpers/analyze.py ../f-submission/report/timings/screen_space/cloud_small_no_adastep.txt -r
# python ../python_helpers/analyze.py ../f-submission/report/timings/screen_space/cloud_big.txt -r
# python ../python_helpers/analyze.py ../f-submission/report/timings/screen_space/cloud_big_no_adastep.txt -r

python ../python_helpers/analyze.py ../f-submission/report/timings/step_size/near/
python ../python_helpers/analyze.py ../f-submission/report/timings/step_size/offset/
python ../python_helpers/analyze.py ../f-submission/report/timings/step_size/adj/