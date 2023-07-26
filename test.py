# import random
# import time

# #Bernoulli Urn model

# gray_balls = ['Gray'] * 3
# white_balls = ['White'] * 7
# current_urn = gray_balls + white_balls

# # print(f'here are the balls combined: {current_urn}')

# #proportion of white balls will converge to 70% according to Law of Large Nums?

# current_sample_size = 10_000_000

# def urn_model(urn, sample_size):
#     start_time = time.time()
#     gray_ball_draw = 0
#     trial_counter = 0
    
#     while trial_counter <= sample_size:
#         random_pick =random.randint(0, len(urn)-1)
#         if urn[random_pick] == 'Gray':
#             gray_ball_draw += 1
#         trial_counter += 1
#     # print(f'Gray ball: {gray_ball_draw/sample_size}, White ball: {1-(gray_ball_draw/sample_size)}')
#     end_time = time.time()
#     print(f'Tony run time is: {end_time - start_time} seconds for {sample_size} samples')

# urn_model(current_urn, current_sample_size)

# #________________________________________________________

# import random
# import time
# # Bernoulli Urn model

# # print(f'Here are the balls combined: {current_urn}')

# # Proportion of white balls will converge to 70% according to the Law of Large Numbers
# # current_sample_size = 1_000_000

# def urn_model_2(urn, sample_size):
#     start_time = time.time()

#     gray_ball_draw = 0
#     trial_counter = 0

#     while trial_counter < sample_size:
#         if random.choice(urn) == 'Gray':
#             gray_ball_draw += 1
#         trial_counter += 1

#     white_ball_draw = sample_size - gray_ball_draw
#     # print(f'Gray ball: {gray_ball_draw/sample_size}, White ball: {white_ball_draw/sample_size}')
#     end_time = time.time()
#     print(f'GPT run time is: {end_time - start_time} seconds for {sample_size} samples')

# urn_model_2(current_urn, current_sample_size)


# class Car:
#     def __init__(self, brand: str):
#         self.brand = brand
    
#     # def __str__(self) -> str:
#     #     return f'Car: {self.brand}'
    
#     def __repr__(self) -> str:
#         return object.__repr__(self)
    

# little_car = Car('Mini Cooper')
# print(little_car )
# little_car # 'Car: Mini Cooper' 

class C:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __hash__(self):
        return hash(self.age)

    def __bool__(self):
        return self.age > 0

alice = C(15)
bob = C(30)
rel = 'younger' if alice < bob else 'older'
print(f'Alice is {rel} than Bob')
print(hash(alice))

