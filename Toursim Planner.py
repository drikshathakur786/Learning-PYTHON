# Create a tourism system that takes the following inputs from the user:
# Name
# Budget
# Destination
# Number of nights of stay
# Option to rent a car

# The system should calculate the total cost of the trip based on the provided inputs 
# Provide appropriate messages according to the budget and chosen options.

# Hotel rate per night is Rs 1200, and the prices for the destinations are as follows:
# Sri Lanka: Rs 40,000
# Goa: Rs 50,000
# Bali: Rs 70,000
# Ladakh: Rs 30,000
# Jammu: Rs 40,000

# If user choose to rent a car, it costs Rs 700 per day. Additionally, offer discounts for longer car rentals:
# 4 or more days: Rs 500 discount
# 6 or more days: Rs 700 discount
# 10 or more days: Rs 1400 discount

# After calculating total cost, tell if it fits within user budget. If it doesn't, inform about the additional amount needed to plan the trip.

print('Sat Sri Akal Mitron!')
hotelrates= {'sri lanka':40000, 'goa':50000, 'bali':70000, 'ladakh':30000, 'jammu':40000}
destination= input("Kiteh? (Sri Lanka, Goa, Bali, Ladakh, Jammu):").strip().lower()
if destination not in hotelrates:
    print("Khud chala ja :)")

else:
    name= input("Apna naa dso:")
    budget= float(input("Kharcha kina kr skde o?:"))
    nights= int(input("Kinniyan Raatan?: "))
    rentcar= input("Gaddi??(yes/no): ").lower()
    hotelcost= nights*1200
    totalcost= hotelcost+hotelrates[destination]
    if rentcar=='yes':
        cardays= int(input("Kine dina vaste gaddi cahidi?: "))
        carcost= cardays*700
        if cardays>=10:
            cardiscount= 1400
        elif cardays>= 6:
            cardiscount= 700
        elif cardays>= 4:
            cardiscount= 500
        else:
            cardiscount= 0
        totalcost+= carcost-cardiscount

    
    if totalcost<=budget:
        print("Ja maujja kr k aa", destination.capitalize(),"!")
        print("\nBill Details:")
        print("------------")
        print("Hotel Cost(", nights, " nights): Rs.", hotelcost)
        print("Destination Cost: Rs.", hotelrates[destination])
        if rentcar=='yes':
            print("Car Rental Cost: Rs.", carcost)
            print("Car Rental Discount: Rs.", cardiscount)
        print("Total Cost: Rs.", totalcost)
        print("Remaining Budget: Rs.", budget - totalcost)
    else:
        additionalcost= totalcost - budget
        print("Gareeb",name.capitalize() +""+ ", ghre baihja nhi ta kistaan te",additionalcost, "ehne paise jodlaa")


