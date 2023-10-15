class FileManager:

    @staticmethod
    def file_reader(path):
        with open(path, 'r') as file:
            data = file.read()
        return data
    
    @staticmethod
    def file_writer(path, data):
        try:
            with open(path, 'w') as file:
                file.write(data)
        except Exception as e:
            print(f'Dogodila se pogreska {e}')
            
    @staticmethod
    def file_append(path, data):
        try:
            with open(path, 'a') as file:
                file.write(data)
        except Exception as e:
            print(f'Dogodila se pogreska {e}')

    @staticmethod
    def read_lines(path):
        with open(path, 'r') as file:
            lines = file.readlines()
            return lines
