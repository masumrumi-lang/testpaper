with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

old_string = 'questionText: "Mr. Habib\'s business had the following transactions in July 2024:<br>July-1: Started business with cash 2,00,000 Tk, office equipment 50,000 Tk and a bank loan of 40,000 Tk.<br>July-10: Provided service of 40,000 Tk to a client and received 30,000 Tk.<br>July-12: Purchased supplies for cash 10,000 Tk.<br>July-15: Paid two months rent 10,000 Tk.<br>July-24: Withdrawn from bank 15,000 Tk.<br>July-28: Paid half of the bank loan.<br>July-30: Amount of used supplies is 6,000 Tk.<br>July-31: Monthly salary paid 10,000 Tk.",'

new_string = '''stem: "<p>Mr. Habib's business had the following transactions in July 2024:</p><ul class='list-disc ml-6 mt-2'><li>July-1: Started business with cash 2,00,000 Tk, office equipment 50,000 Tk and a bank loan of 40,000 Tk.</li><li>July-10: Provided service of 40,000 Tk to a client and received 30,000 Tk.</li><li>July-12: Purchased supplies for cash 10,000 Tk.</li><li>July-15: Paid two months rent 10,000 Tk.</li><li>July-24: Withdrawn from bank 15,000 Tk.</li><li>July-28: Paid half of the bank loan.</li><li>July-30: Amount of used supplies is 6,000 Tk.</li><li>July-31: Monthly salary paid 10,000 Tk.</li></ul>",'''

if old_string in content:
    content = content.replace(old_string, new_string)
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully replaced questionText with stem and formatted it!")
else:
    print("Could not find the exact old_string")
