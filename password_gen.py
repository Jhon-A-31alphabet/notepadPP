import random
import string


class passwords:
    def __init__(self,size) -> str:
        self.size: int = size
        self.character :tuple = string.ascii_letters +string.punctuation
    
    def generate_pass(self):
        pass__= random.sample(self.character,k=self.size)
        print(len(self.character))
        code ="".join(pass__)
        return code





    
        
        