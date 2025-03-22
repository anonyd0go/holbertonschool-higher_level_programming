import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a str")
        return
    if not isinstance(attendees, list):
        print("Error: attendees must be a list of dictionaries")
        return
    if not all(isinstance(cont, dict) for cont in attendees):
        print("Error: attendees must be a list of dictionaries")
        return
    
    if not template.strip():
        print("Template is empty, no output files generated")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for i, attendee in enumerate(attendees, start=1):
        output_file = f"output_{i}.txt"
        for key in attendee:
            if not attendee[key]:
                attendee[key] = "N/A"
        try:
            with open(output_file, 'w', encoding='utf-8') as output:
                output.write(template.format(**attendee))
        except KeyError as e:
            print(f"Error: missing key {str(e)} in template for attendee {i}")
