class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


info = input()
list_of_mails = []
while info != "Stop":
    attributes = info.split(" ")
    sender = attributes[0]
    receiver = attributes[1]
    content = attributes[2]
    email = Email(sender, receiver, content)
    list_of_mails.append(email)
    info = input()
indices = [int(i) for i in input().split(", ")]
for i in indices:
    list_of_mails[i].send()
for email in list_of_mails:
    print(email.get_info())

