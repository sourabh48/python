import os
for root, directories, filenames in os.walk('upload'):    
    for file in filenames:
        print(file)
        
