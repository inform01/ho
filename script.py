from Pyro4 import expose

class Solver:
    def __init__(self, workers=None, input_file_name=None, output_file_name=None):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.workers = workers
        print("Inited")

    def solve(self):
        print("Job Started")
        n = self.read_input()
        step = len(n) // len(self.workers)

        mapped = []
        for i in range(len(self.workers)):
            start_index = i * step
            end_index = (i + 1) * step if i < len(self.workers) - 1 else len(n)
            mapped.append(self.workers[i].mymap(n[start_index:end_index]))

        print('Map finished:', mapped)

        reduced = self.myreduce(mapped)
        print("Reduce finished:", reduced)

        self.write_output(reduced)
        print("Job Finished")

    @staticmethod
    @expose
    def mymap(plaintext):
        if isinstance(plaintext, unicode): 
            plaintext = plaintext.encode('utf-8') 

        key = 'secret'
        key_bytes = key.encode('utf-8') 
        encrypted_bytes = bytearray()
        
        for i, byte in enumerate(plaintext):
            encrypted_bytes.append(ord(byte) ^ ord(key_bytes[i % len(key_bytes)]))
        
        return bytes(encrypted_bytes)


    @staticmethod
    @expose
    def myreduce(mapped):
        output = bytes()
        for future_result in mapped:
            result = future_result.value  
            output += result  
        return output



    def read_input(self):
        with open(self.input_file_name, 'rb') as f:  
            text = f.read()
        return text 

    def write_output(self, output):
        with open(self.output_file_name, 'wb') as f:
            f.write(output)
            f.write(b'\n')
