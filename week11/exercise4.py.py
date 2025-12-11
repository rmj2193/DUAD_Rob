class Head:
    def __init__(self):
        pass

class Torso:
    def __init__(self, head, left_arm, right_arm, left_leg, right_leg):
        self.head = head
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Hand:
    def __init__(self):
        pass

class Leg:
    def __init__(self, foot):
        self.foot = foot

class Feet:
    def __init__(self):
        pass

class Human:
    def __init__(self):
        # Create body parts
        head = Head()

        left_hand = Hand()
        right_hand = Hand()

        left_arm = Arm(left_hand)
        right_arm = Arm(right_hand)

        left_foot = Feet()
        right_foot = Feet()

        left_leg = Leg(left_foot)
        right_leg = Leg(right_foot)

        # Assemble 
        self.torso = Torso(head, left_arm, right_arm, left_leg, right_leg)


# Example 
if __name__ == "__main__":
    person = Human()
    print("Human created successfully!")