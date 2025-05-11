class SimplePreprocessor:
    def __init__(self):
        self.definitions = {}

    def define(self, name, value):
        self.definitions[name] = value

    def include(self, filename):
        with open(filename, 'r') as file:
            return self.process(file.read())

    def process(self, code):
        processed_lines = []
        lines = code.splitlines()

        for line in lines:
            line = line.strip()
            if line.startswith('#define'):
                _, name, value = line.split(maxsplit=2)
                self.define(name, value)
            elif line.startswith('#include'):
                _, filename = line.split(maxsplit=1)
                included_code = self.include(filename.strip('"'))
                processed_lines.append(included_code)
            else:
                for name, value in self.definitions.items():
                    line = line.replace(name, value)
                processed_lines.append(line)

        return '\n'.join(processed_lines)

import sys

if __name__ == "__main__":
    to_preprocess = sys.argv[1]
    input_code = ""

    with open(to_preprocess, 'r', encoding='utf-8') as f:
        input_code = f.read()
        f.close()
    
    preprocessor = SimplePreprocessor()

    processed_code = preprocessor.process(input_code)
    
    with open(to_preprocess.replace(".py", ".ph.py"), 'w', encoding='utf-8') as f:
        f.write(processed_code)
        f.close()