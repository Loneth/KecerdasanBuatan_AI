import json


class TreeNode:
    def __init__(self, label):
        self.label = label
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def build_tree_from_json(data, root_label):
    node = TreeNode(root_label)
    nodes = {root_label: node}

    for item in data:
        label = item["label"]
        children_labels = item.get("children", [])

        parent_node = nodes[label]
        for child_label in children_labels:
            child_node = TreeNode(child_label)
            parent_node.add_child(child_node)
            nodes[child_label] = child_node

    return node


def get_directions(tree, current_location, destination, x):
    if tree.label == current_location:
        return find_path(tree, destination, [], x)

    for child in tree.children:
        path = get_directions(child, current_location, destination, x)
        if path:
            return path

    return None


def find_path(node, destination, path, x):
    if node.label == destination:
        return (path + [node.label])
    listtempatbuang = list()
    for child in node.children:
        if (child.label[-1] == "!"):
            x.add(child.label)
            continue
        else:
            child_path = find_path(child, destination, path + [node.label], x)
            if child_path:
                return child_path

    return None


def main():
    # Membaca data JSON
    with open("tree_data.json") as file:
        data = json.load(file)

    greet = input("Salam mahasiswa!!, Aku adalah bot penunjuk arah Gedung Agape lantai 1 UKDW! \n")
    if (
            greet == "yo" or greet == "y" or greet == "hai" or greet == "ya" or greet == "hi" or greet == "hello" or greet == "ok"):
        while (True):
            # Menerima input pengguna

            start_point = input("Masukkan titik awal: ")
            target_point = input("Masukkan titik tujuan: ")

            # Membangun pohon dari data JSON dengan root berdasarkan input pengguna
            tree = build_tree_from_json(data, "toilet")

            if tree is None:
                print("Titik awal tidak ditemukan dalam pohon.")
                return

            # Memberikan petunjuk arah
            x = set()
            path = get_directions(tree, start_point, target_point, x)

            if path:
                directions = " -> ".join(path)
                for i in x:
                    print("Mohon maaf terjadi pemblokiran jalan di", i[0:-1])
                print(f"Petunjuk arah dari {start_point} ke {target_point} silahkan ikuti rute ini {directions}")

            else:
                print(f"Tidak ditemukan petunjuk arah dari {start_point} ke {target_point}.")

            exit = input("Apakah sudah selesai?\n")
            if (exit == "ya" or exit == "y" or exit == "ok" or exit == "yes"):
                break


# Menjalankan program utama
main()
