# You have to make a tourism system- input: name, budget, where to go, how many nights of stay, if want to rent a car or not 
# Your hotel per night charge is Rs 1200 and cities you deal with are Sri Lanka, Goa, Bali, Ladakh, Jammu
# Price as per Destination: sri lanka= 40000, goa= 50000, bali=70000, ladakh= 30000, jammu=40000. If not from these cities show Error
# If wants to book a car, so car per day is Rs.700 If you book a car for 4 or more than 4 days then discount on total = Rs.500, If 6 or more than 6 days= Rs.700 discount, if more than 10 days=Rs.1400 discount
# Check if total = Budget or less than budget then print enjoy your trip
# if budget is less and your trip amount is more then print all this but tell them that you need this much more money to plan the trip


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


