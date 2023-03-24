import random

# Answer to : What is your gender?
genders = ["male","male","male","male","male","female"]
random_gender = random.choice(genders)

# Answer to : Have you ever bought construction materials online before?
before = ["yes","yes","yes","yes","yes","yes","yes"]
random_before = random.choice(before)

# Answer to : How do you typically buy construction materials?
purchase_methods = ["physical visits to hardware stores","physical visits to hardware stores","physical visits to hardware stores","physical visits to hardware stores","physical visits to hardware stores","physical visits to hardware stores","through phone or email orders to suppliers","through contractors or builders who procure materials","directly from manufacturers' warehouses"]
random_method = random.choice(purchase_methods)

# Answer to : How important is it for you to be able to buy construction materials online?
importance = ["very important","very important","moderately important","moderately important","very important","very important","very important","very important","very important"]
random_importance = random.choice(importance)

# Answer to : How likely are you to use an online platform to buy construction materials?
likely_ness = ["very likely","somewhat likely","very likely","very likely","very likely","very likely","very likely","very likely","very likely"]
random_likely = random.choice(likely_ness)




benefits_list = [
    "can easily be accessed from any location",
    "increased efficiency in the delivery process",
    "enhanced Customer Service",
    "customization in delivery options depending on the needs of the customer",
    "delivery of high quality construction materials",
    "faster delivery of construction materials",
    "access to a wide variety of construction materials",
    "access to construction materials of lower prices."
]


challenge_list = [
    "limited accessibility of construction materials",
    "time-consuming delivery process",
    "limited inventory management system framework",
    "limited information sharing to customers",
    "inefficient scheduling of delivery of construction items",
    "risk of damage to construction materials",
    "damage to construction materials",
    "low quality of construction materials"
]