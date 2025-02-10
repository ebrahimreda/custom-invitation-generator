LETTER_TEMPLATE_PATH = "/home/ibrahim/learning/prejcts/letters/Starting_letter.txt"
NAMES_FILE_PATH = "/home/ibrahim/learning/prejcts/letters/nemas.txt"
INVITATION_LETTERS_DIR = "/home/ibrahim/learning/prejcts/letters/invit_letters/"

def get_letter_template():
    """يقرأ قالب الرسالة من الملف."""
    with open(LETTER_TEMPLATE_PATH, "r") as template_file:
        return template_file.read()

def read_names_file():
    """يقرأ أسماء المدعوين من الملف ويعيدها كسطر لكل اسم."""
    with open(NAMES_FILE_PATH, "r") as names_file:
        return names_file.readlines()

def generate_invitation_letter(recipient):
    """ينشئ رسالة دعوة مخصصة للمدعو."""
    # إزالة الفراغات الزائدة من الاسم (مثل '\n')
    recipient_clean = recipient.strip()
    invitation_path = f"{INVITATION_LETTERS_DIR}{recipient_clean}.txt"
    
    # قراءة قالب الرسالة وتعديلها
    letter_template = get_letter_template()
    personalized_letter = letter_template.replace("name", recipient_clean)
    personalized_letter = personalized_letter.replace("[ send ]", "[ OctuCode ]")
    
    # كتابة الرسالة المخصصة في ملف منفصل
    with open(invitation_path, "w") as invitation_file:
        invitation_file.write(personalized_letter)

def main():
    for recipient in read_names_file():
        # تخطي الأسطر الفارغة
        if not recipient.strip():
            continue
        generate_invitation_letter(recipient)

if __name__ == "__main__":
    main()
