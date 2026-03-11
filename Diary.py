class Diary():

    def __init__(self):
        self.sissekanded = []
        self.loendur = 0

    def add_entry(self, text):
        self.loendur += 1
        sissekanne = f"{self.loendur}: {text}"
        self.sissekanded.append(sissekanne)

    def remove_entry(self, index):
        if 0 <= index < len(self.sissekanded):
            self.sissekanded.pop(index)
    
    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            for sissekanne in self.sissekanded:
                file.write(sissekanne + "\n")
    
    def load(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            self.sissekanded = [line.strip() for line in file]
        self.loendur = len(self.sissekanded)
    
    def print_statistics(self):
        lugeja = len(self.sissekanded)

        if lugeja == 0:
            avg = 0
        else:
            total_chars = sum(len(sissekanne) for sissekanne in self.sissekanded)
            avg = total_chars / lugeja
        
        print(f"Sissekannete arv:", (lugeja))
        print(f"Keskmine tähemärkide arv:", (avg))

    def __str__(self):
        return "\n".join(self.sissekanded)
    

d = Diary()
d.add_entry("Täna oli ilus ilm.")
d.add_entry("Õppisin programmeerimist.")
d.save("diary.txt")

d.print_statistics()