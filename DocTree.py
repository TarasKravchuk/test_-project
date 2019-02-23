import os

way_where_to_save_the_tree = input("Input the path to dir where you want to create a dir tree ")
file_name = input("Input the the name of dir tree file ")
class DirParser:
    def __init__(self, in_path, way_where_to_save_the_tree, file_name):
        self.in_path = in_path
        self.way_where_to_save_the_tree = way_where_to_save_the_tree
        self.file_name = file_name

    def checker(self, way_where_to_save_the_tree, file_name):
        ls_dir = os.listdir(way_where_to_save_the_tree)
        if file_name + ".txt" in ls_dir:
            old_file = os.path.join(way_where_to_save_the_tree, file_name + ".txt")
            new_file = os.path.join(way_where_to_save_the_tree, file_name + "_old" + ".txt")
            os.rename(old_file, new_file)

    def parse_dir(self):
        result = []
        path = self.in_path
        for i in os.walk(self.in_path):
            result.append(i)
        tab_zero = self.in_path.count("/")
        calc = 0
        for adress, dirs, files in result:
            new_tab = result[calc][0].count("/")
            dir_name = (adress.split("/"))[-1]
            if "__init__.py" in files:
                type_dir = "PyP"
            else: type_dir = "Dir"
            path = DirParser.way(self, path, dir_name)
            calc += 1
            tab = new_tab - tab_zero
            if tab < 0:
                tab = 0
            DirParser.dirs_writer(self, dir_name, type_dir, tab, way_where_to_save_the_tree, file_name)

            for file in files:
                file = file
                type_file = file.split(".")[-1]
                if type_file == "py":
                    type_file = "PyF"
                DirParser.file_writer(self, file, type_file, tab, way_where_to_save_the_tree, file_name)

    def way (self,path, dir_name):
        path = os.path.join(path,dir_name)
        return path

    def dirs_writer (self, dir, type_dir, tab, way_where_to_save_the_tree, file_name):
        foo = "  "
        dir_dir_type = tab * "\t" + str(dir) + foo + str(type_dir) + "\n"
        with open(way_where_to_save_the_tree+'/' + file_name + ".txt", 'a') as f:
            f.write(dir_dir_type)

    def file_writer (self, file, type_file, tab, way_where_to_save_the_tree, file_name):
        foo = "  "
        file_file_type = tab * "\t" + str(file) + foo + str(type_file) + "\n"
        with open(way_where_to_save_the_tree+'/' + file_name + ".txt", 'a') as f:
            f.write(file_file_type)

a  = DirParser('/home/taras/Documents', way_where_to_save_the_tree, file_name)
a.checker(way_where_to_save_the_tree, file_name)
a.parse_dir()
