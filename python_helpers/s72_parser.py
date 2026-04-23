import json
import argparse


def duplicate_node(scene, node_name, n):
    root_node = None
    node_to_duplicate = None
    for node in scene[1:]:
        if node["name"] == node_name:
            node_to_duplicate = node
        elif node["type"] == "SCENE":
            root_node = node
    
    if not node_to_duplicate:
        print(f"Node '{node_name}' not found in the scene.")
        return
    
    for i in range(n):
        new_node = node_to_duplicate.copy()
        new_node["name"] = f"{node_name}_{i+1}"
        
        # Add the new node to the scene
        scene.append(new_node)
        root_node["roots"].append(new_node["name"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", help="path to input file")
    parser.add_argument("-o", "--out_file", help="optional output file to write modified scene")
    parser.add_argument("-duplicate", "-d", nargs=2, metavar=("NODE_NAME", "N"), help="duplicate a node N times")
    args = parser.parse_args()

    with open(args.input_path) as f:
        scene = json.load(f)
    
    '''
    scene[0] is version number (can ignore)
    scene[1:] is a list of dictionaries, each representing a node/light/camera/mesh etc.
    '''

    if args.duplicate:
        duplicate_node(scene, args.duplicate[0], int(args.duplicate[1]))

    if args.out_file:
        with open(args.out_file, "w") as f:
            json.dump(scene, f, indent=4)