import json
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", help="path to input file")
    parser.add_argument("-o", "--out_file", help="optional output file to write modified scene")
    args = parser.parse_args()

    with open(args.input_path) as f:
        scene = json.load(f)
    
    '''
    scene[0] is version number (can ignore)
    scene[1:] is a list of dictionaries, each representing a node/light/camera/mesh etc.
    '''

#     def s(i):
#         return '''{
# 	"type":"NODE",
# 	"name":"Cube'''+str(i)+'''",
# 	"translation":[0,3,0],
# 	"rotation":[0,0,0,1],
# 	"scale":[1,1,1],
# 	"mesh":"Cube"
# },
# '''
#     print(s(0))
#     with open("../scenes/temp.txt", "w") as f:
#         for i in range(10000):
#             # f.write(s(i))
#             f.write(f'"Cube{i}", ')