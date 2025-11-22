def get_all_attendees():
    return []
all_attendees = get_all_attendees
def get_attendee_info():      
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    while True:    # Using while loop to check over if user mistakenly enters invalid option
        ticket_type = input("1. Regular \n2. VIP \nChoose your ticket type: ")
        if ticket_type == "1":
            print("Regular")
            break
        elif ticket_type == "2":
            print("VIP")
            break
        else:
            print("Invalid option! Please choose (Regular or VIP)")
    print(f"{name} registered ")
    person = {
        "name": name,
        "age": age,
        "ticket": ticket_type,
    }
    return person
def assign_zone(age, ticket_type):
    if ticket_type == "2":
        return "VIP zone"
    elif age >= 18 and ticket_type == "1":
        return "Standard zone"
    elif age < 18:
        return "Youth zone"
    else:
        return "Invalid option"
def store_attendee(data):
    zone = assign_zone(data['age'], data['ticket'])
    data['zone'] = zone
    all_attendees.append(data)

def summary():
    if len(all_attendees) == 0:
        print("No one registered yet")
        return
    zones = {
        "Youth zone": 0,
        "Standard zone": 0,
        "VIP zone": 0
    }
    total_age = 0
    for attendee in all_attendees:
        name = attendee.get("name")
        age = attendee.get("age", 0)
        zone = attendee.get("zone")
        ticket = attendee.get("ticket")
        print(f"Name: {name} \nAge: {age}years \nTicket: {ticket} \nZone: {zone}")
        total_age += age
        if zone in zones:
            zones[zone] += 1
        else:
            print("Unknown zones")
    for zone, count in zones.items():
        if count > 0:  
            print(f"{zone}: {count}")
    print(f"Total attendees: {len(all_attendees)}")
    if len(all_attendees) > 0:
        average_age = total_age / len(all_attendees)
        print(f"Average age: {average_age:.1f} years")
while True:
    print("\n1. Register new attendee")
    print("2. Show summary")
    print("3. Exit")

    choice = input("Choose 1-3: ")
    if choice == "1":
        data = get_attendee_info()
        store_attendee(data)
    elif choice == "2":
        summary()
    elif choice == "3":
        break
    else:
        print("Invalid option!")
    



