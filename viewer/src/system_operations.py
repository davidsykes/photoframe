
class SystemFileLoader:
    def load_file(self, file_name):
        with open(file_name, 'r') as file:
            data = file.read()
        return data