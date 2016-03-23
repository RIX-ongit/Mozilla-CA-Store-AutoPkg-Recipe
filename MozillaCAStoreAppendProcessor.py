#!/usr/bin/python

from autopkglib import Processor, ProcessorError
import fileinput

__all__ = ["MozillaCAStoreAppendProcessor"]

class MozillaCAStoreAppendProcessor(Processor):
    description = __doc__
    input_variables = {
        "product_name": {
            "required": False,
            "default": "MozillaCAStore",
            "description": "What to name the Final PEM file.",
        },
        "append_pem": {
            "required": True,
            "description": "The PEM file to be appended",
        },
        "mozilla_pem": {
            "required": True,
            "description": "The Mozilla CA Certificate Store location.",
        },
        "final_pem": {
            "required": True,
            "description": "The location of the final PEM file.",
        },
    }
    output_variables = {
        "done": {
            "description": "Returns True when new file is generated."
        }
    }
    
    def main(self):
        product_name = self.env.get("product_name", "MozillaCAStore")
        append_pem = self.env["append_pem"]
        mozilla_pem = self.env["mozilla_pem"]
        final_pem = self.env["final_pem"]
        
        with open(final_pem, 'w') as fout, fileinput.input([mozilla_pem, append_pem]) as fin:
            for line in fin:
                fout.write(line)
        fout.close()
        self.env["done"] = True
        self.output(True)
    
if __name__ == "__main__":
    PROCESSOR = MozillaCAStoreAppendProcessor()
    PROCESSOR.execute_shell()