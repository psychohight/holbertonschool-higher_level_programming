import os

def generate_invitations(template, attendees):
    # Vérifier le type des entrées
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Vérifier si le modèle est vide
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Vérifier si la liste des invités est vide
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Processer chaque invité et créer les fichiers de sortie
    for idx, attendee in enumerate(attendees, start=1):
        # Remplacer les placeholders par les valeurs réelles ou "N/A" si manquantes
        output_content = template
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(placeholder, "N/A")
            if value is None:
                value = "N/A"
            output_content = output_content.replace(f"{{{placeholder}}}", value)

        # Générer le nom de fichier et écrire le contenu dans le fichier
        output_filename = f"output_{idx}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(output_content)

        print(f"Generated {output_filename}")
