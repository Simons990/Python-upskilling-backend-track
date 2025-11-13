all_attendees = []
def get_attendee_info():      
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    ticket_type = input("1. Regular \n2. VIP \nChoose your ticket type: ")
    if ticket_type == "1":
        print("Regular")
    else:
        print("VIP")
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
    for attendee in all_attendees:
        print(f"Name: {attendee['name']} \nAge: {attendee['age']}years \nTicket: {attendee['zone']} ")
    youth = 0
    standard = 0
    VIP = 0
    total_age = 0
    for attendee in all_attendees:
        total_age += attendee['age']
        if attendee['zone'] == "Youth zone":
            youth += 1
        elif attendee['zone'] == "Standard zone":
            standard += 1
        elif attendee['zone'] == "VIP zone":
            VIP += 1
    print(f"Youth: {youth}, Standard: {standard}, VIP: {VIP}")
    print(f"Total: {len(all_attendees)}")
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





