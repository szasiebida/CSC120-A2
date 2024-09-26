class Computer:
    
    #these are attributes of the computer
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    
    
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        
        self.description=description
        self.processor_type=processor_type
        self.hard_drive_capacity=hard_drive_capacity
        self.memory=memory
        self.operating_system=operating_system
        self.year_made=year_made
        self.price=price
        #now all of the attributes are referenced and stored
    

def main():
    
    # First, let's make a computer
    computer =Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    print(computer.description)
    # What methods will you need?
    print(computer.operating_system)
    print(computer.price)


if __name__=='__main__':
    main()