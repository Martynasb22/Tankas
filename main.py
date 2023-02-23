import random

class Tank:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = "North"
        self.shots = {"North": 0, "East": 0, "South": 0, "West": 0}

    def move_forward(self):
        if self.direction == "North":
            self.y += 1
        elif self.direction == "East":
            self.x += 1
        elif self.direction == "South":
            self.y -= 1
        elif self.direction == "West":
            self.x -= 1
        self.update_scores(10)

    def move_backward(self):
        if self.direction == "North":
            self.y -= 1
        elif self.direction == "East":
            self.x -= 1
        elif self.direction == "South":
            self.y += 1
        elif self.direction == "West":
            self.x += 1
        self.update_scores(10)

    def turn_left(self):
        if self.direction == "North":
            self.direction = "West"
        elif self.direction == "West":
            self.direction = "South"
        elif self.direction == "South":
            self.direction = "East"
        elif self.direction == "East":
            self.direction = "North"

    def turn_right(self):
        if self.direction == "North":
            self.direction = "East"
        elif self.direction == "East":
            self.direction = "South"
        elif self.direction == "South":
            self.direction = "West"
        elif self.direction == "West":
            self.direction = "North"

    def shoot(self):
        self.shots[self.direction] += 1
        if self.x == target_x and self.y == target_y:
            print("Pataikei!")
            self.update_scores(50)
            generate_target()
        else:
            print("Nepataikei!")
            self.update_scores(0)

    def info(self):
        print("Kryptis:", self.direction)
        print("Koordinatės:", self.x, self.y)
        print("Iš viso šūvių:", sum(self.shots.values()))
        print("Šūviai į kryptį:", self.shots)

    def update_scores(self, points):
        global score
        score += points

def generate_target():
    global target_x, target_y
    target_x = random.randint(-10, 10)
    target_y = random.randint(-10, 10)

score = 100
tank = Tank()
generate_target()

while score > 0:
    print("Taškai:", score)
    action = input("Pasirinkite veiksmą: \n1. pirmyn\n 2. atgal\n 3. kairėn\n 4. dešinėn\n 5. šūvis\n 6. info\n 7. exit \nĮvesk pasirinkimą: ")
    if action == "1":
        tank.move_forward()
    elif action == "2":
        tank.move_backward()
    elif action == "3":
        tank.turn_left()
    elif action == "4":
        tank.turn_right()
    elif action == "5":
        tank.shoot()
    elif action == "6":
        tank.info()
    elif action == "7":
        break

print("Žaidimas baigtas. Jūs numušėte", sum(tank.shots.values()), "taikinius.")