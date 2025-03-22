#!/usr/bin/python3
import os
"""
This module defines a function that generates invitations by
filling a template with data from a list of attendee dictionaries.
Each invitation is saved to a separate text file.
"""


def generate_invitations(template, attendees):
    """
    Generates invitation files by formatting a template with data.

    The function validates that the template is a non-empty string
    and that attendees is a list of dictionaries. For each attendee,
    it replaces any empty value with "N/A" and writes the formatted
    invitation to an output file (output_<n>.txt).

    Args:
        template (str): Template string with keys for formatting.
        attendees (list): List of dicts with invitation data.

    Returns:
        None

    Side Effects:
        Writes output files in the current working directory and
        prints error messages if validations fail or keys are missing.
    """
    if not isinstance(template, str):
        print("Error: Template must be a str")
        return
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries")
        return
    if not all(isinstance(cont, dict) for cont in attendees):
        print("Error: Attendees must be a list of dictionaries")
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
